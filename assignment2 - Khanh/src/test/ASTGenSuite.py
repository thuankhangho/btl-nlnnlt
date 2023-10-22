import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: class main {} """
    #     input = """class main {}"""
    #     expect = str(Program([ClassDecl(Id("main"),[])]))
    #     self.assertTrue(TestAST.test(input,expect,300))

    # def test_simple_program(self):
    #     input = """class main {func @test(): int {break;}}"""
    #     expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("@test"),[],IntType(),Block([Break()]))])]))
    #     self.assertTrue(TestAST.test(input,expect,301))

    # def test_class_with_one_decl_program(self):
    #     """More complex program"""
    #     input = """class main {
    #         var a, b:int;
    #         var c:int;
    #     }"""
    #     expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType()))])]))
    #     self.assertTrue(TestAST.test(input,expect,302))

    def test_class_with_one_decl_program(self):
        input = """class main {
            var a, b:int;
            const c,d:bool;
            var x,y,z,t: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,303))
    
    # def test_class_with_two_decl_program(self):
    #     """More complex program"""
    #     input = """class main {
    #         var a:int;
    #         var b:int;
    #     }"""
    #     expect = str(Program([ClassDecl(Id("main"),
    #         [AttributeDecl(VarDecl(Id("a"),IntType())),
    #          AttributeDecl(VarDecl(Id("b"),IntType()))])]))
    #     self.assertTrue(TestAST.test(input,expect,304))
   