
"""
 * @author nhphung
"""
## eslint-disable ##
from AST import * 
from Visitor import *
from Utils import Utils, MType
from StaticError import *

#region Custom
# from ClassManager import ClassManager
# from ClassEnv import ClassEnv,AttrEnv,MethodEnv
# from TypeRes import Res
# from typing import List,Dict,Union,Optional
#endregion

from functools import reduce
import copy

UNDECLARED = True
REDECLARED = False

CONST = True
VAR = False

from AST import *
from StaticError import *

class MemberEnv:
    pass
class AttrEnv(MemberEnv):
    # const is True && var is False
    def __init__(self,id:Id,typ:Type,const_var:bool):
        self.attrname = id
        self.typ = typ
        self.const_var = const_var
    def __str__(self):
        return f"AttrEnv(ID: {str(self.attrname)}, Type: {str(self.typ)}, const_var:{str(self.const_var)})" 

class MethodEnv(MemberEnv):

    def __init__(
            self,
            name=None,param=None,ret=None,
            method_decl=None
        ):
        if(method_decl):
            self.methodname = Id(method_decl.name.name)
            self.param_type = [var_decl.varType for var_decl in method_decl.param]
            self.return_type = method_decl.returnType
        else:
            self.methodname = name
            self.param_type = param
            self.return_type = ret
        
    
    def __str__(self):
        return f"MethodEnv(ID: {str(self.methodname)}, param: {[str(param) for param in self.param_type]}, return:{str(self.return_type)})" 


class ClassEnv:

    def __init__(
            self,
            class_decl = None, 
            parent_env = None,
            declared_class = None,
            io = True
        ):
        if(io):
            self.class_name = Id('io')
            self.instance_list = {}
            self.static_list = {
                "@readInt": MethodEnv(
                    name = Id("@readInt"),
                    param = [],
                    ret = IntType()
                ),
                "@writeInt": MethodEnv(
                    name = Id("@writeInt"),
                    param = [IntType()],
                    ret = VoidType()
                ),
                "@readFloat": MethodEnv(
                    name = Id("@readFloat"),
                    param = [],
                    ret = FloatType()
                ),
                "@writeFloat": MethodEnv(
                    name = Id("@writeFloat"),
                    param = [FloatType()],
                    ret = VoidType()
                ),
                "@readBool": MethodEnv(
                    name = Id("@readBool"),
                    param = [],
                    ret = BoolType()
                ),
                "@writeBool": MethodEnv(
                    name = Id("@writeBool"),
                    param = [BoolType()],
                    ret = VoidType()
                ),
                "@readStr": MethodEnv(
                    name = Id("@readStr"),
                    param = [],
                    ret = StringType()
                ),
                "@writeStr": MethodEnv(
                    name = Id("@writeStr"),
                    param = [StringType()],
                    ret = VoidType()
                )
            }
            self.declared_class=[]
            self.mro = []
            self.constructor = []
        else:
            self.class_name = Id(class_decl.classname.name)
            self.declared_class = declared_class if declared_class else []

            self.instance_list = {}
            self.static_list = {}
            self.constructor = []
            reduce(lambda _,member:self.extract_member(copy.deepcopy(member)),class_decl.memlist,{})
            self.mro = [self.class_name]
            #Inheritance
            if(parent_env):
                for instance in parent_env.instance_list:
                    if instance not in self.instance_list:
                        self.instance_list[instance] = parent_env.instance_list[instance]
                self.mro += parent_env.mro
    
    def extract_member(self,member_decl:MemDecl):
        self.extract_attr(member_decl) if(isinstance(member_decl,AttributeDecl)) else self.extract_method(member_decl)

    #region Attribute
    def extract_attr(self,attr_decl:AttributeDecl):
        self.extract_attr_var(attr_decl.decl) if(isinstance(attr_decl.decl,VarDecl)) else self.extract_attr_const(attr_decl.decl)
    def extract_attr_const(self,const_decl:ConstDecl):
        mem_name = const_decl.constant.name
        self.get_member(mem_name, Attribute(), False)

        typ = self.check_type(const_decl.constType)
        static = mem_name[0]=='@'

        res = AttrEnv(Id(mem_name),typ,True)
        if(static):
            self.static_list[mem_name] = res
        else:
            self.instance_list[mem_name] = res
        
    def extract_attr_var(self,var_decl:VarDecl):
        mem_name = var_decl.variable.name
        self.get_member(mem_name,Attribute(),False)

        typ = self.check_type(var_decl.varType)
        static = mem_name[0]=='@'

        res = AttrEnv(Id(mem_name),typ,False)
        if(static):
            self.static_list[mem_name] = res
        else:
            self.instance_list[mem_name] = res
    #endregion
    #region Method
    def extract_method(self,method_decl:MethodDecl):
        self.extract_method_construct(method_decl) if method_decl.name.name=="constructor" else self.extract_method_norm(method_decl)
    
    def extract_method_norm(self,method_decl:MethodDecl):
        method_name = method_decl.name.name
        self.get_member(method_name,Method(),False)

        env = MethodEnv(method_decl=method_decl)
        reduce(lambda _,param:self.check_type(param),env.param_type,{})
        self.check_type(env.return_type)

        static = method_name[0]=="@"
        if(static):
            self.static_list[method_name] = env
        else:
            self.instance_list[method_name] = env

    def extract_method_construct(self,method_decl:MethodDecl):
        env = MethodEnv(method_decl=method_decl)
        reduce(lambda _,param:self.check_type(param),env.param_type,{})
        self.check_type(env.return_type)
        self.constructor += [env]
    #endregion


    #region Utils
    def get_member(self,mem_name:str,kind:Kind, undec_redec:bool):
        #True for retrieving the member
        #False for checking if the member exist
        static = (mem_name[0]=='@')
        check_list = self.static_list if static else self.instance_list
        if(undec_redec):
            if(mem_name in check_list):
                return check_list[mem_name]
            else:
                raise Undeclared(kind,mem_name)
        else:
            if(mem_name in check_list):
                raise Redeclared(kind,mem_name)
    
    def check_type(self,typ:Type):
        if(isinstance(typ,ClassType)):
            if(typ.classname.name not in self.declared_class):
                raise Undeclared(Class(),typ.classname.name)
        elif(isinstance(typ,ArrayType)):
            self.check_type(typ.eleType)
        return typ
    def __str__(self):
        return f"ClassEnv(ID:{str(self.class_name)},instance:{str(self.instance_list)},static:{str(self.static_list)},mro:{str(self.mro)},declared:{str(self.declared_class)},constructor:{str(self.constructor)})"
    #endregion



UNDECLARED = True
REDECLARED = False

class ClassManager:

    def __init__(self,ast:Program):
        self.class_list = {
            "io": ClassEnv()
        }
        self.class_names = [class_decl.classname.name for class_decl in ast.decl]
        for class_decl in ast.decl:
            self.add_class(class_decl)
    
    def add_class(self,class_decl:ClassDecl)->None:
        name = class_decl.classname.name

        self.get_class(name,undec_redec=False)
        
        if(class_decl.parentname):
            parent_name = class_decl.parentname.name
            parent_env = self.get_class(parent_name,undec_redec=True)
            self.class_list[name] = ClassEnv(class_decl,parent_env,self.class_names,io=False)
        else:
            self.class_list[name] = ClassEnv(class_decl,None,self.class_names,io=False)
    
    #region Utils
    def get_class(self,class_name:str,undec_redec:bool):
        #True for retrieving the class
        #False for checking if the class exist
        if(undec_redec):
            if(class_name in self.class_list):
                return self.class_list[class_name]
            else:
                raise Undeclared(Class(),class_name)
        else:
            if(class_name in self.class_list):
                raise Redeclared(Class(),class_name)
    #endregion

    #region Checker
    def check_entry(self):
        starter = "@main"
        if("Program" in self.class_list):
            program = self.class_list["Program"]
            if(starter in program.static_list):
                env = program.static_list[starter]
                if(isinstance(env,MethodEnv) and isinstance(env.return_type,VoidType) and len(env.param_type)==0):
                    return True
        raise NoEntryPoint()
    def check_type(self,typ:Type):
        if(isinstance(typ,ClassType)):
            if(typ.classname.name not in self.class_list):
                raise Undeclared(Class(),typ.classname.name)
        elif(isinstance(typ,ArrayType)):
            self.check_type(typ.eleType)
        return typ

    def check_type_comp_coerce(self,l_typ:Type,r_typ:Type):
        #Both are ClassType
        if(isinstance(l_typ,ClassType) and isinstance(r_typ,ClassType)):
            return l_typ.classname.name in [mro.name for mro in self.get_class(r_typ.classname.name,UNDECLARED).mro]
        elif(isinstance(l_typ,ClassType) and isinstance(r_typ,VoidType)):
            return True
        elif(isinstance(l_typ,FloatType) and isinstance(r_typ,IntType)):
            return True
        elif(isinstance(l_typ,ArrayType) and isinstance(r_typ,ArrayType)):
            return self.check_type_comp_coerce(l_typ.eleType,r_typ.eleType) and (l_typ.size == r_typ.size)
        else:
            return type(l_typ) == type(r_typ)
    
    def check_type_comp_fixed(self,l_typ:Type,r_typ:Type):
        #Both are ClassType
        if(isinstance(l_typ,ClassType) and isinstance(r_typ,ClassType)):
            return l_typ.classname.name == r_typ.classname.name
        elif(isinstance(l_typ,ArrayType) and isinstance(r_typ,ArrayType)):
            return self.check_type_comp_fixed(l_typ.eleType,r_typ.eleType) and (l_typ.size == r_typ.size)
        else:
            return type(l_typ) == type(r_typ)
    
    #endregion



class Res:
    
    def __init__(self,typ, id=None,const_var = True):
        #True is const, False for var
        self.typ = typ
        self.id = id
        self.const_var = const_var
    
    def __str__(self):
        return f"{str(self.id)}: Type {str(self.typ)} and Const_Var {self.const_var}"

class Checker:

    def __init__(self,ast:Program):
        self.manager = ClassManager(ast)
        self.cur_class = None
        self.scope = []
        self.cur_check = None
        self.undec_redec = True
        self.loop_count = 0
        self.return_typ = None

    
    def get_element(self,name:str,kind:Kind,undec_redec:bool):
        #True for retrieving the member
        #False for checking if the member exist
        if(undec_redec):
            for env in self.scope:
                if name in env:
                    return env[name]
            if(not isinstance(kind,(Attribute,Method))):
                kind = Identifier()
            raise Undeclared(kind,name)
        else:
            if(name in self.scope[0]):
                raise Redeclared(kind,name)
    def comp_type_param(self,left_list:List[Type],right_list:List[Type]) -> bool:
        if(len(left_list)==len(right_list)):
            for i in range(len(left_list)):
                if (not self.manager.check_type_comp_coerce(left_list[i],right_list[i])):
                    return False
            return True
        else:
            return False

class StaticChecker(BaseVisitor,Utils):
    def __init__(self,ast:Program):
        self.ast = ast
    def check(self):
        checker = Checker(self.ast)
        checker.manager.check_entry()
        self.visit(self.ast,checker)
    def visitProgram(self,ast:Program,o:Checker):
        reduce(lambda _,decl:self.visit(decl,o),ast.decl,[])
    def visitClassDecl(self, ast:ClassDecl, o:Checker):
        o.cur_class = o.manager.get_class(ast.classname.name,UNDECLARED)
        reduce(lambda _,mem:self.visit(mem,o),ast.memlist,[])

#region attrdecl  
    def visitAttributeDecl(self,ast:AttributeDecl,o:Checker):
        o.cur_check = Attribute()
        self.visit(ast.decl,o)
        o.cur_check = None

    def visitVarDecl(self,ast:VarDecl,o:Checker):
        if(o.cur_check==None): o.cur_check=Variable()
        #Find if there is a variable with the same name declared
        if(not isinstance(o.cur_check,Attribute)):
            o.undec_redec=REDECLARED
            self.visit(ast.variable,o)
        #Check if type is declared
        decl_typ = self.visit(ast.varType,o)
        #Check if type is void
        if(isinstance(decl_typ,VoidType)):
            raise TypeMismatchInDeclaration(ast)
        #Check if init value is compatible with variable
        if(ast.varInit):
            o.undec_redec = UNDECLARED
            res:Res = self.visit(ast.varInit,o)
            if(not o.manager.check_type_comp_coerce(decl_typ,res.typ)):
                raise TypeMismatchInDeclaration(ast)
        #Assign to scope
        if(not isinstance(o.cur_check,Attribute)):
            o.scope[0][ast.variable.name] = Res(decl_typ,Id(ast.variable.name),VAR)
    
    def visitConstDecl(self,ast:ConstDecl,o:Checker):
        if(o.cur_check==None): o.cur_check=Constant()
        #Find if there is a variable with the same name declared
        if(not isinstance(o.cur_check,Attribute)):
            o.undec_redec=REDECLARED
            self.visit(ast.constant,o)
        #Check if type is declared
        decl_typ = self.visit(ast.constType,o)
        #Check if type is void
        if(isinstance(decl_typ,VoidType)):
            raise TypeMismatchInDeclaration(ast)
        
        #Check for value of the constant
        if(ast.value):
            o.undec_redec = UNDECLARED
            res:Res = self.visit(ast.value,o)
            if(not o.manager.check_type_comp_coerce(decl_typ,res.typ)):
                raise TypeMismatchInDeclaration(ast)
        else:
            raise TypeMismatchInDeclaration(ast)
        
        #Assign to scope
        if(not isinstance(o.cur_check,Attribute)):
            o.scope[0][ast.constant.name] = Res(decl_typ,Id(ast.constant.name),CONST)
#endregion
#region methodecl
    def visitMethodDecl(self,ast:MethodDecl,o:Checker):
        o.return_typ = ast.returnType
        o.scope = [{}]+o.scope

        #Parse all the parameter
        o.cur_check = Parameter()
        reduce(lambda _,param:self.visit(param,o),ast.param,[])
        o.cur_check = None
        #End all parameter

        #Body Check
        self.visit(ast.body,o)
        #End Body check
        o.scope.pop(0)
        o.return_typ = None
#endregion

#region Expression
    def visitBinaryOp(self,ast:BinaryOp,o:Checker)->Res:
        o.undec_redec = UNDECLARED
        left_expr:Res = self.visit(ast.left,o)
        right_expr:Res = self.visit(ast.right,o)
        if(ast.op == '^'):
            if(isinstance(left_expr.typ,StringType) and isinstance(right_expr.typ,StringType)):
                return Res(StringType())
            else:
                raise TypeMismatchInExpression(ast)
        elif(ast.op in ["==","!="]):
            if(isinstance(left_expr.typ,BoolType) and isinstance(right_expr.typ,BoolType)):
                return Res(BoolType())
            elif(isinstance(left_expr.typ,IntType) and isinstance(right_expr.typ,IntType)):
                return Res(BoolType())
            else:
                raise TypeMismatchInExpression(ast)
        elif(ast.op in ["<",">","<=",">="]):
            if(isinstance(left_expr.typ,(IntType,FloatType)) and isinstance(right_expr.typ,(IntType,FloatType))):
                return Res(BoolType())
            else: 
                raise TypeMismatchInExpression(ast)
        elif(ast.op in ["&&","||"]):
            if(isinstance(left_expr.typ,BoolType) and isinstance(right_expr.typ,BoolType)):
                return Res(BoolType())
            else:
                raise TypeMismatchInExpression(ast)
        elif(ast.op in ["+","-","*"]):
            if(isinstance(left_expr.typ,(IntType,FloatType)) and isinstance(right_expr.typ,(IntType,FloatType))):
                if(isinstance(left_expr.typ,FloatType) or isinstance(right_expr.typ,FloatType)):
                    return Res(FloatType())
                else:
                    return Res(IntType())
            else:
                raise TypeMismatchInExpression(ast)
        elif(ast.op == "/"):
            if(isinstance(left_expr.typ,(IntType,FloatType)) and isinstance(right_expr.typ,(IntType,FloatType))):
                if(isinstance(left_expr.typ,FloatType) or isinstance(right_expr.typ,FloatType)):
                    return Res(FloatType())
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)
        elif(ast.op in ["\\","%"]):
            if(isinstance(left_expr.typ,IntType) and isinstance(right_expr.typ,IntType)):
                return Res(IntType())
            else:
                raise TypeMismatchInExpression(ast)  
        raise TypeMismatchInExpression(ast)
    def visitUnaryOp(self,ast:UnaryOp,o:Checker):
        o.undec_redec = UNDECLARED
        body:Res = self.visit(ast.body,o)

        if(ast.op == "!"):
            if(isinstance(body.typ,BoolType)):
                return Res(BoolType())
            else:
                raise TypeMismatchInExpression(ast)
        elif(ast.op == "-"):
            if(isinstance(body.typ,(IntType,FloatType))):
                return Res(copy.deepcopy(body.typ))
            else:
                raise TypeMismatchInExpression(ast)
    def visitArrayCell(self,ast:ArrayCell,o:Checker):
        arr:Res = self.visit(ast.arr,o)
        index:Res = self.visit(ast.idx,o)
        if(isinstance(arr.typ,ArrayType) and isinstance(index.typ,IntType)):
            return Res(arr.typ.eleType)
        else:
            raise TypeMismatchInExpression(ast)
    def visitFieldAccess(self,ast:FieldAccess,o:Checker):
        class_name:str = ""
        if(ast.fieldname.name[0]=="@"):
            #Static Attribute
            if(not ast.obj):
                class_name = o.cur_class.class_name.name
            elif(isinstance(ast.obj,Id)):
                class_name = ast.obj.name
            else:
                raise TypeMismatchInExpression(ast)
        else:
            #Instance Attribute
            o.undec_redec = UNDECLARED
            res:Res = self.visit(ast.obj,o)
            if(isinstance(res.typ,ClassType) and Id(res.typ.classname.name) in o.cur_class.mro):
                class_name = res.typ.classname.name
            else:
                raise TypeMismatchInExpression(ast)
            
        obj_env:ClassEnv = o.manager.get_class(class_name,UNDECLARED)
        field = ast.fieldname.name

        member_env = obj_env.get_member(field,Attribute(),UNDECLARED)
        if(isinstance(member_env,AttrEnv)):
            return Res(member_env.typ)
        else:
            raise TypeMismatchInExpression(ast) 
    def visitCallExpr(self,ast:CallExpr,o:Checker):
        class_name:str = ""
        if(ast.method.name[0]=="@"):
            #Static Attribute
            if(not ast.obj):
                class_name = o.cur_class.class_name.name
            elif(isinstance(ast.obj,Id)):
                class_name = ast.obj.name
            else:
                raise TypeMismatchInExpression(ast)
        else:
            #Instance Attribute
            o.undec_redec = UNDECLARED
            res:Res = self.visit(ast.obj,o)
            if(isinstance(res.typ,ClassType)):
                class_name = res.typ.classname.name
            else:
                raise TypeMismatchInExpression(ast)
        
        obj_env:ClassEnv = o.manager.get_class(class_name,UNDECLARED)
        field = ast.method.name

        member_env = obj_env.get_member(field,Method(),UNDECLARED)
        if(isinstance(member_env,MethodEnv)):
            if(isinstance(member_env.return_type,VoidType)):
                raise TypeMismatchInExpression(ast)
            o.undec_redec = UNDECLARED
            expr_list:List[Type] = [self.visit(param,o).typ for param in ast.param]
            param_list = member_env.param_type
            res_comp:bool = o.comp_type_param(param_list,expr_list)
            if(not res_comp):
                raise TypeMismatchInExpression(ast)
            else:
                return Res(member_env.return_type)
        else:
            raise TypeMismatchInExpression(ast) 

    def visitNewExpr(self,ast:NewExpr,o:Checker):
        class_name = ast.classname.name
        class_env = o.manager.get_class(class_name,UNDECLARED)
        class_constructor = class_env.constructor

        for constructor in class_constructor:
            param_list = constructor.param_type
            expr_list:List[Type] = [self.visit(param,o).typ for param in ast.param]
            res_comp:bool = o.comp_type_param(param_list,expr_list)
            if(res_comp):
                return Res(ClassType(Id(class_name)))
        raise TypeMismatchInExpression(ast)
#endregion

#region Statement 
    def visitBlock(self,ast:Block,o:Checker):
        reduce(lambda _,stmt:self.visit(stmt,o),ast.stmt,[])
    def visitAssign(self,ast:Assign,o:Checker):
        o.undec_redec = UNDECLARED
        left_res:Res = self.visit(ast.lhs,o)
        if(left_res.const_var):
            raise CannotAssignToConstant(ast)
        if(isinstance(left_res.typ,VoidType)):
            raise TypeMismatchInStatement(ast)
        right_res:Res = self.visit(ast.exp,o)
        if(not o.manager.check_type_comp_coerce(left_res.typ,right_res.typ)):
            raise TypeMismatchInStatement(ast)
    def visitIf(self,ast:If,o:Checker):
        o.undec_redec = UNDECLARED
        cond_expr:Res = self.visit(ast.expr,o)
        o.undec_redec = None
        if(not isinstance(cond_expr.typ,BoolType)):
            raise TypeMismatchInStatement(ast)
        if(ast.preStmt):
            o.scope = [{}]+o.scope
            self.visit(ast.preStmt,o)
            o.scope.pop(0)
        
        o.scope = [{}]+o.scope
        self.visit(ast.thenStmt,o)
        o.scope.pop(0)

        if(ast.elseStmt):
            o.scope = [{}]+o.scope
            self.visit(ast.elseStmt,o)
            o.scope.pop(0)
    def visitFor(self,ast:For,o:Checker):
        o.loop_count +=1
        self.visit(ast.initStmt,o)
        self.visit(ast.expr,o)
        self.visit(ast.postStmt,o)

        o.scope = [{}] + o.scope
        self.visit(ast.loop,o)
        o.scope.pop(0)

        o.loop_count -=1
        
    def visitContinue(self,ast:Continue,o:Checker):
        if(o.loop_count==0):
            raise MustInLoop(ast)
    
    def visitBreak(self,ast:Break,o:Checker):
        if(o.loop_count==0):
            raise MustInLoop(ast)
    
    def visitReturn(self,ast:Return,o:Checker):
        o.undec_redec = UNDECLARED
        if(ast.expr):
            ret_typ:Res = self.visit(ast.expr,o)
            if(not o.manager.check_type_comp_coerce(o.return_typ,ret_typ.typ)):
                raise TypeMismatchInStatement(ast)
        else:
            if(not isinstance(o.return_typ,VoidType)):
                raise TypeMismatchInStatement(ast)

    def visitCallStmt(self,ast:CallStmt,o:Checker):
        class_name:str = ""
        if(ast.method.name[0]=="@"):
            #Static Attribute
            if(not ast.obj):
                class_name = o.cur_class.class_name.name
            elif(isinstance(ast.obj,Id)):
                class_name = ast.obj.name
            else:
                raise TypeMismatchInExpression(ast)
        else:
            #Instance Attribute
            o.undec_redec = UNDECLARED
            res:Res = self.visit(ast.obj,o)
            if(isinstance(res.typ,ClassType)):
                class_name = res.typ.classname.name
            else:
                raise TypeMismatchInExpression(ast)
        
        obj_env:ClassEnv = o.manager.get_class(class_name,UNDECLARED)
        field = ast.method.name

        member_env = obj_env.get_member(field,Method(),UNDECLARED)
        if(isinstance(member_env,MethodEnv)):
            if(not isinstance(member_env.return_type,VoidType)):
                raise TypeMismatchInExpression(ast)
            o.undec_redec = UNDECLARED
            expr_list:List[Type] = [self.visit(param,o).typ for param in ast.param]
            param_list = member_env.param_type
            res_comp:bool = o.comp_type_param(param_list,expr_list)
            if(not res_comp):
                raise TypeMismatchInExpression(ast)
        else:
            raise TypeMismatchInExpression(ast) 
            
#endregion
#region Type
    def visitIntType(self,ast:IntType,o:Checker) -> IntType:
        return o.manager.check_type(ast)
    def visitFloatType(self,ast:FloatType,o:Checker) -> FloatType:
        return o.manager.check_type(ast)
    def visitBoolType(self,ast:BoolType,o:Checker) -> BoolType:
        return o.manager.check_type(ast)
    def visitStringType(self,ast:StringType,o:Checker) -> StringType:
        return o.manager.check_type(ast)
    def visitVoidType(self,ast:VoidType,o:Checker) -> VoidType:
        return o.manager.check_type(ast)
    def visitArrayType(self,ast:ArrayType,o:Checker) -> ArrayType:
        return o.manager.check_type(ast)
    def visitClassType(self,ast:ClassType,o:Checker) -> ClassType:
        return o.manager.check_type(ast)
#endregion

#region Literal
    def visitIntLiteral(self,ast:IntLiteral,o:Checker)->Res:
        return Res(IntType())
    def visitFloatLiteral(self,ast:FloatLiteral,o:Checker)->Res:
        return Res(FloatType())
    def visitBooleanLiteral(self,ast:BooleanLiteral,o:Checker)->Res:
        return Res(BoolType())
    def visitStringLiteral(self,ast:StringLiteral,o:Checker)->Res:
        return Res(StringType())
    def visitNullLiteral(self,ast:NullLiteral,o:Checker)->Res:
        return Res(VoidType())
    def visitSelfLiteral(self,ast:SelfLiteral,o:Checker)->Res:
        return Res(ClassType(Id(o.cur_class.class_name.name)))
    def visitArrayLiteral(self,ast:ArrayLiteral,o:Checker)->Res:
        typ = VoidType()
        for lit in ast.value:
            res:Res = self.visit(lit,o)
            lit_typ = res.typ
            if(isinstance(typ,VoidType)):
                if(not isinstance(lit_typ,VoidType)):
                    typ = copy.deepcopy(lit_typ)
            else:
                if(not o.manager.check_type_comp_fixed(typ,lit_typ)):
                    raise IllegalArrayLiteral(ast)
                
        return Res(ArrayType(len(ast.value),typ),False)
# endregion


    def visitId(self,ast:Id,o:Checker):
        return o.get_element(ast.name,o.cur_check,o.undec_redec)