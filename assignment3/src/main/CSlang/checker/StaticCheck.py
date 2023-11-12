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

class Attribute_Check:
    def __init__(self, name: str, typ: Type, isStatic = False, constant = False):
        self.name = name
        self.typ = typ
        self.isStatic = isStatic
        self.constant = constant

class Variable_Check:
    def __init__(self, name, typ, scope, constant=False):
        self.name = name
        self.typ = typ
        self.scope = scope
        self.constant = constant

    def __eq__(self, other):
        if isinstance(other, Variable_Check):
            return self.name == other.name and self.typ == other.typ and self.scope == other.scope
        return False

    def get_type(self):
        return self.typ

class Method_Check:
    def __init__(self, method_name:str, static=False, para:List[VarDecl]=[], rettype=None):
        self.clsname = clsname
        self.name = method_name
        self.paratype = list(map(lambda x: x.varType, paratype))
        self.rettype = rettype
        self.isStatic = static
        self.inLoop = 0
        self.variable = {}
        self.scope = 1
        for var in para:
            self.var_decl(var.variable.name,var.varType)
        self.scope = 0

    def __eq__(self, other):
        if isinstance(other, Method_Check):
            return self.clsname == other.name and self.name == method_name and self.paratype == other.paratype
        return self.clsname == other.cls

    def enterScope(self):
        self.scope += 1

    def exitScope(self):
        self.scope -= 1
        for k, lst in self.variable.items():
            if lst[-1].scope > self.scope:
                self.id[k].pop()

    def enterLoop(self):
        self.inLoop += 1

    def exitLoop(self):
        self.inLoop -= 1  

    def _change_ret_type(self, rettype):
        self.rettype = rettype

    def _check_redeclared_variable(self, name):
        if name in self.variable:
            if self.variable[name][-1].scope == self.scope:
                raise Redeclared(Variable(),name)

    def _checkmain(self):
        return name == 'main'

    def get_type(self):
        return self.rettype

    def var_decl(self, name:str, typ:Type):
        self._check_redeclared_variable(name)
        if name not in self.variable:
            self.variable[name] = [Variable_Check(name,typ,self.scope)]
        else:
            self.variable[name] += [Variable_Check(name,typ,self.scope)]

    def const_decl(self, name:str, typ:Type):
        self._check_redeclared_variable(name)
        if name not in self.variable:
            self.variable[name] = [Variable_Check(name,typ,self.scope,True)]
        else:
            self.variable[name] += [Variable_Check(name,typ,self.scope,True)]

class Class_Check:
    def __init__(self, name: str, inherited = None):
        '''
        name : str
        inherited : Class_Check
        '''
        self.att = {}
        self.method = {}
        self.mro = []
        self.name = name
        if inherited:
            self.att = inherited.att.copy()
            self.method = inherited.method.copy()
            self.mro = [inherited.name] + inherited.mro.copy()

    def add_attribute(self, name: str, att_type: Type, isStatic=False, const=False):
        self._check_redeclared_attribute(name)
        self.att[name] = Attribute_Check(name,att_type,isStatic,const)

    def add_method(self, name: str, isStatic=False, paratype:List[VarDecl]=[], rettype=None):
        self._check_redeclared_method(name, typelst)
        self.method[name] = Method_Check(name,isStatic,paratype,rettype)

    def get_method(self, method_name: str):
        return self.method[method_name]

    def get_attribute(self, att_name: str):
        return self.att[att_name]

    def checkentry(self):
        return any([x.checkmain() for x in self.method] if self.method else [False])

    def _check_redeclared_method(self, name: str, typelst: List[VarDecl]):
        if name in self.method.keys() and self.method[name].paratype == list(map(lambda x: x.varType,typelst)):
            raise Redeclared(Method(), name)

    def _check_redeclared_attribute(self, name:str):
        if name in self.att:
            raise Redeclared(Attribute(),name)

class ClassManager:
    def __init__(self):
        self.objid = {}
        '''
        'id': Class_Check
        '''

    def add_class(self, cls_name:str, inherited:str = None):
        self._check_redeclared_class(cls_name)
        if inherited:
            self.objid[cls_name] = Class_Check(cls_name, self.objid[inherited])
        else:
            self.objid[cls_name] = Class_Check(cls_name)

    def add_method(self, cls_name:str, method_name:str, isStatic=False, paratype:List[VarDecl]=[], rettype = None):
        self.objid[cls_name].add_method(method_name, isStatic, paratype, rettype)

    def add_attribute(self, cls_name:str, att_name:str,att_type:Type,isStatic:bool,const:bool):
        self.objid[cls_name].add_attribute(att_name,att_type,isStatic,const)

    def get_class(self, class_name:str):
        return self.objid[class_name]

    def checkentry(self):
        if not any([x.checkentry() for x in self.objid.values()]):
            raise NoEntryPoint()

    def _check_redeclared_class(self, name:str):
        if name in self.objid.keys():
            raise Redeclared(Class(),name)

class StaticChecker(BaseVisitor,Utils):
    inttype = IntType()
    floattype = FloatType()
    voidtype = VoidType()
    booltype = BoolType()
    stringtype = StringType() 
    def __init__(self, ast):
        self.ast = ast
        self.io = [BKClass("io",None,[
                            Member("@readInt", MType([], StaticChecker.inttype), False),
                            Member("@writeInt", MType([StaticChecker.inttype], StaticChecker.voidtype), False),
                            Member("@readFloat", MType([], StaticChecker.floattype), False),
                            Member("@writeFloat", MType([StaticChecker.floattype], StaticChecker.voidtype), False),
                            Member("@readBool", MType([], StaticChecker.booltype), False),
                            Member("@writeBool", MType([StaticChecker.booltype], StaticChecker.voidtype), False),
                            Member("@readString", MType([], StaticChecker.stringtype), False),
                            Member("@writeString", MType([StaticChecker.stringtype], StaticChecker.voidtype), False),
                            ])]
    def check(self):
        self.visit(self.ast, self.io)
        return "successful"
    
    def visit(self, ast, c):
        if isinstance(ast, Id):
            return self.visitId(ast, c)
        elif isinstance(ast, BinaryOp):
            return self.visitBinaryOp(ast, c)
        elif isinstance(ast, UnaryOp):
            return self.visitUnaryOp(ast, c)
        elif isinstance(ast, CallExpr):
            return self.visitCallExpr(ast, c)
        elif isinstance(ast, NewExpr):
            return self.visitNewExpr(ast, c)
        elif isinstance(ast, ArrayCell):
            return self.visitArrayCell(ast, c)
        elif isinstance(ast, FieldAccess):
            return self.visitFieldAccess(ast, c)
        elif isinstance(ast, IntLiteral):
            return self.visitIntLiteral(ast, c)
        elif isinstance(ast, FloatLiteral):
            return self.visitFloatLiteral(ast, c)
        elif isinstance(ast, StringLiteral):
            return self.visitStringLiteral(ast, c)
        elif isinstance(ast, BooleanLiteral):
            return self.visitBooleanLiteral(ast, c)
        elif isinstance(ast, NullLiteral):
            return self.visitNullLiteral(ast, c)
        elif isinstance(ast, SelfLiteral):
            return self.visitSelfLiteral(ast, c)
        elif isinstance(ast, ArrayLiteral):
            return self.visitArrayLiteral(ast, c)
        elif isinstance(ast, Assign):
            return self.visitAssign(ast, c)
        elif isinstance(ast, If):
            return self.visitIf(ast, c)
        elif isinstance(ast, For):
            self.visitFor(ast, c)
        elif isinstance(ast, VarDecl):
            return self.visitVarDecl(ast, c)
        elif isinstance(ast, Block):
            return self.visitBlock(ast, c)
        elif isinstance(ast, ConstDecl):
            return self.visitConstDecl(ast, c)
        elif isinstance(ast, ClassDecl):
            return self.visitClassDecl(ast, c)
        elif isinstance(ast, MethodDecl):
            return self.visitMethodDecl(ast, c)
        elif isinstance(ast, AttributeDecl):
            return self.visitAttributeDecl(ast, c)
        elif isinstance(ast, IntType):
            return self.visitIntType(ast, c)
        elif isinstance(ast, FloatType):
            return self.visitFloatType(ast, c)
        elif isinstance(ast, BoolType):
            return self.visitBoolType(ast, c)
        elif isinstance(ast, StringType):
            return self.visitStringType(ast, c)
        elif isinstance(ast, ArrayType):
            return self.visitArrayType(ast, c)
        elif isinstance(ast, ClassType):
            return self.visitClassType(ast, c)
        elif isinstance(ast, VoidType):
            return self.visitVoidType(ast, c)
        elif type(ast) is Program:
            return self.visitProgram(ast, c)
        
    def visitProgram(self, ast, c = None):
        self.classmng = ClassManager()
        for x in ast.decl:
            self.visit(x,c)
        # [self.visit(x,c) for x in ast.decl]
        # if not self.classmng.checkentry():
        #     raise NoEntryPoint()
        
    def visitClassDecl(self, ast, c):
        if ast.parentname:
            self.classmng.add_class(ast.classname.name,ast.parentname.name)
        else:
            self.classmng.add_class(ast.classname.name)
        for x in ast.memlist:
            # print(x)
            print(self.visit(x,self.classmng.get_class(ast.classname.name)))
        # print(ast.classname.name)
        # [self.visit(x,self.classmng.get_class(ast.classname.name)) for x in ast.memlist]

    def visitAttributeDecl(self,ast,c):
        field = self.visit(ast.decl,c)
        return [field]+c

    def visitVarDecl(self, ast, c):
        if ast.variable.name in map(lambda x: x.name,c):
            raise Redeclared(Attribute(),ast.variable.name)
        return Member(ast.variable.name,ast.varType,True)
    
    def visitMethodDecl(self,ast, c: Class_Check):
        class_ = c[0]
        isStatic = type(ast.kind) is Static
        class_.add_method(ast.name.name,isStatic,ast.param)
        self.visit(ast.body,(c[0],class_.get_method(ast.name.name)))