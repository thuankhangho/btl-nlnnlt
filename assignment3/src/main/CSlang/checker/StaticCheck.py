"""
 * @author nhphung
"""

# Student ID: 2011357
# Name: Ho Thuan Khang
# Line 164 is the return statement of the entire file.
# It is disabled to be submitted, but needs to be un-commented in order to function.

from dataclasses import field
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
        if name[0] != '@':
            self.members[name] = AttributeEnv(Id(name), attributeType, isMutable = False)
        else:
            self.staticMembers[name] = AttributeEnv(Id(name), attributeType, isMutable = False)
        
    def processVariableAttribute(self, member: VarDecl,manager):
        name = member.variable.name
        if name in self.members:
            raise Redeclared(Attribute(), name)
        attributeType = manager.checkForType(member.varType)
        if name[0] != '@':
            self.members[name] = AttributeEnv(Id(name), attributeType, isMutable = True)
        else:
            self.staticMembers[name] = AttributeEnv(Id(name), attributeType, isMutable = True)
        
    def getMember(self, name: str, kind: Kind, mode: bool):
        checkList = self.staticMembers if name[0]=='@' else self.members
        if mode == True: #check Undeclared
            if name in checkList:
                return checkList[name]
            else:
                raise Undeclared(kind, name)
        elif mode == False:
            if name in checkList:
                raise Redeclared(kind, name)
        
class ClassManager:
    classes: Dict[str, BKClass]
    def __init__(self, ast: Program):
        self.classes = {
            "io": BKClass(None)
        }
        self.currentCheck = None #Variable, Constant, Attribute, Parameter
        self.scope = [] #các tầm vực
        self.loop: int = 0 #có vào loop hay chưa (check break & continue)
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
            self.classes[newClassName] = BKClass(classDecl=newClass, parent=Id(parentName), manager=self)
            for mem in parentMembers:
                if mem not in self.classes[newClassName].members:
                    self.classes[newClassName].members[mem] = parentMembers[mem]
                    
        else: # không thừa kế
            self.classes[newClassName] = BKClass(classDecl=newClass, parent=None, manager=self)

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
            self.checkForType(typ.eleType)
        return typ
    
    def getClassEnv(self, name: str, mode: bool):
        if mode == True: # check Undeclared
            if name in self.classes:
                return self.classes[name]
            else:
                raise Undeclared(Class(), name)
        else: # check Redeclared
            if name in self.classes:
                raise Redeclared(Class(), name)
    
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
        
    def compareTypes(self, inputType, checkingType) -> bool:
        if type(inputType) is ClassType and type(checkingType) is ClassType:
            if inputType.classname.name == checkingType.classname.name or inputType.classname.name == self.getClassEnv(checkingType.classname.name, True).parent:
                return True
        elif type(inputType) is ClassType and type(checkingType) is VoidType:
            return True
        elif type(inputType) is FloatType and type(checkingType) is IntType:
            return True
        elif type(inputType) is ArrayType and type(checkingType) is ArrayType:
            return self.compareTypes(inputType.eleType, checkingType.eleType) and (inputType.size == checkingType.size)
        elif type(inputType) == type(checkingType):
        # if type(inputType) == type(checkingType):
            return True
        return False
    
    def compareParams(self, leftParams: List[Type], rightParams: List[Type]):
        if len(leftParams) != len(rightParams):
            return False
        for i in range(len(leftParams)):
            if self.compareTypes(leftParams[i], rightParams[i]) == False:
                return False
        return True
    
    def compareTypeInArray(self, inputType: Type, checkingType: Type)-> bool:
        if type(inputType) is ClassType and type(checkingType) is ClassType:
            if inputType.classname.name == checkingType.classname.name:
                return True
        elif type(inputType) == type(checkingType):
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
        self.visit(ast.decl, o)
        o.currentCheck = None # trả về None để check thứ khác
        
###################################  Expression  ##################################################
        
    def visitConstDecl(self, ast: ConstDecl, o: ClassManager):
        # chuyển current check thành Constant
        if o.currentCheck == None:
            o.currentCheck = Constant()
            
        # check ten bien
        if type(o.currentCheck) is not Attribute: #Const hoac Parameter
            o.mode = False
            self.visit(ast.constant,o)
        
        # check type
        constDeclType = self.visit(ast.constType, o)
        if type(constDeclType) is VoidType:
            raise TypeMismatchInDeclaration(ast)
        
        #check gia tri khoi tao co cung type voi bien
        if ast.value is not None:
            o.mode = True
            valueType = self.visit(ast.value,o) #tim type cua gia tri khoi tao
            if o.compareTypes(constDeclType, valueType.typ) is False:
                raise TypeMismatchInDeclaration(ast)
        else:
            raise TypeMismatchInDeclaration(ast)
            
        # thêm biến vào tầm vực hiện tại
        if type(o.currentCheck) is not Attribute:
            o.scope[0][ast.constant.name] = ConstVarLitEnv(id = Id(ast.constant.name), typ = constDeclType, isMutable = False)
            
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
        self.visit(ast.body, o)
        
        #xóa scope & kiểu trả về khi ra khỏi hàm
        o.scope.pop(0)
        o.returnType = None
        
    def visitBinaryOp(self, ast: BinaryOp, o: ClassManager):
        o.mode = True #check Undeclared
        leftExp: ConstVarLitEnv = self.visit(ast.left, o)
        rightExp: ConstVarLitEnv = self.visit(ast.right, o)
        
        if ast.op in ['+', '-', '*']:
            if type(leftExp.typ) is IntType and type(rightExp.typ) is IntType:
                return ConstVarLitEnv(IntType())
            elif type(leftExp.typ) is FloatType or type(rightExp.typ) is FloatType:
                return ConstVarLitEnv(FloatType())
            raise TypeMismatchInExpression(ast)
        
        elif ast.op == "^":
            if type(leftExp.typ) is StringType and type(rightExp.typ) is StringType:
                return ConstVarLitEnv(StringType())
            raise TypeMismatchInExpression(ast)
            
        elif ast.op in ['==', '!=']:
            if type(leftExp.typ) is IntType and type(rightExp.typ) is IntType:
                return ConstVarLitEnv(BoolType())
            if type(leftExp.typ) is BoolType and type(rightExp.typ) is BoolType:
                return ConstVarLitEnv(BoolType())
            raise TypeMismatchInExpression(ast)
            
        elif ast.op in ["<", ">", "<=", ">="]:
            if type(leftExp.typ) in (IntType, FloatType) and type(rightExp.typ) in (IntType, FloatType):
                return ConstVarLitEnv(BoolType())
            raise TypeMismatchInExpression(ast)
            
        elif ast.op in ["&&", "||"]:
            if type(leftExp.typ) is BoolType and type(rightExp.typ) is BoolType:
                return ConstVarLitEnv(BoolType())
            raise TypeMismatchInExpression(ast)
            
        elif ast.op == "/":
            if type(leftExp.typ) in (IntType, FloatType) and type(rightExp.typ) in (IntType, FloatType):
                if type(leftExp.typ) is FloatType or type(rightExp.typ) is FloatType:
                    return ConstVarLitEnv(FloatType())
            raise TypeMismatchInExpression(ast)
            
        elif(ast.op in ["\\","%"]):
            if type(leftExp.typ) is IntType and type(rightExp.typ) is IntType:
                return ConstVarLitEnv(IntType())
            raise TypeMismatchInExpression(ast)
    
    def visitUnaryOp(self, ast: UnaryOp, o: ClassManager):
        o.mode = True #kiểm tra liệu có undeclared hay không
        body: ConstVarLitEnv = self.visit(ast.body,o)

        if ast.op == "!":
            if type(body.typ) is BoolType:
                return ConstVarLitEnv(BoolType())
            raise TypeMismatchInExpression(ast)
            
        elif ast.op == "-":
            if type(body.typ) in (IntType, FloatType):
                return ConstVarLitEnv(body.typ)
            raise TypeMismatchInExpression(ast)

    def visitArrayCell(self, ast: ArrayCell, o: ClassManager):
        arr = self.visit(ast.arr, o)
        idx = self.visit(ast.idx, o)
        if type(arr.typ) is ArrayType and type(idx) is IntType:
            return ConstVarLitEnv(arr.typ.eleType)
        raise TypeMismatchInExpression(ast)
    
    def visitFieldAccess(self, ast: FieldAccess, o: ClassManager):
        fieldname = ast.fieldname.name
        currentClassChecking = ""

        #TH1: <fieldname> không có @ -> instance attribute access
        if fieldname[0] != '@':
            o.mode = True
            obj = self.visit(ast.obj, o)
            if type(obj.typ) is ClassType:
                if obj.typ.classname == o.currentClass.name or obj.typ.classname == o.currentClass.parent:
                    currentClassChecking = obj.typ.classname.name
            else: raise TypeMismatchInExpression(ast)
           
        #TH2: <fieldname> có @ -> static attribute access
        else:
            if ast.obj is None: #class hiện tại
                currentClassChecking = o.currentClass.name.name
            elif type(ast.obj) is Id:
                currentClassChecking = ast.obj.name
            else:
                raise TypeMismatchInExpression(ast)
            
        objEnv: BKClass = o.getClassEnv(currentClassChecking, True)
        memberEnv: AttributeEnv = objEnv.getMember(fieldname, Attribute(), True)
        
        if memberEnv is not None:
            return ConstVarLitEnv(memberEnv.typ, isMutable = True)
        else:
            raise TypeMismatchInExpression(ast) 
        
    def visitNewExpr(self, ast: NewExpr, o: ClassManager):
        className = ast.classname.name #lấy tên class của expr
        params = ast.param #lấy danh sách param của expr
        
        classEnv = o.getClassEnv(className, True) #lấy môi trường của class có đối tượng khai báo new
        classConstructors = classEnv.constructor #lấy các constructor của class có đối tượng khai báo new
        
        for constructor in classConstructors:
            constructorParamType = constructor.paramList #lấy danh sách param của từng constructor
            paramTypeList = [self.visit(param, o).typ for param in params] #lấy danh sách type của từng param trong khai báo new
            if o.compareParams(constructorParamType, paramTypeList) is True:
                return ConstVarLitEnv(ClassType(Id(className)))

        raise TypeMismatchInExpression(ast)
    
    def visitCallExpr(self, ast: CallExpr, o: ClassManager):
        currentClassChecking = ""
        fieldname = ast.method.name

        #TH1: <fieldname> không có @ -> instance method access
        if fieldname[0] != '@':
            o.mode = True
            obj = self.visit(ast.obj, o)
            if type(obj.typ) is ClassType:
                currentClassChecking = obj.typ.classname.name
            else: raise TypeMismatchInExpression(ast)
           
        #TH2: <fieldname> có @ -> static method access
        else:
            if ast.obj is None: #class hiện tại
                currentClassChecking = o.currentClass.name.name
            elif type(ast.obj) is Id:
                currentClassChecking = ast.obj.name
            else:
                raise TypeMismatchInExpression(ast)
            
        objEnv: BKClass = o.getClassEnv(currentClassChecking, True)
        memberEnv: MethodEnv = objEnv.getMember(fieldname, Method(), True)
        
        if memberEnv is not None:
            if type(memberEnv.returnType) is VoidType:
                raise TypeMismatchInExpression(ast)
            o.mode = True #check Undeclared
            paramList: List[Type] = []
            for param in ast.param:
                paramList.append(self.visit(param, o).typ)
            memberEnvparamList = memberEnv.paramList
            if o.compareParams(paramList, memberEnvparamList) == False:
                raise TypeMismatchInExpression(ast)
            return ConstVarLitEnv(memberEnv.returnType)
        else: raise TypeMismatchInExpression(ast) 
            
###################################  Statement  ##################################################
    
    def visitContinue(self, ast: Continue, o: ClassManager):
        if o.loop == 0:
            raise MustInLoop(ast)
    
    def visitBreak(self, ast: Break, o: ClassManager):
        if o.loop == 0:
            raise MustInLoop(ast)
        
    def visitFor(self, ast: For, o: ClassManager):
        o.loop += 1 #+1 cho loop khi vao loop
        o.scope = [{}] + o.scope
        
        self.visit(ast.initStmt, o)
        self.visit(ast.expr, o)
        self.visit(ast.postStmt, o)

        self.visit(ast.loop, o)
        
        o.scope.pop(0)
        o.loop -=1 #-1 khi ra loop
        
    def visitAssign(self, ast: Assign, o: ClassManager):
        o.mode = True #check Undeclared
        lhs: ConstVarLitEnv = self.visit(ast.lhs, o)
        if lhs.isMutable == False:
            raise CannotAssignToConstant(ast)
        if type(lhs.typ) is VoidType:
            raise TypeMismatchInStatement(ast)
        rhs: ConstVarLitEnv = self.visit(ast.exp, o)
        if o.compareTypes(lhs.typ, rhs.typ) == False:
            raise TypeMismatchInStatement(ast)
        
    def visitIf(self, ast: If, o: ClassManager):
        o.mode = True #check Undeclared
        expr: ConstVarLitEnv = self.visit(ast.expr, o)
        o.mode = None
        
        if type(expr.typ) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        if ast.preStmt is not None:
            o.scope = [{}] + o.scope
            self.visit(ast.preStmt, o)
            o.scope.pop(0)

        o.scope = [{}] + o.scope
        self.visit(ast.thenStmt, o)
        o.scope.pop(0)

        if ast.elseStmt is not None:
            o.scope = [{}] + o.scope
            self.visit(ast.elseStmt, o)
            o.scope.pop(0)
            
    def visitCallStmt(self, ast: CallStmt, o: ClassManager):
        currentClassChecking = ""
        fieldname = ast.method.name

        #TH1: <fieldname> không có @ -> instance method access
        if fieldname[0] != '@':
            o.mode = True
            obj = self.visit(ast.obj, o)
            if type(obj.typ) is ClassType:
                currentClassChecking = obj.typ.classname.name
            else: raise TypeMismatchInExpression(ast)
           
        #TH2: <fieldname> có @ -> static method access
        elif fieldname[0] == '@':
            if ast.obj is None: #class hiện tại
                currentClassChecking = o.currentClass.name.name
            elif type(ast.obj) is Id:
                currentClassChecking = ast.obj.name
            else:
                raise TypeMismatchInExpression(ast)
            
        objEnv: BKClass = o.getClassEnv(currentClassChecking, True)
        memberEnv: MethodEnv = objEnv.getMember(fieldname, Method(), True)
        
        if memberEnv is not None:
            if type(memberEnv.returnType) is not VoidType:
                raise TypeMismatchInExpression(ast)
            o.mode = True #check Undeclared
            paramList: List[Type] = []
            for param in ast.param:
                paramList.append(self.visit(param, o).typ)
            memberEnvparamList = memberEnv.paramList
            if o.compareParams(paramList, memberEnvparamList) == False:
                raise TypeMismatchInExpression(ast)
            return ConstVarLitEnv(memberEnv.returnType)
        else: raise TypeMismatchInExpression(ast) 

    def visitId(self, ast: Id, o: ClassManager):
        return o.checkUndeclaredRedeclared(ast.name, o.currentCheck, o.mode)
    
    def visitBlock(self, ast: Block, o: ClassManager):
        reduce(lambda _,stmt:self.visit(stmt, o), ast.stmt, [])
        
##########################################  Type & literal  ####################################################

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
    def visitArrayType(self, ast: ArrayType, o: ClassManager):
        return o.checkForType(ast)
    def visitClassType(self, ast: ClassType, o: ClassManager):
        return o.checkForType(ast)
    
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
        return ConstVarLitEnv(ClassType(Id(o.currentClass.name.name)))
    def visitArrayLiteral(self, ast: ArrayLiteral, o: ClassManager):
        currentType = VoidType()
        value = ast.value
        for x in value:
            temp: ConstVarLitEnv = self.visit(x, o)
            litType = temp.typ
            if type(currentType) is not VoidType:
                if o.compareTypeInArray(currentType, litType) == False:
                    raise IllegalArrayLiteral(ast)
            elif type(litType) is not VoidType:
                currentType = litType
        return ConstVarLitEnv(ArrayType(len(ast.value), currentType), False)