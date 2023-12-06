"""
 * @author nhphung and ltkhanh
"""
from AST import * 
from Visitor import *
from Utils import Utils, MType
from StaticError import *
from functools import reduce
from typing import Dict, List
import copy

UNDECLARED = True
REDECLARED = False

class MembrEnv: pass

class AttrEnv(MembrEnv): 
    id: Id
    typ: Type
    isMutable: bool
    isStatic: bool
    
    def __init__(self, id, typ, isMutable, isStatic):
        self.id = id
        self.typ = typ
        self.isMutable = isMutable
        self.isStatic = isStatic
        
class MthdEnv(MembrEnv):
    id: Id
    param: List[Type]
    returnType: Type
    isStatic: bool
    
    def __init__(self, id, param, returnType, isStatic):
        self.id = id
        self.param = param
        self.returnType = returnType
        self.isStatic = isStatic
        
    # def __eq__(self, val):
    #     if type(val) != MthdEnv:
    #         return False
    #     if self.name.name != val.name.name:
    #         return False
    #     if list(map(lambda prm: str(prm), self.param)) != list(map(lambda prm: str(prm), val.param)):
    #         return False
    #     if self.returnType != val.returnType:
    #         return False
    #     return True    
    
class ClassEnv:
    classname: Id
    memlist: Dict[str, MembrEnv]
    staticmem: Dict[str, MembrEnv]
    prtname: Id
    constructors: List[MthdEnv]
    
    def __init__(self, classdecl: ClassDecl, parent: Id = None, glb = None):
        self.constructors = []
        if classdecl:
            self.name = classdecl.classname
            self.prtname = parent
            self.memlist = {}
            self.staticmem = {}
            reduce(lambda trash, x: self.extmem(x, glb), classdecl.memlist, self.memlist)
        else:
            self.name = Id("io")
            self.staticmem = {"@readInt": MthdEnv(Id("@readInt"), [], IntType(), True),
                "@writeInt": MthdEnv(Id("@writeInt"), [IntType()], VoidType(), True),
                "@readFloat": MthdEnv(Id("@readFloat"), [], FloatType(), True),
                "@writeFloat": MthdEnv(Id("@writeFloat"), [FloatType()], VoidType(), True),
                "@readBool": MthdEnv(Id("@readBool"), [], BoolType(), True),
                "@writeBool": MthdEnv(Id("@writeBool"), [BoolType()], VoidType(), True),
                "@readStr": MthdEnv(Id("@readStr"), [], StringType(), True),
                "@writeStr": MthdEnv(Id("@writeStr"), [StringType()], VoidType(), True)}
    
    def extmem(self, memdecl: MemDecl, glb):
        if type(memdecl) is AttributeDecl:
            self.extattr(memdecl, glb)
        else:
            self.extmthd(memdecl, glb)
            
    def extattr(self, attrdecl: AttributeDecl, glb):
        decl = attrdecl.decl
        if type(decl) is ConstDecl:
            self.extConstAttr(attrdecl.decl, glb) ###ConstDecl
        else:
            self.extVarAttr(attrdecl.decl, glb) ###VarDecl
            
    def extConstAttr(self, constdecl: ConstDecl, glb):
        name = constdecl.constant.name
        if name in self.memlist:
            raise Redeclared(Attribute(), name)
        else:
            attrType = glb.checkType(constdecl.constType)
            if name[0] != '@':
                self.memlist[name] = AttrEnv(Id(name), attrType, isMutable = False, isStatic = (name[0] == '@'))
            else:
                self.staticmem[name] = AttrEnv(Id(name), attrType, isMutable = False, isStatic = (name[0] == '@'))
            
    def extVarAttr(self, vardecl:VarDecl, glb):
        name = vardecl.variable.name
        if name in self.memlist:
            raise Redeclared(Attribute(), name)
        else:
            attrType = glb.checkType(vardecl.varType)
            if name[0] != '@':
                self.memlist[name]= AttrEnv(Id(name), attrType, isMutable = True, isStatic = (name[0] == '@'))
            else:
                self.memlist[name]= AttrEnv(Id(name), attrType, isMutable = True, isStatic = (name[0] == '@'))
            
    def extmthd(self, mthddecl: MethodDecl, glb):
        name = mthddecl.name.name
        if name in self.memlist and name != "constructor":
            raise Redeclared(Method(), name)
        param = list(map(lambda x: glb.checkType(x.varType), mthddecl.param))
        returnType = glb.checkType(mthddecl.returnType)
        mthd = MthdEnv(Id(name), param, returnType, isStatic = (name[0] == '@'))
        
        if name == "constructor":
            self.constructors.append(mthd)
        elif name[0] != '@':
            self.memlist[name] = mthd    
        else:
            self.staticmem[name] = mthd
            
class Global:
    lst = Dict[str, ClassEnv]
    def __init__(self, ast: Program):
        self.lst = {"io": ClassEnv(None)}
        self.currClass = None
        self.currEle = None
        self.check = False
        self.scope = []
        self.returnType = None
        self.looptime = 0
        for classdecl in ast.decl:
            self.newclass(classdecl)    
            
    def newclass(self, classdecl: ClassDecl):
        name = classdecl.classname.name
        if name in self.lst:
            raise Redeclared(Class(), name)
        else:
            if classdecl.parentname:
                parentname = classdecl.parentname.name
                if parentname not in self.lst:
                    raise Undeclared(Class(), parentname)
                else:
                    parentmemlist = self.lst[parentname].memlist
                    self.lst[name] = ClassEnv(classdecl, Id(parentname), self)
                    for mem in parentmemlist:
                         if mem not in self.classes[name].members:
                             self.classes[name].members[mem] = parentmemlist[mem]
            else:
                self.lst[name] = ClassEnv(classdecl, None, self)
                
    def checkPoint(self):
        if "Program" not in self.lst:
            raise NoEntryPoint()
        pgclass = self.lst["Program"]
        if "@main" not in pgclass.staticmem or isinstance(pgclass.staticmem["@main"], MthdEnv) is False or isinstance(pgclass.staticmem["@main"].returnType, VoidType) is False:
            raise NoEntryPoint()
        
    def checkType(self, typ: Type):
        if type(typ) == ClassType:
            if typ.classname.name not in self.lst:
                raise Undeclared(Class(), typ.classname.name)
        elif type(typ) == ArrayType:
            self.checkType(typ.eleType)
        else:
            return typ
        
    def cmpType(self, expr1, expr2):
        if type(expr1) == type(expr2):
            return True
        else: return False
        
    def getEle(self, name, errType, check):
        if check == REDECLARED:
            if name in self.scope[0]:
                raise Redeclared(errType, name)
        elif check == UNDECLARED:
            for scope in self.scope:
                if name in scope:
                    return scope[name]
            if type(errType) not in [Attribute, Method]:
                errType = Identifier()
            raise Undeclared(errType, name) 
        
class TypeDef:
    def __init__(self, Type, Id = None, isMutable = False):
        self.Type = Type
        self.Id = Id
        self.isMutable = isMutable

class StaticChecker(BaseVisitor,Utils):
    def __init__(self, ast):
        self.ast = ast
        
    def check(self):
        self.glb = Global(self.ast)
        self.glb.checkPoint()
        self.visit(self.ast, self.glb)
        return ""
    
    def visitProgram(self, ast, obj):
        reduce(lambda _, x: self.visit(x, obj), ast.decl, [])
        
    def visitClassDecl(self, ast, obj):
        obj.currClass = obj.lst[ast.classname.name]
        reduce(lambda _, x: self.visit(x, obj), ast.memlist, [])
    
    def visitAttributeDecl(self, ast, obj):
        obj.currEle = Attribute()
        self.visit(ast.decl, obj)
        obj.currEle = None
        
    def visitVarDecl(self, ast, obj):
        if obj.currEle == None:
            obj.currEle = Variable()
        VarDeclType = self.visit(ast.varType, obj)
        if type(obj.currEle) != Attribute:
            obj.check = REDECLARED
            self.visit(ast.variable, obj)
            obj.scope[0][ast.variable.name] = TypeDef(VarDeclType, ast.variable, True)
        if type(VarDeclType) == VoidType: ###################################################################
            raise TypeMismatchInDeclaration(ast)
        if ast.varInit != None:
            obj.check = UNDECLARED
            varInitType = self.visit(ast.varInit, obj)
            if obj.cmpType(VarDeclType, varInitType.Type) == False:
                raise TypeMismatchInDeclaration(ast)
            
    def visitConstDecl(self, ast, obj):
        if obj.currEle == None:
            obj.currEle = Constant()
        ConstDeclType = self.visit(ast.constType, obj)
        if type(obj.currEle) != Attribute:
            obj.check = REDECLARED
            self.visit(ast.constant, obj)
            obj.scope[0][ast.constant.name] = TypeDef(ConstDeclType, ast.constant, False)
        if type(ConstDeclType) == VoidType: ###################################################################
            raise TypeMismatchInDeclaration(ast)
        if ast.value != None:
            obj.check = UNDECLARED
            constInitType = self.visit(ast.value, obj)
            if obj.cmpType(ConstDeclType, constInitType.Type) == False:
                raise TypeMismatchInDeclaration(ast)
    
    def visitMethodDecl(self, ast, obj):
        obj.scope = [{}]+obj.scope
        obj.currEle = Parameter()
        reduce(lambda _, x: self.visit(x, obj), ast.param, [])
        obj.currEle = None
        obj.returnType = ast.returnType
        self.visit(ast.body, obj)
        obj.scope.pop(0)
        obj.returnType = None
        
    def visitBinaryOp(self, ast, obj):
        obj.check = UNDECLARED
        expr1 = self.visit(ast.left, obj)
        expr2 = self.visit(ast.right, obj)
        if ast.op in ["+", "-", "*"]:
            if type(expr1.Type) == IntType and type(expr2.Type) == IntType:
                return TypeDef(IntType())
            elif type(expr1.Type) == FloatType or type(expr2.Type) == FloatType:
                return TypeDef(FloatType())
            else:
                raise TypeMismatchInExpression(ast)
        if ast.op in ["^"]:
            if type(expr1.Type) == StringType and type(expr2.Type) == StringType:
                return TypeDef(StringType())
            else:
                raise TypeMismatchInExpression(ast)
        if ast.op in ["==", "!="]:
            if type(expr1.Type) == IntType and type(expr2.Type) == IntType:
                return TypeDef(BoolType())
            elif type(expr1.Type) == BoolType and type(expr2.Type) == BoolType:
                return TypeDef(BoolType())
            else:
                raise TypeMismatchInExpression(ast)
        if ast.op in [">", "<", "<=", ">="]:
            if type(expr1.Type) in [IntType, FloatType] and type(expr2.Type) in [IntType, FloatType]:
                return TypeDef(BoolType())
            else:
                raise TypeMismatchInExpression(ast)
        if ast.op in ["&&", "||"]:
            if type(expr1.Type) == BoolType and type(expr2.Type) == BoolType:
                return TypeDef(BoolType())
            else:
                raise TypeMismatchInExpression(ast)
        if ast.op in ["/"]:
            if type(expr1.Type) in [IntType, FloatType] and type(expr2.Type) in [IntType, FloatType]:
                if type(expr1.Type) == FloatType or type(expr2.Type) == FloatType:
                    return TypeDef(FloatType())
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)
        if ast.op in ["\\", "%"]:
            if type(expr1.Type) == IntType and type(expr2.Type) == IntType:
                return TypeDef(IntType())
            else: raise TypeMismatchInExpression(ast)
            
    def visitUnaryOp(self, ast, obj):
        obj.check = UNDECLARED
        body = self.visit(ast.body, obj)
        if ast.op in ["!"]:
            if type(body.Type) == BoolType:
                return TypeDef(BoolType())
            else:
                raise TypeMismatchInExpression(ast)
        if ast.op in ["-"]:
            if type(body.Type) in [IntType, FloatType]:
                return TypeDef(body.Type)
            else:
                raise TypeMismatchInExpression(ast)
            
    def visitArrayCell(self, ast, obj):
        array = self.visit(ast.arr, obj)
        idx = self.visit(ast.idx, obj)
        if type(array.Type) is ArrayType and type(idx) is IntType:
            return TypeDef(array.Type.eleType)
        else:
            raise TypeMismatchInExpression(ast)
        
    def visitBlock(self, ast, obj):
        reduce(lambda _, x: self.visit(x, obj), ast.stmt, [])
    
    def visitContinue(self, ast, obj):
        if obj.looptime == 0:
            raise MustInLoop(ast)
        
    def visitBreak(self, ast, obj):
        if obj.looptime == 0:
            raise MustInLoop(ast)
        
    def visitAssign(self, ast, obj):
        obj.check = UNDECLARED
        expr1 = self.visit(ast.lhs, obj)
        if expr1.isMutable == False:
            raise CannotAssignToConstant(ast)
        elif type(expr1.Type) == VoidType:
            raise TypeMismatchInStatement(ast)
        expr2 = self.visit(ast.exp, obj)
        if obj.cmpType(expr1.Type, expr2.Type) == False:
            raise TypeMismatchInStatement(ast)
        
    def visitFor(self, ast, obj):
        obj.looptime = obj.looptime + 1
        self.visit(ast.initStmt, obj)
        self.visit(ast.expr, obj)
        self.visit(ast.postStmt, obj)
        obj.scope = [{}] + obj.scope
        self.visit(ast.loop, obj)
        obj.scope.pop(0)
        obj.looptime = obj.looptime - 1
        
    def visitIf(self, ast, obj):
        obj.check = UNDECLARED
        expr = self.visit(ast.expr, obj)
        obj.check = None
        if type(expr.Type) is not bool:
            raise TypeMismatchInStatement(ast)
        if ast.preStmt != None:
            obj.scope = [{}]+obj.scope
            self.visit(ast.preStmt, obj)
            obj.scope.pop(0)
        obj.scope = [{}]+obj.scope
        self.visit(ast.thenStmt, obj)
        obj.scope.pop(0)
        if ast.elseStmt != None:
            obj.scope = [{}]+obj.scope
            self.visit(ast.thenStmt, obj)
            obj.scope.pop(0)
    
    def A():
        return
    
    def visitId(self, ast, obj):
        return obj.getEle(ast.name, obj.currEle, obj.check)
    
    def visitIntType(self, ast, obj):
        return IntType()
    
    def visitFloatType(self, ast, obj):
        return FloatType()
    
    def visitStringType(self, ast, obj):
        return StringType()
    
    def visitBoolType(self, ast, obj):
        return BoolType()
    
    def visitVoidType(self, ast, obj):
        return VoidType()
    
    def visitIntLiteral(self, ast, obj):
        return TypeDef(IntType())
    
    def visitFloatLiteral(self, ast, obj):
        return TypeDef(FloatType())
    
    def visitBooleanLiteral(self, ast, obj):
        return TypeDef(BoolType())
    
    def visitStringLiteral(self, ast, obj):
        return TypeDef(StringType())
    
    def visitNullLiteral(self, ast, obj):
        return TypeDef(VoidType())
    
    def visitSelfLiteral(self, ast, obj):
        return TypeDef(ClassType(obj.currClass.classname))