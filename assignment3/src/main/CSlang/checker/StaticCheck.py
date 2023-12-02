"""
 * @author nhphung
"""

# Student ID: 2011357
# Name: Ho Thuan Khang
# Line 164 is the return statement of the entire file.
# It is disabled to be submitted, but needs to be un-commented in order to function.

from AST import * 
from Visitor import *
from Utils import *
from StaticError import *
from functools import reduce
from typing import Dict, List

class MemberEnv:
    pass
    
class MethodEnv(MemberEnv):
    name: Id
    paramList: List[Type]
    returnType: Type
    
    def __init__(self, name: Id, paramList: List[Type], returnType: Type):
        self.name = name
        self.paramList = paramList
        self.returnType = returnType

class AttributeEnv(MemberEnv):
    id: Id
    typ: Type
    isMutable: bool #const = false, var = true

    def __init__(self, id: Id, typ: Type, isMutable: bool):
        self.id = id
        self.typ = typ
        self.isMutable = isMutable

class BKClass:
    name: Id
    parent: Id
    members: Dict[str, MemberEnv]
    staticMembers: Dict[str, MemberEnv]
    constructor: List[MethodEnv]
    
    def __init__(self, classDecl: ClassDecl = None, parent: Id = None, manager = None):
        self.constructor = []
        if classDecl:
            self.name = classDecl.classname
            self.parent = parent
            self.members = {}
            self.staticMembers = {}
            reduce(lambda _, mem: self.sortMember(mem, manager), classDecl.memlist, self.members)
        else:
            self.name = Id("io")
            self.members = {}
            self.staticMembers = {
                "@readInt": MethodEnv(Id("@readInt"), [], IntType()),
                "@writeInt": MethodEnv(Id("@writeInt"), [IntType()], VoidType()),
                "@readFloat": MethodEnv(Id("@readFloat"), [], FloatType()),
                "@writeFloat": MethodEnv(Id("@writeFloat"), [FloatType()], VoidType()),
                "@readBool": MethodEnv(Id("@readBool"), [], BoolType()),
                "@writeBool": MethodEnv(Id("@writeBool"), [BoolType()], VoidType()),
                "@readStr": MethodEnv(Id("@readStr"), [], StringType()),
                "@writeStr": MethodEnv(Id("@writeStr"), [StringType()], VoidType())
            }
    
    def sortMember(self, mem: MemDecl, manager):
        if type(mem) is AttributeDecl:
            # Attribute
            self.processAttribute(mem, manager)
        else:
            # Method
            self.processMethod(mem, manager)
        
    def processMethod(self, member: MethodDecl, manager):
        methodName = member.name.name
        if methodName in self.members and methodName != "constructor":
            raise Redeclared(Method(), methodName)
        paramType = list(map(lambda el: manager.checkForType(el.varType), member.param))
        paramList = []
        for x in member.param:
            if x not in paramList:
                paramList.append(x)
            else: raise Redeclared(Parameter(), x.variable.name)
        returnType = manager.checkForType(member.returnType)
        method = MethodEnv(Id(methodName), paramType, returnType)
        if methodName == "constructor":
            self.constructor += [method]
        else:
            if methodName[0] != '@':
                self.members[methodName] = method
            self.staticMembers[methodName] = method
            
    def processAttribute(self, member: AttributeDecl, manager):
        decl = member.decl
        if type(decl) is ConstDecl:
            self.processConstantAttribute(decl, manager)
        else:
            self.processVariableAttribute(decl, manager)
            
    def processConstantAttribute(self, member: ConstDecl, manager):
        name = member.constant.name
        if name in self.members:
            raise Redeclared(Attribute(), name)
        attributeType = manager.checkForType(member.constType)
        self.staticMembers[name] = AttributeEnv(Id(name), attributeType, isMutable = False)
        
    def processVariableAttribute(self, member: VarDecl,manager):
        name = member.variable.name
        if name in self.members:
            raise Redeclared(Attribute(), name)
        attributeType = manager.checkForType(member.varType)
        self.members[name] = AttributeEnv(Id(name), attributeType, isMutable = True)
        
class ClassManager:
    classes: Dict[str, BKClass]
    def __init__(self, ast: Program):
        self.classes = {
            "io": BKClass()
        }
        self.currentCheck = None #Variable, Constant, Attribute, Parameter
        self.scope = []
        self.loop = False
        self.mode = True
        
        for classDecl in ast.decl:
            self.appendClass(classDecl)

    def appendClass(self, newClass: ClassDecl):
        newClassName = newClass.classname.name
        if newClassName in self.classes:
            raise Redeclared(Class(), newClassName)
        if newClass.parentname: # có thừa kế
            parentName = newClass.parentname.name
            if parentName not in self.classes:
                raise Undeclared(Class(), parentName)
            parentMembers = self.classes[parentName].members
            self.classes[newClassName] = BKClass(newClass, Id(parentName), self)
            for mem in parentMembers:
                if mem not in self.classes[newClassName].members:
                    self.classes[newClassName].members[mem] = parentMembers[mem]
        else: # không thừa kế
            self.classes[newClassName] = BKClass(newClass, manager=self)

    def checkNoEntryPoint(self):
        if "Program" not in self.classes:
            raise NoEntryPoint()
        programClass = self.classes["Program"]
        if "@main" not in programClass.staticMembers or type(programClass.staticMembers["@main"]) is not MethodEnv or type(programClass.staticMembers["@main"].returnType) is not VoidType:
            raise NoEntryPoint()
    
    def checkForType(self, typ: Type):
        if type(typ) is ClassType:
            if typ.classname.name not in self.classes:
                raise Undeclared(Class(), typ.classname.name)
        elif type(typ) is ArrayType:
            self.check_type(typ.eleType)
        return typ
    
    def getClassEnv(self, class_name):
        return self.classes[class_name]
    
    def checkUndeclaredRedeclared(self, name: str, kind: Kind, mode: bool):
    # mode = true: undeclared, mode = false: redeclared
        if name in self.scope[0]:
            raise Redeclared(Identifier, ast.name)

class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast):
        self.ast = ast
        
    def check(self):
        manager = ClassManager(self.ast)
        manager.checkNoEntryPoint()
        self.visit(self.ast, manager)
        return ""
        
    def visitProgram(self, ast: Program, o: ClassManager):
        reduce(lambda _, decl: self.visit(decl, o), ast.decl, [])
        
    def visitClassDecl(self, ast: ClassDecl, o: ClassManager):
        currentClass = o.classes[ast.classname.name]
        print(currentClass)
        reduce(lambda _, member: self.visit(member, o), ast.memlist, [])
    
    def visitAttributeDecl(self, ast: AttributeDecl, o: ClassManager):
        o.currentCheck = Attribute()
        self.visit(ast.decl,o)
        o.currentCheck = None
        
    def visitVarDecl(self, ast: VarDecl, o: ClassManager):
        if o.currentCheck == None:
            o.currentCheck = Variable()
            
        # check tên biến
        if o.currentCheck is not Attribute(): #Variable hoặc Parameter
            self.visit(ast.variable,o)
        
        # check type
        varDeclType = self.visit(ast.varType, o)
        if type(varDeclType) is VoidType:
            raise TypeMismatchInDeclaration(ast)
        
        # check giá trị khởi tạo có cùng type với biến
        if ast.varInit:
            res = self.visit(ast.varInit, o)
            
        
        
            
    def visitFor(self, ast: For, o: ClassManager):
        o.loop = True
        self.visit(ast.initStmt, o)
        self.visit(ast.expr, o)
        self.visit(ast.postStmt, o)
        
        o.loop = False
    
    def visitId(self, ast: Id, o: ClassManager):
        return o.checkUndeclaredRedeclared(ast.name, o.currentCheck, o.mode)
    
    def visitIntType(self, ast: IntType, o):
        return IntType()
    def visitFloatType(self, ast: FloatType, o):
        return FloatType()
    def visitBoolType(self, ast: BoolType, o):
        return BoolType()
    def visitStringType(self,ast: StringType, o):
        return StringType()
    def visitVoidType(self, ast: VoidType, o):
        return VoidType()
    def visitArrayType(self, ast: ArrayType, o):
        return ArrayType()
    def visitClassType(self, ast: ClassType, o):
        return ClassType()