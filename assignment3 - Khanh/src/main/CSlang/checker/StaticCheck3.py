
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils, MType
from StaticError import *
from functools import reduce
import copy
from typing import Dict,List
UNDECLARED = True
REDECLARED = False

class BKType: 
  def __init__(self,typeBK,id,var):
    self.typeBK = typeBK
    self.id = id
    self.var = var
    
class BKMember: pass 
class BKAttribute(BKMember): 
  def __init__(self,id,typeBK,var,static):
    self.id = id
    self.typeBK = typeBK
    self.var = var
    self.static = static
  
class BKMethod(BKMember):
  def __init__(self,id,param,returnType,static):
    self.id = id
    self.param = param
    self.returnType = returnType
    self.static = static

class BKClass:
  def __init__(self,classdeclare,parentclass = None,gbl = None):
    self.constructor = []
    if classdeclare: 
      self.name = classdeclare.classname
      self.parentclass = parentclass
      self.member = {}
      self.staticmember = {}
      reduce(lambda x,y: self.addmem(y,gbl),classdeclare.memlist,self.member)
    else: 
      self.name = "io"
      self.staticmember = {
                "@readInt": BKMethod(Id("@readInt"), [], IntType(), True),
                "@writeInt": BKMethod(Id("@writeInt"), [IntType()], VoidType(), True),
                "@readFloat": BKMethod(Id("@readFloat"), [], FloatType(), True),
                "@writeFloat": BKMethod(Id("@writeFloat"), [FloatType()], VoidType(), True),
                "@readBool": BKMethod(Id("@readBool"), [], BoolType(), True),
                "@writeBool": BKMethod(Id("@writeBool"), [BoolType()], VoidType(), True),
                "@readStr": BKMethod(Id("@readStr"), [], StringType(), True),
                "@writeStr": BKMethod(Id("@writeStr"), [StringType()], VoidType(), True)
            }
            
  def addmem(self,member,gbl):
    if type(member) is AttributeDecl: 
      self.addAttribute(member,gbl)
    else: self.addMethod(member,gbl)
    
  def addAttribute(self,member,gbl):
    memberDecl = member.decl
    if type(memberDecl) is VarDecl : 
      self.addVariable(memberDecl,gbl)
    else: self.addConstant(memberDecl,gbl)
    
  def addVariable(self,memberDecl,gbl):
    variablename = memberDecl.variable.name
    if variablename in self.member: raise Redeclared(Attribute(),variablename)
    variabletype = gbl.checkForType(memberDecl.varType)
    self.member[variablename] = BKAttribute(Id(variablename),variabletype,True,variablename[0] == '@')
  
  def addConstant(self,memberDecl,gbl):
    constname = memberDecl.constant.name
    if constname in self.member: raise Redeclared(Attribute(),constname)
    consttype = gbl.checkForType(memberDecl.constType)
    self.member[constname] = BKAttribute(Id(constname),consttype,False,constname[0] == '@')
    
  def addMethod(self,member,gbl):
    methodname = member.name.name
    if methodname in self.member and methodname != "constructor": raise Redeclared(Method(),methodname)
    paramType =  []
    for x in member.param: paramType.append(gbl.checkForType(x.varType))
    returnType = gbl.checkForType(member.returnType)
    newMethod = BKMethod(Id(methodname),paramType,returnType,methodname[0] == '@')
    if methodname == "constructor" : self.constructor.append(newMethod)
    else: 
      if methodname[0] == '@': self.staticmember[methodname] = newMethod
      else: self.member[methodname] = newMethod
    
      

class Global:
    def __init__(self,ast: Program):
        self.classList = {
            "io": BKClass(None)
        }
        self.currentCheck = None
        self.scope = []
        self.loop = 0
        self.undeclaredredeclared = True 
        self.currentClass = None
        self.returnType = None
        for x in ast.decl:
          self.addClass(x)
          
    def addClass(self,newClass):
      newClassName = newClass.classname.name
      if newClassName in self.classList: 
        raise Redeclared(Class(),newClassName)
      if newClass.parentname: 
        parentName = newClass.parentname.name
        if parentName in self.classList:
          raise Redeclared(Class(),parentName)
        parentmemlist = self.classList[parentName].member
        self.classList[newClassName] = BKClass(newClass,Id(parentName),self)
        for x in parentmemlist: 
          if x not in self.classList[newClassName].member: 
            self.classList[newClassName].member[x] = parentmemlist[x]
      else: self.classList[newClassName] = BKClass(newClass,None,self)
           
    def checkEntryPoint(self):
      if "Program" not in self.classList: raise NoEntryPoint()
      outsideClass = self.classList["Program"]
      if "@main" not in outsideClass.staticmember or type(outsideClass.staticmember["@main"]) is not BKMethod or type(outsideClass.staticmember["@main"].returnType) is not VoidType:
        raise NoEntryPoint()
      
    def checkForType(self,typeP):
      if type(typeP) is ClassType: 
        if typeP.classname.name not in self.classList: raise Undeclared(Class(),typeP.classname.name)
      elif type(typeP) is ArrayType:
        self.checkForType(typeP.eleType)
      return typeP
      
    def getClassEnv(self,name,undeclaredredeclared):
      if undeclaredredeclared == UNDECLARED:
        if name in self.classList: return self.classList[name]
        else : raise Undeclared(Class(),name)
      elif undeclaredredeclared == REDECLARED:
        if name in self.classList: raise Redeclared(Class(),name)
        
    def checkUndeclaredRedeclared(self,name,kind,undeclaredredeclared):
      if undeclaredredeclared ==UNDECLARED:
        for x in self.scope:
          if name in x: return x[name]
        if kind not in [Attribute,Method]: kind = Identifier()
        raise Undeclared(kind,name)
      elif undeclaredredeclared == REDECLARED:
        if name in self.scope[0]: raise Redeclared(kind,name)
        
    def compareType(self, type1, type2):
      if type(type1) == type(type2): return True
      else: return False
      
class StaticChecker(BaseVisitor,Utils):
    def __init__(self,ast):
      self.ast = ast
    
    def check(self):
        self.gbl = Global(self.ast)
        self.gbl.checkEntryPoint() 
        self.visit(self.ast, self.gbl) 
        return ""
    
    def visitProgram(self, ast, o):
        reduce(lambda _,x: self.visit(x,o), ast.decl, [])
      
    def visitClassDecl(self, ast, o):
        o.currentClass = o.classList[ast.classname.name]
        reduce(lambda _,x: self.visit(x,o), ast.memlist, [])
      
    def visitAttributeDecl(self, ast, o):
        o.currentCheck = Attribute()
        self.visit(ast.decl, o)
        o.currentCheck = None
      
    def visitVarDecl(self, ast, o):
        print(ast)
        if o.currentCheck == None :
            o.currentCheck = Variable()
        varDeclType = self.visit(ast.varType, o)
        if type(o.currentCheck) is not Attribute: 
            o.undeclaredredeclared = REDECLARED
            self.visit(ast.variable, o)
            o.scope[0][ast.variable.name] = BKType(varDeclType,ast.variable,True)
        if type(varDeclType) is VoidType: 
            raise TypeMismatchInDeclaration(ast)
        if ast.varInit is not None: 
            o.undeclaredredeclared = UNDECLARED
            varInitType = self.visit(ast.varInit, o)
            if o.compareType(varDeclType,varInitType) == False: raise TypeMismatchInDeclaration(ast)
        
    def visitConstDecl(self, ast, o):
        if o.currentCheck == None : o.currentCheck = Constant()
        constDeclType = self.visit(ast.constType, o)
        if type(o.currentCheck) is not Attribute: 
          o.undeclaredredeclared = REDECLARED
          self.visit(ast.constant, o)
          o.scope[0][ast.constant.name] = BKType(constDeclType,ast.variable,False)
        if type(constDeclType) is VoidType: raise TypeMismatchInDeclaration(ast)
        if ast.value is not None: 
          o.undeclaredredeclared = UNDECLARED
          valueType = self.visit(ast.value, o)
          if o.compareType(constDeclType,valueType) == False: raise TypeMismatchInDeclaration(ast)
          
    def visitMethodDecl(self,ast,o):
        o.scope = [{}] + o.scope
        o.currentCheck = Parameter()
        reduce(lambda _,x: self.visit(x,o), ast.param, [])
        o.returnType = ast.returnType
        self.visit(ast.body, o)
        o.scope.pop(0)
        o.returnType = None
        
    def visitBlockDecl(self,ast,o):
        reduce(lambda _,x: self.visit(x,o), ast.stmt,[])
        
    def visitIntType(self,ast,o):
        return IntType()
        
    def visitFloatType(self,ast,o):
        return FloatType()
        
    def visitStringType(self,ast,o):
        return StringType()
        
    def visitBoolType(self,ast,o):
        return BoolType()
        
    def visitVoidType(self,ast,o):
        return VoidType()
        
    def visitArrayType(self,ast,o):
        return o.checkForType(ast)
        
    def visitClassType(self,ast,o):
        return o.checkForType(ast)
        
    def visitIntLiteral(self,ast,o):
        return BKType(IntType(),None,None)
    def visitFloatLiteral(self,ast,o):
        return BKType(FloatType(),None,None)
    def visitBooleanLiteral(self,ast,o):
        return BKType(BoolType(),None,None)
    def visitStringLiteral(self,ast,o):
        return BKType(StringType(),None,None)
    def visitNullLiteral(self,ast,o):
        return BKType(VoidType(),None,None)
    def visitSelfLiteral(self,ast,o):
        return BKType(ClassType(o.currentClass.name),None,None)
        
    def visitId(self,ast,o):
        return o.checkUndeclaredRedeclared(ast.name,o.currentCheck,o.undeclaredredeclared)