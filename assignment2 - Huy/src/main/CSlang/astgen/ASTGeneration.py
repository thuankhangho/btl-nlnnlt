# Student ID: 2052496
# Name: Nguyễn Khánh Huy

from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *

class ASTGeneration(CSlangVisitor):

    def visitTypee(self,ctx:CSlangParser.TypeeContext):
        if ctx.BOOL():
            return BoolType()
        elif ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
    
    def visitTypev(self,ctx:CSlangParser.TypevContext):
        if ctx.BOOL():
            return BoolType()
        elif ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.VOID():
            return ctx.VOID().getText()

    def visitArr_type(self,ctx:CSlangParser.Arr_typeContext):
        return ArrayType(IntLiteral(),self.visit(ctx.typee()))

    def visitClass_type(self,ctx:CSlangParser.Class_typeContext):
        return ClassType(Id(ctx.IDENTIFIER().getText()))

    def visitLiteral(self,ctx:CSlangParser.LiteralContext): #INTLIT | FLOATLIT | BOOLLIT | STRLIT | SELF | NULL | arrlit | xdd;
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(False if ctx.BOOLLIT().getText() == ctx.FALSE().getText() else True)
        elif ctx.STRLIT():
            return StringLiteral(ctx.STRLIT().getText())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.NULL():
            return NullLiteral()
        elif ctx.arrlit():
            return self.visit(ctx.arrlit())
        return self.visit(ctx.xdd())
    
    def visitBreak_statement(self,ctx:CSlangParser.Break_statementContext):
        return Break()
    
    def visitContinue_statement(self,ctx:CSlangParser.Continue_statementContext):
        return Continue()
    
    def visitXdd(self,ctx:CSlangParser.XddContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.AT_ID():
            return Id(ctx.AT_ID().getText())
        
    def visitArr(self,ctx:CSlangParser.ArrContext):
        if ctx.getChildCount() == 1: return self.visit(ctx.literal())
        return self.visit(ctx.literal()) + self.visit(ctx.arr())
    
    def visitArrlit(self,ctx:CSlangParser.ArrlitContext):
        return self.visit(ctx.arr())
    
    def visitSuperX(self,ctx:CSlangParser.SuperXContext):
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        return None
    
    def visitProgram(self,ctx:CSlangParser.ProgramContext):
        return Program(self.visit(ctx.class_declarelist()))
    
    def visitClass_declarelist(self,ctx:CSlangParser.Class_declarelistContext):
        if ctx.getChildCount() == 0:  return []
        return [self.visit(ctx.class_declare())] + self.visit(ctx.class_declarelist())
    
    def visitClass_declare(self,ctx:CSlangParser.Class_declareContext):
        return ClassDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.list_of_member()),self.visit(ctx.superX()))
    
    def visitList_of_member(self,ctx:CSlangParser.List_of_memberContext):
        if ctx.getChildCount() == 0:  return []
        return [self.visit(ctx.member())] + self.visit(ctx.list_of_member())
    
    def visitMember(self,ctx:CSlangParser.MemberContext):
        if ctx.attribute(): return self.visit(ctx.attribute())
        return self.visit(ctx.method())
    
    def visitAttribute(self,ctx:CSlangParser.AttributeContext):
        if ctx.attribute1(): return self.visit(ctx.attribute1())
        return self.visit(ctx.attribute2())
    #sau nayf con lamf nua :sleep:

    def visitAttribute1(self, ctx:CSlangParser.Attribute1Context):
        if ctx.attribute1const():
            attribute1_const = self.visit(ctx.attribute1const())
            print(attribute1_const)
            res = []
            for x in attribute1_const:
                res.append(AttributeDecl(x))
            return res
        return self.visit(ctx.attribute1var())
    
    def visitAttribute1const(self, ctx:CSlangParser.Attribute1constContext):
        attribute_decl = self.visit(ctx.attributedecl())
        res = []
        for x in attribute_decl:
            res.append(ConstDecl(x["id"],x["type"],None))
        print(res)
        return res
    
    def visitAttributedecl(self, ctx:CSlangParser.AttributedeclContext):
        list_of_attribute = self.visit(ctx.list_of_attribute())
        type = self.visit(ctx.typeorarrtype())
        res = []
        for x in list_of_attribute:
            res.append(x, type)
        return res

    def visitTypeorarrtype(self,ctx:CSlangParser.TypeorarrtypeContext):
        if ctx.typee():
            return self.visit(ctx.typee())
        return self.visit(ctx.arr_type())
    
    def visitList_of_attribute(self, ctx:CSlangParser.List_of_attributeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.xdd())]
        return [self.visit(ctx.xdd())] + self.visit(ctx.list_of_attribute())

    def visitMethod(self,ctx:CSlangParser.MethodContext):
        if ctx.constructor(): return self.visit(ctx.constructor())
        return MethodDecl(self.visit(ctx.xdd()),self.visit(ctx.list_of_param()),self.visit(ctx.typev()),self.visit(ctx.block_statement()))
    
    def visitList_of_param(self,ctx:CSlangParser.List_of_paramContext):
        if ctx.list_of_param1(): return self.visit(ctx.list_of_param1())
        return self.visit(ctx.list_of_param2())

    def visitList_of_param1(self,ctx:CSlangParser.List_of_param1Context):
        if ctx.getChildCount() == 0:  return []
        return self.visit(ctx.primee())
    
    def visitPrimee(self,ctx:CSlangParser.PrimeeContext):
        if ctx.getChildCount() == 1:  return [self.visit(ctx.param_declare())]
        return [self.visit(ctx.param_declare())] + self.visit(ctx.primee())

    def visitParam_declare(self,ctx:CSlangParser.Param_declareContext):
        return VarDecl(ctx.IDENTIFIER().getText(),self.visit(ctx.typee()))

    def visitConstructor(self,ctx:CSlangParser.ConstructorContext):
        return MethodDecl(Id(ctx.CONSTRUCTOR().getText()),self.visit(ctx.list_of_param()),VoidType(),self.visit(ctx.block_statement()))

    def visitVar_const_statement(self,ctx:CSlangParser.Var_const_statementContext):
        return self.visit(ctx.attribute())

    def visitAss_statement(self,ctx:CSlangParser.Ass_statementContext):
        return self.visit(ctx.lhs()) + self.visit(ctx.exp())
    
    def visitIf_statement(self,ctx:CSlangParser.If_statementContext):
        if ctx.getChildCount() == 3: return If(self.visit(ctx.exp()),self.visit(ctx.block_statement()))
        elif ctx.getChildCount() == 4: return If(self.visit(ctx.exp()),self.visit(ctx.block_statement()), self.visit(ctx.block_statement()))
        elif ctx.getChildCount() == 5: return If(self.visit(ctx.exp()),self.visit(ctx.block_statement()), None ,self.visit(ctx.block_statement()))
        return If(self.visit(ctx.exp()),self.visit(ctx.block_statement()), self.visit(ctx.block_statement()) ,self.visit(ctx.block_statement()))
    
    def visitFor_statement(self,ctx:CSlangParser.For_statementContext):
        return For(self.visit(ctx.ass_statement()),self.visit(ctx.exp()),self.visit(ctx.assex_statement()),self.visit(ctx.block_statement()))

    def visitReturn_statement(self,ctx:CSlangParser.Return_statementContext):
         if ctx.exp(): return Return(self.visit(ctx.exp()))
         return Return(None)

    def visitBlock_statement(self,ctx:CSlangParser.Block_statementContext):
        return Block(self.visit(ctx.list_of_statement()))
    
    def visitList_of_statement(self,ctx:CSlangParser.List_of_statementContext):
        if ctx.getChildCount() == 0:  return []
        return [self.visit(ctx.statement())] + self.visit(ctx.list_of_statement())
    
    def visitStatement(self,ctx:CSlangParser.StatementContext):
        if ctx.var_const_statement(): return self.visit(ctx.var_const_statement())
        elif ctx.ass_statement(): return self.visit(ctx.ass_statement())
        elif ctx.if_statement(): return self.visit(ctx.if_statement())
        elif ctx.for_statement(): return self.visit(ctx.for_statement())
        elif ctx.break_statement(): return self.visit(ctx.break_statement())
        elif ctx.continue_statement(): return self.visit(ctx.continue_statement())
        elif ctx.return_statement(): return self.visit(ctx.return_statement())
        elif ctx.method_invocation_statement(): return self.visit(ctx.method_invocation_statement())
        return self.visit(ctx.block_statement())
    
from abc import ABC, abstractmethod, ABCMeta
#from Visitor import Visitor
from dataclasses import dataclass
from typing import List, Tuple


class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    def accept(self, v, param):
        method_name = 'visit{}'.format(self.__class__.__name__)
        visit = getattr(v, method_name)
        return visit(self,param)

class Stmt(AST):
    __metaclass__ = ABCMeta
    pass

class Expr(Stmt):
    __metaclass__ = ABCMeta
    pass

class LHS(Expr):
    __metaclass__ = ABCMeta
    pass

class Type(AST):
    __metaclass__ = ABCMeta
    pass

class MemDecl(AST):
    __metaclass__ = ABCMeta
    pass

@dataclass
class Id(LHS):
    name:str
    def __str__(self):
        return "Id(" + self.name + ")"
        

# used for binary expression
@dataclass
class BinaryOp(Expr):
    op:str
    left:Expr
    right:Expr
    def __str__(self):
        return "BinaryOp(" + self.op + "," + str(self.left) + "," + str(self.right) + ")"

#used for unary expression with orerand like !,+,-
@dataclass
class UnaryOp(Expr):
    op:str
    body:Expr
    def __str__(self):
        return "UnaryOp(" + self.op + "," + str(self.body) + ")"

@dataclass
class CallExpr(Expr):
    obj: Expr # None if there is no obj
    method:Id
    param:List[Expr]
    def __str__(self):
        return "CallExpr(" + ((str(self.obj) + ",") if self.obj else "") + str(self.method) + ",[" +  ','.join(str(i) for i in self.param) + "])"

@dataclass
class NewExpr(Expr):
    classname:Id
    param:List[Expr]
    def __str__(self):
        return "NewExpr(" + str(self.classname) + ",[" +  ','.join(str(i) for i in self.param) + "])"

@dataclass
class ArrayCell(LHS):
    arr:Expr
    idx:Expr
    def __str__(self):
        return "ArrayCell(" + str(self.arr) + "," + str(self.idx) + ")"

@dataclass
class FieldAccess(LHS):
    obj:Expr # None if there is no obj
    fieldname:Id
    def __str__(self):
        return "FieldAccess(" + ((str(self.obj) + ",") if self.obj else "") + str(self.fieldname) + ")"

class Literal(Expr):
    __metaclass__ = ABCMeta
    pass

@dataclass
class IntLiteral(Literal):
    value:int
    def __str__(self):
        return "IntLit(" + str(self.value) + ")"

@dataclass
class FloatLiteral(Literal):
    value:float
    def __str__(self):
        return "FloatLit(" + str(self.value) + ")"

@dataclass
class StringLiteral(Literal):
    value:str
    def __str__(self):
        return "StringLit(" + self.value + ")"

@dataclass
class BooleanLiteral(Literal):
    value:bool
    def __str__(self):
        return "BooleanLit(" + str(self.value) + ")"

class NullLiteral(Literal):
    def __str__(self):
        return "NullLiteral()"

class SelfLiteral(Literal):
    def __str__(self):
        return "Self()"
@dataclass
class ArrayLiteral(Literal):
    value: List[Literal]
    def __str__(self):
        return '[' + ','.join(str(i) for i in self.value)+ ']'
class Decl(AST):
    __metaclass__ = ABCMeta
    pass
class StoreDecl(Stmt):
    __metaclass__ = ABCMeta
    pass

@dataclass
class Block(Stmt):
    stmt:List[Stmt] # empty list if there is no statement in block
    def __str__(self):
        return "Block([" + ','.join(str(i) for i in self.stmt) + "])"

@dataclass
class Assign(Stmt):
    lhs:Expr
    exp:Expr
    def __str__(self):
        return "AssignStmt(" + str(self.lhs) + "," +  str(self.exp) + ")"

@dataclass
class If(Stmt):
    expr:Expr
    thenStmt:Block
    preStmt:Block = None # None if there is no pre-statement
    elseStmt:Block = None # None if there is no else branch
    def __str__(self):
        return "If(" + ((str(self.preStmt) + ",") if self.preStmt else "") + str(self.expr) + "," + str(self.thenStmt) + (("," +  str(self.elseStmt)) if self.elseStmt else "")  + ")"

@dataclass
class For(Stmt):
    initStmt:Assign
    expr:Expr
    postStmt:Assign
    loop:Block  
    def __str__(self):
        return "For(" + str(self.initStmt) + "," + str(self.expr) + "," + str(self.postStmt) + ',' + str(self.loop)  + "])"

class Break(Stmt):
    def __str__(self):
        return "Break"

class Continue(Stmt):
    def __str__(self):
        return "Continue"

@dataclass
class Return(Stmt):
    expr:Expr
    def __str__(self):
        return "Return(" + (str(self.expr)  if  self.expr else "") + ")"

@dataclass
class CallStmt(Stmt):
    obj: Expr  # None if there is no obj 
    method:Id
    param:List[Expr]
    def __str__(self):
        return "Call(" + ((str(self.obj) + ",") if self.obj else "") + str(self.method) + ",[" +  ','.join(str(i) for i in self.param) + "])"

# used for local variable or parameter declaration 
@dataclass
class VarDecl(StoreDecl):
    variable : Id
    varType : Type
    varInit : Expr = None # None if there is no initial
    def __str__(self):
        return "VarDecl(" + str(self.variable) + "," + str(self.varType) + (","+ str(self.varInit) if self.varInit else "") + ")"
    def toParam(self):
        return "Param(" + str(self.variable) + "," + str(self.varType) + ")"


# used for local constant declaration
@dataclass
class ConstDecl(StoreDecl):
    constant : Id
    constType : Type
    value : Expr
    def __str__(self):
        return "ConstDecl(" + str(self.constant) + "," + str(self.constType) + "," + str(self.value) + ")"

 
#used for a class declaration
@dataclass
class ClassDecl(Decl):
    classname : Id
    memlist : List[MemDecl]
    parentname : Id = None # None if there is no parent
    def __str__(self):
        return "ClassDecl(" + str(self.classname) + (("," + str(self.parentname)) if self.parentname else "") + ",[" + ','.join(str(i) for i in self.memlist) + "])"



# used for a normal or special method declaration. 
# In the case of special method declaration, the return type is VoidType()
@dataclass
class MethodDecl(MemDecl):
    name: Id
    param: List[VarDecl]
    returnType: Type  # VoidType for constructor
    body: Block
    def __str__(self):
        return "MethodDecl(" + str(self.name) +  ",[" +  ','.join(i.toParam() for i in self.param) + "]," + ((str(self.returnType) ) if self.returnType else str(VoidType())) + "," + str(self.body) + ")"

@dataclass
class AttributeDecl(MemDecl):
    decl: StoreDecl #VarDecl or ConstDecl
    def __str__(self):
        return "AttributeDecl(" +  str(self.decl) + ")"


class IntType(Type):
    def __str__(self):
        return "IntType"

class FloatType(Type):
    def __str__(self):
        return "FloatType"

class BoolType(Type):
    def __str__(self):
        return "BoolType"

class StringType(Type):
    def __str__(self):
        return "StringType"

@dataclass
class ArrayType(Type):
    size : int
    eleType:Type
    def __str__(self):
        return "ArrayType(" + str(self.size) +  "," + str(self.eleType) + ")"

@dataclass
class ClassType(Type):
    classname:Id
    def __str__(self):
        return "ClassType(" + str(self.classname)  + ")"


class VoidType(Type):
    def __str__(self):
        return "VoidType"


# used for whole program
@dataclass
class Program(AST):
    decl : List[ClassDecl]
    def __str__(self):
        return "Program([" + ','.join(str(i) for i in self.decl) + "])"
