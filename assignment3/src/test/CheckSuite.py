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

    # def test_419(self):
    #     input = """
    #     class Program {
    #         func @main(a: int): int {}
    #     }
    #     class Program <- b {
    #         func test(a: int): void {}
    #         func constructor(a: bool) {}
    #         func @test(a: int): int {}
    #         var a: int;
    #         const a: string;
    #     }
    #     """
    #     expect = "Redeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input,expect,419))
        
    # def test_420(self):
    #     input = """
    #     class Program {
    #         func @main(): void {}
    #         var a, b: int = 1, "3.0";
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: VarDecl(Id(b),IntType,StringLit(3.0))"
    #     self.assertTrue(TestChecker.test(input,expect,420))

    # def test_421(self):
    #     input = """
    #     class A {
    #         func constructor(a: int, b: string) {}
    #     }
    #     class Program {
    #         func @main(): void {
    #             var a: string = new A(1, "2");
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: VarDecl(Id(a),StringType,NewExpr(Id(A),[IntLit(1),StringLit(2)]))"
    #     self.assertTrue(TestChecker.test(input,expect,421))

    # def test_422(self):
    #     input = """
    #     class A {
    #         func constructor(a: int, b: string) {}
    #     }
    #     class Program {
    #         func @main(): void {
    #             var a: bool = true;
    #             var b: int = 90;
    #             var c: int = a*b;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(*,Id(a),Id(b))"
    #     self.assertTrue(TestChecker.test(input,expect,422))
    
    # def test_423(self):
    #     input = """
    #     class A {
    #         func constructor(a: int, b: string) {}
    #     }
    #     class Program {
    #         func @main(): void {
    #             var i: int;
    #             continue;
    #             for i:= 0; i < 10; i:= i + 1 {
    #                 break;
    #             }
    #         }
    #     }
    #     """
    #     expect = "Continue Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,423))
        
    # def test_424(self): #sai
    #     input = """
    #     class Program {
    #         func @main(): void {
    #             var i: int;
    #             const x: string = "Hello";
    #             if {
    #                 for i := 0; i < 10; i := i + 1 {
    #                     break;
    #                 }
    #             }
    #             i > 10
    #             {
    #                 x := "Hi";
    #             }
    #         }
    #     }
    #     """
    #     expect = "Cannot Assign To Constant: AssignStmt(Id(x),StringLit(Hi))"
    #     self.assertTrue(TestChecker.test(input,expect,424))
    
    # def test_425(self):
    #     input = Program([ClassDecl(Id("Program"),[MethodDecl(Id("@main"),[],VoidType(),Block([ConstDecl(Id("a"),IntType(),IntLiteral(1)),Assign(Id("a"),IntLiteral(2))]))])])
    #     expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(2))"
    #     self.assertTrue(TestChecker.test(input,expect,425))
        
    # def test_426(self):
    #     input = Program([ClassDecl(Id("Program"),[MethodDecl(Id("@main"),[],VoidType(),Block([ConstDecl(Id("a"),IntType(),None)]))])])
    #     expect = "Type Mismatch In Declaration: ConstDecl(Id(a),IntType,None)"
    #     self.assertTrue(TestChecker.test(input,expect,426))
        
    # def test_427(self):
    #     input = """
    #     class A {
    #         func constructor(a: int, b: string) {}
    #     }
    #     class Program {
    #         func @main(): void {
    #             var i: int;
    #             continue;
    #             for i:= 0; i < 10; i:= i + 1 {
    #                 if {i := 15} i > 10 {i := 10}
    #             }
    #         }
    #     }
    #     """
    #     expect = "Continue Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,427))
        
    # def test_428(self):
    #     input = """
    #     class A {
    #         func constructor(a: int, b: string) {}
    #     }
    #     class Program {
    #         func @main(): void {
    #             if {i := 15} i > 10 {i := 10}
    #         }
    #     }
    #     """
    #     expect = "Undeclared Identifier: i"
    #     self.assertTrue(TestChecker.test(input,expect,428))
        
    # def test_429(self):
    #     input = """
    #     class A {
    #         func constructor(a: int, b: string) {}
    #     }
    #     class Program {
    #         func @main(): void {
    #             var a: int = 4.5;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: VarDecl(Id(a),IntType,FloatLit(4.5))"
    #     self.assertTrue(TestChecker.test(input,expect,429))
        
    # def test_430(self):
    #     input = """
    #     class A {
    #         func constructor(a: int, b: string) {}
    #     }
    #     class Program {
    #         func @main(): void {
    #             const a: int = 5;
    #             a := 10;
    #         }
    #     }
    #     """
    #     expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(10))"
    #     self.assertTrue(TestChecker.test(input,expect,430))
        
    # def test_431(self):
    #     input = """
    #     class Program {
    #         func @main(): void {
    #             const a: string;
    #             a := 10;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: ConstDecl(Id(a),StringType,None)"
    #     self.assertTrue(TestChecker.test(input,expect,431))
        
    # def test_432(self):
    #     input = """
    #     class Program {
    #         func @main(): void {
    #             a := 10;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(input,expect,432))
        
    # def test_433(self):
    #     input = """
    #     class Program {
    #         func @main(): void {
    #             if {i := 15} i > 10 {i := 10}
    #         }
    #     }
    #     """
    #     expect = "Undeclared Identifier: i"
    #     self.assertTrue(TestChecker.test(input,expect,433))
        
    # def test_434(self):
    #     input = """
    #     class Program {
    #         func @main(): void {
    #             var i: int = 0;
    #             if {i := 15} i > 10 {
    #                 for i := 0; i < 10; i := i + 1; {}
    #             }
    #         }
    #     }
    #     """
    #     expect = "Undeclared Identifier: i"
    #     self.assertTrue(TestChecker.test(input,expect,434))
        
    # def test_435(self):
    #     input = """
    #     class Program{
    #         func @main(): void {}
    #         var a:[1]int = [true];
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: VarDecl(Id(a),ArrayType(1,IntType),[BooleanLit(True)])"
    #     self.assertTrue(TestChecker.test(input,expect,435))
        
    # def test_436(self):
    #     input = """
    #     class Program{
    #         func @main(): void {}
    #         var a: int = [true];
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: VarDecl(Id(a),ArrayType(1,IntType),[BooleanLit(True)])"
    #     self.assertTrue(TestChecker.test(input,expect,436))
        
    # def test_437(self):
    #     input = """
    #     class Program{
    #         func @main(): void {}
    #         const @a:int = 2.0;
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: ConstDecl(Id(@a),IntType,FloatLit(2.0))"
    #     self.assertTrue(TestChecker.test(input,expect,437))
        
    # def test_438(self):
    #     input = """
    #     class Program{
    #         func @main(): void {}
    #         const @a: int;
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: ConstDecl(Id(@a),IntType,FloatLit(2.0))"
    #     self.assertTrue(TestChecker.test(input,expect,438))
        
    # def test_439(self):
    #     input = """
    #     class Program{
    #         func @main(): void {
    #             var b: string = true;
    #         }
    #         var a: int = 1;
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: ConstDecl(Id(@a),IntType,FloatLit(2.0))"
    #     self.assertTrue(TestChecker.test(input,expect,438))
        
    # def test_439(self):
    #     input = """
    #     class Program{
    #         func @main(): void {
    #             var a: int = 1;
    #         }
    #         a := 5;
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: ConstDecl(Id(@a),IntType,FloatLit(2.0))"
    #     self.assertTrue(TestChecker.test(input,expect,439))
        
    # def test_440(self):
    #     input = """
    #     class Program{
    #         func @main(): void {
    #             var a: int = 1;
    #             self.a := 5;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input,expect,440))
        
    # def test_441(self):
    #     input = """
    #     class Program{
    #         var a: int = 2;
    #         func @main(): void {
    #             self.a := 5;
    #         }
    #         const b: int;
    #     }
    #     """
    #     expect = "Undeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input,expect,441))
    
    # def test_442(self):
    #     input = """
    #     class Program{
    #         func @main():void{
    #             var arr: [2]int = [2, 5];
    #         }
    #         const temp: int;
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
    #     self.assertTrue(TestChecker.test(input,expect,442))
        
    # def test_443(self):
    #     input = """
    #     class Program{
    #         func @main():void{
    #             var arr: [3]int = [2, 5];
    #         }
    #         const temp: int = 5;
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: VarDecl(Id(arr),ArrayType(3,IntType),[IntLit(2),IntLit(5)])"
    #     self.assertTrue(TestChecker.test(input,expect,443))
        
    # def test_444(self):
    #     input = """
    #     class Program{
    #         func @main():void{
    #             var arr: [1]int = [2, 5];
    #         }
    #         const temp: int = 2;
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: VarDecl(Id(arr),ArrayType(1,IntType),[IntLit(2),IntLit(5)])"
    #     self.assertTrue(TestChecker.test(input,expect,444))
        
    # def test_445(self):
    #     input = """
    #     class Program{
    #         var @test: int = 5;
    #         func @main(): void{
    #             self.test := 10;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Attribute: test"
    #     self.assertTrue(TestChecker.test(input,expect,445))

    # def test_446(self):
    #     input = """
    #     class Program{
    #         var @test: int = 5;
    #         func @main(): void{
    #             Program.@test := 10;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Identifier: Program"
    #     self.assertTrue(TestChecker.test(input,expect,446))
        
    # def test_447(self):
    #     input = """
    #     class A{
    #         var @test: int = 5;
    #         var a: string;
    #     }
    #     class A <- Program{
    #         func @main(): void{
    #             @test := 10;
    #         }
    #         const test: int;
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: ConstDecl(Id(test),IntType,None)"
    #     self.assertTrue(TestChecker.test(input,expect,447))
        
    # def test_448(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             io.@writeInt(Shape.@numOfShape);
    #         }
    #     }
    #     """
    #     expect = "Undeclared Class: Shape"
    #     self.assertTrue(TestChecker.test(input,expect,448))
    
    # def test_449(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             io.@readInt(3);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: Call(Id(io),Id(@readInt),[IntLit(3)])"
    #     self.assertTrue(TestChecker.test(input,expect,449))
        
    # def test_450(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             io.@readFloat(3);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: Call(Id(io),Id(@readFloat),[IntLit(3)])"
    #     self.assertTrue(TestChecker.test(input,expect,450))
        
    # def test_451(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             io.@writeFloat(3);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: Call(Id(io),Id(@writeFloat),[IntLit(3)])"
    #     self.assertTrue(TestChecker.test(input,expect,451))
        
    # def test_452(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             io.@writeFloat(3.0);
    #         }
    #         const temp: int;
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
    #     self.assertTrue(TestChecker.test(input,expect,452))
        
    # def test_453(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             io.@readBool(3);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: Call(Id(io),Id(@readBool),[IntLit(3)])"
    #     self.assertTrue(TestChecker.test(input,expect,453))
        
    # def test_454(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             io.@writeBool(3);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: Call(Id(io),Id(@writeBool),[IntLit(3)])"
    #     self.assertTrue(TestChecker.test(input,expect,454))
        
    # def test_455(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             io.@writeBool(true);
    #         }
    #         const temp: int;
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
    #     self.assertTrue(TestChecker.test(input,expect,455))
        
    # def test_456(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             io.@readStr(3);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: Call(Id(io),Id(@readStr),[IntLit(3)])"
    #     self.assertTrue(TestChecker.test(input,expect,456))
        
    # def test_457(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             io.@writeStr(3);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: Call(Id(io),Id(@writeStr),[IntLit(3)])"
    #     self.assertTrue(TestChecker.test(input,expect,457))
        
    # def test_458(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             io.@writeStr("Hi");
    #         }
    #         const temp: int;
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
    #     self.assertTrue(TestChecker.test(input,expect,458))
        
    # def test_459(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var a: int = io.@readInt();
    #         }
    #         const temp: int;
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
    #     self.assertTrue(TestChecker.test(input,expect,459))
        
    # def test_460(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var a: string = io.@readInt();
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: VarDecl(Id(a),StringType,CallExpr(Id(io),Id(@readInt),[]))"
    #     self.assertTrue(TestChecker.test(input,expect,460))
        
    # def test_461(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var a: float = io.@readFloat();
    #         }
    #         const temp: int;
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
    #     self.assertTrue(TestChecker.test(input,expect,461))
        
    # def test_462(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var a: string = io.@readFloat();
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: VarDecl(Id(a),StringType,CallExpr(Id(io),Id(@readFloat),[]))"
    #     self.assertTrue(TestChecker.test(input,expect,462))
        
    # def test_463(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var a: bool = io.@readBool();
    #         }
    #         const temp: int;
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
    #     self.assertTrue(TestChecker.test(input,expect,463))
        
    # def test_464(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var a: float = io.@readBool();
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: VarDecl(Id(a),FloatType,CallExpr(Id(io),Id(@readBool),[]))"
    #     self.assertTrue(TestChecker.test(input,expect,464))
        
    # def test_465(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var a: string = io.@readStr();
    #         }
    #         const temp: int;
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: ConstDecl(Id(temp),IntType,None)"
    #     self.assertTrue(TestChecker.test(input,expect,465))
        
    # def test_466(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var a: float = io.@readStr();
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: VarDecl(Id(a),FloatType,CallExpr(Id(io),Id(@readStr),[]))"
    #     self.assertTrue(TestChecker.test(input,expect,466))
        
    # def test_467(self):
    #     input = """
    #     class main{
    #         func @main():void{
    #             I[5] := t[5];
    #         }}
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,467))
        
    # def test_468(self):
    #     input = """
    #     class main{
    #         func @main():void{
    #             I[5] := t[5];
    #         }}
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,468))
        
    # def test_469(self):
    #     input = """
    #     class main {
    #         var x, y, z, t: string;
    #     }
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,469))
        
    # def test_470(self):
    #     input = """
    #     class main {}
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,470))
        
    # def test_471(self):
    #     input = """
    #     class Program {
    #         var u, i, a, b, g, h: int;
    #         const c, d: bool;
    #         func @main(a: int, b:string): void {}
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: ConstDecl(Id(c),BoolType,None)"
    #     self.assertTrue(TestChecker.test(input,expect,471))
        
    # def test_472(self):
    #     input = """
    #     class main {func @test1(): int {return;}}
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,472))
    
    # def test_473(self):
    #     input = """
    #     class A {
    #         func constructor(a: int) {}
    #     }
    #     class Program {
    #         var u, i, a, b, g, h: int;
    #         var t: A = new A();
    #         func @main(a: int, b:string): void {}
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: NewExpr(Id(A),[])"
    #     self.assertTrue(TestChecker.test(input,expect,473))
        
    # def test_474(self):
    #     input = """
    #     class A {
    #         func constructor() {}
    #     }
    #     class Program {
    #         var u, i, a, b, g, h: int;
    #         var t: A = new A(self.u);
    #         func @main(a: int, b:string): void {}
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: NewExpr(Id(A),[FieldAccess(Self(),Id(u))])"
    #     self.assertTrue(TestChecker.test(input,expect,474))
        
    # def test_475(self):
    #     input = """
    #     class A {
    #         func constructor(a: string) {}
    #     }
    #     class Program {
    #         var u, i, a, b, g, h: int;
    #         var t: A = new A(self.u);
    #         func @main(a: int, b:string): void {}
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: NewExpr(Id(A),[FieldAccess(Self(),Id(u))])"
    #     self.assertTrue(TestChecker.test(input,expect,475))
        
    def test_476(self):
        input = """
        class A {
            func constructor(a: float) {}
        }
        class Program {
            var u, i, a, b, g, h: int;
            var t: A = new A(null);
            func @main(a: int, b:string): void {}
        }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(A),[NullLiteral()])"
        self.assertTrue(TestChecker.test(input,expect,476))
        
    def test_477(self):
        input = """
        class Program{
            func @main():void{
                var arr:[2]int = [2,5,3];
            }
        }
        """
        expect = "Type Mismatch In Declaration: VarDecl(Id(arr),ArrayType(2,IntType),[IntLit(2),IntLit(5),IntLit(3)])"
        self.assertTrue(TestChecker.test(input,expect,477))
        
    def test_478(self):
        input = """
        class Program{
            func @main():void{
                var arr:[3]int = [2,5,3];
                arr := "3"^"4";
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(arr),BinaryOp(^,StringLit(3),StringLit(4)))"
        self.assertTrue(TestChecker.test(input,expect,478))
        
    def test_479(self):
        input = """
        class Program{
            func @main():void{
                var arr:[3]int = [2,5,3];
                var temp: int = 9.0*5;
            }
        }
        """
        expect = "Type Mismatch In Declaration: VarDecl(Id(temp),IntType,BinaryOp(*,FloatLit(9.0),IntLit(5)))"
        self.assertTrue(TestChecker.test(input,expect,479))
        
    def test_480(self):
        input = """
        class Program{
            func @main():void{
                var arr:[3]int = [2,5,3];
                var temp: int = 9.0*5;
            }
        }
        """
        expect = "Type Mismatch In Declaration: VarDecl(Id(temp),IntType,BinaryOp(*,FloatLit(9.0),IntLit(5)))"
        self.assertTrue(TestChecker.test(input,expect,480))
        
    def test_481(self):
        input = """
        class Program{
            func @main():void{
                var arr:[3]int = [2,5,3];
                var temp: bool = 9*5;
            }
        }
        """
        expect = "Type Mismatch In Declaration: VarDecl(Id(temp),BoolType,BinaryOp(*,IntLit(9),IntLit(5)))"
        self.assertTrue(TestChecker.test(input,expect,481))