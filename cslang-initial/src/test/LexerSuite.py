import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
    def test_0(self):
        input = "123"
        expected = "123,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 102))
    def test_1(self):
        input = """func constructor"""
        expected = "func,constructor,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 102))
