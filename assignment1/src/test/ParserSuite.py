import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_0(self):
        """Simple program"""
        input = """class A {}"""
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
        input = """func @fact(n: int):int {
            var a: [12]int;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))