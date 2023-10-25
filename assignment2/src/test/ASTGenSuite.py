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
        input = """class main {
            var b: float;
            }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("b"),FloatType()))])]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_321(self):
        input = """class main {
            func @test(): void {return a;}
            }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("@test"),[],VoidType(),Block([Return(Id("a"))]))])]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_322(self):
        input = """class prog {
            const a, b: bool = true, false;
            var c, d: string;
        }"""
        expect = str(Program([ClassDecl(Id("prog"),[
            AttributeDecl(ConstDecl(Id("a"),BoolType(),BooleanLiteral(True))),
            AttributeDecl(ConstDecl(Id("b"),BoolType(),BooleanLiteral(False))),
            AttributeDecl(VarDecl(Id("c"),StringType())),
            AttributeDecl(VarDecl(Id("d"),StringType()))])]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_323(self):
        input = """class main {
            var a, b: float;
            var c, d: int;
            const e, f: string = "abc", "def";
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            AttributeDecl(VarDecl(Id("a"),FloatType())),
            AttributeDecl(VarDecl(Id("b"),FloatType())),
            AttributeDecl(VarDecl(Id("c"),IntType())),
            AttributeDecl(VarDecl(Id("d"),IntType())),
            AttributeDecl(ConstDecl(Id("e"),StringType(),StringLiteral("abc"))),
            AttributeDecl(ConstDecl(Id("f"),StringType(),StringLiteral("def")))])]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_324(self):
        input = """class main {
            var i1, i2: int;
            var a, b, g, h: int;
            const c, d: bool;
            func test(X: int, _Y: float): void {return "abc";}
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("i1"),IntType())),
                    AttributeDecl(VarDecl(Id("i2"),IntType())),
                    AttributeDecl(VarDecl(Id("a"),IntType())),
                    AttributeDecl(VarDecl(Id("b"),IntType())),
                    AttributeDecl(VarDecl(Id("g"),IntType())),
                    AttributeDecl(VarDecl(Id("h"),IntType())),
                    AttributeDecl(ConstDecl(Id("c"),BoolType(),None)),
                    AttributeDecl(ConstDecl(Id("d"),BoolType(),None)),
                    MethodDecl(Id("test"),[VarDecl(Id("X"),IntType()),VarDecl(Id("_Y"),FloatType())],VoidType(),Block([Return(StringLiteral("abc"))]))
                    ])]))
        self.assertTrue(TestAST.test(input,expect,324))
    
    def test_325(self):
        input = """class main {
            func constructor() {
                main.@printInt(a + b);
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            MethodDecl(Id("constructor"),[],VoidType(),Block([CallStmt(Id("main"),Id("@printInt"),[BinaryOp("+",Id("a"),Id("b"))])]))])]))
        self.assertTrue(TestAST.test(input,expect,325))
   
    def test_326(self):
        input = """class main {
            var u, i: int = 1, test.printInt(a + b);
            var a, b, g, h: int;
            const c, d: bool;
            func test(a: int, b:string): void {
                var cc: int = 1;
                var pi, alpha, tau: float = 3.14197, 22*7, 3 / 4;
                const ddd, eee, fff: bool;
            }
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
                              VarDecl(Id("pi"),FloatType(),FloatLiteral(3.14197)),
                              VarDecl(Id("alpha"),FloatType(),BinaryOp("*",IntLiteral(22),IntLiteral(7))),
                              VarDecl(Id("tau"),FloatType(),BinaryOp("/",IntLiteral(3),IntLiteral(4))),
                              ConstDecl(Id("ddd"),BoolType(),None),
                              ConstDecl(Id("eee"),BoolType(),None),
                              ConstDecl(Id("fff"),BoolType(),None)]))
            ])]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_327(self):
        input = """class main{
            func foo (a: string, b: bool): int {}
            func @main():void{
                io.printInt(a / 4);
            }}"""
        expect = str(Program([ClassDecl(Id("main"),[
            MethodDecl(Id("foo"),[VarDecl(Id("a"),StringType()),VarDecl(Id("b"),BoolType())],IntType(),Block([])),
            MethodDecl(Id("@main"),[],VoidType(),Block([CallStmt(Id("io"),Id("printInt"),[BinaryOp("/",Id("a"),IntLiteral(4))])]))])]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_328(self):
        input = """class main {
            var u, i: int = A, B;
            const c, d: J;
            func test(a: int, b:string): void {
                return test + test1;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            AttributeDecl(VarDecl(Id("u"),IntType(),Id("A"))),
            AttributeDecl(VarDecl(Id("i"),IntType(),Id("B"))),
            AttributeDecl(ConstDecl(Id("c"),ClassType(Id("J")),None)),
            AttributeDecl(ConstDecl(Id("d"),ClassType(Id("J")),None)),
            MethodDecl(Id("test"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),StringType())],VoidType(),Block([Return(BinaryOp("+",Id("test"),Id("test1")))]))
            ])]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test_329(self):
        input = """class main2 {
            var a: float;
            }
            class main3 {
                var b: string;
                }
                class main1 {
                    var c: float;
                    }"""
        expect = str(Program([
            ClassDecl(Id("main2"),[AttributeDecl(VarDecl(Id("a"),FloatType()))]),
            ClassDecl(Id("main3"),[AttributeDecl(VarDecl(Id("b"),StringType()))]),
            ClassDecl(Id("main1"),[AttributeDecl(VarDecl(Id("c"),FloatType()))]),
            ]))
        self.assertTrue(TestAST.test(input,expect,329))
        
    def test_330(self):
        input = """class main {
            const a, b: int = 1, a[9].printInt();
            }"""
        expect = str(Program([ClassDecl(Id("main"),[
            AttributeDecl(ConstDecl(Id("a"),IntType(),IntLiteral(1))),
            AttributeDecl(ConstDecl(Id("b"),IntType(),CallExpr(ArrayCell(Id("a"),IntLiteral(9)),Id("printInt"),[])))])]))
        self.assertTrue(TestAST.test(input,expect,330))

    def test_331(self):
        input = """class main {
            func @__test(): int {
                self.aPI := 3.14;
                }
            }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("@__test"),[],IntType(),Block([Assign(FieldAccess(SelfLiteral(),Id("aPI")),FloatLiteral(3.14))]))])]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test_332(self):
        input = """class main {
            var a, b:int;
            var c: int = x.foo(5);
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("b"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType(),CallExpr(Id("x"),Id("foo"),[IntLiteral(5)])))])]))
        self.assertTrue(TestAST.test(input,expect,332))

    def test_333(self):
        input = """class main {
            var a, b: [5]float;
            const c: bool;
            var d: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),ArrayType(IntLiteral(5),FloatType()))),AttributeDecl(VarDecl(Id("b"),ArrayType(IntLiteral(5),FloatType()))),AttributeDecl(ConstDecl(Id("c"),BoolType(),None)),AttributeDecl(VarDecl(Id("d"),StringType()))])]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_334(self):
        input = """class main {
            var u, i: float;
            const c, d: string = "false", "false";
            func test(a: int, b:string): void {}
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("u"),FloatType())),
                    AttributeDecl(VarDecl(Id("i"),FloatType())),
                    AttributeDecl(ConstDecl(Id("c"),StringType(),StringLiteral("false"))),
                    AttributeDecl(ConstDecl(Id("d"),StringType(),StringLiteral("false"))),
                    MethodDecl(Id("test"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),StringType())],VoidType(),Block([]))
                    ])]))
        self.assertTrue(TestAST.test(input,expect,334))
    
    def test_335(self):
        input = """class main {
            func test():void{
                Shape.@getArea(15);
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("test"),[],VoidType(),Block([CallStmt(Id("Shape"),Id("@getArea"),[IntLiteral(15)])]))])]))
        self.assertTrue(TestAST.test(input,expect,335))
   
    def test_336(self):
        input = """class main {
            var u, i:int = 1,2;
            var a, b, g, h: int;
            const c, d: bool;
            func test(a: int, b:string): void {
                var cc: int = 1;
                var dd, ee, ff: string = "2", "3", "4";
                Shape.@getArea(1 + 2, 3 * 4);
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
                              CallStmt(Id("Shape"),Id("@getArea"),[
                                  BinaryOp("+",IntLiteral(1),IntLiteral(2)),BinaryOp("*",IntLiteral(3),IntLiteral(4))])])),
            AttributeDecl(VarDecl(Id("x"),StringType())),
            AttributeDecl(VarDecl(Id("y"),StringType())),
            AttributeDecl(VarDecl(Id("z"),StringType())),
            AttributeDecl(VarDecl(Id("t"),StringType()))])]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test_337(self):
        input = """class main {
            func test():void{
                a:=new X().a[2].t[7+2];
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("test"),[],VoidType(),Block([Assign(Id("a"),ArrayCell(FieldAccess(ArrayCell(FieldAccess(NewExpr(Id("X"),[]),Id("a")),IntLiteral(2)),Id("t")),BinaryOp("+",IntLiteral(7),IntLiteral(2))))]))])]))
        self.assertTrue(TestAST.test(input,expect,337))

    def test_338(self):
        input = """class main {
            func test():void{
                Shape.a := true;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("test"),[],VoidType(),Block([Assign(FieldAccess(Id("Shape"),Id("a")),BooleanLiteral(True))]))])]))
        self.assertTrue(TestAST.test(input,expect,338))

    def test_339(self):
        input = """class main {
            var a: int;
            }
            class main1 {
                const b: int = 100;
                }"""
        expect = str(Program([
            ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType()))]),
            ClassDecl(Id("main1"),[AttributeDecl(ConstDecl(Id("b"),IntType(),IntLiteral(100)))])]))
        self.assertTrue(TestAST.test(input,expect,339))
        
    def test_340(self):
        input = """class main {const a: int = 0;}"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(ConstDecl(Id("a"),IntType(),IntLiteral(0)))])]))
        self.assertTrue(TestAST.test(input,expect,340))

    def test_341(self):
        input = """class main {func @test(): int {l[3] := value * 2;}}"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("@test"),[],IntType(),Block([Assign(ArrayCell(Id("l"),IntLiteral(3)),BinaryOp("*",Id("value"),IntLiteral(2)))]))])]))
        self.assertTrue(TestAST.test(input,expect,341))

    def test_342(self):
        input = """class main {
            func test():void{
                if {i := 0;} j > i {j := j - 1;} else {j := j + 1;}
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("test"),[],VoidType(),Block([If(BinaryOp(">",Id("j"),Id("i")),Block([Assign(Id("j"),BinaryOp("-",Id("j"),IntLiteral(1)))]),Block([Assign(Id("i"),IntLiteral(0))]),Block([Assign(Id("j"),BinaryOp("+",Id("j"),IntLiteral(1)))]))]))])]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test_343(self):
        input = """class main {
            var a, b:int;
            var c: int;
            const d: string = false;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("b"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType())),AttributeDecl(ConstDecl(Id("d"),StringType(),BooleanLiteral(False)))])]))
        self.assertTrue(TestAST.test(input,expect,343))

    def test_344(self):
        input = """class main {
            var u, i: int;
            const c, d: bool;
            var x, y, z, t: string;
            func test(a: int, b: string): bool {}
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("u"),IntType())),
                    AttributeDecl(VarDecl(Id("i"),IntType())),
                    AttributeDecl(ConstDecl(Id("c"),BoolType(),None)),
                    AttributeDecl(ConstDecl(Id("d"),BoolType(),None)),
                    AttributeDecl(VarDecl(Id("x"),StringType())),
                    AttributeDecl(VarDecl(Id("y"),StringType())),
                    AttributeDecl(VarDecl(Id("z"),StringType())),
                    AttributeDecl(VarDecl(Id("t"),StringType())),
                    MethodDecl(Id("test"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),StringType())],BoolType(),Block([]))
                    ])]))
        self.assertTrue(TestAST.test(input,expect,344))
    
    def test_345(self):
        input = """class main {
            var a, b: int;
            var c, d: int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("a"),IntType())),
             AttributeDecl(VarDecl(Id("b"),IntType())),
             AttributeDecl(VarDecl(Id("c"),IntType())),
             AttributeDecl(VarDecl(Id("d"),IntType()))
             ])]))
        self.assertTrue(TestAST.test(input,expect,345))
   
    def test_346(self):
        input = """class main {
            var u, i: int = a + b, c + d;
            var a, b: bool;
            const c, d: bool;
            func test(a: int, b:string): void {
                var dd, ee, ff: string = "2", "3", "4";
                const ddd, eee, fff: bool;
            }
            var x, y, z, t: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            AttributeDecl(VarDecl(Id("u"),IntType(),BinaryOp("+",Id("a"),Id("b")))),
            AttributeDecl(VarDecl(Id("i"),IntType(),BinaryOp("+",Id("c"),Id("d")))),
            AttributeDecl(VarDecl(Id("a"),BoolType())),
            AttributeDecl(VarDecl(Id("b"),BoolType())),
            AttributeDecl(ConstDecl(Id("c"),BoolType(),None)),
            AttributeDecl(ConstDecl(Id("d"),BoolType(),None)),
            MethodDecl(Id("test"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),StringType())],VoidType(),
                       Block([
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
        self.assertTrue(TestAST.test(input,expect,346))

    def test_347(self):
        input = """class main{
            func foobar (a: bool, b: float): float {}
            func @main():void{
                test[5].printInt(4);
            }}"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("foobar"),[VarDecl(Id("a"),BoolType()),VarDecl(Id("b"),FloatType())],FloatType(),Block([])),MethodDecl(Id("@main"),[],VoidType(),Block([CallStmt(ArrayCell(Id("test"),IntLiteral(5)),Id("printInt"),[IntLiteral(4)])]))])]))
        self.assertTrue(TestAST.test(input,expect,347))

    def test_348(self):
        input = """class main {
            var a, b, g, h: int;
            const c, d: bool;
            var x, y, z, t: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            AttributeDecl(VarDecl(Id("a"),IntType())),
            AttributeDecl(VarDecl(Id("b"),IntType())),
            AttributeDecl(VarDecl(Id("g"),IntType())),
            AttributeDecl(VarDecl(Id("h"),IntType())),
            AttributeDecl(ConstDecl(Id("c"),BoolType(),None)),
            AttributeDecl(ConstDecl(Id("d"),BoolType(),None)),
            AttributeDecl(VarDecl(Id("x"),StringType())),
            AttributeDecl(VarDecl(Id("y"),StringType())),
            AttributeDecl(VarDecl(Id("z"),StringType())),
            AttributeDecl(VarDecl(Id("t"),StringType()))])]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test_349(self):
        input = """class Parent <- Child {
                var a: int;
                const b: int = 5;
            }"""
        expect = str(Program([ClassDecl(Id("Child"),[AttributeDecl(VarDecl(Id("a"), IntType(), None)),AttributeDecl(ConstDecl(Id("b"), IntType(), IntLiteral(5))),],Id("Parent")),]))
        self.assertTrue(TestAST.test(input,expect,349))

    def test_350(self):
        input = """class main {
                func @main(a, b, c: int, d: float, e: string): bool {
                    return;
                }
            }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("@main"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType()),VarDecl(Id("d"),FloatType()),VarDecl(Id("e"),StringType())],BoolType(),Block([Return(None)]))])]))
        self.assertTrue(TestAST.test(input,expect,350))

    def test_351(self):
        input = """class main {
                func test(): void {
                    io.readString("Hello World");
                }
            }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("test"),[],VoidType(),Block([CallStmt(Id("io"),Id("readString"),[StringLiteral("Hello World")])]))])]))
        self.assertTrue(TestAST.test(input,expect,351))

    def test_352(self):
        input = """class main {
                func test():void {
                    @Shape.getArea(@graph(length));
                }
            }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("test"),[],VoidType(),Block([CallStmt(FieldAccess(None,Id("@Shape")),Id("getArea"),[CallExpr(None,Id("@graph"),[Id("length")])])]))])]))
        self.assertTrue(TestAST.test(input,expect,352))

    def test_353(self):
        input = """class main {
                func test():void {
                    const a, b: int = a + 1, true - "string";
                }
            }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("test"),[],VoidType(),Block([ConstDecl(Id("a"),IntType(),BinaryOp("+",Id("a"),IntLiteral(1))),ConstDecl(Id("b"),IntType(),BinaryOp("-",BooleanLiteral(True),StringLiteral("string")))]))])]))
        self.assertTrue(TestAST.test(input,expect,353))

    def test_354(self):
        input = """class main {
            var u, i: int;
            var a, b, g1, h: bool;
            const c, d1: bool = false, false;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("u"),IntType())),
                    AttributeDecl(VarDecl(Id("i"),IntType())),
                    AttributeDecl(VarDecl(Id("a"),BoolType())),
                    AttributeDecl(VarDecl(Id("b"),BoolType())),
                    AttributeDecl(VarDecl(Id("g1"),BoolType())),
                    AttributeDecl(VarDecl(Id("h"),BoolType())),
                    AttributeDecl(ConstDecl(Id("c"),BoolType(),BooleanLiteral(False))),
                    AttributeDecl(ConstDecl(Id("d1"),BoolType(),BooleanLiteral(False))),
                    ])]))
        self.assertTrue(TestAST.test(input,expect,354))
    
    def test_355(self):
        input = """class Shape {
            var @numOfShape: int = 0;
            const immutableAttribute: int = 0;
            var length, width: int;
            func @getNumOfShape():int {
                return @numOfShape;
                }
            }"""
        expect = str(Program([ClassDecl(Id("Shape"),[AttributeDecl(VarDecl(Id("@numOfShape"),IntType(),IntLiteral(0))),AttributeDecl(ConstDecl(Id("immutableAttribute"),IntType(),IntLiteral(0))),AttributeDecl(VarDecl(Id("length"),IntType())),AttributeDecl(VarDecl(Id("width"),IntType())),MethodDecl(Id("@getNumOfShape"),[],IntType(),Block([Return(FieldAccess(None,Id("@numOfShape")))]))])]))
        self.assertTrue(TestAST.test(input,expect,355))
   
    def test_356(self):
        input = """class main {
            var u, i: bool = true, false;
            var a, b: int = 1, 2;
            const c, d: bool;
            func test(a: int, b:string): void {
                var cc: int = 1;
                const ddd, eee, fff: bool;
            }
            var x, y, z, t: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            AttributeDecl(VarDecl(Id("u"),BoolType(),BooleanLiteral(True))),
            AttributeDecl(VarDecl(Id("i"),BoolType(),BooleanLiteral(False))),
            AttributeDecl(VarDecl(Id("a"),IntType(),IntLiteral(1))),
            AttributeDecl(VarDecl(Id("b"),IntType(),IntLiteral(2))),
            AttributeDecl(ConstDecl(Id("c"),BoolType(),None)),
            AttributeDecl(ConstDecl(Id("d"),BoolType(),None)),
            MethodDecl(Id("test"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),StringType())],VoidType(),
                       Block([VarDecl(Id("cc"),IntType(),IntLiteral(1)),
                              ConstDecl(Id("ddd"),BoolType(),None),
                              ConstDecl(Id("eee"),BoolType(),None),
                              ConstDecl(Id("fff"),BoolType(),None)])),
            AttributeDecl(VarDecl(Id("x"),StringType())),
            AttributeDecl(VarDecl(Id("y"),StringType())),
            AttributeDecl(VarDecl(Id("z"),StringType())),
            AttributeDecl(VarDecl(Id("t"),StringType()))])]))
        self.assertTrue(TestAST.test(input,expect,356))

    def test_357(self):
        input = """class main{
            func foo  (a: int, b: float):void {}
            func @main():void{
                io.setInt(4);
            }}"""
        expect = str(Program([ClassDecl(Id("main"),[
            MethodDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],VoidType(),Block([])),
            MethodDecl(Id("@main"),[],VoidType(),Block([CallStmt(Id("io"),Id("setInt"),[IntLiteral(4)])]))])]))
        self.assertTrue(TestAST.test(input,expect,357))

    def test_358(self):
        input = """class main {
            var u, i: int = 1,2;
            const a, b: float;
            const c, d: bool;
            func test(a: int, b: string, c: float): void {}
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            AttributeDecl(VarDecl(Id("u"),IntType(),IntLiteral(1))),
            AttributeDecl(VarDecl(Id("i"),IntType(),IntLiteral(2))),
            AttributeDecl(ConstDecl(Id("a"),FloatType(),None)),
            AttributeDecl(ConstDecl(Id("b"),FloatType(),None)),
            AttributeDecl(ConstDecl(Id("c"),BoolType(),None)),
            AttributeDecl(ConstDecl(Id("d"),BoolType(),None)),
            MethodDecl(Id("test"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),StringType()),VarDecl(Id("c"),FloatType())],VoidType(),Block([]))
            ])]))
        self.assertTrue(TestAST.test(input,expect,358))

    def test_359(self):
        input = """class main {
            var a: [5]foo;
            }
            class main1 {
                var b: int;
                }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),ArrayType(IntLiteral(5),ClassType(Id("foo")))))]),ClassDecl(Id("main1"),[AttributeDecl(VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,359))
        
    def test_360(self):
        input = """class main {var b, c: int;}"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("b"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,360))

    def test_361(self):
        input = """class main {
                func constructor() {
                    a[0].b[0].getText();
                }
            }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("constructor"),[],VoidType(),Block([CallStmt(ArrayCell(FieldAccess(ArrayCell(Id("a"),IntLiteral(0)),Id("b")),IntLiteral(0)),Id("getText"),[])]))])]))
        self.assertTrue(TestAST.test(input,expect,361))

    def test_362(self):
        input = """class Shape <- Rectangle {
            func getArea():int {
                return self.length * self.width;
                }
            }"""
        expect = str(Program([ClassDecl(Id("Rectangle"),[MethodDecl(Id("getArea"),[],IntType(),Block([Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))]))],Id("Shape"))]))
        self.assertTrue(TestAST.test(input,expect,362))

    def test_363(self):
        input = """class main {
            var a, b:int;
            var c: int;
            const testString: string = "testString";
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("b"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType())),AttributeDecl(ConstDecl(Id("testString"),StringType(),StringLiteral("testString")))])]))
        self.assertTrue(TestAST.test(input,expect,363))

    def test_364(self):
        input = """class main {
            var u, i: int;
            var a, b, g, h: int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("u"),IntType())),
                    AttributeDecl(VarDecl(Id("i"),IntType())),
                    AttributeDecl(VarDecl(Id("a"),IntType())),
                    AttributeDecl(VarDecl(Id("b"),IntType())),
                    AttributeDecl(VarDecl(Id("g"),IntType())),
                    AttributeDecl(VarDecl(Id("h"),IntType()))
                    ])]))
        self.assertTrue(TestAST.test(input,expect,364))
    
    def test_365(self):
        input = """class main {
            var a:int;
            const b: int = 25102023;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("a"),IntType())),
             AttributeDecl(ConstDecl(Id("b"),IntType(),IntLiteral(25102023)))])]))
        self.assertTrue(TestAST.test(input,expect,365))
   
    def test_366(self):
        input = """class main {
            func test(a: int, b:string): void {
                var cc: int = 1;
                var dd, ee, ff: string = "aa", "bb", "cc";
                const ddd, eee, fff: bool;
            }
            var x, t: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            MethodDecl(Id("test"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),StringType())],VoidType(),
                       Block([VarDecl(Id("cc"),IntType(),IntLiteral(1)),
                              VarDecl(Id("dd"),StringType(),StringLiteral("aa")),
                              VarDecl(Id("ee"),StringType(),StringLiteral("bb")),
                              VarDecl(Id("ff"),StringType(),StringLiteral("cc")),
                              ConstDecl(Id("ddd"),BoolType(),None),
                              ConstDecl(Id("eee"),BoolType(),None),
                              ConstDecl(Id("fff"),BoolType(),None)])),
            AttributeDecl(VarDecl(Id("x"),StringType())),
            AttributeDecl(VarDecl(Id("t"),StringType()))])]))
        self.assertTrue(TestAST.test(input,expect,366))

    def test_367(self):
        input = """class main {
                func constructor() {
                    a[0] := b[0];
                }
            }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("constructor"),[],VoidType(),Block([Assign(ArrayCell(Id("a"),IntLiteral(0),),ArrayCell(Id("b"),IntLiteral(0)))]))])]))
        self.assertTrue(TestAST.test(input,expect,367))

    def test_368(self):
        input = """class main {
            var u, i:int = 1,2;
            var a, b, g, h: int;
            const c, d: bool;
            func test(a: int, b: int): void {}
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
            MethodDecl(Id("test"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([])),
            ])]))
        self.assertTrue(TestAST.test(input,expect,368))

    def test_369(self):
        input = """class main {
            const a: string = 1;
            }
            class main1 {
                var b: int;
                }"""
        expect = str(Program([
            ClassDecl(Id("main"),[AttributeDecl(ConstDecl(Id("a"),StringType(),IntLiteral(1)))]),
            ClassDecl(Id("main1"),[AttributeDecl(VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,369))
        
    def test_370(self):
        input = """class main {
            func constructor(a, b: int, c: Shape){}
        }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("constructor"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ClassType(Id("Shape")))],VoidType(),Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,370))
        
    def test_371(self):
        input = """class main {
            func constructor(){
                var t: int = null;
                var a: string = self;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("constructor"),[],VoidType(),Block([VarDecl(Id("t"),IntType(),NullLiteral()),VarDecl(Id("a"),StringType(),SelfLiteral())]))])]))
        self.assertTrue(TestAST.test(input,expect,371))
        
    def test_372(self):
        input = """class Shape <- Rectangle {
            func getArea():int {
                return self.length * self.width;
                }
            func getLength(): int {
                return self.length;
                }
            }"""
        expect = str(Program([ClassDecl(Id("Rectangle"),[MethodDecl(Id("getArea"),[],IntType(),Block([Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))])),MethodDecl(Id("getLength"),[],IntType(),Block([Return(FieldAccess(SelfLiteral(),Id("length")))]))],Id("Shape"))]))
        self.assertTrue(TestAST.test(input,expect,372))

    def test_373(self):
        input = """class main {
            func constructor(){
                var a:string = new X("Hello");
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
                    [
                        MethodDecl(
                            Id("constructor"),
                            [
                            ],
                            VoidType(),
                            Block([
                                VarDecl(Id("a"),StringType(),NewExpr(Id("X"),[StringLiteral("Hello")]))
                            ])
                        ),
                    ])]))
        self.assertTrue(TestAST.test(input,expect,373))

    def test_374(self):
        input = """class main {
            func constructor(){
                var a:string = "Hello";
                if true {
                    io.@Write("See ya");
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("constructor"),
                    [
                    ],
                    VoidType(),
                    Block([
                        VarDecl(Id("a"),StringType(),StringLiteral("Hello")),
                        If(
                            BooleanLiteral(True),
                            Block([
                                CallStmt(
                                    Id("io"),
                                    Id("@Write"),
                                    [
                                        StringLiteral("See ya")
                                    ]
                                )
                            ])
                        )
                    ])
                ),
            ])]))
        self.assertTrue(TestAST.test(input,expect,374))
    
    def test_375(self):
        input = """class main {
            func test():void{
                Shape[2].length := 2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [
                MethodDecl(
                    Id("test"),
                    [
                        
                    ],
                    VoidType(),
                    Block([
                        Assign(
                            FieldAccess(
                                ArrayCell(
                                    Id("Shape"),
                                    IntLiteral(2)
                                ),
                                Id("length")
                            ),
                            IntLiteral(2)
                        )
                    ])
                )
            ])]))
        self.assertTrue(TestAST.test(input,expect,375))
   
    def test_376(self):
        input = """class main {
            func test(a: int, b:string): void {
                var cc: int = 1;
                const ddd, eee, fff: bool;
            }
            var x, t: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            MethodDecl(Id("test"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),StringType())],VoidType(),
                       Block([VarDecl(Id("cc"),IntType(),IntLiteral(1)),
                              ConstDecl(Id("ddd"),BoolType(),None),
                              ConstDecl(Id("eee"),BoolType(),None),
                              ConstDecl(Id("fff"),BoolType(),None)])),
            AttributeDecl(VarDecl(Id("x"),StringType())),
            AttributeDecl(VarDecl(Id("t"),StringType()))])]))
        self.assertTrue(TestAST.test(input,expect,376))

    def test_377(self):
        input = """class main {
                func constructor() {
                    a[0] := new X();
                }
            }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("constructor"),[],VoidType(),Block([Assign(ArrayCell(Id("a"),IntLiteral(0),),NewExpr(Id("X"),[]))]))])]))
        self.assertTrue(TestAST.test(input,expect,377))

    def test_378(self):
        input = """class main {
            var u, i:int = 1,2;
            var a, b, g, h: int;
            const c, d: bool;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            AttributeDecl(VarDecl(Id("u"),IntType(),IntLiteral(1))),
            AttributeDecl(VarDecl(Id("i"),IntType(),IntLiteral(2))),
            AttributeDecl(VarDecl(Id("a"),IntType())),
            AttributeDecl(VarDecl(Id("b"),IntType())),
            AttributeDecl(VarDecl(Id("g"),IntType())),
            AttributeDecl(VarDecl(Id("h"),IntType())),
            AttributeDecl(ConstDecl(Id("c"),BoolType(),None)),
            AttributeDecl(ConstDecl(Id("d"),BoolType(),None))
            ])]))
        self.assertTrue(TestAST.test(input,expect,378))

    def test_379(self):
        input = """class main {
            var a: string = 1;
            }
            class main2 {
                const b: int;
                }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),StringType(),IntLiteral(1)))]),ClassDecl(Id("main2"),[AttributeDecl(ConstDecl(Id("b"),IntType(),None))])]))
        self.assertTrue(TestAST.test(input,expect,379))
        
    def test_380(self):
        input = """class main {
            func constructor(a: int){}
            func constructor(b: string){}
        }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("constructor"),[VarDecl(Id("a"),IntType())],VoidType(),Block([])),MethodDecl(Id("constructor"),[VarDecl(Id("b"),StringType())],VoidType(),Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,380))

    def test_381(self):
        input = """class main {
            func constructor(a: int, b: float, c: string){}
        }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("constructor"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),StringType())],VoidType(),Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,381))

    def test_382(self):
        input = """class main {
            func test(a, b: float, c: Test): void{}
        }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("test"),[VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),ClassType(Id("Test")))],VoidType(),Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,382))

    def test_383(self):
        input = """class main {
            var a, b:int;
            var c: int = 100;
            const d: string = 200;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("b"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType(),IntLiteral(100))),AttributeDecl(ConstDecl(Id("d"),StringType(),IntLiteral(200)))])]))
        self.assertTrue(TestAST.test(input,expect,383))

    def test_384(self):
        input = """class main {
            var a, b, g, h: int;
            const c, d: bool;
            func test(a: int, b:string): void {}
            var x, y, z, t: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
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
        self.assertTrue(TestAST.test(input,expect,384))
    
    def test_385(self):
        input = """class main {
            var a, b: int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("a"),IntType())),
             AttributeDecl(VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,385))
   
    def test_386(self):
        input = """class main {
            var u, i: int = 100, 250;
            var a, b, g, h: int;
            const c, d: bool;
            func test(a: int, b: float): void {
                var cc: int = 1;
                var dd, ee, ff: string = "2", "3", "4";
                const ddd, eee, fff: bool;
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            AttributeDecl(VarDecl(Id("u"),IntType(),IntLiteral(100))),
            AttributeDecl(VarDecl(Id("i"),IntType(),IntLiteral(250))),
            AttributeDecl(VarDecl(Id("a"),IntType())),
            AttributeDecl(VarDecl(Id("b"),IntType())),
            AttributeDecl(VarDecl(Id("g"),IntType())),
            AttributeDecl(VarDecl(Id("h"),IntType())),
            AttributeDecl(ConstDecl(Id("c"),BoolType(),None)),
            AttributeDecl(ConstDecl(Id("d"),BoolType(),None)),
            MethodDecl(Id("test"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],VoidType(),
                       Block([VarDecl(Id("cc"),IntType(),IntLiteral(1)),
                              VarDecl(Id("dd"),StringType(),StringLiteral("2")),
                              VarDecl(Id("ee"),StringType(),StringLiteral("3")),
                              VarDecl(Id("ff"),StringType(),StringLiteral("4")),
                              ConstDecl(Id("ddd"),BoolType(),None),
                              ConstDecl(Id("eee"),BoolType(),None),
                              ConstDecl(Id("fff"),BoolType(),None)])),
            ])]))
        self.assertTrue(TestAST.test(input,expect,386))

    def test_387(self):
        input = """class main{
            func foo  (a: int, b: float):void {}
            func @main():void{
                io.printInt(50);
            }}"""
        expect = str(Program([ClassDecl(Id("main"),[
            MethodDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],VoidType(),Block([])),
            MethodDecl(Id("@main"),[],VoidType(),Block([CallStmt(Id("io"),Id("printInt"),[IntLiteral(50)])]))])]))
        self.assertTrue(TestAST.test(input,expect,387))

    def test_388(self):
        input = """class main {
            var u, v: int = 1,2;
            var a, b, g, h: float;
            func test(a: int, b:string): void {}
            var x, y, z, t: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            AttributeDecl(VarDecl(Id("u"),IntType(),IntLiteral(1))),
            AttributeDecl(VarDecl(Id("v"),IntType(),IntLiteral(2))),
            AttributeDecl(VarDecl(Id("a"),FloatType())),
            AttributeDecl(VarDecl(Id("b"),FloatType())),
            AttributeDecl(VarDecl(Id("g"),FloatType())),
            AttributeDecl(VarDecl(Id("h"),FloatType())),
            MethodDecl(Id("test"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),StringType())],VoidType(),Block([])),
            AttributeDecl(VarDecl(Id("x"),StringType())),
            AttributeDecl(VarDecl(Id("y"),StringType())),
            AttributeDecl(VarDecl(Id("z"),StringType())),
            AttributeDecl(VarDecl(Id("t"),StringType()))])]))
        self.assertTrue(TestAST.test(input,expect,388))

    def test_389(self):
        input = """class main {
            var a: int;
            var b: int;
            }
            class main1 {
                var b: int;
                }"""
        expect = str(Program([
            ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("b"),IntType()))]),
            ClassDecl(Id("main1"),[AttributeDecl(VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,389))

    def test_390(self):
        input = """class main {
            var a: int;
            var b: int;
            }
            class main1 {
                var b: int;
                }"""
        expect = str(Program([
            ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("b"),IntType()))]),
            ClassDecl(Id("main1"),[AttributeDecl(VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,390))

    def test_391(self):
        input = """class main {func @test1(): int {return;}}"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("@test1"),[],IntType(),Block([Return(None)]))])]))
        self.assertTrue(TestAST.test(input,expect,391))

    def test_392(self):
        input = """class main {
            var a, b, c:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("b"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,392))

    def test_393(self):
        input = """class main {
            var a, b, c:int;
            const d:string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("b"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType())),AttributeDecl(ConstDecl(Id("d"),StringType(),None))])]))
        self.assertTrue(TestAST.test(input,expect,393))

    def test_394(self):
        input = """class main {
            var u, i, a, b, g, h: int;
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
        self.assertTrue(TestAST.test(input,expect,394))
    
    def test_395(self):
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,395))
   
    def test_396(self):
        input = """class main {
            var x, y, z, t: string;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[
            AttributeDecl(VarDecl(Id("x"),StringType())),
            AttributeDecl(VarDecl(Id("y"),StringType())),
            AttributeDecl(VarDecl(Id("z"),StringType())),
            AttributeDecl(VarDecl(Id("t"),StringType()))])]))
        self.assertTrue(TestAST.test(input,expect,396))

    def test_397(self):
        input = """class main{
            func @main():void{
                I[5] := t[5];
            }}"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("@main"),[],VoidType(),Block([Assign(ArrayCell(Id("I"),IntLiteral(5)),ArrayCell(Id("t"),IntLiteral(5)))]))])]))
        self.assertTrue(TestAST.test(input,expect,397))

    def test_398(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input,expect,398))

    def test_399(self):
        input = """class the {
            var a: int = 3;
            }
            class final {
                var b: int = 2;
            }
            class countdown {
                var c: int = 1;
            }"""
        expect = str(Program([
            ClassDecl(Id("the"),[AttributeDecl(VarDecl(Id("a"),IntType(),IntLiteral(3)))]),
            ClassDecl(Id("final"),[AttributeDecl(VarDecl(Id("b"),IntType(),IntLiteral(2)))]),
            ClassDecl(Id("countdown"),[AttributeDecl(VarDecl(Id("c"),IntType(),IntLiteral(1)))]),
            ]))
        self.assertTrue(TestAST.test(input,expect,399))