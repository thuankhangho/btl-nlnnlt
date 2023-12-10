
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils, MType
from StaticError import *

#region Custom
from ClassEnv import *
from TypeRes import *
#endregion

from functools import reduce
import copy

class StaticChecker(BaseVisitor,Utils):
    def __init__(self,ast):
        self.ast = ast
        

    def check(self):
        self.manager = ClassManager(self.ast)
        self.manager.check_entry()
        self.visit(self.ast,[])
        return ""

    def visitProgram(self,ast,o):
        env = reduce(lambda _,el:self.visit(el,o),ast.decl,[])
        
    def visitClassDecl(self, ast:ClassDecl, o):
        o = {
            "env": self.manager.get_class_env(ast.classname.name),  # const in class
            "class": ast.classname.name,                            # const in class
            "scope": [{}],              
            "type": None
        }
        
        reduce(lambda _,mem:self.visit(mem,o),ast.memlist,o)
    
    def visitAttributeDecl(self,ast:AttributeDecl,o):
        o["type"] = Attribute()
        self.visit(ast.decl,o)
        o["type"] = None

    def visitMethodDecl(self,ast:MethodDecl,o):
        o["type"] = Method()
        # self.visit()
        o["type"] = None

    def visitVarDecl(self,ast:VarDecl,o):
        name = ast.variable.name
        if(name in o["scope"][0]):
            if(str(o["type"])=="Attribute"):
                raise Redeclared(Attribute(),name)
            else:
                pass
        
        typ = self.visit(ast.varType,o)
        expr = self.visit(ast.varInit,o)
    def visitConstDecl(self,ast:ConstDecl,o):
        pass

#region Type
    def visitIntType(self,ast:IntType,o):
        return self.manager.check_class_type(ast)
    def visitFloatType(self,ast:FloatType,o):
        return self.manager.check_class_type(ast)
    def visitBoolType(self,ast:BoolType,o):
        return self.manager.check_class_type(ast)
    def visitStringType(self,ast:StringType,o):
        return self.manager.check_class_type(ast)
    def visitVoidType(self,ast:VoidType,o):
        return self.manager.check_class_type(ast)
    def visitArrayType(self,ast:ArrayType,o):
        self.manager.check_class_type(ast.eleType)
        return ast
    def visitClassType(self,ast:ClassType,o):
        return self.manager.check_class_type(ast)
#endregion
#region Literal
    def visitIntLiteral(self,ast:IntLiteral,o):
        return IntType()
    def visitFloatLiteral(self,ast:FloatLiteral,o):
        return FloatType()
    def visitBooleanLiteral(self,ast:BooleanLiteral,o):
        return BoolType()
    def visitStringLiteral(self,ast:StringLiteral,o):
        return StringType()
    def visitNullLiteral(self,ast:NullLiteral,o):
        return NullLiteral()
    def visitSelfLiteral(self,ast:SelfLiteral,o):
        return ClassType(o["class"])
    def visitArrayLiteral(self,ast:ArrayLiteral,o):
        typ = VoidType()
        for lit in ast.value:
            lit_typ = self.visit(lit,o)
            if(typ == None):
                if(str(lit_typ)!= "NullLiteral()"):
                    typ=lit_typ
            else:
                if(str(typ)!=str(lit_typ)):
                    raise IllegalArrayLiteral(ast)
        return ArrayType(len(ast.value,typ))
#endregion




# class Member:
#     def __init__(self,n,t,isMu=False):
#         self.name = n
#         self.typ = t
#         self.isMu = isMu
#     def __str__(self):
#         return "Member("+self.name+","+str(self.typ)+","+str(self.kind)+","+str(self.isMu)+")"

# class BKClass:
#     def __init__(self,n,p,m):
#         self.name = n
#         self.parent = p
#         self.member = m
#     def __str__(self):
#         return "Class("+self.name+","+(self.parent if type(self.parent) == str else "None" if self.parent is None else self.parent.name)+",["+",".join(str(i) for i in self.member) +"])"


# class StaticChecker(BaseVisitor,Utils):
#     inttype = IntType()
#     floattype = FloatType()
#     voidtype = VoidType()
#     booltype = BoolType()
#     stringtype = StringType() 
#     def __init__(self,ast):
#         self.ast = ast
#         self.io = [BKClass("io",None,[
#                             Member("@readInt",MType([],StaticChecker.inttype),False),
#                             Member("@writeIntLn",MType([StaticChecker.inttype],StaticChecker.voidtype),False),
#                             ])]
#     def check(self):
#         self.visit(self.ast,self.io)
#         return "successful"

#     def visitProgram(self,ast, c):
#         env = reduce(lambda a,e: self.visit(e,a), ast.decl,c)
        
#     def visitClassDecl(self, ast, c):
#         if ast.classname.name in map(lambda x: x.name,c):
#             raise Redeclared(Class(),ast.classname.name)
#         mem = reduce(lambda a,e: self.visit(e,a) ,ast.memlist,[])
#         return [BKClass(ast.classname.name,ast.parentname,mem)]+c

#     def visitAttributeDecl(self,ast,c):
#         field = self.visit(ast.decl,c) 
#         return [field]+c

#     def visitVarDecl(self, ast, c):
#         if ast.variable.name in map(lambda x: x.name,c):
#             raise Redeclared(Attribute(),ast.variable.name)
#         return Member(ast.variable.name,ast.varType,True)