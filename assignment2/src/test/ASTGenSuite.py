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
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("u"),IntType())),
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
            func foo  (a: int, b: float):void {}
            func @main():void{
                io.printInt(4);
            }}"""
        expect = str(Program([ClassDecl(Id("main"),[
            MethodDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],VoidType(),Block([])),
            MethodDecl(Id("@main"),[],VoidType(),Block([CallStmt(Id("io"),Id("printInt"),[IntLiteral(4)])]))])]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_308(self):
        input = """class main {
            var u, i:int = 1,2;
            var a, b, g, h: int;
            const c, d: bool;
            func test(a: int, b:string): void {}
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
            MethodDecl(Id("test"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),StringType())],VoidType(),Block([])),
            AttributeDecl(VarDecl(Id("x"),StringType())),
            AttributeDecl(VarDecl(Id("y"),StringType())),
            AttributeDecl(VarDecl(Id("z"),StringType())),
            AttributeDecl(VarDecl(Id("t"),StringType()))])]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test_309(self):
        input = """class main {
            var a: int;
            }
            class main1 {
                var b: int;
                }"""
        expect = str(Program([
            ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType()))]),
            ClassDecl(Id("main1"),[AttributeDecl(VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_310(self):
        input = """class main {var b: bool;}"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("b"),BoolType()))])]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_311(self):
        input = """class main {func @test(): void {continue;}}"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("@test"),[],VoidType(),Block([Continue()]))])]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_312(self):
        """More complex program"""
        input = """class main {
            const a, b: bool;
            var c, d: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            AttributeDecl(ConstDecl(Id("a"),BoolType(),None)),
            AttributeDecl(ConstDecl(Id("b"),BoolType(),None)),
            AttributeDecl(VarDecl(Id("c"),StringType())),
            AttributeDecl(VarDecl(Id("d"),StringType()))])]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_313(self):
        input = """class main {
            var a, b: float;
            var c, d: int;
            const e, f: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            AttributeDecl(VarDecl(Id("a"),FloatType())),
            AttributeDecl(VarDecl(Id("b"),FloatType())),
            AttributeDecl(VarDecl(Id("c"),IntType())),
            AttributeDecl(VarDecl(Id("d"),IntType())),
            AttributeDecl(ConstDecl(Id("e"),StringType(),None)),
            AttributeDecl(ConstDecl(Id("f"),StringType(),None))])]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_314(self):
        input = """class main {
            var u, i: int;
            var a, b, g, h: int;
            const c, d: bool;
            func test(X: int, _Y: float): int {}
            var x, y, z, t: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("u"),IntType())),
                    AttributeDecl(VarDecl(Id("i"),IntType())),
                    AttributeDecl(VarDecl(Id("a"),IntType())),
                    AttributeDecl(VarDecl(Id("b"),IntType())),
                    AttributeDecl(VarDecl(Id("g"),IntType())),
                    AttributeDecl(VarDecl(Id("h"),IntType())),
                    AttributeDecl(ConstDecl(Id("c"),BoolType(),None)),
                    AttributeDecl(ConstDecl(Id("d"),BoolType(),None)),
                    MethodDecl(Id("test"),[VarDecl(Id("X"),IntType()),VarDecl(Id("_Y"),FloatType())],IntType(),Block([])),
                    AttributeDecl(VarDecl(Id("x"),StringType())),
                    AttributeDecl(VarDecl(Id("y"),StringType())),
                    AttributeDecl(VarDecl(Id("z"),StringType())),
                    AttributeDecl(VarDecl(Id("t"),StringType()))
                    ])]))
        self.assertTrue(TestAST.test(input,expect,314))
    
    def test_315(self):
        """More complex program"""
        input = """class main {
            func constructor() {
                main.@printInt(4);
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            MethodDecl(Id("constructor"),[],VoidType(),Block([CallStmt(Id("main"),Id("@printInt"),[IntLiteral(4)])]))])]))
        self.assertTrue(TestAST.test(input,expect,315))
   
    def test_316(self):
        input = """class main {
            var u, i: int = 1, test.printInt(a + b);
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
            AttributeDecl(VarDecl(Id("i"),IntType(),CallExpr(Id("test"),Id("printInt"),[BinaryOp("+",Id("a"),Id("b"))]))),
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
        self.assertTrue(TestAST.test(input,expect,316))

    def test_317(self):
        input = """class main{
            func foo  (a: int, b: float):void {}
            func @main():void{
                io.printInt(4);
            }}"""
        expect = str(Program([ClassDecl(Id("main"),[
            MethodDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],VoidType(),Block([])),
            MethodDecl(Id("@main"),[],VoidType(),Block([CallStmt(Id("io"),Id("printInt"),[IntLiteral(4)])]))])]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_318(self):
        input = """class main {
            var u, i:int = A, B;
            var a, b, g, h: int;
            const c, d: J;
            func test(a: int, b:string): void {}
            var x, y, z, t: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            AttributeDecl(VarDecl(Id("u"),IntType(),Id("A"))),
            AttributeDecl(VarDecl(Id("i"),IntType(),Id("B"))),
            AttributeDecl(VarDecl(Id("a"),IntType())),
            AttributeDecl(VarDecl(Id("b"),IntType())),
            AttributeDecl(VarDecl(Id("g"),IntType())),
            AttributeDecl(VarDecl(Id("h"),IntType())),
            AttributeDecl(ConstDecl(Id("c"),ClassType(Id("J")),None)),
            AttributeDecl(ConstDecl(Id("d"),ClassType(Id("J")),None)),
            MethodDecl(Id("test"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),StringType())],VoidType(),Block([])),
            AttributeDecl(VarDecl(Id("x"),StringType())),
            AttributeDecl(VarDecl(Id("y"),StringType())),
            AttributeDecl(VarDecl(Id("z"),StringType())),
            AttributeDecl(VarDecl(Id("t"),StringType()))])]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_319(self):
        input = """class main {
            var a: int;
            }
            class main1 {
                var b: int;
                }
                class main2 {
                    var c: float;
                    }"""
        expect = str(Program([
            ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType()))]),
            ClassDecl(Id("main1"),[AttributeDecl(VarDecl(Id("b"),IntType()))]),
            ClassDecl(Id("main2"),[AttributeDecl(VarDecl(Id("c"),FloatType()))]),
            ]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_320(self):
        input = """class main {var b: bool;}"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("b"),BoolType()))])]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_321(self):
        input = """class main {func @test(): void {continue;}}"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("@test"),[],VoidType(),Block([Continue()]))])]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_322(self):
        """More complex program"""
        input = """class main {
            const a, b: bool;
            var c, d: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            AttributeDecl(ConstDecl(Id("a"),BoolType(),None)),
            AttributeDecl(ConstDecl(Id("b"),BoolType(),None)),
            AttributeDecl(VarDecl(Id("c"),StringType())),
            AttributeDecl(VarDecl(Id("d"),StringType()))])]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_323(self):
        input = """class main {
            var a, b: float;
            var c, d: int;
            const e, f: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            AttributeDecl(VarDecl(Id("a"),FloatType())),
            AttributeDecl(VarDecl(Id("b"),FloatType())),
            AttributeDecl(VarDecl(Id("c"),IntType())),
            AttributeDecl(VarDecl(Id("d"),IntType())),
            AttributeDecl(ConstDecl(Id("e"),StringType(),None)),
            AttributeDecl(ConstDecl(Id("f"),StringType(),None))])]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_324(self):
        input = """class main {
            var u, i: int;
            var a, b, g, h: int;
            const c, d: bool;
            func test(X: int, _Y: float): int {}
            var x, y, z, t: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("u"),IntType())),
                    AttributeDecl(VarDecl(Id("i"),IntType())),
                    AttributeDecl(VarDecl(Id("a"),IntType())),
                    AttributeDecl(VarDecl(Id("b"),IntType())),
                    AttributeDecl(VarDecl(Id("g"),IntType())),
                    AttributeDecl(VarDecl(Id("h"),IntType())),
                    AttributeDecl(ConstDecl(Id("c"),BoolType(),None)),
                    AttributeDecl(ConstDecl(Id("d"),BoolType(),None)),
                    MethodDecl(Id("test"),[VarDecl(Id("X"),IntType()),VarDecl(Id("_Y"),FloatType())],IntType(),Block([])),
                    AttributeDecl(VarDecl(Id("x"),StringType())),
                    AttributeDecl(VarDecl(Id("y"),StringType())),
                    AttributeDecl(VarDecl(Id("z"),StringType())),
                    AttributeDecl(VarDecl(Id("t"),StringType()))
                    ])]))
        self.assertTrue(TestAST.test(input,expect,324))
    
    def test_325(self):
        """More complex program"""
        input = """class main {
            func constructor() {
                main.@printInt(4);
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            MethodDecl(Id("constructor"),[],VoidType(),Block([CallStmt(Id("main"),Id("@printInt"),[IntLiteral(4)])]))])]))
        self.assertTrue(TestAST.test(input,expect,325))
   
    def test_326(self):
        input = """class main {
            var u, i: int = 1, test.printInt(a + b);
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
            AttributeDecl(VarDecl(Id("i"),IntType(),CallExpr(Id("test"),Id("printInt"),[BinaryOp("+",Id("a"),Id("b"))]))),
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
        self.assertTrue(TestAST.test(input,expect,326))

    def test_327(self):
        input = """class main{
            func foo  (a: int, b: float):void {}
            func @main():void{
                io.printInt(4);
            }}"""
        expect = str(Program([ClassDecl(Id("main"),[
            MethodDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],VoidType(),Block([])),
            MethodDecl(Id("@main"),[],VoidType(),Block([CallStmt(Id("io"),Id("printInt"),[IntLiteral(4)])]))])]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_328(self):
        input = """class main {
            var u, i:int = A, B;
            var a, b, g, h: int;
            const c, d: J;
            func test(a: int, b:string): void {}
            var x, y, z, t: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            AttributeDecl(VarDecl(Id("u"),IntType(),Id("A"))),
            AttributeDecl(VarDecl(Id("i"),IntType(),Id("B"))),
            AttributeDecl(VarDecl(Id("a"),IntType())),
            AttributeDecl(VarDecl(Id("b"),IntType())),
            AttributeDecl(VarDecl(Id("g"),IntType())),
            AttributeDecl(VarDecl(Id("h"),IntType())),
            AttributeDecl(ConstDecl(Id("c"),ClassType(Id("J")),None)),
            AttributeDecl(ConstDecl(Id("d"),ClassType(Id("J")),None)),
            MethodDecl(Id("test"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),StringType())],VoidType(),Block([])),
            AttributeDecl(VarDecl(Id("x"),StringType())),
            AttributeDecl(VarDecl(Id("y"),StringType())),
            AttributeDecl(VarDecl(Id("z"),StringType())),
            AttributeDecl(VarDecl(Id("t"),StringType()))])]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test_329(self):
        input = """class main {
            var a: int;
            }
            class main1 {
                var b: int;
                }
                class main2 {
                    var c: float;
                    }"""
        expect = str(Program([
            ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType()))]),
            ClassDecl(Id("main1"),[AttributeDecl(VarDecl(Id("b"),IntType()))]),
            ClassDecl(Id("main2"),[AttributeDecl(VarDecl(Id("c"),FloatType()))]),
            ]))
        self.assertTrue(TestAST.test(input,expect,329))