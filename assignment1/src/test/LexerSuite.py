# Student ID: 2011357
# Name: Ho Thuan Khang
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
        input = "\"Hello \q World!\""
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
    def test_array_literal_51(self):
        input = "[\"a\",\"b\",\"c\"]"
        expected = "[,a,,,b,,,c,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 151))
    def test_array_literal_52(self):
        input = "[1,2,3]"
        expected = "[,1,,,2,,,3,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 152))
    def test_array_literal_53(self):
        input = "[\"a\",1,true]"
        expected = "[,a,,,1,,,true,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 153))
    def test_array_literal_54(self):
        input = "var a: [4]int = [\"a\",\"b\",\"c\",\"d\"]"
        expected = "var,a,:,[,4,],int,=,[,a,,,b,,,c,,,d,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 154))
    def test_array_literal_55(self):
        input = "[[a,b,c],a,b,c]"
        expected = "[,[,a,,,b,,,c,],,,a,,,b,,,c,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 155))
    def test_random_56(self):
        input = "[a,b,c,d],e]"
        expected = "[,a,,,b,,,c,,,d,],,,e,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 156))
    def test_random_57(self):
        input = "[new X(),b,c,d],e]"
        expected = "[,new,X,(,),,,b,,,c,,,d,],,,e,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 157))
    def test_random_58(self):
        input = "\"new X()\""
        expected = "new X(),<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 158))
    def test_random_59(self):
        input = "\"\"\"\""
        expected = ",,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 159))
    def test_random_60(self):
        input = "var a: int = 1E+3;"
        expected = "var,a,:,int,=,1E+3,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 160))
    def test_random_61(self):
        input = "[2.3, 4.2, 102e3]"
        expected = "[,2.3,,,4.2,,,102e3,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 161))
    def test_random_62(self):
        input = "abc\t"
        expected = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 162))
    def test_random_63(self):
        input = "1234567"
        expected = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 163))
    def test_random_64(self):
        input = "1234.567"
        expected = "1234.567,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 164))
    def test_random_65(self):
        input = "class A{var delta: int = 3;}"
        expected = "class,A,{,var,delta,:,int,=,3,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 165))
    def test_random_66(self):
        input = "class Program{ const a, b, c: int = 3, 4, 6;}"
        expected = "class,Program,{,const,a,,,b,,,c,:,int,=,3,,,4,,,6,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 166))
    def test_random_67(self):
        input = "class Program{var  a, b, c, d: int = 3, 4, 6;}"
        expected = "class,Program,{,var,a,,,b,,,c,,,d,:,int,=,3,,,4,,,6,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 167))
    def test_random_68(self):
        input = "class Program {func @main():int {}}"
        expected = "class,Program,{,func,@main,(,),:,int,{,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 168))
    def test_random_69(self):
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
        }} """
        expected = "class,Program,{,var,x,:,int,=,65,;,func,@fact,(,n,:,int,),:,int,{,if,n,==,0,{,return,1,;,},else,{,return,n,*,@fact,(,n,-,1,),;,},},func,@inc,(,n,,,delta,:,int,),:,void,{,n,:=,n,+,delta,;,return,n,;,},func,@main,(,),:,int,{,var,delta,:,int,=,@fact,(,3,),;,@inc,(,self,.,x,,,delta,),;,io,.,@writeInt,(,self,.,x,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 169))
    def test_random_70(self):
        input = "\"Hi\"\""
        expected = "Hi,Unclosed String: "
        self.assertTrue(TestLexer.test(input, expected, 170))
    def test_random_71(self):
        input = "a == 2"
        expected = "a,==,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 171))
    def test_random_72(self):
        input = "a % 5 == 2"
        expected = "a,%,5,==,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 172))
    def test_random_73(self):
        input = "a && 2"
        expected = "a,&&,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 173))
    def test_random_74(self):
        input = "a &&& 2"
        expected = "a,&&,Error Token &"
        self.assertTrue(TestLexer.test(input, expected, 174))
    def test_random_75(self):
        input = "a ||| 2"
        expected = "a,||,Error Token |"
        self.assertTrue(TestLexer.test(input, expected, 175))
    def test_random_76(self):
        input = "a \\\ 2"
        expected = "a,\,\,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 176))
    def test_random_77(self):
        input = "a != 2"
        expected = "a,!=,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 177))
    def test_random_78(self):
        input = "void"
        expected = "void,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 178))
    def test_random_79(self):
        input = "func constructor"
        expected = "func,constructor,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 179))
    def test_random_80(self):
        input = "/* This is a block comment,\nthat span in many lines*/"
        expected = "<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 180))
    def test_random_81(self):
        input = "(1,3)"
        expected = "(,1,,,3,),<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 181))
    def test_random_82(self):
        input = "[0-9][a-zA-Z]"
        expected = "[,0,-,9,],[,a,-,zA,-,Z,],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 182))
    def test_random_83(self):
        input = "sleep/study/relax/aesthetic"
        expected = "sleep,/,study,/,relax,/,aesthetic,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 183))
    def test_random_84(self):
        input = "\"\#metoo\""
        expected = "Illegal Escape In String: \#"
        self.assertTrue(TestLexer.test(input, expected, 184))
    def test_random_85(self):
        input = "\"Lofi \And \Chill\""
        expected = "Illegal Escape In String: Lofi \A"
        self.assertTrue(TestLexer.test(input, expected, 185))
    def test_random_86(self):
        input = "\"$$$\""
        expected = "$$$,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 186))
    def test_random_87(self):
        input = "[\"$\"$$]"
        expected = "[,$,Error Token $"
        self.assertTrue(TestLexer.test(input, expected, 187))
    def test_random_88(self):
        input = "$$$"
        expected = "Error Token $"
        self.assertTrue(TestLexer.test(input, expected, 188))
    def test_random_89(self):
        input = """\b"""
        expected = "Error Token "
        self.assertTrue(TestLexer.test(input, expected, 189))
    def test_random_90(self):
        input = "\"\%\""
        expected = "Illegal Escape In String: \%"
        self.assertTrue(TestLexer.test(input, expected, 190))
    def test_random_91(self):
        input = """ class Test <- test{
            func main():void{
                a[2+y.a()] := !a.t[2];
            }
        } """
        expected = "class,Test,<-,test,{,func,main,(,),:,void,{,a,[,2,+,y,.,a,(,),],:=,!,a,.,t,[,2,],;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 191))
    def test_random_92(self):
        input = "class Program { }"
        expected = "class,Program,{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 192))
    def test_random_93(self):
        input = "a[2] := a[].t[2];"
        expected = "a,[,2,],:=,a,[,],.,t,[,2,],;,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 193))
    def test_random_94(self):
        input = "a[2[3[4[5[6[7[8[9]]]]]]]]"
        expected = "a,[,2,[,3,[,4,[,5,[,6,[,7,[,8,[,9,],],],],],],],],<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 194))
    def test_random_95(self):
        input = """string a = test string //this comment is irrelevant"; print a;"""
        expected = "string,a,=,test,string,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 195))
    def test_random_96(self):
        input = "var a: [69]int =[a,b,c,d,e,...];"
        expected = "var,a,:,[,69,],int,=,[,a,,,b,,,c,,,d,,,e,,,.,.,.,],;,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 196))
    def test_random_97(self):
        input = "WS : [ \t\r\n]+ -> skip ;"
        expected = "WS,:,[,],+,-,>,skip,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 197))
    def test_random_98(self):
        input = """print "Hello \nWorld"""
        expected = "print,Unclosed String: Hello "
        self.assertTrue(TestLexer.test(input, expected, 198))
    def test_random_99(self):
        input = """ print "Hello \\nWorld" """
        expected = "print,Hello \\nWorld,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 199))