import unittest
from TestUtils import TestChecker
from AST import *
 
class CheckSuite(unittest.TestCase): 
    # def test_400(self):
    #     input = Program([ClassDecl(Id("a"),[])])
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,400))
        
    # def test_401(self):
    #     input = Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),[],VoidType(),Block([])),AttributeDecl(VarDecl(Id("c"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType()))])])
    #     expect = "Redeclared Attribute: c"
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
    #     expect = "successful"
    #     self.assertTrue(TestChecker.test(input,expect,404))
    
    # def test_405(self):
    #     input = Program([ClassDecl(Id("io"),[])])
    #     expect = "Redeclared Class: io"
    #     self.assertTrue(TestChecker.test(input,expect,405))
    
    def test_406(self):
        input = Program([ClassDecl(Id("Program"),[MethodDecl(Id("@main"),[],VoidType(),Block([])),
                                                  ]),
                         ClassDecl(Id("Test"),[MethodDecl(Id("test"),[],VoidType(),Block([])),
                                                  ])])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,406))