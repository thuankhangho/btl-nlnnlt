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

class MemberEnv:
    pass
    
class MethodEnv(MemberEnv):
    name: Id
    paramList: List[Type]
    returnType: Type
    
    def __init__(self, name: Id, paramList: List[Type], returnType: Type):
        self.name = name
        self.paramList = paramList
        self.returnType = returnType

class AttributeEnv(MemberEnv):
    id: Id
    typ: Type
    isMutable: bool #const = false, var = true

    def __init__(self, id: Id, typ: Type, isMutable: bool):
        self.id = id
        self.typ = typ
        self.isMutable = isMutable
        
class ConstVarLitEnv: # variable, constant & literal env
    id: Id
    typ: Type
    isMutable: bool #const = false, var = true

    def __init__(self, typ: Type, id: Id = None, isMutable: bool = False):
        self.typ = typ
        self.id = id
        self.isMutable = isMutable
        
class BKClass:
    name: Id
    parent: Id
    members: Dict[str, MemberEnv]
    staticMembers: Dict[str, MemberEnv]
    constructor: List[MethodEnv]
    
    def __init__(self, classDecl: ClassDecl = None, parent: Id = None, manager = None):
        self.constructor = []
        if classDecl:
            self.name = classDecl.classname
            self.parent = parent
            self.members = {}
            self.staticMembers = {}
            reduce(lambda _, mem: self.sortMember(mem, manager), classDecl.memlist, self.members)
        else:
            self.name = Id("io")
            self.members = {}
            self.staticMembers = {
                "@readInt": MethodEnv(Id("@readInt"), [], IntType()),
                "@writeInt": MethodEnv(Id("@writeInt"), [IntType()], VoidType()),
                "@readFloat": MethodEnv(Id("@readFloat"), [], FloatType()),
                "@writeFloat": MethodEnv(Id("@writeFloat"), [FloatType()], VoidType()),
                "@readBool": MethodEnv(Id("@readBool"), [], BoolType()),
                "@writeBool": MethodEnv(Id("@writeBool"), [BoolType()], VoidType()),
                "@readStr": MethodEnv(Id("@readStr"), [], StringType()),
                "@writeStr": MethodEnv(Id("@writeStr"), [StringType()], VoidType())
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
        paramType = list(map(lambda el: manager.checkForType(el.varType), member.param))
        paramList = []
        for x in member.param:
            if x not in paramList:
                paramList.append(x)
            else: raise Redeclared(Parameter(), x.variable.name)
        returnType = manager.checkForType(member.returnType)
        method = MethodEnv(Id(methodName), paramType, returnType)
        if methodName == "constructor":
            self.constructor += [method]
        else:
            if methodName[0] != '@':
                self.members[methodName] = method
            else: self.staticMembers[methodName] = method
            
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
        attributeType = manager.checkForType(member.constType)
        self.members[name] = AttributeEnv(Id(name), attributeType, isMutable = False)
        
    def processVariableAttribute(self, member: VarDecl,manager):
        name = member.variable.name
        if name in self.members:
            raise Redeclared(Attribute(), name)
        attributeType = manager.checkForType(member.varType)
        self.members[name] = AttributeEnv(Id(name), attributeType, isMutable = True)
        
class ClassManager:
    classes: Dict[str, BKClass]
    def __init__(self, ast: Program):
        self.classes = {
            "io": BKClass()
        }
        self.currentCheck = None #Variable, Constant, Attribute, Parameter
        self.scope = [] #các tầm vực
        self.loop: bool = False #có vào loop hay chưa (check break & continue)
        self.mode: bool = True #undeclared = true hay redeclared = false
        self.currentClass: BKClass = None #class hiện tại đang được duyệt
        self.returnType = None #kiểu trả về của hàm
        
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
            parentMembers = self.classes[parentName].members
            self.classes[newClassName] = BKClass(newClass, Id(parentName), self)
            for mem in parentMembers:
                if mem not in self.classes[newClassName].members:
                    self.classes[newClassName].members[mem] = parentMembers[mem]
        else: # không thừa kế
            self.classes[newClassName] = BKClass(newClass, manager=self)

    def checkNoEntryPoint(self):
        if "Program" not in self.classes:
            raise NoEntryPoint()
        programClass = self.classes["Program"]
        if "@main" not in programClass.staticMembers or type(programClass.staticMembers["@main"]) is not MethodEnv or type(programClass.staticMembers["@main"].returnType) is not VoidType:
            raise NoEntryPoint()
    
    def checkForType(self, typ: Type):
        if type(typ) is ClassType:
            if typ.classname.name not in self.classes:
                raise Undeclared(Class(), typ.classname.name)
        elif type(typ) is ArrayType:
            self.check_type(typ.eleType)
        return typ
    
    def getClassEnv(self, class_name):
        return self.classes[class_name]
    
    def checkUndeclaredRedeclared(self, name: str, kind: Kind, mode: bool):
    # mode = true: undeclared, mode = false: redeclared
        if mode == True:
            for sc in self.scope:
                if name in sc:
                    return sc[name]
            if kind not in (Attribute, Method):
                kind = Identifier()
            raise Undeclared(kind, name)
        elif name in self.scope[0]:
            raise Redeclared(kind, name)
        
    def compareTypes(self, inputType: ConstVarLitEnv, checkingType: ConstVarLitEnv) -> bool:
        if type(inputType) == type(checkingType):
            return True
        return False

class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast):
        self.ast = ast
        
    def check(self):
        manager = ClassManager(self.ast)
        manager.checkNoEntryPoint()
        self.visit(self.ast, manager)
        return ""
        
    def visitProgram(self, ast: Program, o: ClassManager):
        reduce(lambda _, decl: self.visit(decl, o), ast.decl, [])
        
    def visitClassDecl(self, ast: ClassDecl, o: ClassManager):
        o.currentClass = o.classes[ast.classname.name]
        reduce(lambda _, member: self.visit(member, o), ast.memlist, [])
    
    def visitAttributeDecl(self, ast: AttributeDecl, o: ClassManager):
        o.currentCheck = Attribute() # hiện tại check Attribute
        self.visit(ast.decl,o)
        o.currentCheck = None # trả về None để check thứ khác
        
    def visitConstDecl(self, ast: ConstDecl, o: ClassManager):
        # chuyển current check thành Constant
        if o.currentCheck == None:
            o.currentCheck = Constant()
            
        # check tên biến
        if type(o.currentCheck) is not Attribute: #Const hoặc Parameter
            o.mode = False
            self.visit(ast.constant,o)
        
        # check type
        constDeclType = self.visit(ast.constType, o)
        if type(constDeclType) is VoidType: #nếu type của constdecl là void
            raise TypeMismatchInDeclaration(ast) #ném lỗi
        
        #check giá trị khởi tạo có cùng type với biến
        o.mode = True
        valueType = self.visit(ast.value,o) #tìm type của giá trị khởi tạo
        if o.compareType(constDeclType, valueType.typ) is False:
            raise TypeMismatchInDeclaration(ast)
            
        # thêm biến vào tầm vực hiện tại
        if type(o.currentCheck) is not Attribute:
            o.scope[0][ast.variable.name] = ConstVarLitEnv(id = Id(ast.variable.name), typ = constDeclType, isMutable = False)
            
    def visitVarDecl(self, ast: VarDecl, o: ClassManager):
        # chuyển current check thành Variable
        if o.currentCheck == None:
            o.currentCheck = Variable()
            
        # check tên biến
        if type(o.currentCheck) is not Attribute: #Variable hoặc Parameter
            o.mode = False
            self.visit(ast.variable,o)
        
        # check type
        varDeclType = self.visit(ast.varType, o)
        if type(varDeclType) is VoidType: #nếu type của vardecl là void
            raise TypeMismatchInDeclaration(ast) #ném lỗi
        
        # check giá trị khởi tạo có cùng type với biến
        if ast.varInit is not None: #nếu có giá trị khởi tạo
            o.mode = True
            varInitType = self.visit(ast.varInit,o) #tìm type của giá trị khởi tạo
            if o.compareTypes(varDeclType, varInitType.typ) is False:
                raise TypeMismatchInDeclaration(ast)
            
        # thêm biến vào tầm vực hiện tại
        if type(o.currentCheck) is not Attribute:
            o.scope[0][ast.variable.name] = ConstVarLitEnv(id = Id(ast.variable.name), typ = varDeclType, isMutable = True)
      
    def visitMethodDecl(self, ast: MethodDecl, o: ClassManager):
        o.scope = [{}] + o.scope #tạo thêm scope cho method
        
        #visit Parameter
        paramList = []
        o.currentCheck = Parameter()
        for x in ast.param:
            paramList.append(self.visit(x, o))
        o.currentCheck = None
        
        #gán kiểu trả về
        o.returnType = ast.returnType
        
        #visit thân hàm
        # self.visit(ast.body, o)
        
        #xóa scope & kiểu trả về khi ra khỏi hàm
        o.scope.pop(0)
        o.returnType = None
        
    def visitBinaryOp(self, ast: BinaryOp, o: ClassManager):
        o.mode = True #kiểm tra liệu có undeclared hay không
        leftExp = self.visit(ast.left, o)
        rightExp = self.visit(ast.right, o)
        
        if ast.op in ['+', '-', '*']:
            if type(leftExp.typ) is IntType and type(rightExp.typ) is IntType:
                return ConstVarLitEnv(StringType())
            elif type(leftExp.typ) is FloatType and type(rightExp.typ) is FloatType:
                return ConstVarLitEnv(StringType())
            else:
                raise TypeMismatchInExpression(ast)
        
        elif ast.op == "^":
            if type(leftExp.typ) is StringType and type(rightExp.typ) is StringType:
                return ConstVarLitEnv(StringType())
            else:
                raise TypeMismatchInExpression(ast)
            
        elif ast.op in ['==', '!=']:
            if type(leftExp.typ) is IntType and type(rightExp.typ) is IntType:
                return ConstVarLitEnv(BoolType())
            elif type(leftExp.typ) is BoolType and type(rightExp.typ) is BoolType:
                return ConstVarLitEnv(BoolType())
            else:
                raise TypeMismatchInExpression(ast)
            
    def visitId(self, ast: Id, o: ClassManager):
        return o.checkUndeclaredRedeclared(ast.name, o.currentCheck, o.mode)
    
    def visitBlock(self, ast: Block, o: ClassManager):
        reduce(lambda _,stmt:self.visit(stmt, o), ast.stmt, [])
    
    
    
    
    
    
    
    
    
    
    
    def visitIntType(self, ast: IntType, o):
        return IntType()
    def visitFloatType(self, ast: FloatType, o):
        return FloatType()
    def visitBoolType(self, ast: BoolType, o):
        return BoolType()
    def visitStringType(self,ast: StringType, o):
        return StringType()
    def visitVoidType(self, ast: VoidType, o):
        return VoidType()
    def visitArrayType(self, ast: ArrayType, o):
        return ArrayType()
    def visitClassType(self, ast: ClassType, o):
        return ClassType()
    
    def visitIntLiteral(self, ast: IntLiteral, o):
        return ConstVarLitEnv(IntType())
    def visitFloatLiteral(self, ast: FloatLiteral, o):
        return ConstVarLitEnv(FloatType())
    def visitBooleanLiteral(self, ast: BooleanLiteral, o):
        return ConstVarLitEnv(BoolType())
    def visitStringLiteral(self, ast: StringLiteral, o):
        return ConstVarLitEnv(StringType())
    def visitNullLiteral(self, ast: NullLiteral, o):
        return ConstVarLitEnv(VoidType())
    def visitSelfLiteral(self, ast: SelfLiteral, o):
        return ConstVarLitEnv(ClassType(Id(o.currentClass.class_name.name)))