import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_comment_0(self):
        input = "a := 5;//this is a line comment"
        expected = "a,:=,5,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 100))
    def test_comment_1(self):
        input = "/* This is a block comment, that\nmay span in many lines*/"
        expected = "<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 101))
    def test_comment_2(self):
        input = "/* This is a block comment, that\nmay span in many lines*/"
        expected = "<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 102))
    def test_comment_3(self):
        input = "a := 5;/* This is a block comment, that\nmay span in many lines*/"
        expected = "a,:=,5,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 103))
    def test_comment_4(self):
        input = "var a: int = 5;//Hi\n/* This is a block comment, that\nmay span in many lines*/"
        expected = "var,a,:,int,=,5,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 104))
    def test_comment_5(self):
        input = "/*//Hi This is a block comment, that\nmay span in many lines*/"
        expected = "<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 105))
    def test_comment_6(self):
        input = "/* This is a block comment so // has no meaning here */\n//This is a line comment so /* has no meaning here"
        expected = "<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 106))
    def test_identifier_7(self):
        input = "@a123"
        expected = "@a123,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 107))
    def test_identifier_8(self):
        input = "@_"
        expected = "@_,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 108))
    def test_identifier_9(self):
        input = "__main__"
        expected = "__main__,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 109))
    def test_identifier_10(self):
        input = "a\r"
        expected = "a,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 110))
    def test_keyword_operator_separator_11(self):
        input = "const"
        expected = "const,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 111))
    def test_keyword_operator_separator_12(self):
        input = "^"
        expected = "^,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 112))
    def test_keyword_operator_separator_13(self):
        input = "%"
        expected = "%,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 113))
    def test_keyword_operator_separator_14(self):
        input = "}"
        expected = "},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 114))
    def test_keyword_operator_separator_15(self):
        input = "."
        expected = ".,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 115))
    # def test_keyword_operator_separator_16(self):
    #     input = "[\"a\",\"b\",\"c\"]"
    #     expected = ".,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 116))
    def test_keyword_operator_separator_17(self):
        input = "\"Valid: \\n \\\""
        expected = "<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 117))
    # def test_1(self):
    #     input = "\"123\k Hi\""
    #     expected = "Illegal Escape In String: 123\k"
    #     self.assertTrue(TestLexer.test(input, expected, 101))
    # def test_2(self):
    #     input = "\"123 Hi\""
    #     expected = "123 Hi,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 102))
    # def test_3(self):
    #     input = """ "print \\"Hello, World!\\"" """
    #     expected = "print \"Hello, World!\",<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 103))
    # def test_4(self):
    #     input = """ "Hello \q World!" """
    #     expected = "Illegal Escape In String: Hello \q"
    #     self.assertTrue(TestLexer.test(input, expected, 104))
    # def test_5(self):
    #     input = """ "He asked me: \\"Where is John?\\"" """
    #     expected = "He asked me: \"Where is John?\",<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 105))
    # def test_6(self):
    #     input = "He asked me: \"Where is John?\""
    #     expected = "He,asked,me,:,Where is John?,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 106))
    # def test_7(self):
    #     input = """ He asked me: \"Where is John? """
    #     expected = "He asked me: \"Where is John?\",<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 107))
    # def test_8(self):
    #     input = "\"dkjoiue\\s\""
    #     expected = "Illegal Escape In String: dkjoiue\s"
    #     self.assertTrue(TestLexer.test(input, expected, 108))
    # def test_9(self):
    #     input = ",./;'p[213]!@#@!$"
    #     expected = "Illegal Escape In String: dkjoiue\s"
    #     self.assertTrue(TestLexer.test(input, expected, 109))
    # # def test_10(self):
    #     input = "class Program {func @main():int {@isSth := !a.x[1] && b [2];}}"
    #     expected = "Illegal Escape In String: dkjoiue\s"
    #     self.assertTrue(TestLexer.test(input, expected, 110))
    # # def test_11(self):
    #     input = "class Program {func @main():int {@text := !(a && b);}}"
    #     expected = "Illegal Escape In String: dkjoiue\s"
    #     self.assertTrue(TestLexer.test(input, expected, 111))