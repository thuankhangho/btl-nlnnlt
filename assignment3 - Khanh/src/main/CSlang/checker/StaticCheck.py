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

class BKMember: pass

class BKType: 
  def __init__(self, typeBK, id = None, var = False):
    self.typeBK = typeBK
    self.id = id
    self.var = var

class BKAttribute(BKMember): 
  def __init__(self, id, typeBK, var):
    self.id = id
    self.typeBK = typeBK
    self.var = var
  
class BKMethod(BKMember):
  def __init__(self,id,param,returnType):
    self.id = id
    self.param = param
    self.returnType = returnType

class BKClass:
    def __init__(self,classdeclare,parentclass = None,gbl = None):
        self.constructor = []
        if classdeclare is not None: 
            self.name = classdeclare.classname
            self.parentclass = parentclass
            self.member = {}
            self.staticmember = {}
            reduce(lambda x,y: self.addmem(y,gbl),classdeclare.memlist,self.member)
        else: 
            self.name = "io"
            self.staticmember = {
                "@readInt": BKMethod(Id("@readInt"), [], IntType()),
                "@writeInt": BKMethod(Id("@writeInt"), [IntType()], VoidType()),
                "@readFloat": BKMethod(Id("@readFloat"), [], FloatType()),
                "@writeFloat": BKMethod(Id("@writeFloat"), [FloatType()], VoidType()),
                "@readBool": BKMethod(Id("@readBool"), [], BoolType()),
                "@writeBool": BKMethod(Id("@writeBool"), [BoolType()], VoidType()),
                "@readStr": BKMethod(Id("@readStr"), [], StringType()),
                "@writeStr": BKMethod(Id("@writeStr"), [StringType()], VoidType())
                }
        
    def addmem(self, member, gbl):
        if type(member) is AttributeDecl: 
            self.addAttribute(member,gbl)
        else:
            self.addMethod(member,gbl)
    
    def addAttribute(self,member,gbl):
        memberDecl = member.decl
        if type(memberDecl) is VarDecl : 
            self.addVariable(memberDecl,gbl)
        else: self.addConstant(memberDecl,gbl)
    
    def addVariable(self,memberDecl,gbl):
        variablename = memberDecl.variable.name
        if variablename in self.member: raise Redeclared(Attribute(),variablename)
        variabletype = gbl.checkForType(memberDecl.varType)
        if variablename[0] == '@':
            self.staticmember[variablename] = BKAttribute(Id(variablename),variabletype,True)
        else: self.member[variablename] = BKAttribute(Id(variablename),variabletype,True)
  
    def addConstant(self,memberDecl,gbl):
        constname = memberDecl.constant.name
        if constname in self.member: raise Redeclared(Attribute(),constname)
        consttype = gbl.checkForType(memberDecl.constType)
        if constname[0] == '@':
            self.staticmember[constname] = BKAttribute(Id(constname),consttype,False)
        else: self.member[constname] = BKAttribute(Id(constname),consttype,False)
    
    def addMethod(self,member,gbl):
        methodname = member.name.name
        if methodname in self.member and methodname != "constructor": raise Redeclared(Method(),methodname)
        paramType =  []
        for x in member.param: paramType.append(gbl.checkForType(x.varType))
        returnType = gbl.checkForType(member.returnType)
        newMethod = BKMethod(Id(methodname),paramType,returnType)
        if methodname == "constructor" : self.constructor.append(newMethod)
        else: 
            if methodname[0] == '@': self.staticmember[methodname] = newMethod
            else: self.member[methodname] = newMethod
            
    def getMember(self, name, kind, undeclaredRedeclared):
        checkList = self.staticmember if name[0]=='@' else self.member
        
        if undeclaredRedeclared == UNDECLARED:
            if name in checkList:
                return checkList[name]
            else:
                raise Undeclared(kind, name)
            
        elif undeclaredRedeclared == REDECLARED:
            if name in checkList:
                raise Redeclared(kind, name)
    
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
            else: raise Undeclared(Class(),name)
        elif undeclaredredeclared == REDECLARED:
            if name in self.classList: raise Redeclared(Class(),name)
        
    def checkUndeclaredRedeclared(self,name,kind,undeclaredredeclared):
        if undeclaredredeclared == UNDECLARED:
            for x in self.scope:
                if name in x: return x[name]
            if kind not in [Attribute,Method]: kind = Identifier()
            raise Undeclared(kind,name)
        elif undeclaredredeclared == REDECLARED:
            if name in self.scope[0]: raise Redeclared(kind,name)
        
    def compareTypes(self, type1, type2):
        if type(type1) is ClassType and type(type2) is ClassType:
            if type1.classname.name == type2.classname.name or type1.classname.name == self.getClassEnv(type2.classname.name, True).parentclass:
                return True
        elif type(type1) is ClassType and type(type2) is VoidType:
            return True
        elif type(type1) is FloatType and type(type2) is IntType:
            return True
        elif type(type1) is ArrayType and type(type2) is ArrayType:
            return self.compareTypes(type1.eleType, type2.eleType) and (type1.size == type2.size)
        elif type(type1) == type(type2):
        # if type(type1) == type(type2):
            return True
        return False
    
    def compareParams(self, leftParams, rightParams):
        if len(leftParams) != len(rightParams):
            return False
        for i in range(len(leftParams)):
            if self.compareTypes(leftParams[i], rightParams[i]) == False:
                return False
        return True
    
    def compareTypeInArray(self, inputType, checkingType):
        if type(inputType.typeBK) is ClassType and type(checkingType.typeBK) is ClassType:
            if inputType.classname.name == checkingType.classname.name:
                return True
        elif type(inputType) == type(checkingType):
            return True
        return False
      
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
            print(varInitType)
            if o.compareType(varDeclType,varInitType.typeBK) == False: raise TypeMismatchInDeclaration(ast)
        
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
        
    def visitBinaryOp(self, ast, o: Global):
        o.undeclaredredeclared = UNDECLARED
        lhs = self.visit(ast.left, o)
        rhs = self.visit(ast.right, o)
        
        if ast.op == '^':
            if type(lhs.typeBK) is StringType and type(rhs.typeBK) is StringType:
                return BKType(StringType())
            else: raise TypeMismatchInExpression(ast)
        
        elif ast.op in ['+', '-', '*']:
            if type(lhs.typeBK) is IntType and type(rhs.typeBK) is IntType:
                return BKType(IntType())
            elif type(lhs.typeBK) is FloatType or type(rhs.typeBK) is FloatType:
                return BKType(FloatType())
            else: raise TypeMismatchInExpression(ast)
        
        elif ast.op in ['==', '!=']:
            if type(lhs.typeBK) is IntType and type(rhs.typeBK) is IntType:
                return BKType(BoolType())
            if type(lhs.typeBK) is BoolType and type(rhs.typeBK) is BoolType:
                return BKType(BoolType())
            raise TypeMismatchInExpression(ast)
        
        elif ast.op in ["<", ">", "<=", ">="]:
            if type(lhs.typeBK) in [IntType, FloatType] and type(rhs.typeBK) in [IntType, FloatType]:
                return BKType(BoolType())
            raise TypeMismatchInExpression(ast)
        
        elif ast.op in ["&&", "||"]:
            if type(lhs.typeBK) is BoolType and type(rhs.typeBK) is BoolType:
                return BKType(BoolType())
            raise TypeMismatchInExpression(ast)
            
        elif ast.op == "/":
            if type(lhs.typeBK) in [IntType, FloatType] and type(rhs.typeBK) in [IntType, FloatType]:
                if type(lhs.typeBK) is FloatType or type(rhs.typeBK) is FloatType:
                    return BKType(FloatType())
            raise TypeMismatchInExpression(ast)
            
        elif(ast.op in ["\\","%"]):
            if type(lhs.typeBK) is IntType and type(rhs.typeBK) is IntType:
                return BKType(IntType())
            raise TypeMismatchInExpression(ast)
        
    def visitUnaryOp(self, ast, o: Global):
        o.undeclaredredeclared = UNDECLARED
        body = self.visit(ast.body,o)

        if ast.op == "!":
            if type(body.typeBK) is BoolType:
                return BKType(BoolType())
            raise TypeMismatchInExpression(ast)
            
        elif ast.op == "-":
            if type(body.typeBK) in [IntType, FloatType]:
                return BKType(body.typeBK)
            raise TypeMismatchInExpression(ast)
        
    def visitArrayCell(self, ast, o: Global):
        arr = self.visit(ast.arr, o)
        idx = self.visit(ast.idx, o)
        if type(arr.typeBK) is ArrayType and type(idx) is IntType:
            return BKType(arr.typeBK.eleType)
        raise TypeMismatchInExpression(ast)
    
    def visitFieldAccess(self, ast, o: Global):
        fieldname = ast.fieldname.name
        currClass = ""

        if fieldname[0] != '@':
            o.undeclaredredeclared = True
            obj = self.visit(ast.obj, o)
            if type(obj.typ) is ClassType:
                if obj.typ.classname == o.currentClass.name or obj.typ.classname == o.currentClass.parentclass:
                    currClass = obj.typ.classname.name
            else: raise TypeMismatchInExpression(ast)
           
        elif fieldname[0] == '@':
            if obj is None:
                currClass = o.currentClass.name.name
            elif type(ast.obj) is Id:
                currClass = ast.obj.name
            else:
                raise TypeMismatchInExpression(ast)
            
        objEnv = o.getClassEnv(currClass, True)
        memberEnv = objEnv.getMember(fieldname, Attribute(), True)
        
        if memberEnv is not None: return BKType(memberEnv.typeBK, isMutable = True)
        else: raise TypeMismatchInExpression(ast)
    
    def visitNewExpr(self, ast, o: Global):
        className = ast.classname.name
        params = ast.param
        
        classEnv = o.getClassEnv(className, True)
        classConstructors = classEnv.constructor
        
        for constructor in classConstructors:
            constructorParamType = constructor.paramList
            paramTypeList = [self.visit(param, o).typ for param in params]
            if o.compareParams(constructorParamType, paramTypeList) is True:
                return BKType(ClassType(Id(className)))

        raise TypeMismatchInExpression(ast)
    
    def visitCallExpr(self, ast, o: Global):
        currClass = ""
        fieldname = ast.method.name

        if fieldname[0] != '@':
            o.undeclaredredeclared = UNDECLARED
            obj = self.visit(ast.obj, o)
            if type(obj.typ) is ClassType:
                currClass = obj.typ.classname.name
            else: raise TypeMismatchInExpression(ast)
           
        elif fieldname[0] == '@':
            if obj is None:
                currClass = o.currentClass.name.name
            elif type(ast.obj) is Id:
                currClass = ast.obj.name
            else:
                raise TypeMismatchInExpression(ast)
            
        objEnv = o.getClassEnv(currClass, True)
        memberEnv = objEnv.getMember(fieldname, Method(), True)
        
        if memberEnv is not None:
            if type(memberEnv.returnType) is VoidType:
                raise TypeMismatchInExpression(ast)
            o.undeclaredredeclared = UNDECLARED
            paramList: List[Type] = []
            for param in ast.param:
                paramList.append(self.visit(param, o).typeBK)
            memberEnvparamList = memberEnv.param
            if o.compareParams(paramList, memberEnvparamList) == False:
                raise TypeMismatchInExpression(ast)
            return BKType(memberEnv.returnType, var = True)
        else: raise TypeMismatchInExpression(ast)

    def visitContinue(self, ast, o: Global):
        if o.loop == False:
            raise MustInLoop(ast)
    
    def visitBreak(self, ast, o: Global):
        if o.loop == False:
            raise MustInLoop(ast)
        
    def visitAssign(self, ast, o: Global):
        o.undeclaredredeclared = UNDECLARED
        lhs = self.visit(ast.lhs, o)
        if lhs.var == False:
            raise CannotAssignToConstant(ast)
        if type(lhs.typeBK) is VoidType:
            raise TypeMismatchInStatement(ast)
        rhs = self.visit(ast.exp, o)
        if o.compareTypes(lhs.typeBK, rhs.typeBK) == False:
            raise TypeMismatchInStatement(ast)
        
    def visitFor(self, ast, o: Global):
        o.loop = o.loop + 1
        o.scope = [{}] + o.scope
        
        self.visit(ast.initStmt, o)
        self.visit(ast.expr, o)
        self.visit(ast.postStmt, o)

        self.visit(ast.loop, o)
        
        o.scope.pop(0)
        o.loop = o.loop - 1

    def visitIf(self, ast, o: Global):
        o.undeclaredredeclared = UNDECLARED
        expr = self.visit(ast.expr, o)
        o.undeclaredredeclared = None
        
        if type(expr.typeBK) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        if ast.preStmt is not None:
            o.scope = [{}] + o.scope
            self.visit(ast.preStmt, o)
            o.scope.pop(0)

        o.scope = [{}] + o.scope
        self.visit(ast.thenStmt, o)
        o.scope.pop(0)

        if ast.elseStmt is not None:
            o.scope = [{}] + o.scope
            self.visit(ast.elseStmt, o)
            o.scope.pop(0)
            
    def visitCallStmt(self, ast, o: Global):
        fieldname = ast.method.name
        currClass = ""

        if fieldname[0] != '@':
            o.undeclaredredeclared = UNDECLARED
            obj = self.visit(ast.obj, o)
            if type(obj.typ) is ClassType:
                currClass = obj.typ.classname.name
            else: raise TypeMismatchInExpression(ast)
           
        elif fieldname[0] == '@':
            if obj is None:
                currClass = o.currentClass.name.name
            elif type(ast.obj) is Id:
                currClass = ast.obj.name
            else:
                raise TypeMismatchInExpression(ast)
            
        objEnv = o.getClassEnv(currClass, True)
        memberEnv = objEnv.getMember(fieldname, Method(), True)
        
        if memberEnv is not None:
            if type(memberEnv.returnType) is not VoidType:
                raise TypeMismatchInExpression(ast)
            o.undeclaredredeclared = UNDECLARED
            paramList: List[Type] = []
            for param in ast.param:
                paramList.append(self.visit(param, o).typeBK)
            memberEnvparamList = memberEnv.param
            if o.compareParams(paramList, memberEnvparamList) == False:
                raise TypeMismatchInExpression(ast)
            return BKType(memberEnv.returnType)
        else: raise TypeMismatchInExpression(ast)
    
    def visitBlock(self, ast, o):
        reduce(lambda _,x: self.visit(x,o), ast.stmt,[])
        
    def visitId(self,ast,o):
        return o.checkUndeclaredRedeclared(ast.name,o.currentCheck,o.undeclaredredeclared)
        
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
        return BKType(IntType())
    def visitFloatLiteral(self,ast,o):
        return BKType(FloatType())
    def visitBooleanLiteral(self,ast,o):
        return BKType(BoolType())
    def visitStringLiteral(self,ast,o):
        return BKType(StringType())
    def visitNullLiteral(self,ast,o):
        return BKType(VoidType())
    def visitSelfLiteral(self,ast,o):
        return BKType(ClassType(o.currentClass.name))
    def visitArrayLiteral(self,ast,o: Global):
        currentType = VoidType()
        value = ast.value
        for x in value:
            temp: BKType = self.visit(x, o)
            litType = temp.typ
            if type(currentType) is not VoidType:
                if o.compareTypeInArray(currentType, litType) == False:
                    raise IllegalArrayLiteral(ast)
            elif type(litType) is not VoidType:
                currentType = litType
        return BKType(ArrayType(IntLiteral(len(ast.value)), currentType), False)