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
import copy

class MemberEnv:
    pass
    
class MethodEnv(MemberEnv):
    name: Id
    paramList: List[Type]
    returnType: Type
    static: bool # có @ hay không
    
    def __init__(self, name: Id, paramList: List[Type], returnType: Type, static: bool):
        self.name = name
        self.paramList = paramList
        self.returnType = returnType
        self.static = static
        
    # def __eq__(self, value: object) -> bool:
    #     if type(value) != MethodEnv:
    #         return False
    #     if self.name.name != value.name.name:
    #         return False
    #     if list(map(lambda param: str(param), self.paramList)) != list(map(lambda param: str(param), value.paramList)):
    #         return False
    #     if self.returnType != value.returnType:
    #         return False
    #     return True

class AttributeEnv(MemberEnv):
    id: Id
    typ: Type
    isMutable: bool
    static: bool # có @ hay không
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
        
        if newClass.parentname: # có thừa kế
            parentName = newClass.parentname.name
            if parentName not in self.classes:
                raise Undeclared(Class(), parentName)
            self.classes[newClassName] = BKClass(newClass, Id(parentName), self)
        else: # không thừa kế
            self.classes[newClassName] = BKClass(newClass, manager=self)

    def checkNoEntryPoint(self):
        if "Program" not in self.classes:
            raise NoEntryPoint()
        programClass = self.classes["Program"]
        if "@main" not in programClass.members:
            raise NoEntryPoint()
    
    def checkForClassType(self, typ: Type):
        if type(typ) is ClassType:
            if typ.classname.name not in self.classes:
                raise Undeclared(Class(), typ.classname.name)
        return typ
    
    def get_class_env(self, class_name):
        return self.classes[class_name]

class StaticChecker(BaseVisitor,Utils):
    def __init__(self, ast):
        self.ast = ast
        
    def check(self):
        self.manager = ClassManager(self.ast)
        self.manager.checkNoEntryPoint()
        self.visit(self.ast, [])
        return ""
    
    def visit(self, ast, o):
        if type(ast) is Id:
            return self.visitId(ast, o)
        elif type(ast) is BinaryOp:
            return self.visitBinaryOp(ast, o)
        elif type(ast) is UnaryOp:
            return self.visitUnaryOp(ast, o)
        elif type(ast) is CallExpr:
            return self.visitCallExpr(ast, o)
        elif type(ast) is NewExpr:
            return self.visitNewExpr(ast, o)
        elif type(ast) is ArrayCell:
            return self.visitArrayCell(ast, o)
        elif type(ast) is FieldAccess:
            return self.visitFieldAccess(ast, o)
        elif type(ast) is IntLiteral:
            return self.visitIntLiteral(ast, o)
        elif type(ast) is FloatLiteral:
            return self.visitFloatLiteral(ast, o)
        elif type(ast) is StringLiteral:
            return self.visitStringLiteral(ast, o)
        elif type(ast) is BooleanLiteral:
            return self.visitBooleanLiteral(ast, o)
        elif type(ast) is NullLiteral:
            return self.visitNullLiteral(ast, o)
        elif type(ast) is SelfLiteral:
            return self.visitSelfLiteral(ast, o)
        elif type(ast) is ArrayLiteral:
            return self.visitArrayLiteral(ast, o)
        elif type(ast) is Assign:
            return self.visitAssign(ast, o)
        elif type(ast) is If:
            return self.visitIf(ast, o)
        elif type(ast) is For:
            return self.visitFor(ast, o)
        elif type(ast) is Break:
            return self.visitBreak(ast, o)
        elif type(ast) is Continue:
            return self.visitContinue(ast, o)
        elif type(ast) is Return:
            return self.visitReturn(ast, o)
        elif type(ast) is CallStmt:
            return self.visitCallStmt(ast, o)
        elif type(ast) is VarDecl:
            return self.visitVarDecl(ast, o)
        elif type(ast) is Block:
            return self.visitBlock(ast, o)
        elif type(ast) is ConstDecl:
            return self.visitConstDecl(ast, o)
        elif type(ast) is ClassDecl:
            return self.visitClassDecl(ast, o)
        elif type(ast) is MethodDecl:
            return self.visitMethodDecl(ast, o)
        elif type(ast) is AttributeDecl:
            return self.visitAttributeDecl(ast, o)
        elif type(ast) is IntType:
            return self.visitIntType(ast, o)
        elif type(ast) is FloatType:
            return self.visitFloatType(ast, o)
        elif type(ast) is BoolType:
            return self.visitBoolType(ast, o)
        elif type(ast) is StringType:
            return self.visitStringType(ast, o)
        elif type(ast) is ArrayType:
            return self.visitArrayType(ast, o)
        elif type(ast) is ClassType:
            return self.visitClassType(ast, o)
        elif type(ast) is VoidType:
            return self.visitVoidType(ast, o)
        elif type(ast) is Program:
            return self.visitProgram(ast, o)
    
    def visitProgram(self, ast, o):
        # print(self.manager.classes)
        for x in self.manager.classes.values():
            # self.visit(x, o)
            print(x.members)
        # [self.visit(x, o) for x in ast.decl]
        
    def visitClassDecl(self, ast: BKClass, o):
        classDecl = ast.classDecl
        parent = ast.parent
        manager = ast.manager
        print(classDecl)
        
    def visitIntLiteral(self, ast: IntLiteral, o):
        return IntType()
    def visitFloatLiteral(self, ast: FloatLiteral, o):
        return FloatType()
    def visitBoolLiteral(self, ast: BooleanLiteral, o):
        return BoolType()
    def visitStringLiteral(self,ast: StringLiteral,o):
        return StringType()
    def visitNullLiteraleral(self,ast: NullLiteral,o):
        return NullLiteral()
    
###############################################################################################################
# from abc import ABC, abstractmethod, ABCMeta
# #from Visitor import Visitor
# from dataclasses import dataclass
# from typing import List, Tuple


# class AST(ABC):
#     def __eq__(self, other): 
#         return self.__dict__ == other.__dict__

#     def accept(self, v, param):
#         method_name = 'visit{}'.format(self.__class__.__name__)
#         visit = getattr(v, method_name)
#         return visit(self,param)

# class Stmt(AST):
#     __metaclass__ = ABCMeta
#     pass

# class Expr(Stmt):
#     __metaclass__ = ABCMeta
#     pass

# class LHS(Expr):
#     __metaclass__ = ABCMeta
#     pass

# class Type(AST):
#     __metaclass__ = ABCMeta
#     pass

# class MemDecl(AST):
#     __metaclass__ = ABCMeta
#     pass

# @dataclass
# class Id(LHS):
#     name:str
#     def __str__(self):
#         return "Id(" + self.name + ")"
        

# # used for binary expression
# @dataclass
# class BinaryOp(Expr):
#     op:str
#     left:Expr
#     right:Expr
#     def __str__(self):
#         return "BinaryOp(" + self.op + "," + str(self.left) + "," + str(self.right) + ")"

# #used for unary expression with orerand like !,+,-
# @dataclass
# class UnaryOp(Expr):
#     op:str
#     body:Expr
#     def __str__(self):
#         return "UnaryOp(" + self.op + "," + str(self.body) + ")"

# @dataclass
# class CallExpr(Expr):
#     obj: Expr # None if there is no obj
#     method:Id
#     param:List[Expr]
#     def __str__(self):
#         return "CallExpr(" + ((str(self.obj) + ",") if self.obj else "") + str(self.method) + ",[" +  ','.join(str(i) for i in self.param) + "])"

# @dataclass
# class NewExpr(Expr):
#     classname:Id
#     param:List[Expr]
#     def __str__(self):
#         return "NewExpr(" + str(self.classname) + ",[" +  ','.join(str(i) for i in self.param) + "])"

# @dataclass
# class ArrayCell(LHS):
#     arr:Expr
#     idx:Expr
#     def __str__(self):
#         return "ArrayCell(" + str(self.arr) + "," + str(self.idx) + ")"

# @dataclass
# class FieldAccess(LHS):
#     obj:Expr # None if there is no obj
#     fieldname:Id
#     def __str__(self):
#         return "FieldAccess(" + ((str(self.obj) + ",") if self.obj else "") + str(self.fieldname) + ")"

# class Literal(Expr):
#     __metaclass__ = ABCMeta
#     pass

# @dataclass
# class IntLiteral(Literal):
#     value:int
#     def __str__(self):
#         return "IntLit(" + str(self.value) + ")"

# @dataclass
# class FloatLiteral(Literal):
#     value:float
#     def __str__(self):
#         return "FloatLit(" + str(self.value) + ")"

# @dataclass
# class StringLiteral(Literal):
#     value:str
#     def __str__(self):
#         return "StringLit(" + self.value + ")"

# @dataclass
# class BooleanLiteral(Literal):
#     value:bool
#     def __str__(self):
#         return "BooleanLit(" + str(self.value) + ")"

# class NullLiteral(Literal):
#     def __str__(self):
#         return "NullLiteral()"

# class SelfLiteral(Literal):
#     def __str__(self):
#         return "Self()"
# @dataclass
# class ArrayLiteral(Literal):
#     value: List[Literal]
#     def __str__(self):
#         return '[' + ','.join(str(i) for i in self.value)+ ']'
# class Decl(AST):
#     __metaclass__ = ABCMeta
#     pass
# class StoreDecl(Stmt):
#     __metaclass__ = ABCMeta
#     pass

# @dataclass
# class Block(Stmt):
#     stmt:List[Stmt] # empty list if there is no statement in block
#     def __str__(self):
#         return "Block([" + ','.join(str(i) for i in self.stmt) + "])"

# @dataclass
# class Assign(Stmt):
#     lhs:Expr
#     exp:Expr
#     def __str__(self):
#         return "AssignStmt(" + str(self.lhs) + "," +  str(self.exp) + ")"

# @dataclass
# class If(Stmt):
#     expr:Expr
#     thenStmt:Block
#     preStmt:Block = None # None if there is no pre-statement
#     elseStmt:Block = None # None if there is no else branch
#     def __str__(self):
#         return "If(" + ((str(self.preStmt) + ",") if self.preStmt else "") + str(self.expr) + "," + str(self.thenStmt) + (("," +  str(self.elseStmt)) if self.elseStmt else "")  + ")"

# @dataclass
# class For(Stmt):
#     initStmt:Assign
#     expr:Expr
#     postStmt:Assign
#     loop:Block  
#     def __str__(self):
#         return "For(" + str(self.initStmt) + "," + str(self.expr) + "," + str(self.postStmt) + ',' + str(self.loop)  + "])"

# class Break(Stmt):
#     def __str__(self):
#         return "Break"

# class Continue(Stmt):
#     def __str__(self):
#         return "Continue"

# @dataclass
# class Return(Stmt):
#     expr:Expr = None # None if there is no expression after return
#     def __str__(self):
#         return "Return(" + (str(self.expr)  if  self.expr else "") + ")"

# @dataclass
# class CallStmt(Stmt):
#     obj: Expr  # None if there is no obj 
#     method:Id
#     param:List[Expr]
#     def __str__(self):
#         return "Call(" + ((str(self.obj) + ",") if self.obj else "") + str(self.method) + ",[" +  ','.join(str(i) for i in self.param) + "])"

# # used for local variable or parameter declaration 
# @dataclass
# class VarDecl(StoreDecl):
#     variable : Id
#     varType : Type
#     varInit : Expr = None # None if there is no initial
#     def __str__(self):
#         return "VarDecl(" + str(self.variable) + "," + str(self.varType) + (","+ str(self.varInit) if self.varInit else "") + ")"
#     def toParam(self):
#         return "Param(" + str(self.variable) + "," + str(self.varType) + ")"


# # used for local constant declaration
# @dataclass
# class ConstDecl(StoreDecl):
#     constant : Id
#     constType : Type
#     value : Expr
#     def __str__(self):
#         return "ConstDecl(" + str(self.constant) + "," + str(self.constType) + "," + str(self.value) + ")"

 
# #used for a class declaration
# @dataclass
# class ClassDecl(Decl):
#     classname : Id
#     memlist : List[MemDecl]
#     parentname : Id = None # None if there is no parent
#     def __str__(self):
#         return "ClassDecl(" + str(self.classname) + (("," + str(self.parentname)) if self.parentname else "") + ",[" + ','.join(str(i) for i in self.memlist) + "])"



# # used for a normal or special method declaration. 
# # In the case of special method declaration, the return type is VoidType()
# @dataclass
# class MethodDecl(MemDecl):
#     name: Id
#     param: List[VarDecl]
#     returnType: Type  # VoidType for constructor
#     body: Block
#     def __str__(self):
#         return "MethodDecl(" + str(self.name) +  ",[" +  ','.join(i.toParam() for i in self.param) + "]," + ((str(self.returnType) ) if self.returnType else str(VoidType())) + "," + str(self.body) + ")"

# @dataclass
# class AttributeDecl(MemDecl):
#     decl: StoreDecl #VarDecl or ConstDecl
#     def __str__(self):
#         return "AttributeDecl(" +  str(self.decl) + ")"


# class IntType(Type):
#     def __str__(self):
#         return "IntType"

# class FloatType(Type):
#     def __str__(self):
#         return "FloatType"

# class BoolType(Type):
#     def __str__(self):
#         return "BoolType"

# class StringType(Type):
#     def __str__(self):
#         return "StringType"

# @dataclass
# class ArrayType(Type):
#     size : int
#     eleType:Type
#     def __str__(self):
#         return "ArrayType(" + str(self.size) +  "," + str(self.eleType) + ")"

# @dataclass
# class ClassType(Type):
#     classname:Id
#     def __str__(self):
#         return "ClassType(" + str(self.classname)  + ")"


# class VoidType(Type):
#     def __str__(self):
#         return "VoidType"


# # used for whole program
# @dataclass
# class Program(AST):
#     decl : List[ClassDecl]
#     def __str__(self):
#         return "Program([" + ','.join(str(i) for i in self.decl) + "])"