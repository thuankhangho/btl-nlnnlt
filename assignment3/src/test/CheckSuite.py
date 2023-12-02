import unittest
from TestUtils import TestChecker
from AST import *
 
class CheckSuite(unittest.TestCase):
    # def test_400(self):
    #     input = Program([ClassDecl(Id("a"),[])])
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,400))
        
    # def test_401(self):
    #     input = Program([ClassDecl(Id("Program"),[MethodDecl(Id("@main"),[],VoidType(),Block([])),AttributeDecl(VarDecl(Id("c"),IntType())),AttributeDecl(VarDecl(Id("b"),IntType()))])])
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input,expect,401))
        
    # def test_402(self):
    #     input = Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),[],VoidType(),Block([])),AttributeDecl(VarDecl(Id("c"),IntType())),MethodDecl(Id("c"),[],IntType(),Block([]))])])
    #     expect = "Redeclared Method: c"
    #     self.assertTrue(TestChecker.test(input,expect,402))
        
    # def test_403(self):
    #     input = Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),[],VoidType(),Block([]))]),ClassDecl(Id("c"),[]),ClassDecl(Id("c"),[])])
    #     expect = "Redeclared Class: c"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_404(self):
    #     input = Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),[],VoidType(),Block([]))])])
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,404))
    
    # def test_405(self):
    #     input = Program([ClassDecl(Id("io"),[])])
    #     expect = "Redeclared Class: io"
    #     self.assertTrue(TestChecker.test(input,expect,405))
    
    # def test_406(self):
    #     input = Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),[],VoidType(),Block([])),
    #                                               ]),
    #                      ClassDecl(Id("Test"),[MethodDecl(Id("test"),[],VoidType(),Block([])),
    #                                               ])])
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,406))
    
    # def test_407(self):
    #     input = """
    #     class Program {
    #         func @main(): void {
                
    #         }
    #     }
    #     class Program {}
    #     """
    #     expect = "Redeclared Class: Program"
    #     self.assertTrue(TestChecker.test(input,expect,407))
        
    # def test_408(self):
    #     input = """
    #     class Program {
    #         func @main(): void {
                
    #         }
    #     }
    #     class a {
    #         var a: int;
    #     }
    #     class a {
    #         var a: string;
    #     }
    #     """
    #     expect = "Redeclared Class: a"
    #     self.assertTrue(TestChecker.test(input,expect,408))

    # def test_409(self):
    #     input = """
    #     class Program {
    #         func @main(): void {
                
    #         }
    #     }
    #     class a {
    #         var a: int;
    #     }
    #     class b <- a {
    #         var a: string;
    #     }
    #     """
    #     expect = "Redeclared Class: a"
    #     self.assertTrue(TestChecker.test(input,expect,409))

    # def test_410(self):
    #     input = """
    #     class Program {
    #         func @main(): void {
                
    #         }
    #     }
    #     class a {
    #         var a: int;
    #         func constructor(a: int) {}
    #         func constructor(a: string) {}
    #     }
    #     class b <- a {
    #         var a: string;
    #     }
    #     """
    #     expect = "Redeclared Class: a"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_411(self):
    #     input = """
    #     class Program {}
    #     class Program {
    #         func @main(): void {
                
    #         }
    #     }
    #     """
    #     expect = "Redeclared Class: Program"
    #     self.assertTrue(TestChecker.test(input,expect,411))

    # def test_412(self):
    #     input = """
    #     class Program {
    #         func @main(): void {
                
    #         }
    #     }
    #     class Program <- Test {
    #         var a: string;
    #         var a: int;
    #     }
    #     """
    #     expect = "Redeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input,expect,412))

    # def test_413(self):
    #     input = """
    #     class Program {
    #         func @main(): void {
                
    #         }
    #     }
    #     class Program <- Test {
    #         func test(): void {}
    #         func test(): int {}
    #     }
    #     """
    #     expect = "Redeclared Method: test"
    #     self.assertTrue(TestChecker.test(input,expect,413))

    # def test_414(self):
    #     input = """
    #     class Program {
    #         func @main(): void {}
    #     }
    #     class a {} class b {} class c {} class a {}
    #     """
    #     expect = "Redeclared Class: a"
    #     self.assertTrue(TestChecker.test(input,expect,414))

    # def test_415(self):
    #     input = """
    #     class Program {
    #         func @main(): void {}
    #     }
    #     class io {}
    #     """
    #     expect = "Redeclared Class: io"
    #     self.assertTrue(TestChecker.test(input,expect,415))

    # def test_416(self):
    #     input = """
    #     class Program {}
    #     class a <- Program {
    #         func @main(): void
    #     }
    #     """
    #     expect = "Redeclared Class: Program"
    #     self.assertTrue(TestChecker.test(input,expect,416))

    # def test_417(self):
    #     input = """
    #     class Program {
    #         func @main(): void {}
    #         var a: int;
    #         func a(): void {}
    #     }
    #     """
    #     expect = "Redeclared Method: a"
    #     self.assertTrue(TestChecker.test(input,expect,417))

    # def test_418(self):
    #     input = """
    #     class a {}
    #     class b {}
    #     class a <- Program {
    #         func @main(): void {}
    #     }
    #     class b <- Program {
    #         func @main(): int {}
    #     }
    #     """
    #     expect = "Redeclared Class: Program"
    #     self.assertTrue(TestChecker.test(input,expect,418))

    def test_419(self):
        input = """
        class Program {
            func @main(): void {}
            var a: int;
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,419))