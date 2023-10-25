import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        input = """class main {var a: int;}"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_301(self):
        input = """class main {func @test(): int {break;}}"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("@test"),[],IntType(),Block([Break()]))])]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_302(self):
        """More complex program"""
        input = """class main {
            var a, b:int;
            var c:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("b"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_303(self):
        input = """class main {
            var a, b:int;
            var c:int;
            const d:string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("b"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType())),AttributeDecl(ConstDecl(Id("d"),StringType(),None))])]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_304(self):
        input = """class main {
            var u, i: int;
            var a, b, g, h: int;
            const c, d: bool;
            func test(a: int, b:string): void {}
            var x, y, z, t: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
                    AttributeDecl(VarDecl(Id("u"),IntType())),
                    AttributeDecl(VarDecl(Id("i"),IntType())),
                    AttributeDecl(VarDecl(Id("a"),IntType())),
                    AttributeDecl(VarDecl(Id("b"),IntType())),
                    AttributeDecl(VarDecl(Id("g"),IntType())),
                    AttributeDecl(VarDecl(Id("h"),IntType())),
                    AttributeDecl(ConstDecl(Id("c"),BoolType(),None)),
                    AttributeDecl(ConstDecl(Id("d"),BoolType(),None)),
                    MethodDecl(Id("test"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),StringType())],VoidType(),Block([])),
                    AttributeDecl(VarDecl(Id("x"),StringType())),
                    AttributeDecl(VarDecl(Id("y"),StringType())),
                    AttributeDecl(VarDecl(Id("z"),StringType())),
                    AttributeDecl(VarDecl(Id("t"),StringType()))
                    ])]))
        self.assertTrue(TestAST.test(input,expect,304))
    
    def test_305(self):
        """More complex program"""
        input = """class main {
            var a:int;
            var b:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("a"),IntType())),
             AttributeDecl(VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,305))
   
    def test_306(self):
        input = """class main {
            var u, i:int = 1,2;
            var a, b, g, h: int;
            const c, d: bool;
            func test(a: int, b:string): void {
                var cc: int = 1;
                var dd, ee, ff: string = "2", "3", "4";
                const ddd, eee, fff: bool;
            }
            var x, y, z, t: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            AttributeDecl(VarDecl(Id("u"),IntType(),IntLiteral(1))),
            AttributeDecl(VarDecl(Id("i"),IntType(),IntLiteral(2))),
            AttributeDecl(VarDecl(Id("a"),IntType())),
            AttributeDecl(VarDecl(Id("b"),IntType())),
            AttributeDecl(VarDecl(Id("g"),IntType())),
            AttributeDecl(VarDecl(Id("h"),IntType())),
            AttributeDecl(ConstDecl(Id("c"),BoolType(),None)),
            AttributeDecl(ConstDecl(Id("d"),BoolType(),None)),
            MethodDecl(Id("test"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),StringType())],VoidType(),
                       Block([VarDecl(Id("cc"),IntType(),IntLiteral(1)),
                              VarDecl(Id("dd"),StringType(),StringLiteral("2")),
                              VarDecl(Id("ee"),StringType(),StringLiteral("3")),
                              VarDecl(Id("ff"),StringType(),StringLiteral("4")),
                              ConstDecl(Id("ddd"),BoolType(),None),
                              ConstDecl(Id("eee"),BoolType(),None),
                              ConstDecl(Id("fff"),BoolType(),None)])),
            AttributeDecl(VarDecl(Id("x"),StringType())),
            AttributeDecl(VarDecl(Id("y"),StringType())),
            AttributeDecl(VarDecl(Id("z"),StringType())),
            AttributeDecl(VarDecl(Id("t"),StringType()))])]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_307(self):
        input = """class main{
            func @main():void{
                io.printInt(4);
            }}"""
        expect = str(Program([ClassDecl(Id("main"),[
            MethodDecl(Id("@main"),[],VoidType(),Block([CallStmt(Id("io"),Id("printInt"),[IntLiteral(4)])]))])]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_308(self):
        input = """class main {
            var u, i: int = 1,2;
            var a, b, g, h: int;
            const c, d: bool;
            func test(a: int, b:string): void {}
            var x, y, z, t: string;
        }"""
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(VarDecl(Id(u),IntType,IntLit(1))),AttributeDecl(VarDecl(Id(i),IntType,IntLit(2))),AttributeDecl(VarDecl(Id(a),IntType)),AttributeDecl(VarDecl(Id(b),IntType)),AttributeDecl(VarDecl(Id(g),IntType)),AttributeDecl(VarDecl(Id(h),IntType)),AttributeDecl(ConstDecl(Id(c),BoolType,None)),AttributeDecl(ConstDecl(Id(d),BoolType,None)),MethodDecl(Id(test),[Param(Id(a),IntType),Param(Id(b),StringType)],VoidType,Block([])),AttributeDecl(VarDecl(Id(x),StringType)),AttributeDecl(VarDecl(Id(y),StringType)),AttributeDecl(VarDecl(Id(z),StringType)),AttributeDecl(VarDecl(Id(t),StringType))])])"
        self.assertTrue(TestAST.test(input,expect,308))