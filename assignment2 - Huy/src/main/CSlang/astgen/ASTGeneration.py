# Student ID: 2052496
# Name: Nguyễn Khánh Huy

from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *

class ASTGeneration(CSlangVisitor):    
    def visitProgram(self,ctx:CSlangParser.ProgramContext):
        return Program(self.visit(ctx.class_declarelist()))
    
    def visitClass_declarelist(self,ctx:CSlangParser.Class_declarelistContext):
        if ctx.getChildCount() == 0:  return []
        return [self.visit(ctx.class_declare())] + self.visit(ctx.class_declarelist())
    
    def visitClass_declare(self,ctx:CSlangParser.Class_declareContext):
        return ClassDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.list_of_member()),self.visit(ctx.superX()))
    
    def visitSuperX(self,ctx:CSlangParser.SuperXContext):
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        return None
    
    def visitList_of_member(self,ctx:CSlangParser.List_of_memberContext):
        if ctx.getChildCount() == 0:  return []
        res = []
        for x in self.visit(ctx.member()):
            res = res + [x]
        return res + self.visit(ctx.list_of_member())
        
    def visitMember(self,ctx:CSlangParser.MemberContext):
        if ctx.attribute():
            res = []
            for x in self.visit(ctx.attribute()):
                res = res + [AttributeDecl(x)]
            return res
        return [self.visit(ctx.method())]
    
    def visitAttribute(self,ctx:CSlangParser.AttributeContext): # attributeconst | attributevar;
        if ctx.attributeconst(): return self.visit(ctx.attributeconst())
        return self.visit(ctx.attributevar())

    def visitAttributeconst(self, ctx:CSlangParser.AttributeconstContext): # CONST attributedecl SM;
        res = []
        for x, y, z in self.visit(ctx.attributedecl()):
            res = res + [ConstDecl(x, y, z)]
        return res
    
    def visitAttributevar(self, ctx:CSlangParser.AttributevarContext): # VAR attributedecl SM;
        res = []
        for x, y, z in self.visit(ctx.attributedecl()):
            res = res + [VarDecl(x, y, z)]
        return res
    
    def visitAttributedecl(self, ctx:CSlangParser.AttributedeclContext): # attribute1 | attribute2;
        if ctx.attribute1():
            attribute1 = self.visit(ctx.attribute1())
            res = []
            for x in attribute1:
                res = res + [(x[0],x[1],None)]
            return res
        attribute2 = self.visit(ctx.attribute2())
        res = []
        for x in attribute2:
            res = res + [(x[0],x[2],x[1])]
        return res
    
    def visitAttribute1(self, ctx:CSlangParser.Attribute1Context): # list_of_attribute CL typeorarrtype;
        list_of_attribute = self.visit(ctx.list_of_attribute())
        type = self.visit(ctx.typeorarrtype())
        res = []
        for x in list_of_attribute:
            res.append((x, type))
        return res
    
    def visitList_of_attribute(self, ctx:CSlangParser.List_of_attributeContext): #xdd CM list_of_attribute | xdd ;
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.xdd())]
        return [self.visit(ctx.xdd())] + self.visit(ctx.list_of_attribute())
    
    def visitAttribute2(self, ctx:CSlangParser.Attribute2Context): # list_of_a
        attlist = self.visit(ctx.list_of_a())
        type = attlist[-1]
        attlist = attlist[0:len(attlist) - 1]
        attribute = []
        value = []
        for x in attlist:
            attribute = attribute + [x[0]]
            value = value + [x[1]]
        value.reverse()
        res = []
        for (x, y) in zip(attribute, value):
            res = res + [(x, y, type)]
        return res
    
    def visitList_of_a(self, ctx:CSlangParser.List_of_aContext): #xdd CM list_of_a CM exp | xdd CL typeorarrtype DECLARE exp ;
        if ctx.typeorarrtype():
            return [(self.visit(ctx.xdd()), self.visit(ctx.exp()))] + [self.visit(ctx.typeorarrtype())]
        return [(self.visit(ctx.xdd()), self.visit(ctx.exp()))] + self.visit(ctx.list_of_a())

#################################################################################################################################

    def visitMethod(self,ctx:CSlangParser.MethodContext): # FUNC xdd LB list_of_param RB CL typev block_statement | constructor;
        if ctx.constructor(): return self.visit(ctx.constructor())
        return MethodDecl(self.visit(ctx.xdd()),self.visit(ctx.list_of_param()),self.visit(ctx.typev()),self.visit(ctx.block_statement()))
    
    def visitList_of_param(self,ctx:CSlangParser.List_of_paramContext): # primee | ;
        if ctx.getChildCount() == 0: return []
        return self.visit(ctx.primee())

    def visitPrimee(self,ctx:CSlangParser.PrimeeContext): # list_of_param1 | list_of_param2;
        if ctx.list_of_param1(): return self.visit(ctx.list_of_param1())
        return self.visit(ctx.list_of_param2())
    
    def visitList_of_param1(self,ctx:CSlangParser.List_of_param1Context): # param_declare CM primee | param_declare;
        if ctx.getChildCount() == 1: return [self.visit(ctx.param_declare())]
        return [self.visit(ctx.param_declare())] + self.visit(ctx.primee())

    def visitParam_declare(self,ctx:CSlangParser.Param_declareContext): # IDENTIFIER CL typee;
        return VarDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.typee()))
    
    def visitList_of_param2(self,ctx:CSlangParser.List_of_param2Context): # list_of_identifier CL typee CM list_of_param2 | list_of_identifier CL typee;
        if ctx.getChildCount() == 5: return [self.visit(ctx.typee())] + [self.visit(ctx.list_of_identifier())] + self.visit(ctx.list_of_param2())
        return [self.visit(ctx.typee())] + [self.visit(ctx.list_of_identifier())] 
    
    def visitList_of_identifier(self, ctx:CSlangParser.List_of_identifierContext): # IDENTIFIER CM list_of_identifier | IDENTIFIER;
        if ctx.list_of_identifier(): return [Id(ctx.IDENTIFIER().getText())] + self.visit(ctx.list_of_identifier())
        return [Id(ctx.IDENTIFIER().getText())]

    def visitConstructor(self,ctx:CSlangParser.ConstructorContext): # FUNC CONSTRUCTOR LB list_of_param RB block_statement;
        return MethodDecl(Id(ctx.CONSTRUCTOR().getText()),self.visit(ctx.list_of_param()),VoidType(),self.visit(ctx.block_statement()))

#################################################################################################################################
    
    def visitExp(self, ctx:CSlangParser.ExpContext): # exp1 CONCAT exp1 | exp1;
        if ctx.CONCAT(): return BinaryOp(ctx.CONCAT().getText(), self.visit(ctx.exp1()[0]), self.visit(ctx.exp1()[1]))
        return self.visit(ctx.exp1()[0])
    
    def visitExp1(self, ctx:CSlangParser.Exp1Context): # exp2 relational_ops exp2| exp2;
        if ctx.getChildCount() == 3: return BinaryOp(self.visit(ctx.relational_ops()), self.visit(ctx.exp2()[0]),self.visit(ctx.exp2()[1]))
        return self.visit(ctx.exp2()[0])
    
    def visitExp2(self, ctx:CSlangParser.Exp2Context): # exp2 and_or exp3| exp3;
        if ctx.getChildCount() == 3: return BinaryOp(self.visit(ctx.and_or()), self.visit(ctx.exp2()),self.visit(ctx.exp3()))
        return self.visit(ctx.exp3())
    
    def visitExp3(self, ctx:CSlangParser.Exp3Context): # exp3 plus_minus exp4 | exp4;
        if ctx.getChildCount() == 3: return BinaryOp(self.visit(ctx.plus_minus()), self.visit(ctx.exp3()),self.visit(ctx.exp4()))
        return self.visit(ctx.exp4())
    
    def visitExp4(self, ctx:CSlangParser.Exp4Context): # exp4 divide_and_multiply exp5 | exp5;
        if ctx.getChildCount() == 3: return BinaryOp(self.visit(ctx.divide_and_multiply()), self.visit(ctx.exp4()),self.visit(ctx.exp5()))
        return self.visit(ctx.exp5())
    
    def visitExp5(self, ctx:CSlangParser.Exp5Context): # CHAMTHAN exp5 | exp6;
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.CHAMTHAN().getText(), self.visit(ctx.exp5()))
        return self.visit(ctx.exp6())
    
    def visitExp6(self, ctx:CSlangParser.Exp6Context): # MINUS exp6 | exp7;
        if ctx.getChildCount() == 2: return UnaryOp(ctx.MINUS().getText(), self.visit(ctx.exp6()))
        return self.visit(ctx.exp7())
    
    def visitExp7(self, ctx:CSlangParser.Exp7Context):
        if ctx.getChildCount() == 4:
            return ArrayCell(self.visit(ctx.exp8()), self.visit(ctx.exp()))
        return self.visit(ctx.exp8())
    
    def visitExp8(self, ctx:CSlangParser.Exp8Context): # exp8 DOT IDENTIFIER (LB list_of_exp RB | ) | exp9;
        if ctx.getChildCount() == 9:
            return CallExpr(ArrayCell(self.visit(ctx.exp8()), self.visit(ctx.exp())), Id(ctx.IDENTIFIER().getText()), self.visit(ctx.list_of_exp()))
        elif ctx.getChildCount() == 6:
            if ctx.list_of_exp():
                return CallExpr(self.visit(ctx.exp8()), Id(ctx.IDENTIFIER().getText()), self.visit(ctx.list_of_exp()))
            return FieldAccess(ArrayCell(self.visit(ctx.exp8()), self.visit(ctx.exp())), Id(ctx.IDENTIFIER().getText())) # exp8 LSB exp RSB DOT ID
        elif ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.exp8()), Id(ctx.IDENTIFIER().getText()))
        return self.visit(ctx.exp9())
    
    def visitExp9(self, ctx:CSlangParser.Exp9Context): # (IDENTIFIER DOT | ) AT_ID | (IDENTIFIER DOT | ) AT_ID LB list_of_exp RB | exp10;
        if ctx.getChildCount() == 6:
            return CallExpr(Id(ctx.IDENTIFIER().getText()), Id(ctx.AT_ID().getText()), self.visit(ctx.list_of_exp()))
        elif ctx.getChildCount() == 4:
            return CallExpr(None, Id(ctx.AT_ID().getText()), self.visit(ctx.list_of_exp()))
        elif ctx.getChildCount() == 3:
            return FieldAccess(Id(ctx.IDENTIFIER().getText()), Id(ctx.AT_ID().getText()))
        elif ctx.AT_ID():
            return FieldAccess(None,Id(ctx.AT_ID().getText()))
        elif ctx.exp10():
            return self.visit(ctx.exp10())

    def visitExp10(self, ctx:CSlangParser.Exp10Context): # NEW IDENTIFIER LB list_of_exp RB | exp11;
        if ctx.IDENTIFIER():
            return NewExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.list_of_exp()))
        return self.visit(ctx.exp11())
    
    def visitExp11(self, ctx:CSlangParser.Exp11Context): # LB exp RB | exp12;
        if ctx.exp():
            return self.visit(ctx.exp())
        return self.visit(ctx.exp12())
    
    def visitExp12(self, ctx:CSlangParser.Exp12Context): # literal;
        return self.visit(ctx.literal())
        
    def visitList_of_exp(self, ctx:CSlangParser.List_of_expContext): # primu | ;
        return self.visit(ctx.primu()) if ctx.primu() else []
    
    def visitPrimu(self, ctx:CSlangParser.PrimuContext): # primu: exp CM primu | exp;
        return self.visit(ctx.exp()) if ctx.getChildCount() == 1 else [self.visit(ctx.exp())] + self.visit(ctx.primu())
    
    def visitRelational_ops(self, ctx:CSlangParser.Relational_opsContext): # EQUAL | DIFFER | SMOL | BIG | SMOL_EQUAL | BIG_EQUAL;
        if ctx.EQUAL():
            return ctx.EQUAL().getText()
        elif ctx.DIFFER():
            return ctx.DIFFER().getText()
        elif ctx.SMOL():
            return ctx.SMOL().getText()
        elif ctx.BIG():
            return ctx.BIG().getText()
        elif ctx.SMOL_EQUAL():
            return ctx.SMOL_EQUAL().getText()
        return ctx.BIG_EQUAL().getText()
    
    def visitAnd_or(self, ctx:CSlangParser.And_orContext): # AND | OR;
        if ctx.AND():
            return ctx.AND().getText()
        return ctx.OR().getText()
    
    def visitPlus_minus(self, ctx:CSlangParser.Plus_minusContext): # PLUS | MINUS;
        if ctx.PLUS():
            return ctx.PLUS().getText()
        return ctx.MINUS().getText()
    
    def visitDivide_and_multiply(self, ctx:CSlangParser.Divide_and_multiplyContext): # MULTIPLY | DIVIDE_FLOAT | DIVIDE_INT | MOD;
        if ctx.MULTIPLY():
            return ctx.MULTIPLY().getText()
        elif ctx.DIVIDE_FLOAT():
            return ctx.DIVIDE_FLOAT().getText()
        elif ctx.DIVIDE_INT():
            return ctx.DIVIDE_INT().getText()
        return ctx.MOD().getText()

#################################################################################################################################

    def visitVar_const_statement(self,ctx:CSlangParser.Var_const_statementContext):
        return self.visit(ctx.attribute())

    def visitAss_statement(self,ctx:CSlangParser.Ass_statementContext): # lhs ASSIGN exp SM;
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.exp()))
    
    def visitIf_statement(self,ctx:CSlangParser.If_statementContext): # IF (block_statement |) exp block_statement (ELSE block_statement |);
        if ctx.getChildCount() == 3: return If(self.visit(ctx.exp()),self.visit(ctx.block_statement()[0]))
        elif ctx.getChildCount() == 4: return If(self.visit(ctx.exp()),self.visit(ctx.block_statement()[0]), self.visit(ctx.block_statement()[1]))
        elif ctx.getChildCount() == 5: return If(self.visit(ctx.exp()),self.visit(ctx.block_statement()[1]), None ,self.visit(ctx.block_statement()[0]))
        return If(self.visit(ctx.exp()),self.visit(ctx.block_statement()[0]), self.visit(ctx.block_statement()[1]) ,self.visit(ctx.block_statement()[2]))
    
    def visitFor_statement(self,ctx:CSlangParser.For_statementContext):
        return For(self.visit(ctx.ass_statement()),self.visit(ctx.exp()[0]),Assign(self.visit(ctx.exp()[1]),self.visit(ctx.exp()[1])),self.visit(ctx.block_statement()))

    def visitReturn_statement(self,ctx:CSlangParser.Return_statementContext):
        if ctx.exp(): return Return(self.visit(ctx.exp()))
        return Return(None)
     
    def visitBreak_statement(self,ctx:CSlangParser.Break_statementContext):
        return Break()
    
    def visitContinue_statement(self,ctx:CSlangParser.Continue_statementContext):
        return Continue()
    
    def visitMethod_invocation_statement(self, ctx:CSlangParser.Method_invocation_statementContext):
        if ctx.instance_method_invocation(): return self.visit(ctx.instance_method_invocation())
        return self.visit(ctx.static_method_invocation())
        
    def visitInstance_method_invocation(self, ctx:CSlangParser.Instance_method_invocationContext): # exp DOT IDENTIFIER LB list_of_exp RB;
        return CallStmt(self.visit(ctx.exp()), Id(ctx.IDENTIFIER().getText()), self.visit(ctx.list_of_exp()))
    
    def visitStatic_method_invocation(self, ctx:CSlangParser.Static_method_invocationContext): # (IDENTIFIER DOT |) AT_ID LB list_of_exp RB;
        if ctx.getChildCount() == 6:
            return CallStmt(Id(ctx.IDENTIFIER().getText()), Id(ctx.AT_ID().getText()), self.visit(ctx.list_of_exp()))
        return CallStmt(None, Id(ctx.AT_ID().getText()), self.visit(ctx.list_of_exp()))

    def visitBlock_statement(self,ctx:CSlangParser.Block_statementContext):
        return Block(self.visit(ctx.list_of_statement()))
    
    def visitList_of_statement(self,ctx:CSlangParser.List_of_statementContext):
        if ctx.getChildCount() == 0:  return []
        if (type(self.visit(ctx.statement()))) is list: return self.visit(ctx.statement()) + self.visit(ctx.list_of_statement())
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
            return ClassType(ctx.IDENTIFIER().getText())
        elif ctx.VOID():
            return VoidType()

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
            return BooleanLiteral(False if ctx.BOOLLIT().getText() == "False" else True)
        elif ctx.STRLIT():
            return StringLiteral(ctx.STRLIT().getText())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.NULL():
            return NullLiteral()
        elif ctx.arrlit():
            return self.visit(ctx.arrlit())
        return Id(self.visit(ctx.xdd()))
    
    def visitXdd(self,ctx:CSlangParser.XddContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.AT_ID():
            return Id(ctx.AT_ID().getText())
        
    def visitArr(self,ctx:CSlangParser.ArrContext):
        if ctx.getChildCount() == 1: return self.visit(ctx.literal())
        return self.visit(ctx.literal()) + self.visit(ctx.arr())
    
    def visitTypeorarrtype(self,ctx:CSlangParser.TypeorarrtypeContext): #typee|arr_type;
        if ctx.typee():
            return self.visit(ctx.typee())
        return self.visit(ctx.arr_type())

    
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
