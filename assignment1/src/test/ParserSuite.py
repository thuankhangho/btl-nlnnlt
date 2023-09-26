import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_0(self):
        """Simple program"""
        input = """class A{var delta: int = 3;}"""
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