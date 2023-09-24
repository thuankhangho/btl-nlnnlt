# Generated from d:\btl1-nlnnlt\cslang-initial\src\main\CSlang\parser\CSlang.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


	from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\29")
        buf.write("\u014b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3")
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\6\64\u012c\n\64\r\64\16")
        buf.write("\64\u012d\3\64\7\64\u0131\n\64\f\64\16\64\u0134\13\64")
        buf.write("\3\64\3\64\6\64\u0138\n\64\r\64\16\64\u0139\5\64\u013c")
        buf.write("\n\64\3\65\6\65\u013f\n\65\r\65\16\65\u0140\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\67\3\67\38\38\2\29\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\61a\62c\63e\64g\65i\66k\67m8o9\3\2\5\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\5\2\n\f\16\17\"\"\2\u014f\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\3q\3\2\2\2\5t\3\2\2\2")
        buf.write("\7z\3\2\2\2\t\u0083\3\2\2\2\13\u0086\3\2\2\2\r\u008b\3")
        buf.write("\2\2\2\17\u008f\3\2\2\2\21\u0094\3\2\2\2\23\u009a\3\2")
        buf.write("\2\2\25\u009e\3\2\2\2\27\u00a4\3\2\2\2\31\u00a9\3\2\2")
        buf.write("\2\33\u00b0\3\2\2\2\35\u00b7\3\2\2\2\37\u00bc\3\2\2\2")
        buf.write("!\u00c2\3\2\2\2#\u00ce\3\2\2\2%\u00d2\3\2\2\2\'\u00d7")
        buf.write("\3\2\2\2)\u00db\3\2\2\2+\u00e0\3\2\2\2-\u00e6\3\2\2\2")
        buf.write("/\u00eb\3\2\2\2\61\u00ed\3\2\2\2\63\u00ef\3\2\2\2\65\u00f1")
        buf.write("\3\2\2\2\67\u00f3\3\2\2\29\u00f5\3\2\2\2;\u00f7\3\2\2")
        buf.write("\2=\u00fa\3\2\2\2?\u00fd\3\2\2\2A\u0100\3\2\2\2C\u0102")
        buf.write("\3\2\2\2E\u0105\3\2\2\2G\u0107\3\2\2\2I\u010a\3\2\2\2")
        buf.write("K\u010c\3\2\2\2M\u010f\3\2\2\2O\u0112\3\2\2\2Q\u0114\3")
        buf.write("\2\2\2S\u0116\3\2\2\2U\u0118\3\2\2\2W\u011a\3\2\2\2Y\u011c")
        buf.write("\3\2\2\2[\u011e\3\2\2\2]\u0120\3\2\2\2_\u0122\3\2\2\2")
        buf.write("a\u0124\3\2\2\2c\u0126\3\2\2\2e\u0128\3\2\2\2g\u013b\3")
        buf.write("\2\2\2i\u013e\3\2\2\2k\u0144\3\2\2\2m\u0147\3\2\2\2o\u0149")
        buf.write("\3\2\2\2qr\7>\2\2rs\7/\2\2s\4\3\2\2\2tu\7d\2\2uv\7t\2")
        buf.write("\2vw\7g\2\2wx\7c\2\2xy\7m\2\2y\6\3\2\2\2z{\7e\2\2{|\7")
        buf.write("q\2\2|}\7p\2\2}~\7v\2\2~\177\7k\2\2\177\u0080\7p\2\2\u0080")
        buf.write("\u0081\7w\2\2\u0081\u0082\7g\2\2\u0082\b\3\2\2\2\u0083")
        buf.write("\u0084\7k\2\2\u0084\u0085\7h\2\2\u0085\n\3\2\2\2\u0086")
        buf.write("\u0087\7g\2\2\u0087\u0088\7n\2\2\u0088\u0089\7u\2\2\u0089")
        buf.write("\u008a\7g\2\2\u008a\f\3\2\2\2\u008b\u008c\7h\2\2\u008c")
        buf.write("\u008d\7q\2\2\u008d\u008e\7t\2\2\u008e\16\3\2\2\2\u008f")
        buf.write("\u0090\7v\2\2\u0090\u0091\7t\2\2\u0091\u0092\7w\2\2\u0092")
        buf.write("\u0093\7g\2\2\u0093\20\3\2\2\2\u0094\u0095\7h\2\2\u0095")
        buf.write("\u0096\7c\2\2\u0096\u0097\7n\2\2\u0097\u0098\7u\2\2\u0098")
        buf.write("\u0099\7g\2\2\u0099\22\3\2\2\2\u009a\u009b\7k\2\2\u009b")
        buf.write("\u009c\7p\2\2\u009c\u009d\7v\2\2\u009d\24\3\2\2\2\u009e")
        buf.write("\u009f\7h\2\2\u009f\u00a0\7n\2\2\u00a0\u00a1\7q\2\2\u00a1")
        buf.write("\u00a2\7c\2\2\u00a2\u00a3\7v\2\2\u00a3\26\3\2\2\2\u00a4")
        buf.write("\u00a5\7d\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7\7q\2\2\u00a7")
        buf.write("\u00a8\7n\2\2\u00a8\30\3\2\2\2\u00a9\u00aa\7u\2\2\u00aa")
        buf.write("\u00ab\7v\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad\7k\2\2\u00ad")
        buf.write("\u00ae\7p\2\2\u00ae\u00af\7i\2\2\u00af\32\3\2\2\2\u00b0")
        buf.write("\u00b1\7t\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3\7v\2\2\u00b3")
        buf.write("\u00b4\7w\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6\7p\2\2\u00b6")
        buf.write("\34\3\2\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9\7w\2\2\u00b9")
        buf.write("\u00ba\7n\2\2\u00ba\u00bb\7n\2\2\u00bb\36\3\2\2\2\u00bc")
        buf.write("\u00bd\7e\2\2\u00bd\u00be\7n\2\2\u00be\u00bf\7c\2\2\u00bf")
        buf.write("\u00c0\7u\2\2\u00c0\u00c1\7u\2\2\u00c1 \3\2\2\2\u00c2")
        buf.write("\u00c3\7e\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5\7p\2\2\u00c5")
        buf.write("\u00c6\7u\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8\7t\2\2\u00c8")
        buf.write("\u00c9\7w\2\2\u00c9\u00ca\7e\2\2\u00ca\u00cb\7v\2\2\u00cb")
        buf.write("\u00cc\7q\2\2\u00cc\u00cd\7t\2\2\u00cd\"\3\2\2\2\u00ce")
        buf.write("\u00cf\7x\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1\7t\2\2\u00d1")
        buf.write("$\3\2\2\2\u00d2\u00d3\7u\2\2\u00d3\u00d4\7g\2\2\u00d4")
        buf.write("\u00d5\7n\2\2\u00d5\u00d6\7h\2\2\u00d6&\3\2\2\2\u00d7")
        buf.write("\u00d8\7p\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7y\2\2\u00da")
        buf.write("(\3\2\2\2\u00db\u00dc\7x\2\2\u00dc\u00dd\7q\2\2\u00dd")
        buf.write("\u00de\7k\2\2\u00de\u00df\7f\2\2\u00df*\3\2\2\2\u00e0")
        buf.write("\u00e1\7e\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3\7p\2\2\u00e3")
        buf.write("\u00e4\7u\2\2\u00e4\u00e5\7v\2\2\u00e5,\3\2\2\2\u00e6")
        buf.write("\u00e7\7h\2\2\u00e7\u00e8\7w\2\2\u00e8\u00e9\7p\2\2\u00e9")
        buf.write("\u00ea\7e\2\2\u00ea.\3\2\2\2\u00eb\u00ec\7-\2\2\u00ec")
        buf.write("\60\3\2\2\2\u00ed\u00ee\7/\2\2\u00ee\62\3\2\2\2\u00ef")
        buf.write("\u00f0\7,\2\2\u00f0\64\3\2\2\2\u00f1\u00f2\7\61\2\2\u00f2")
        buf.write("\66\3\2\2\2\u00f3\u00f4\7^\2\2\u00f48\3\2\2\2\u00f5\u00f6")
        buf.write("\7#\2\2\u00f6:\3\2\2\2\u00f7\u00f8\7(\2\2\u00f8\u00f9")
        buf.write("\7(\2\2\u00f9<\3\2\2\2\u00fa\u00fb\7~\2\2\u00fb\u00fc")
        buf.write("\7~\2\2\u00fc>\3\2\2\2\u00fd\u00fe\7?\2\2\u00fe\u00ff")
        buf.write("\7?\2\2\u00ff@\3\2\2\2\u0100\u0101\7?\2\2\u0101B\3\2\2")
        buf.write("\2\u0102\u0103\7#\2\2\u0103\u0104\7?\2\2\u0104D\3\2\2")
        buf.write("\2\u0105\u0106\7>\2\2\u0106F\3\2\2\2\u0107\u0108\7>\2")
        buf.write("\2\u0108\u0109\7?\2\2\u0109H\3\2\2\2\u010a\u010b\7@\2")
        buf.write("\2\u010bJ\3\2\2\2\u010c\u010d\7@\2\2\u010d\u010e\7?\2")
        buf.write("\2\u010eL\3\2\2\2\u010f\u0110\7<\2\2\u0110\u0111\7?\2")
        buf.write("\2\u0111N\3\2\2\2\u0112\u0113\7`\2\2\u0113P\3\2\2\2\u0114")
        buf.write("\u0115\7\'\2\2\u0115R\3\2\2\2\u0116\u0117\7*\2\2\u0117")
        buf.write("T\3\2\2\2\u0118\u0119\7+\2\2\u0119V\3\2\2\2\u011a\u011b")
        buf.write("\7]\2\2\u011bX\3\2\2\2\u011c\u011d\7_\2\2\u011dZ\3\2\2")
        buf.write("\2\u011e\u011f\7\60\2\2\u011f\\\3\2\2\2\u0120\u0121\7")
        buf.write(".\2\2\u0121^\3\2\2\2\u0122\u0123\7=\2\2\u0123`\3\2\2\2")
        buf.write("\u0124\u0125\7<\2\2\u0125b\3\2\2\2\u0126\u0127\7}\2\2")
        buf.write("\u0127d\3\2\2\2\u0128\u0129\7\177\2\2\u0129f\3\2\2\2\u012a")
        buf.write("\u012c\t\2\2\2\u012b\u012a\3\2\2\2\u012c\u012d\3\2\2\2")
        buf.write("\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u0132\3")
        buf.write("\2\2\2\u012f\u0131\t\3\2\2\u0130\u012f\3\2\2\2\u0131\u0134")
        buf.write("\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133")
        buf.write("\u013c\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u0137\7B\2\2")
        buf.write("\u0136\u0138\t\3\2\2\u0137\u0136\3\2\2\2\u0138\u0139\3")
        buf.write("\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013c")
        buf.write("\3\2\2\2\u013b\u012b\3\2\2\2\u013b\u0135\3\2\2\2\u013c")
        buf.write("h\3\2\2\2\u013d\u013f\t\4\2\2\u013e\u013d\3\2\2\2\u013f")
        buf.write("\u0140\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141\3\2\2\2")
        buf.write("\u0141\u0142\3\2\2\2\u0142\u0143\b\65\2\2\u0143j\3\2\2")
        buf.write("\2\u0144\u0145\13\2\2\2\u0145\u0146\b\66\3\2\u0146l\3")
        buf.write("\2\2\2\u0147\u0148\13\2\2\2\u0148n\3\2\2\2\u0149\u014a")
        buf.write("\13\2\2\2\u014ap\3\2\2\2\b\2\u012d\u0132\u0139\u013b\u0140")
        buf.write("\4\b\2\2\3\66\2")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    BREAK = 2
    CONTINUE = 3
    IF = 4
    ELSE = 5
    FOR = 6
    TRUE = 7
    FALSE = 8
    INT = 9
    FLOAT = 10
    BOOL = 11
    STRING = 12
    RETURN = 13
    NULL = 14
    CLASS = 15
    CONSTRUCTOR = 16
    VAR = 17
    SELF = 18
    NEW = 19
    VOID = 20
    CONST = 21
    FUNC = 22
    PLUS = 23
    MINUS = 24
    MULTIPLY = 25
    DIVIDE_FLOAT = 26
    DIVIDE_INT = 27
    DIFF = 28
    AND = 29
    OR = 30
    EQUAL = 31
    DECLARE = 32
    NEQ = 33
    LE = 34
    LEQ = 35
    GE = 36
    GEQ = 37
    ASSIGN = 38
    XOR = 39
    MOD = 40
    LRB = 41
    RRB = 42
    LSB = 43
    RSB = 44
    DOT = 45
    CM = 46
    SM = 47
    COLON = 48
    LCB = 49
    RCB = 50
    IDENTIFIER = 51
    WS = 52
    ERROR_CHAR = 53
    UNCLOSE_STRING = 54
    ILLEGAL_ESCAPE = 55

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<-'", "'break'", "'continue'", "'if'", "'else'", "'for'", 
            "'true'", "'false'", "'int'", "'float'", "'bool'", "'string'", 
            "'return'", "'null'", "'class'", "'constructor'", "'var'", "'self'", 
            "'new'", "'void'", "'const'", "'func'", "'+'", "'-'", "'*'", 
            "'/'", "'\\'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "':='", "'^'", "'%'", "'('", "')'", 
            "'['", "']'", "'.'", "','", "';'", "':'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", 
            "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
            "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", "PLUS", "MINUS", 
            "MULTIPLY", "DIVIDE_FLOAT", "DIVIDE_INT", "DIFF", "AND", "OR", 
            "EQUAL", "DECLARE", "NEQ", "LE", "LEQ", "GE", "GEQ", "ASSIGN", 
            "XOR", "MOD", "LRB", "RRB", "LSB", "RSB", "DOT", "CM", "SM", 
            "COLON", "LCB", "RCB", "IDENTIFIER", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", 
                  "FALSE", "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", 
                  "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", 
                  "CONST", "FUNC", "PLUS", "MINUS", "MULTIPLY", "DIVIDE_FLOAT", 
                  "DIVIDE_INT", "DIFF", "AND", "OR", "EQUAL", "DECLARE", 
                  "NEQ", "LE", "LEQ", "GE", "GEQ", "ASSIGN", "XOR", "MOD", 
                  "LRB", "RRB", "LSB", "RSB", "DOT", "CM", "SM", "COLON", 
                  "LCB", "RCB", "IDENTIFIER", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "CSlang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[52] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


