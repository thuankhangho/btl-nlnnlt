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
