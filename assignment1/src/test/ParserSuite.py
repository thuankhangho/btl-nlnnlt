# Student ID: 2011357
# Name: Ho Thuan Khang
import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_0(self):
        input = """class Program {
            func @main():int {
                @isSth := !a.x[1] && b [2];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))
    def test_1(self):
        input = """class Shape {
            var @numOfShape: int = 0;
            const immutableAttribute: int = 0;
            var length, width: int;
            func @getNumOfShape():int {
                return @numOfShape;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test_2(self):
        input = """class Program{var  a, b, c, d: int = 3, 4, 6;}"""
        expect = "Error on line 1 col 44: ;"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_3(self):
        input = """class Program {
      var x: int = 65;
      func @fact(n: int):int {
            if n == 0 {return 1;}
            else {return n * @fact(n - 1);}
        }
        func  @inc( n, delta: int):void {
            n := n + delta;
            return n;
        }
        func @main():int {
            var delta: int = @fact(3);
            @inc(self.x, delta);
            io.@writeInt(self.x);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test_4(self):
        input = """class A {func @fact(n: int):int {
            if n == 0 {return 1;}
            else {return n * @fact(n - 1);}
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test_5(self):
        input = """class A {var a: [5]int;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test_6(self):
        input = """var a: [5]int;"""
        expect = "Error on line 1 col 0: var"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test_7(self):
        input = """class Program{
            func railfence(ciphertext: string, key: int):string {
            if key <= 1
                {return ciphertext;}
            var matrix: [15]string;
            for i := 0; i < 15; i := i+1 {
                /*
                    15 for each row
                    maximum 15 rows
                */
                var matrix_a: [15]string;
            }
            var dir: bool = true;
            // true for down, false for up

            var row, col: int= 0, 0;

            for i := 0; i < length(ciphertext); i:=i + 1 {
                if row == 0 {dir := true;}
                if row == key - 1 {dir := false;}
                rail[row] := null;
                
                col := col + 1;
                if dir
                    {row := row + 1;}
                else {row := row - 1;}
            }

            var index: int = 0;
            for i := 0; i < key; i:=i + 1 {
                for j := 0; j < length(ciphertext);j:= j + 1{
                    if matrix[i] == null && (index < length(ciphertext)) {
                        matrix[i] := ciphertext[index];
                        index := index + 1;
                    }}
            
            row := 0; col := 0;
            var result: string;
            for i:=0; i< length(ciphertext);i:= i + 1 
            {
                // check the direction of flow
                if row == 0
                    {dir := true;}
                if row == key - 1
                    {dir := false;}
 
                // place the marker
                if rail[row] != "*"
                    {result := result.rail[col];}
                col := col + 1;
 
                // find the next row using direction flag
                if dir
                    {row := row + 1;}
                else {row := row - 1;}
            }
            return result;
        }
        }}"""
        expect = "Error on line 18 col 34: ("
        self.assertTrue(TestParser.test(input, expect, 207))
    def test_8(self):
        input = """class Program {
            func @main():int {
                @text := "Hello" ^ 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test_9(self):
        input = """class Program {func @main():int {func @foo():int {return 1;} @foo();}}"""
        expect = "Error on line 1 col 33: func"
        self.assertTrue(TestParser.test(input, expect, 209))
    def test_10(self):
        input = """class Program {
            func thieuDusk (n: niga): void {
            @text := @text + nian;
            for i:=0; i<@thieuSuzu(); i:=i+1 {
                //comment 1
                if {@x := 0;} _test > i
                {
                    _test := _test - @_a;
                }
                else
                {
                    @_ := @_ + 1;
                }
            }
            }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test_11(self):
        input = """class Program {
            var a: [2]int = 2,"why not";
            }"""
        expect = "Error on line 2 col 29: ,"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test_12(self):
        input = """class Program {
            var a: [3]int = [2,"why not",false];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
    def test_13(self):
        input = """class Program {
            var a: [2]int = [2,"why not"];
            func @main():void{
            a[1],a[2] := [1,2] ,[2,3];
            }}"""
        expect = "Error on line 4 col 16: ,"
        self.assertTrue(TestParser.test(input, expect, 213))
    def test_14(self):
        input = """class Program{
        func @fact(n: int):int {
            if n == 0 {return 1;}
            else {return n * @fact(n - 1);}
        }
        func  @inc( n, delta: int):void {
            n := n + delta;
            return n;
        }
        func @main():int {
            var delta: int = @fact(3);
            @inc(self.x, delta);
            io.@writeInt(self.x);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
    def test_15(self):
        input = """class Program{
        const @numOfShape: int = 0;
        const immutableAttribute: int = 0;
        var length, width: int;
        func @getnumOfShape(): void {
        if {} else { if k < 1 {} else {}}
        }
        }"""
        expect = "Error on line 6 col 14: else"
        self.assertTrue(TestParser.test(input, expect, 215))
    def test_16(self):
        input = """class Program{ var a, b, c: int = 1,2,3;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    def test_17(self):
        input = """class Main{
    var x:int = Shape.@t.t[3].t[3].a();
    const t:Shape;
    func test(i,j:int, t:string):void{
        Shape.@t.t[3].t[3].a := 2;
    }
}"""
        expect = "Error on line 2 col 29: ."
        self.assertTrue(TestParser.test(input, expect, 217))
    def test_18(self):
        input = """class Program {
      var x: int = 65;
      func @fact(n: int):int {
            if n == 0 {return 1;}
            else {return n * @fact(n - 1);}
        }
        func  @inc( n, delta: int):void {
            n := n + delta;
            return n;
        }
        func @main():int {
            var delta: int = @fact(3);
            @inc(self.x, delta);
            io.@writeInt(self.x);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    def test_19(self):
        input = """class Program {
                func HorrorScene():void {
                    if {
                    You.@location := "balcony"; 
                    io.@writeStr("Welcome to our house!");
                    }
                    You.goDown("floor4")
                    {
                        if You.goDown("floor3")
                        {
                            if You.goDown("floor2")
                            {
                                if You.goDown("floor1") 
                                {
                                    io.@writeStr("You seriously shouldnt go to the basement");
                                    if You.goDown("basement")
                                    {
                                        io.@writeStr("Hey there Valak!");
                                    }
                                    else{
                                        You.goUp();
                                    }
                                }
                                else{
                                    You.goUp();
                                }
                            }
                            else
                            {
                                You.goUp();
                            }
                        }
                        else
                        {
                            You.goUp();
                        }
                    }
                    else{
                        You.goUp();
                    }                      
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_20(self):
        input = """class Prog {
                    const @numOfShape: int = 0;
                    const immutableAttribute: int = 0;
                    var length, width: int;

                    func @main():void {
                        if test.test1(Me) == true {
                            io.@writeLn("This is line 1");
                        }
                        else{
                            io.@writeLn("This is line 2");
                        }
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
    def test_21(self):
        input = """class A {func @fact(n: int):int {
            if (i % 5 != 2) && (12 == 2) {return;}
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
    def test_22(self):
        input = """class Program {
            func @how(): void {
                if (i % 5 != 2 && true) {return;}
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test_23(self):
        input = """class A{
            var a: [3]int = [[a,b,c],b,c];
        }"""
        expect = "Error on line 2 col 29: ["
        self.assertTrue(TestParser.test(input, expect, 223))
    def test_24(self):
        input = """class Test <- test{
            func main():void{
                a[2+y.a()] := new new Y().k;
            }
        }"""
        expect = "Error on line 3 col 34: new"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test_25(self):
        input = """class Test <- test{
            func main():void{
                a[2+y.a()] := [1,2.0];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
    def test_26(self):
        input = """class Test <- test{
            func main():void{
                a[2+y.a()] := !a.t[2];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test_27(self):
        input = "class B <- a{var x: [3]int = [fact(), 1 + 2, 3 + 4];}"
        expect = "Error on line 1 col 30: fact"
        self.assertTrue(TestParser.test(input, expect, 227))
    def test_28(self):
        input = """class B <- a{const a:[5]int = ["string", "arr",8,9.2]; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
    def test_29(self):
        input = """class Program {
            func @main():int {
                @text := !(a && b);
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
    def test_30(self):
        input = """class Program { 
            class A {
                func test(): int {
                    func test(): void { }
                }
            }
        }"""
        expect = "Error on line 2 col 12: class"
        self.assertTrue(TestParser.test(input, expect, 230))
    def test_31(self):
        input = """class Program { 
        for i:=0; i<5; i:=i+1 { // for loop
            if i==3 {
                continue; // skip rest of loop
            }
            io.@writeInt(i);
        }
        io.@writeStr("Press 1 to exit: ");
        if input==1 {
            break; // terminate loop
            }
        }"""
        expect = "Error on line 2 col 8: for"
        self.assertTrue(TestParser.test(input, expect, 231))
    def test_32(self):
        input = """class Shape{
            func setLength(): int{
                return self.length = 5;
            }
        }"""
        expect = "Error on line 3 col 35: ="
        self.assertTrue(TestParser.test(input, expect, 232))
    def test_33(self):
        input = """class Program {
            func @main(): void {
                var message: string = "This is an unclosed string literal";
                io.@writeString(message);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
    def test_34(self):
        input = """class Program {
            @main(): void {
                io.@writeString("Hello, World!");
            }
        }"""
        expect = "Error on line 2 col 12: @main"
        self.assertTrue(TestParser.test(input, expect, 234))
    def test_35(self):
        input = """class Program {
            @main(): void {
                io.@writeString("Hello, World!");
            }
        }"""
        expect = "Error on line 2 col 12: @main"
        self.assertTrue(TestParser.test(input, expect, 235))