import unittest
from TestUtils import TestLexer

# Lexer testcases:
# 1 -> 5: comment
# 6 -> 10: identifier
# 11 -> 15: keywords, operators & separators
# 16 -> 30: integer & float literals
# 31 -> 33: bool literals
# 34 -> 50: string literals
# 50 -> 55: array literals
# 56 -> 100: random

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
        input = ">="
        expected = ">=,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 115))
    def test_integer_float_literal_16(self):
        input = "123"
        expected = "123,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 116))
    def test_integer_float_literal_17(self):
        input = ".5"
        expected = ".,5,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 117))
    def test_integer_float_literal_18(self):
        input = "1."
        expected = "1.,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 118))
    def test_integer_float_literal_19(self):
        input = "1e1"
        expected = "1e1,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 119))
    def test_integer_float_literal_20(self):
        input = "1.e1"
        expected = "1.e1,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 120))
    def test_integer_float_literal_21(self):
        input = "e1"
        expected = "e1,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 121))
    def test_integer_float_literal_22(self):
        input = "1.E+1"
        expected = "1.E+1,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 122))
    def test_integer_float_literal_23(self):
        input = "e+1"
        expected = "e,+,1,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 123))
    def test_integer_float_literal_24(self):
        input = "E1e"
        expected = "E1e,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 124))
    def test_integer_float_literal_25(self):
        input = "10.1e-10"
        expected = "10.1e-10,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 125))
    def test_integer_float_literal_26(self):
        input = "143e"
        expected = "143,e,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 126))
    def test_integer_float_literal_27(self):
        input = "0.33E-3"
        expected = "0.33E-3,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 127))
    def test_integer_float_literal_28(self):
        input = "128e+42"
        expected = "128e+42,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 128))
    def test_integer_float_literal_29(self):
        input = "1E-3"
        expected = "1E-3,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 129))
    def test_integer_float_literal_30(self):
        input = "2E3.2"
        expected = "2E3,.,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 130))
    def test_bool_literal_31(self):
        input = "a := true"
        expected = "a,:=,true,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 131))
    def test_bool_literal_32(self):
        input = "a := fals"
        expected = "a,:=,fals,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 132))
    def test_bool_literal_33(self):
        input = "falsetrue"
        expected = "falsetrue,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 133))
    def test_string_literal_34(self):
        input = "\"\""
        expected = ",<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 134))
    def test_string_literal_35(self):
        input = "\"123\k Hi\""
        expected = "Illegal Escape In String: 123\k"
        self.assertTrue(TestLexer.test(input, expected, 135))
    def test_string_literal_36(self):
        input = "\"123 Hi\""
        expected = "123 Hi,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 136))
    def test_string_literal_37(self):
        input = "\"Hello\" \"World\""
        expected = "Hello,World,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 137))
    def test_string_literal_38(self):
        input = "print \"Hello, World!\""
        expected = "print,Hello, World!,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 138))
    def test_string_literal_39(self):
        input = "Hello \q World!"
        expected = "Illegal Escape In String: Hello \q"
        self.assertTrue(TestLexer.test(input, expected, 139))
    def test_string_literal_40(self):
        input = "He asked me: \"Where's John?\""
        expected = "He,asked,me,:,Where's John?,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 140))
    def test_string_literal_41(self):
        input = "He asked me: \"Where is John?\""
        expected = "He,asked,me,:,Where is John?,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 141))
    def test_string_literal_42(self):
        input = "He asked me: \"Where is John?"
        expected = "He,asked,me,:,Unclosed String: Where is John?"
        self.assertTrue(TestLexer.test(input, expected, 142))
    def test_string_literal_43(self):
        input = "\"dkjoiue\\s\""
        expected = "Illegal Escape In String: dkjoiue\s"
        self.assertTrue(TestLexer.test(input, expected, 143))
    def test_string_literal_44(self):
        input = "\",./;'p[213]!@#@!$\""
        expected = ",./;'p[213]!@#@!$,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 144))
    def test_string_literal_45(self):
        input = "\"Hello\^\""
        expected = "Illegal Escape In String: Hello\^"
        self.assertTrue(TestLexer.test(input, expected, 145))
    def test_string_literal_46(self):
        input = "\"Hello$\""
        expected = "Hello$,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 146))
    def test_string_literal_47(self):
        input = "\"Hello\$\""
        expected = "Illegal Escape In String: Hello\$"
        self.assertTrue(TestLexer.test(input, expected, 147))
    def test_string_literal_48(self):
        input = "\"Hello // World\""
        expected = "Hello // World,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 148))
    def test_string_literal_49(self):
        input = "\"Hello ^ World\""
        expected = "Hello ^ World,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 149))
    def test_string_literal_50(self):
        input = "\"Hello \& World\""
        expected = "Illegal Escape In String: Hello \&"
        self.assertTrue(TestLexer.test(input, expected, 150))
    # def test_keyword_operator_separator_16(self):
    #     input = "[\"a\",\"b\",\"c\"]"
    #     expected = ".,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 116))
    # def test_string_literal_45(self):
    #     input = ",./;'p[213]!@#@!$"
    #     expected = ",,.,/,;,Error Token '"
    #     self.assertTrue(TestLexer.test(input, expected, 145))
