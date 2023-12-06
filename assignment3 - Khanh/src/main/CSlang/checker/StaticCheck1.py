"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils, MType
from StaticError import *
from functools import reduce
from typing import List, Dict

# used for checking declared
UNDECLARED = True
REDECLARED = False

class MemEnv:
    pass

class AttrEnv(MemEnv):
    id: Id
    typ: Type
    isMutable: bool

    def __init__(self, id, typ, isMutable):
        self.id = id
        self.typ = typ
        self.isMutable = isMutable

class MthdEnv(MemEnv):
    id: Id
    param: List[Type]
    returnType: Type

    def __init__(self, id, param, returnType):
        self.id = id
        self.param = param
        self.returnType = returnType

class ClassEnv:
    classname: Id
    prtname: Id
    memlist: Dict[str, MemEnv]
    staticmem: Dict[str, MemEnv]
    constructors: List[MthdEnv]

    def __init__(self, classdecl: ClassDecl, parent: Id = None, glb = None):
        self.constructors = []
        if classdecl:
            self.name = classdecl.classname
            self.prtname = parent
            self.memlist = {}
            self.staticmem = {}
            reduce(lambda _, x: self.addMem(x, glb), classdecl.memlist, self.memlist)
        else:
            self.name = Id("io")
            self.memlist = {}
            self.staticmem = {
                "@readInt": MthdEnv(Id("@readInt"), [], IntType()),
                "@writeInt": MthdEnv(Id("@writeInt"), [IntType()], VoidType()),
                "@readFloat": MthdEnv(Id("@readFloat"), [], FloatType()),
                "@writeFloat": MthdEnv(Id("@writeFloat"), [FloatType()], VoidType()),
                "@readBool": MthdEnv(Id("@readBool"), [], BoolType()),
                "@writeBool": MthdEnv(Id("@writeBool"), [BoolType()], VoidType()),
                "@readStr": MthdEnv(Id("@readStr"), [], StringType()),
                "@writeStr": MthdEnv(Id("@writeStr"), [StringType()], VoidType()),
            }

    def addMem(self, memdecl: MemDecl, glb):
        if type(memdecl) is AttributeDecl:
            self.addAttr(memdecl, glb)
        else:
            self.addMthd(memdecl, glb)

    def addAttr(self, attrdecl: AttributeDecl, glb):
        decl = attrdecl.decl
        if type(decl) is ConstDecl:
            self.addConstAttr(decl, glb)
        else:
            self.addVarAttr(decl, glb)
    
    def addConstAttr(self, constdecl: ConstDecl, glb):
        name = constdecl.constant.name
        if name in self.memlist:
            raise Redeclared(Attribute(), name)
        else:
            attrType = glb.checkType(constdecl.constType)
            self.memlist[name] = AttrEnv(Id(name), attrType, isMutable = False)

    def addVarAttr(self, vardecl: VarDecl, glb):
        name = vardecl.variable.name
        if name in self.memlist:
            raise Redeclared(Attribute(), name)
        else:
            attrType = glb.checkType(vardecl.varType)
            self.memlist[name] = AttrEnv(Id(name), attrType, isMutable = True)
    
    def addMthd(self, mthddecl: MethodDecl, glb):
        name = mthddecl.name.name
        if name in self.memlist and name != 'constructor':
            raise Redeclared(Method(), name)
        
        param = list(map(lambda x: glb.checkType(x.varType), mthddecl.param))
        returnType = glb.checkType(mthddecl.returnType)
        newMthd = MthdEnv(Id(name), param, returnType)

        if name == 'constructor':
            self.constructors.append(newMthd)
        else:
            if name[0] != '@':
                self.memlist[name] = newMthd
            else:
                self.staticmem[name] = newMthd

class GeneralType:
    def __init__(self, typ, id = None, isMutable = False):
        self.typ = typ
        self.id = id
        self.isMutable = isMutable

class Global:
    lst = Dict[str, ClassEnv]

    def __init__(self, ast: Program):
        self.lst = {"io": ClassEnv(None)}
        self.currClass = None
        self.currCheckInClass = None
        self.checkDeclared = False
        self.scope = []
        self.returnType = None
        self.loopCount = 0

        for classdecl in ast.decl:
            self.newClass(classdecl)

    def compareType(self, typ1: GeneralType, typ2: GeneralType):
        # if type(typ1) == type(typ2):
        #     if type(typ1) == ArrayType:
        #         return self.compareType(typ1.eleType, typ2.eleType)
        #     elif type(typ1) == ClassType:
        #         return typ1.classname.name == typ2.classname.name
        #     else:
        #         return True
        # else:
        #     return False
        if type(typ1) == type(typ2):
            return True
        return False

    def newClass(self, classdecl: ClassDecl):
        name = classdecl.classname.name
        if name in self.lst:
            raise Redeclared(Class(), name)
        else:
            if classdecl.parentname:
                parentname = classdecl.parentname.name
                if parentname not in self.lst:
                    raise Undeclared(Class(), parentname)
                else:
                    parentMemlist = self.lst[parentname].memlist
                    self.lst[name] = ClassEnv(classdecl, Id(parentname), self)
                    for x in parentMemlist:
                        if x not in self.lst[name].memlist:
                            self.lst[name].memlist[x] = parentMemlist[x]
            else:
                self.lst[name] = ClassEnv(classdecl, None, self)

    def checkEntry(self):
        if 'Program' not in self.lst:
            raise NoEntryPoint()
        prgclass = self.lst['Program']
        if "@main" not in prgclass.staticmem or type(prgclass.staticmem["@main"].returnType) != VoidType or type(prgclass.staticmem["@main"]) != MthdEnv:
            raise NoEntryPoint()
        
    def checkType(self, typ: Type):
        if type(typ) == ClassType:
            if typ.classname.name not in self.lst:
                raise Undeclared(Class(), typ.classname.name)
        elif type(typ) == ArrayType:
            self.checkType(typ.eleType)
        return typ

    def checkId(self, name: str, checkInClass: Kind, checkDeclared: bool):
        if checkDeclared == UNDECLARED:
            for i in self.scope:
                if name in i:
                    return i[name]
            if checkInClass not in [Attribute, Method]:
                checkInClass = Identifier()
            raise Undeclared(checkInClass, name)
        else:
            if checkDeclared == REDECLARED:
                if name in self.scope[0]:
                    raise Redeclared(checkInClass, name)

class StaticChecker(BaseVisitor,Utils):
    def __init__(self,ast):
        self.ast = ast
    
    def check(self):
        self.glb = Global(self.ast)
        self.glb.checkEntry() 
        self.visit(self.ast, self.glb)
        return "Never Gonna Give You Up!"

    def visitProgram(self, ast: Program, o: Global):
        for classdecl in ast.decl:
            self.visit(classdecl, o)
        
    def visitClassDecl(self, ast: ClassDecl, o: Global):
        o.currClass = o.lst[ast.classname.name]
        for memdecl in ast.memlist:
            self.visit(memdecl, o)

    def visitAttributeDecl(self, ast: AttributeDecl, o: Global):
        o.currCheckInClass = Attribute()
        self.visit(ast.decl, o)
        o.currCheckInClass = None

    def visitConstDecl(self, ast: ConstDecl, o: Global):
        if o.currCheckInClass is None:
            o.currCheckInClass = Constant()

        TypeConst = self.visit(ast.constType, o)

        if type(o.currCheckInClass) != Attribute:
            o.checkDeclared = REDECLARED
            self.visit(ast.constant, o)
            o.scope[0][ast.constant.name] = GeneralType(TypeConst, Id(ast.constant.name), False)

        if type(TypeConst) is VoidType:
            raise TypeMismatchInDeclaration(ast)

        o.checkDeclared = UNDECLARED
        TypeValue = self.visit(ast.value, o)
        if o.compareType(TypeConst, TypeValue) is False:
            raise TypeMismatchInDeclaration(ast)

    def visitVarDecl(self, ast: VarDecl, o: Global):
        if o.currCheckInClass is None:
            o.currCheckInClass = Variable()

        TypeVar = self.visit(ast.varType, o)

        if type(o.currCheckInClass) != Attribute:
            o.checkDeclared = REDECLARED
            self.visit(ast.variable, o)
            o.scope[0][ast.variable.name] = GeneralType(TypeVar, Id(ast.variable.name), True)

        if type(TypeVar) is VoidType:
            raise TypeMismatchInDeclaration(ast)
        
        if ast.varInit:
            o.checkDeclared = UNDECLARED
            TypeValue = self.visit(ast.varInit, o)
            if o.compareType(TypeVar, TypeValue) is False:
                raise TypeMismatchInDeclaration(ast)
            
    def visitMethodDecl(self, ast: MethodDecl, o: Global):
        o.scope = [{}] + o.scope
        o.currCheckInClass = Parameter()
        for param in ast.param:
            self.visit(param, o)
        o.currCheckInClass = None
        o.returnType = ast.returnType
        self.visit(ast.body, o)
        o.returnType = None
        o.scope.pop(0)

    def visitBinaryOp(self, ast: BinaryOp, o: Global):
        o.checkDeclared = UNDECLARED
        leftType = self.visit(ast.left, o)
        rightType = self.visit(ast.right, o)
        if ast.op in ['+', '-', '*']:
            if type(leftType.type) is IntType and type(rightType.type) is IntType:
                return GeneralType(IntType())
            else:
                if type(leftType.type) is FloatType and type(rightType.type) is FloatType:
                    return GeneralType(FloatType())
            raise TypeMismatchInExpression(ast)
        elif ast.op in ['\\', '%']:
            if type(leftType.type) is IntType and type(rightType.type) is IntType:
                return GeneralType(IntType())
            raise TypeMismatchInExpression(ast)
        elif ast.op in ['<', '>', '<=', '>=']:
            if type(leftType.type) in [IntType, FloatType] and type(rightType.type) in [IntType, FloatType]:
                return GeneralType(BoolType())
            raise TypeMismatchInExpression(ast)
        elif ast.op in ['==', '!=']:
            if type(leftType.type) is BoolType and type(rightType.type) is BoolType:
                return GeneralType(BoolType())
            else:
                if type(leftType.type) is IntType and type(rightType.type) is IntType:
                    return GeneralType(BoolType())
            raise TypeMismatchInExpression(ast)
        elif ast.op in ['&&', '||']:
            if type(leftType.type) is BoolType and type(rightType.type) is BoolType:
                return GeneralType(BoolType())
            raise TypeMismatchInExpression(ast)
        elif ast.op in ['^']:
            if type(leftType.type) is StringType and type(rightType.type) is StringTyoe:
                return GeneralType(StringType())
            raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast: UnaryOp, o: Global):
        o.checkDeclared = UNDECLARED
        bodyType = self.visit(ast.body, o)
        if ast.op == '-':
            if type(bodyType.type) is IntType:
                return GeneralType(IntType())
            else:
                if type(bodyType.type) is FloatType:
                    return GeneralType(FloatType())
            raise TypeMismatchInExpression(ast)
        elif ast.op == '!':
            if type(bodyType.type) is BoolType:
                return GeneralType(BoolType())
            raise TypeMismatchInExpression(ast)

    def visitArrayCell(self, ast: ArrayCell, o: Global):
        arrType = self.visit(ast.arr, o)
        idxType = self.visit(ast.idx, o)
        if type(arrType.type) is ArrayType:
            if type(idxType.type) is IntType:
                return GeneralType(arrType.type.eleType)
            raise TypeMismatchInExpression(ast)
        raise TypeMismatchInExpression(ast)
    
    def visitBlock(self, ast: Block, o: Global):
        reduce(lambda _,stmt:self.visit(stmt, o), ast.stmt, [])

    def visitBreak(self, ast: Break, o: Global):
        if o.loopCount == 0:
            raise MustInLoop(ast)
        
    def visitContinue(self, ast: Continue, o: Global):
        if o.loopCount == 0:
            raise MustInLoop(ast)
    
    def visitAssign(self, ast: Assign, o: Global):
        o.checkDeclared = UNDECLARED
        lhsType = self.visit(ast.lhs, o)
        if lhsType.isMutable is False:
            raise CannotAssignToConstant(ast)
        if type(lhsType.type) is VoidType:
            raise TypeMismatchInStatement(ast)
        rhsType = self.visit(ast.rhs, o)
        if o.compareType(lhsType.type, rhsType.type) is False:
            raise TypeMismatchInStatement(ast)
        
    def visitFor(self, ast: For, o: Global):
        o.loopCount += 1
        self.visit(ast.initStmt, o)
        self.visit(ast.expr, o)
        self.visit(ast.postStmt, o)
        o.scope = [{}] + o.scope
        self.visit(ast.loop, o)
        o.scope.pop(0)
        o.loopCount -= 1

    def visitIf(self, ast: If, o: Global):
        o.checkDeclared = UNDECLARED
        exprVisit = self.visit(ast.expr, o)
        o.checkDeclared = None
        if type(exprVisit.type) is not BoolType:
            raise TypeMismatchInStatement(ast)
        if ast.preStmt is not None:
            o.scope = [{}] + o.scope
            self.visit(ast.preStmt, o)
            o.scope.pop(0)
        o.scope = [{}] + o.scope
        self.visit(ast.thenStmt, o)
        o.scope.pop(0)
        if ast.elseStmt:
            o.scope = [{}] + o.scope
            self.visit(ast.elseStmt, o)
            o.scope.pop(0)

    def visitIntType(self, ast: IntType, o: Global):
        return IntType()

    def visitFloatType(self, ast: FloatType, o: Global):
        return FloatType()

    def visitBoolType(self, ast: BoolType, o: Global):
        return BoolType()

    def visitStringType(self, ast: StringType, o: Global):
        return StringType()

    def visitVoidType(self, ast: VoidType, o: Global):
        return VoidType()

    def visitArrayType(self, ast: ArrayType, o: Global):
        return o.checkType(ast)

    def visitClassType(self, ast: ClassType, o: Global):
        return o.checkType(ast)

    def visitId(self, ast: Id, o: Global):
        return o.checkId(ast.name, o.currCheckInClass, o.checkDeclared)

    def visitIntLiteral(self, ast: IntLiteral, o: Global):
        return GeneralType(IntType())

    def visitFloatLiteral(self, ast: FloatLiteral, o: Global):
        return GeneralType(FloatType())

    def visitStringLiteral(self, ast: StringLiteral, o: Global):
        return GeneralType(StringType())

    def visitBooleanLiteral(self, ast: BooleanLiteral, o: Global):
        return GeneralType(BoolType())

    def visitNullLiteral(self, ast: NullLiteral, o: Global):
        return GeneralType(VoidType())

    def visitSelfLiteral(self, ast: SelfLiteral, o: Global):
        return GeneralType(ClassType(Id(o.currClass.class_name.name)))