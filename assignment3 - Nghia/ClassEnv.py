from functools import reduce
from typing import Dict, List

from AST import *
from StaticError import *

class MemberEnv:
    pass
class MethodEnv:
    name:Id
    paramList: List[Type]
    returnType: Type
    static: bool
    def __init__(self,_name:Id,_param:List[Type],_returnType:Type,_static:bool):
        self.name=_name
        self.paramList = _param
        self.returnType = _returnType
        self.static = _static
    
    def __eq__(self, __value: object) -> bool:
        if(type(__value)==MethodEnv):
            return (
                self.name.name == __value.name.name and
                list(map(lambda param:str(param),self.paramList)) == list(map(lambda param:str(param),__value.paramList)) and
                self.returnType == __value.returnType
            )
        return False
class AttrEnv:
    id: Id
    typ: Type
    const_var:bool
    static:bool
    def __init__(self,_id:Id,_typ:Type,_const_var:bool,_static:bool):
        # const is True && var is False
        self.id = _id
        self.typ = _typ
        self.const_var = _const_var
        self.static = _static
class ClassEnv:
    classname:Id
    memlist: Dict[str,MemberEnv]
    mro: List[Id]
    constructor: List[MethodEnv]
    
    def __init__(self,class_decl:ClassDecl,par_memlist:Dict[str,MemberEnv]={},par_mro:List[Id]=[],manager=None):
        self.constructor=[]
        if(class_decl):
            self.classname = Id(class_decl.classname.name)

            self.memlist = par_memlist
            reduce(lambda _,mem:self.extract_mem(mem,manager),class_decl.memlist,self.memlist)

            self.mro = [self.classname] + par_mro
        else:
            self.classname = Id("io")
            self.memlist = {
                "@readInt": MethodEnv(
                    Id("@readInt"),
                    [],
                    IntType(),
                    True
                ),
                "@writeInt": MethodEnv(
                    Id("@writeInt"),
                    [IntType()],
                    VoidType(),
                    True
                ),
                "@readFloat": MethodEnv(
                    Id("@readFloat"),
                    [],
                    FloatType(),
                    True
                ),
                "@writeFloat": MethodEnv(
                    Id("@writeFloat"),
                    [FloatType()],
                    VoidType(),
                    True
                ),
                "@readBool": MethodEnv(
                    Id("@readBool"),
                    [],
                    BoolType(),
                    True
                ),
                "@writeBool": MethodEnv(
                    Id("@writeBool"),
                    [BoolType()],
                    VoidType(),
                    True
                ),
                "@readStr": MethodEnv(
                    Id("@readStr"),
                    [],
                    StringType(),
                    True
                ),
                "@writeStr": MethodEnv(
                    Id("@writeStr"),
                    [StringType()],
                    VoidType(),
                    True
                )
            }
            self.mro = []

    def extract_mem(self,mem:MemDecl,manager):
        if(type(mem)==AttributeDecl):
            # Attribute
            self.extract_mem_attr(mem,manager)
        else:
            # Method
            self.extract_mem_method(mem,manager)
    
    def extract_mem_attr(self,mem:AttributeDecl,manager):
        decl:StoreDecl = mem.decl
        if(type(decl) == ConstDecl):
            self.extract_attr_const(decl,manager)
        else:
            self.extract_attr_var(decl,manager)
    def extract_mem_method(self,mem:MethodDecl,manager):
        name = mem.name.name
        if(name in self.memlist and name != "constructor"):
            raise Redeclared(Method(),name)
        paramTyp = list(map(lambda el:manager.check_class_type(el.varType),mem.param))
        returnTyp = manager.check_class_type(mem.returnType)
        method = MethodEnv(Id(name),paramTyp,returnTyp,(name[0]=='@'))
        if(name == 'constructor'):
            if(any(map(lambda el:method==el,self.constructor))):
                raise Redeclared(Method(),name)
            else:
                self.constructor +=[method]
        else:
            self.memlist[name] = method
    

    def extract_attr_const(self,mem:ConstDecl,manager):
        name = mem.constant.name
        if(name in self.memlist):
            raise Redeclared(Attribute(),name)
        
        typ = manager.check_class_type(mem.constType)
        
        self.memlist[name] = AttrEnv(Id(name),typ,_const_var=True,_static=(name[0]=='@'))
    def extract_attr_var(self,mem:VarDecl,manager):
        name = mem.variable.name
        if(name in self.memlist):
            raise Redeclared(Attribute(),name)
        
        typ = manager.check_class_type(mem.varType)
        
        self.memlist[name] = AttrEnv(Id(name),typ,_const_var=False,_static=(name[0]=='@'))
class ClassManager:
    class_list: Dict[str,ClassEnv]
    def __init__(self,ast:Program):
        self.class_list = {
            "io": ClassEnv(None)
        }
        for class_decl in ast.decl:
            self.add_class(class_decl)

    def add_class(self,class_decl:ClassDecl):
        name = class_decl.classname.name
        if(name in self.class_list):
            raise Redeclared(Class(),name)
        
        if(class_decl.parentname):
            # Có thừa kế
            par_name = class_decl.parentname.name
            if(par_name not in self.class_list):
                raise Undeclared(Class(),par_name)
            par_env = self.class_list[par_name]
            self.class_list[name] = ClassEnv(class_decl,par_env.memlist.copy(),par_env.mro.copy(),self)
        else:
            self.class_list[name] = ClassEnv(class_decl,{},[],self)

    def check_class_type(self,typ:Type):
        if(type(typ) == ClassType):
            if(typ.classname.name not in self.class_list):
                raise Undeclared(Class(),typ.classname.name)
        return typ
    
    def check_entry(self)->bool:
        if("Program" in self.class_list):
            program = self.class_list["Program"]
            if("@main" in program.memlist):
                mems = program.memlist
                if(type(mems["@main"])==MethodEnv):
                    if(
                        mems["@main"].returnType == VoidType() and 
                        mems["@main"].paramList == []
                    ):
                        return True
        
        raise NoEntryPoint()

    def get_class_env(self,class_name:str)->ClassEnv:
        return self.class_list[class_name]