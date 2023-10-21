from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *

class ASTGeneration(CSlangVisitor):

    def visitProgram(self,ctx:CSlangParser.ProgramContext):
        return Program(self.visit(ctx.decllist()))
    
    # decllist: classdecl decllist | ;
    def visitDecllist(self, ctx:CSlangParser.DecllistContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.classdecl())] + self.visit(ctx.decllist())

    # classdecl: CLASS (superpart | ) ID LCB memberlist RCB;
    def visitClassdecl(self, ctx:CSlangParser.ClassdeclContext):
        if ctx.superpart():
            return ClassDecl(Id(ctx.ID().getText()), self.visit(ctx.memberlist()), self.visit(ctx.superpart()))
        return ClassDecl(Id(ctx.ID().getText()), self.visit(ctx.memberlist()))
    
    def visitMemberlist(self, ctx:CSlangParser.MemberlistContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.member())] + self.visit(ctx.memberlist())
    
    def visitMember(self, ctx:CSlangParser.MemberContext):
        return self.visit(ctx.attributedecl()) if ctx.attributedecl() else self.visit(ctx.methoddecl())
    
    # vardecl | constdecl;
    def visitAttributedecl(self, ctx:CSlangParser.AttributedeclContext):
        if ctx.VAR():
            return AttributeDecl(self.visit(ctx.vardecl()))
        return AttributeDecl(self.visit(ctx.constdecl()))
    
    # attributewithdeclare | attributenodeclare;
    def visitVardecl(self, ctx:CSlangParser.VardeclContext):
        if ctx.attributewithdeclare():
            return self.visit(ctx.attributewithdeclare())
        return self.visit(ctx.attributenodeclare())
        
    # attlist SM;
    def visitAttributewithdeclare(self, ctx:CSlangParser.AttributewithdeclareContext):
        return self.visit(ctx.attlist())
    
    # identifier CM attlist CM INTLIT | identifier COLON typedecl DECLARE INTLIT;
    # def visitAttlist(self, ctx:CSlangParser.AttlistContext):
    

    # FUNC identifier LRB parameterlist RRB COLON (typ | VOID | arraydecl) blockstate;
    def visitMethoddecl(self, ctx:CSlangParser.MethoddeclContext):
        return MethodDecl(self.visit(ctx.identifier()), self.visit(ctx.parameterlist()), self.visit(ctx.typ()), self.visit(ctx.blockstate()))

    # parameterprime | ;
    def visitParameterlist(self, ctx:CSlangParser.ParameterlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.parameterprime())
    
    # parameterpart1 | parameterpart2;
    def visitParameterprime(self, ctx:CSlangParser.ParameterprimeContext):
        if ctx.parameterpart1():
            return self.visit(ctx.parameterpart1())
        return self.visit(ctx.parameterpart2())
    
    # (ID COLON typ) CM parameterpart1 | (ID COLON typ);
    def visitParameterpart1(self, ctx:CSlangParser.Parameterpart1Context):
        if ctx.getChildCount() == 5:
            return [VarDecl(self.visit(ctx.identifier()), self.visit(ctx.typ()))] + self.visit(ctx.parameterpart1())
        return [VarDecl(self.visit(ctx.identifier()), self.visit(ctx.typ()))]

    # LCB stmtlist RCB;
    def visitBlockstate(self, ctx:CSlangParser.BlockstateContext):
        return Block(self.visit(ctx.stmtlist()))
    
    # stmt stmtlist | ;
    def visitStmtlist(self, ctx:CSlangParser.StmtlistContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist())
    
    def visitStmt(self, ctx:CSlangParser.StmtContext):
        return self.visit(ctx.Returnstate())

    # typ | arraydecl;
    def visitTypedecl(self, ctx:CSlangParser.TypedeclContext):
        return self.visit(ctx.typ()) if ctx.typ() else self.visit(ctx.arraydecl())

    # CONTINUE SM;
    def visitContinuestate(self, ctx:CSlangParser.ContinuestateContext):
        return Continue()
    
    # BREAK SM;
    def visitBreakstate(self, ctx:CSlangParser.BreakstateContext):
        return Break()
    
    # RETURN (exp | ) SM;
    def visitReturnstate(self, ctx:CSlangParser.ReturnstateContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        return Return()

    # LSB INTLIT RSB typ;
    def visitArraydecl(self, ctx:CSlangParser.ArraydeclContext):
        return ArrayType(ctx.INT().getType(), self.visit(ctx.typ()))
    
    # BOOL | INT | FLOAT | STRING | ID;
    def visitTyp(self, ctx:CSlangParser.TypContext):
        if ctx.BOOL():
            return BoolType()
        elif ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        return Id()

    # ID | ATIDENTIFIER;
    def visitIdentifer(self, ctx:CSlangParser.IdentifierContext):
        return Id() if ctx.ID() else ctx.ATIDENTIFIER()
    
    # LSB literallist RSB;
    def visitArraylit(self, ctx:CSlangParser.ArraylitContext):
        return ArrayLiteral(self.visit(ctx.literallist()))

    # (INTLIT | FLOATLIT | boolit | STRINGLIT | NULL) CM literallist | (INTLIT | FLOATLIT | boolit | STRINGLIT | NULL);
    def visitLiterallist(self, ctx:CSlangParser.LiterallistContext):
        return [self.visit(ctx.literal())]

    # INTLIT | FLOATLIT | boolit | STRINGLIT | arraylit;
    def visitLiteral(self, ctx:CSlangParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral()
        elif ctx.FLOATLIT():
            return FloatLiteral()
        elif ctx.STRINGLIT():
            return StringLiteral()
        elif ctx.BOOLLIT():
            return BooleanLiteral()
        elif ctx.NULL():
            return NullLiteral()
        elif ctx.SELF():
            return SelfLiteral()
        

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