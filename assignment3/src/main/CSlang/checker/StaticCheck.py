"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import *
from StaticError import *
from functools import reduce
from typing import Dict, List
import copy

class MemberEnv:
    pass
    
class MethodEnv(MemberEnv):
    name: Id
    paramList: List[Type]
    returnType: Type
    static: bool #có @ hay không
    
    def __init__(self, name: Id, paramList: List[Type], returnType: Type, static: bool):
        self.name = name
        self.paramList = paramList
        self.returnType = returnType
        self.static = static
        
    def __eq__(self, value: object) -> bool:
        if type(value) != MethodEnv:
            return False
        if self.name.name != value.name.name:
            return False
        if list(map(lambda param: str(param), self.paramList)) != list(map(lambda param: str(param), value.paramList)):
            return False
        if self.returnType != value.returnType:
            return False
        return True

class AttributeEnv(MemberEnv):
    id: Id
    typ: Type
    isMutable: bool
    static: bool #có @ hay không
    def __init__(self, id: Id, typ: Type, isMutable: bool, static: bool):
        self.id = id
        self.typ = typ
        self.isMutable = isMutable
        self.static = static

class BKClass:
    name: Id
    parent: Id
    members: Dict[str, MemberEnv]
    constructor: List[MethodEnv]
    
    def __init__(self, classDecl: ClassDecl, parent: Id = None, manager = None):
        self.constructor = []
        if classDecl:
            self.name = classDecl.classname
            self.parent = parent
            self.members = {}
            reduce(lambda _, mem: self.sortMember(mem, manager), classDecl.memlist, self.members)
        else:
            self.name = Id("io")
            self.members = {
                "@readInt": MethodEnv(Id("@readInt"), [], IntType(), True),
                "@writeInt": MethodEnv(Id("@writeInt"), [IntType()], VoidType(), True),
                "@readFloat": MethodEnv(Id("@readFloat"), [], FloatType(), True),
                "@writeFloat": MethodEnv(Id("@writeFloat"), [FloatType()], VoidType(), True),
                "@readBool": MethodEnv(Id("@readBool"), [], BoolType(), True),
                "@writeBool": MethodEnv(Id("@writeBool"), [BoolType()], VoidType(), True),
                "@readStr": MethodEnv(Id("@readStr"), [], StringType(), True),
                "@writeStr": MethodEnv(Id("@writeStr"), [StringType()], VoidType(), True)
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
        paramType = list(map(lambda el: manager.checkForClassType(el.varType), member.param))
        returnType = manager.checkForClassType(member.returnType)
        method = MethodEnv(Id(methodName), paramType, returnType, static = (methodName[0]=='@'))
                
        if methodName == "constructor":
            if any(map(lambda el: method == el, self.constructor)):
                raise Redeclared(Method(), methodName)
            else:
                self.constructor += [method]
        else:
            self.members[methodName] = method
            
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
        attributeType = manager.checkForClassType(member.constType)
        self.members[name] = AttributeEnv(Id(name), attributeType, isMutable = False, static = (name[0]=='@'))
        
    def processVariableAttribute(self, member: VarDecl,manager):
        name = member.variable.name
        if name in self.members:
            raise Redeclared(Attribute(), name)
        attributeType = manager.checkForClassType(member.varType)
        self.members[name] = AttributeEnv(Id(name), attributeType, isMutable = True, static = (name[0]=='@'))
        
class ClassManager:
    classes = Dict[str, BKClass]
    def __init__(self, ast: Program):
        self.classes = {
            "io": BKClass(None)
        }
        for classDecl in ast.decl:
            self.appendClass(classDecl)

    def appendClass(self, newClass: ClassDecl):
        newClassName = newClass.classname.name
        if newClassName in self.classes:
            raise Redeclared(Class(), newClassName)
        
        if newClass.parentname: #có thừa kế
            parentName = newClass.parentname.name
            if parentName not in self.classes:
                raise Undeclared(Class(), parentName)
            self.classes[newClassName] = BKClass(newClass, Id(parentName), self)
        else: #không thừa kế
            self.classes[newClassName] = BKClass(newClass, manager=self)

    def checkRedeclared(self):
        if "Program" not in self.classes:
            raise NoEntryPoint()
        programClass = self.classes["Program"]
        if "@main" not in programClass.members:
            raise NoEntryPoint()
        
    def getClassEnv(self, className: str) -> BKClass:
        return self.classes[className]
    
    def checkForClassType(self, typ: Type):
        if type(typ) is ClassType:
            if typ.classname.name not in self.classes:
                raise Undeclared(Class(), typ.classname.name)
        return typ

class StaticChecker(BaseVisitor,Utils):
    def __init__(self, ast):
        self.ast = ast
        
    def check(self):
        self.manager = ClassManager(self.ast)
        self.manager.checkRedeclared()
        return "successful"