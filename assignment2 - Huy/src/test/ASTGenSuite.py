import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """class main {
            func test(a: string, b: int): int {}
        }"""
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(VarDecl(Id(a),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,300))

#     def test_simple_program(self):
#         input = """class main {var x, y, z: int = false, 2, 3;}"""
#         expect = "Program([ClassDecl(Id(main),[AttributeDecl(VarDecl(Id(x),IntType,IntLit(1))),AttributeDecl(VarDecl(Id(y),IntType,IntLit(2))),AttributeDecl(VarDecl(Id(z),IntType,IntLit(3)))])])"
#         self.assertTrue(TestAST.test(input,expect,301))

#     def test_class_with_one_decl_program(self):
#         input = """class object<-main{ const x, y, z: int = 1, 2, 3;
#         var a, b: float;}"""
#         expect = "Program([ClassDecl(Id(main),Id(object),[AttributeDecl(ConstDecl(Id(x),IntType,IntLit(1))),AttributeDecl(ConstDecl(Id(y),IntType,IntLit(2))),AttributeDecl(ConstDecl(Id(z),IntType,IntLit(3))),AttributeDecl(VarDecl(Id(a),FloatType)),AttributeDecl(VarDecl(Id(b),FloatType))])])"
#         self.assertTrue(TestAST.test(input,expect,302))
    
#     def test_class_with_two_decl_program(self):
#         input = """class main{ func a(): void {}}"""
#         expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(a),[],VoidType,Block([]))])])"
#         self.assertTrue(TestAST.test(input,expect,303))
   
#     def test_class_with_two_decl_program(self):
#         input = """class main{
# func foo  (a: int, b: float):void {}

# func @main():void{
#      io.printInt(4);
# }}"""
#         expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(foo),[Param(Id(a),IntType),Param(Id(b),FloatType)],VoidType,Block([])),MethodDecl(Id(@main),[],VoidType,Block([Call(Id(io),Id(printInt),[IntLit(4)])]))])])"
#         self.assertTrue(TestAST.test(input,expect,303))