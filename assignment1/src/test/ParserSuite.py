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
            func @main(): int {
                io.@writeString("Hello, World!");
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
    def test_36(self):
        input = """class Program {
            func @main(): void{
                @io.writeint(2);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
    def test_37(self):
        input = """class Program {
            func @main(): void{
                self.x := self.y;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
    def test_38(self):
        input = """class Program {
            func @main(): void{
                @io.readInt(3);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
    def test_39(self):
        input = """class Program {
            func @main(): void{
                self.test[3]();
            }
        }"""
        expect = "Error on line 3 col 28: ("
        self.assertTrue(TestParser.test(input, expect, 239))
    def test_40(self):
        input = """class Program {
            func @main(): void{
                Test.y := self.x + self.y;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
    def test_41(self):
        input = """class Program {
            func @main(): void{
                for i:=0; i<10; i:=i+1 {
                    var x: int = new Test();
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
    def test_42(self):
        input = """class Program {
            func Test(): void {
                for test[0] := 0; test[0] < test[1]; test[0]:=test[0] + 1 {
                    io.@writeInt(test[0]);
                    if test[0] < 10 {
                        continue;
                    }
                    else {
                        break;
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))
    def test_43(self):
        input = """class Program {
            func Test(): void {
                    io.@writeInt(test[0]);
                    if test[0] < 10 {
                        continue;
                    }
                    else {
                        break;
                    }
                }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
    def test_44(self):
        input = """class Program {
            func @main(): void{
                break;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
    def test_45(self):
        input = """class Program {
            func @main(): void{
                continue;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
    def test_46(self):
        input = """class Program {
            func @main(): void{
                return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
    def test_47(self):
        input = """class Program {
            func @main(): void{
                return x > y;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
    def test_48(self):
        input = """class Program {
            func @main(): void{
                return x == y;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))
    def test_49(self):
        input = """class Program {
            func @main(): void{
                return a != b;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))
    def test_50(self):
        input = """class Program {
            func @main(): void{
                self.aPI := 3.14159;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    def test_51(self):
        input = """class Program {
            func @main(): void{
                emp[0].t := 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))
    def test_52(self):
        input = """class Program {
            func @main(): void{
                var a: [3]int = a := 1;
            }
        }"""
        expect = "Error on line 3 col 34: :="
        self.assertTrue(TestParser.test(input, expect, 252))
    def test_53(self):
        input = """class Program {
            func @main(): void{
                a := b.t[3];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))
    def test_54(self):
        input = """class Program {
            func @main(): void{
                e.t[1] := a.c[1];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
    def test_55(self):
        input = """class Program {
            func @main(): void{
                const a: int = 3;
                var b: string = "C";
                var c: string = a ^ c;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))
    def test_56(self):
        input = """class Program {
            func @main(): void{
                if {i := 0;} j > i {
                    j := j - 1;
                }
                else {
                    j := j + 1;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))
    def test_57(self):
        input = """class Program {
            func @main(): void{
                l[3] := value * 2;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
    def test_58(self):
        input = """class Program {
            func @main(): void{
                value := x.foo(5);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))
    def test_59(self):
        input = """class Program {
            func @main(): void{
                lhs := expr;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
    def test_60(self):
        input = """class Program {
            func @main(): void{
                if a + 4 == 5 {
                    return a + 1;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))
    def test_61(self):
        input = """class Program {
            func @main(): void{
                if a > 3 {
                    return a + 1;
                }
                else {
                    if a < 3 {
                        return a - 1;
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
    def test_62(self):
        input = """class Program {
            func @main(): void{
                var a: [2]int = [2, 4];
                for i := 0; i < 10; i:=i + 1 {
                    a[i] := 5;
                    }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
    def test_63(self):
        input = """class Program {
            func @main(): void{
                var a: [2]int = [2, 4];
                for i := 0; i < 10; i:=i + 1 {
                    a[i] := 5;
                    }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
    def test_64(self):
        input = """class Program {
            func @main(): void{
                var a: [2]int = [2, 4];
            }
        }
        class A { var a: int = 3;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))
    def test_65(self):
        input = """class Program {
            func @main(): void{
                return int;
            }
        }"""
        expect = "Error on line 3 col 23: int"
        self.assertTrue(TestParser.test(input, expect, 265))
    def test_66(self):
        input = """class Program {
            func @main(): void{
                func test(): void {
                    
                }
            }
        }
        class A { var a: int = 3;}"""
        expect = "Error on line 3 col 16: func"
        self.assertTrue(TestParser.test(input, expect, 266))
    def test_67(self):
        input = """class Program {
            func @main(): void{
                class C <- B {}
            }
        }
        class A { var a: int = 3;}"""
        expect = "Error on line 3 col 16: class"
        self.assertTrue(TestParser.test(input, expect, 267))
    def test_68(self):
        input = """class Program {
            func @main(): void{
                return io.@writeInt(3,2,1);
            }
        }
        class A { var a: int = 3;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))
    def test_69(self):
        input = """class A <- a {
            func test (n: bool): void {
                break;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))
    def test_70(self):
        input = """class Program {
            func jNnzegvZco (x: string): [32278]string {  }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))
