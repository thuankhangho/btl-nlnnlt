"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils, MType
from StaticError import *
from functools import reduce
import copy


class Member:
    def __init__(self,n,t,isMu=False):
        self.name = n
        self.typ = t
        self.isMu = isMu
    def __str__(self):
        return "Member("+self.name+","+str(self.typ)+","+str(self.kind)+","+str(self.isMu)+")"

class BKClass:
    def __init__(self,n,p,m):
        self.name = n
        self.parent = p
        self.member = m
    def __str__(self):
        return "Class("+self.name+","+(self.parent if type(self.parent) == str else "None" if self.parent is None else self.parent.name)+",["+",".join(str(i) for i in self.member) +"])"


class StaticChecker(BaseVisitor,Utils):
    inttype = IntType()
    floattype = FloatType()
    voidtype = VoidType()
    booltype = BoolType()
    stringtype = StringType() 
    def __init__(self,ast):
        self.ast = ast
        self.io = [BKClass("io",None,[
                            Member("@readInt",MType([],StaticChecker.inttype),False),
                            Member("@writeIntLn",MType([StaticChecker.inttype],StaticChecker.voidtype),False),
                            ])]
    def check(self):
        self.visit(self.ast,self.io)
        return "successful"

    def visitProgram(self,ast, c):
        env = reduce(lambda a,e: self.visit(e,a), ast.decl,c)
        
    def visitClassDecl(self, ast, c):
        if ast.classname.name in map(lambda x: x.name,c):
            raise Redeclared(Class(),ast.classname.name)
        mem = reduce(lambda a,e: self.visit(e,a) ,ast.memlist,[])
        return [BKClass(ast.classname.name,ast.parentname,mem)]+c

    def visitAttributeDecl(self,ast,c):
        field = self.visit(ast.decl,c) 
        return [field]+c

    def visitVarDecl(self, ast, c):
        if ast.variable.name in map(lambda x: x.name,c):
            raise Redeclared(Attribute(),ast.variable.name)
        return Member(ast.variable.name,ast.varType,True)
    
    def visitIntType(self, ast, c):
        return inttype
    
    def visitFloatType(self, ast, c):
        return floattype
    
    def visitBoolType(self, ast, c):
        return booltype
    
    def visitStringType(self, ast, c):
        return stringtype
    
    def visitVoidType(self, ast, c):
        return voidtype
    
    def visitArrayType(self, ast, c):
        ArrayType
        return None
    
    def visitClassType(self, ast, c):
        return None
    
    def visitBinaryOp(self, ast, c):
        return None
    
    def visitUnaryOp(self, ast, c):
        return None
    
    def visitCallExpr(self, ast, c):
        return None
    
    def visitNewExpr(self, ast, c):
        return None
    
    def visitId(self, ast, c):
        return None
    
    def visitArrayCell(self, ast, c):
        return None
    
    def visitFieldAccess(self, ast, c):
        return None
    
    def visitBlock(self, ast, c):
        return None
    
    def visitIf(self, ast, c):
        return None
    
    def visitFor(self, ast, c):
        return None
    
    def visitContinue(self, ast, c):
        return None
    
    def visitBreak(self, ast, c):
        return None
    
    def visitReturn(self, ast, c):
        return None
    
    def visitAssign(self, ast, c):
        return None
    
    def visitCallStmt(self, ast, c):
        return None
    
    def visitIntLiteral(self, ast, c):
        return None
    
    def visitFloatLiteral(self, ast, c):
        return None
    
    def visitBooleanLiteral(self, ast, c):
        return None
    
    def visitStringLiteral(self, ast, c):
        return None
    
    def visitNullLiteral(self, ast, c):
        return None
    
    def visitSelfLiteral(self, ast, c):
        return None 
        
    def visitArrayLiteral(self, ast, c):
        return None 
