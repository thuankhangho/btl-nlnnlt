# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01ca\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\6\64\u0140")
        buf.write("\n\64\r\64\16\64\u0141\3\65\3\65\3\65\3\65\3\65\5\65\u0149")
        buf.write("\n\65\3\65\3\65\5\65\u014d\n\65\3\66\3\66\7\66\u0151\n")
        buf.write("\66\f\66\16\66\u0154\13\66\3\66\3\66\3\66\3\67\3\67\3")
        buf.write("\67\3\67\7\67\u015d\n\67\f\67\16\67\u0160\13\67\3\67\3")
        buf.write("\67\3\67\3\67\3\67\38\38\38\38\78\u016b\n8\f8\168\u016e")
        buf.write("\138\38\58\u0171\n8\38\38\39\39\79\u0177\n9\f9\169\u017a")
        buf.write("\139\3:\3:\6:\u017e\n:\r:\16:\u017f\3;\5;\u0183\n;\3;")
        buf.write("\7;\u0186\n;\f;\16;\u0189\13;\3<\3<\5<\u018d\n<\3<\6<")
        buf.write("\u0190\n<\r<\16<\u0191\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3=\5=\u01a2\n=\3>\3>\3>\3>\5>\u01a8\n>\3?\6?\u01ab")
        buf.write("\n?\r?\16?\u01ac\3?\3?\3@\3@\7@\u01b3\n@\f@\16@\u01b6")
        buf.write("\13@\3@\3@\3A\3A\3A\3A\7A\u01be\nA\fA\16A\u01c1\13A\3")
        buf.write("A\3A\3A\3A\3A\3B\3B\3B\4\u015e\u016c\2C\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u\2w\2y\2{\2}<\177")
        buf.write("=\u0081>\u0083?\3\2\13\3\2\62;\3\3\f\f\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\5\2\13\f")
        buf.write("\17\17\"\"\t\2))^^ddhhppttvv\2\u01dd\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3")
        buf.write("\2\2\2\3\u0085\3\2\2\2\5\u0088\3\2\2\2\7\u008e\3\2\2\2")
        buf.write("\t\u0097\3\2\2\2\13\u009a\3\2\2\2\r\u009f\3\2\2\2\17\u00a3")
        buf.write("\3\2\2\2\21\u00a8\3\2\2\2\23\u00ae\3\2\2\2\25\u00b2\3")
        buf.write("\2\2\2\27\u00b8\3\2\2\2\31\u00bd\3\2\2\2\33\u00c4\3\2")
        buf.write("\2\2\35\u00cb\3\2\2\2\37\u00d0\3\2\2\2!\u00d6\3\2\2\2")
        buf.write("#\u00e2\3\2\2\2%\u00e6\3\2\2\2\'\u00eb\3\2\2\2)\u00ef")
        buf.write("\3\2\2\2+\u00f4\3\2\2\2-\u00fa\3\2\2\2/\u00ff\3\2\2\2")
        buf.write("\61\u0101\3\2\2\2\63\u0103\3\2\2\2\65\u0105\3\2\2\2\67")
        buf.write("\u0107\3\2\2\29\u0109\3\2\2\2;\u010c\3\2\2\2=\u010f\3")
        buf.write("\2\2\2?\u0112\3\2\2\2A\u0115\3\2\2\2C\u0118\3\2\2\2E\u011b")
        buf.write("\3\2\2\2G\u011e\3\2\2\2I\u0120\3\2\2\2K\u0122\3\2\2\2")
        buf.write("M\u0124\3\2\2\2O\u0126\3\2\2\2Q\u0128\3\2\2\2S\u012a\3")
        buf.write("\2\2\2U\u012c\3\2\2\2W\u012e\3\2\2\2Y\u0130\3\2\2\2[\u0132")
        buf.write("\3\2\2\2]\u0134\3\2\2\2_\u0136\3\2\2\2a\u0138\3\2\2\2")
        buf.write("c\u013a\3\2\2\2e\u013c\3\2\2\2g\u013f\3\2\2\2i\u014c\3")
        buf.write("\2\2\2k\u014e\3\2\2\2m\u0158\3\2\2\2o\u0166\3\2\2\2q\u0174")
        buf.write("\3\2\2\2s\u017b\3\2\2\2u\u0182\3\2\2\2w\u018a\3\2\2\2")
        buf.write("y\u01a1\3\2\2\2{\u01a7\3\2\2\2}\u01aa\3\2\2\2\177\u01b0")
        buf.write("\3\2\2\2\u0081\u01b9\3\2\2\2\u0083\u01c7\3\2\2\2\u0085")
        buf.write("\u0086\7>\2\2\u0086\u0087\7/\2\2\u0087\4\3\2\2\2\u0088")
        buf.write("\u0089\7d\2\2\u0089\u008a\7t\2\2\u008a\u008b\7g\2\2\u008b")
        buf.write("\u008c\7c\2\2\u008c\u008d\7m\2\2\u008d\6\3\2\2\2\u008e")
        buf.write("\u008f\7e\2\2\u008f\u0090\7q\2\2\u0090\u0091\7p\2\2\u0091")
        buf.write("\u0092\7v\2\2\u0092\u0093\7k\2\2\u0093\u0094\7p\2\2\u0094")
        buf.write("\u0095\7w\2\2\u0095\u0096\7g\2\2\u0096\b\3\2\2\2\u0097")
        buf.write("\u0098\7k\2\2\u0098\u0099\7h\2\2\u0099\n\3\2\2\2\u009a")
        buf.write("\u009b\7g\2\2\u009b\u009c\7n\2\2\u009c\u009d\7u\2\2\u009d")
        buf.write("\u009e\7g\2\2\u009e\f\3\2\2\2\u009f\u00a0\7h\2\2\u00a0")
        buf.write("\u00a1\7q\2\2\u00a1\u00a2\7t\2\2\u00a2\16\3\2\2\2\u00a3")
        buf.write("\u00a4\7v\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6\7w\2\2\u00a6")
        buf.write("\u00a7\7g\2\2\u00a7\20\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9")
        buf.write("\u00aa\7c\2\2\u00aa\u00ab\7n\2\2\u00ab\u00ac\7u\2\2\u00ac")
        buf.write("\u00ad\7g\2\2\u00ad\22\3\2\2\2\u00ae\u00af\7k\2\2\u00af")
        buf.write("\u00b0\7p\2\2\u00b0\u00b1\7v\2\2\u00b1\24\3\2\2\2\u00b2")
        buf.write("\u00b3\7h\2\2\u00b3\u00b4\7n\2\2\u00b4\u00b5\7q\2\2\u00b5")
        buf.write("\u00b6\7c\2\2\u00b6\u00b7\7v\2\2\u00b7\26\3\2\2\2\u00b8")
        buf.write("\u00b9\7d\2\2\u00b9\u00ba\7q\2\2\u00ba\u00bb\7q\2\2\u00bb")
        buf.write("\u00bc\7n\2\2\u00bc\30\3\2\2\2\u00bd\u00be\7u\2\2\u00be")
        buf.write("\u00bf\7v\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7k\2\2\u00c1")
        buf.write("\u00c2\7p\2\2\u00c2\u00c3\7i\2\2\u00c3\32\3\2\2\2\u00c4")
        buf.write("\u00c5\7t\2\2\u00c5\u00c6\7g\2\2\u00c6\u00c7\7v\2\2\u00c7")
        buf.write("\u00c8\7w\2\2\u00c8\u00c9\7t\2\2\u00c9\u00ca\7p\2\2\u00ca")
        buf.write("\34\3\2\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd\7w\2\2\u00cd")
        buf.write("\u00ce\7n\2\2\u00ce\u00cf\7n\2\2\u00cf\36\3\2\2\2\u00d0")
        buf.write("\u00d1\7e\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7c\2\2\u00d3")
        buf.write("\u00d4\7u\2\2\u00d4\u00d5\7u\2\2\u00d5 \3\2\2\2\u00d6")
        buf.write("\u00d7\7e\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7p\2\2\u00d9")
        buf.write("\u00da\7u\2\2\u00da\u00db\7v\2\2\u00db\u00dc\7t\2\2\u00dc")
        buf.write("\u00dd\7w\2\2\u00dd\u00de\7e\2\2\u00de\u00df\7v\2\2\u00df")
        buf.write("\u00e0\7q\2\2\u00e0\u00e1\7t\2\2\u00e1\"\3\2\2\2\u00e2")
        buf.write("\u00e3\7x\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5\7t\2\2\u00e5")
        buf.write("$\3\2\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8\7g\2\2\u00e8")
        buf.write("\u00e9\7n\2\2\u00e9\u00ea\7h\2\2\u00ea&\3\2\2\2\u00eb")
        buf.write("\u00ec\7p\2\2\u00ec\u00ed\7g\2\2\u00ed\u00ee\7y\2\2\u00ee")
        buf.write("(\3\2\2\2\u00ef\u00f0\7x\2\2\u00f0\u00f1\7q\2\2\u00f1")
        buf.write("\u00f2\7k\2\2\u00f2\u00f3\7f\2\2\u00f3*\3\2\2\2\u00f4")
        buf.write("\u00f5\7e\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7p\2\2\u00f7")
        buf.write("\u00f8\7u\2\2\u00f8\u00f9\7v\2\2\u00f9,\3\2\2\2\u00fa")
        buf.write("\u00fb\7h\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd\7p\2\2\u00fd")
        buf.write("\u00fe\7e\2\2\u00fe.\3\2\2\2\u00ff\u0100\7-\2\2\u0100")
        buf.write("\60\3\2\2\2\u0101\u0102\7/\2\2\u0102\62\3\2\2\2\u0103")
        buf.write("\u0104\7,\2\2\u0104\64\3\2\2\2\u0105\u0106\7\61\2\2\u0106")
        buf.write("\66\3\2\2\2\u0107\u0108\7^\2\2\u01088\3\2\2\2\u0109\u010a")
        buf.write("\7(\2\2\u010a\u010b\7(\2\2\u010b:\3\2\2\2\u010c\u010d")
        buf.write("\7~\2\2\u010d\u010e\7~\2\2\u010e<\3\2\2\2\u010f\u0110")
        buf.write("\7?\2\2\u0110\u0111\7?\2\2\u0111>\3\2\2\2\u0112\u0113")
        buf.write("\7<\2\2\u0113\u0114\7?\2\2\u0114@\3\2\2\2\u0115\u0116")
        buf.write("\7#\2\2\u0116\u0117\7?\2\2\u0117B\3\2\2\2\u0118\u0119")
        buf.write("\7>\2\2\u0119\u011a\7?\2\2\u011aD\3\2\2\2\u011b\u011c")
        buf.write("\7@\2\2\u011c\u011d\7?\2\2\u011dF\3\2\2\2\u011e\u011f")
        buf.write("\7#\2\2\u011fH\3\2\2\2\u0120\u0121\7?\2\2\u0121J\3\2\2")
        buf.write("\2\u0122\u0123\7>\2\2\u0123L\3\2\2\2\u0124\u0125\7@\2")
        buf.write("\2\u0125N\3\2\2\2\u0126\u0127\7`\2\2\u0127P\3\2\2\2\u0128")
        buf.write("\u0129\7\'\2\2\u0129R\3\2\2\2\u012a\u012b\7*\2\2\u012b")
        buf.write("T\3\2\2\2\u012c\u012d\7+\2\2\u012dV\3\2\2\2\u012e\u012f")
        buf.write("\7]\2\2\u012fX\3\2\2\2\u0130\u0131\7_\2\2\u0131Z\3\2\2")
        buf.write("\2\u0132\u0133\7\60\2\2\u0133\\\3\2\2\2\u0134\u0135\7")
        buf.write(".\2\2\u0135^\3\2\2\2\u0136\u0137\7=\2\2\u0137`\3\2\2\2")
        buf.write("\u0138\u0139\7<\2\2\u0139b\3\2\2\2\u013a\u013b\7}\2\2")
        buf.write("\u013bd\3\2\2\2\u013c\u013d\7\177\2\2\u013df\3\2\2\2\u013e")
        buf.write("\u0140\t\2\2\2\u013f\u013e\3\2\2\2\u0140\u0141\3\2\2\2")
        buf.write("\u0141\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142h\3\2\2")
        buf.write("\2\u0143\u0144\5g\64\2\u0144\u0145\5u;\2\u0145\u014d\3")
        buf.write("\2\2\2\u0146\u0148\5g\64\2\u0147\u0149\5u;\2\u0148\u0147")
        buf.write("\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a\3\2\2\2\u014a")
        buf.write("\u014b\5w<\2\u014b\u014d\3\2\2\2\u014c\u0143\3\2\2\2\u014c")
        buf.write("\u0146\3\2\2\2\u014dj\3\2\2\2\u014e\u0152\7$\2\2\u014f")
        buf.write("\u0151\5{>\2\u0150\u014f\3\2\2\2\u0151\u0154\3\2\2\2\u0152")
        buf.write("\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0155\3\2\2\2")
        buf.write("\u0154\u0152\3\2\2\2\u0155\u0156\7$\2\2\u0156\u0157\b")
        buf.write("\66\2\2\u0157l\3\2\2\2\u0158\u0159\7\61\2\2\u0159\u015a")
        buf.write("\7,\2\2\u015a\u015e\3\2\2\2\u015b\u015d\13\2\2\2\u015c")
        buf.write("\u015b\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015f\3\2\2\2")
        buf.write("\u015e\u015c\3\2\2\2\u015f\u0161\3\2\2\2\u0160\u015e\3")
        buf.write("\2\2\2\u0161\u0162\7,\2\2\u0162\u0163\7\61\2\2\u0163\u0164")
        buf.write("\3\2\2\2\u0164\u0165\b\67\3\2\u0165n\3\2\2\2\u0166\u0167")
        buf.write("\7\61\2\2\u0167\u0168\7\61\2\2\u0168\u016c\3\2\2\2\u0169")
        buf.write("\u016b\13\2\2\2\u016a\u0169\3\2\2\2\u016b\u016e\3\2\2")
        buf.write("\2\u016c\u016d\3\2\2\2\u016c\u016a\3\2\2\2\u016d\u0170")
        buf.write("\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u0171\t\3\2\2\u0170")
        buf.write("\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173\b8\3\2")
        buf.write("\u0173p\3\2\2\2\u0174\u0178\t\4\2\2\u0175\u0177\t\5\2")
        buf.write("\2\u0176\u0175\3\2\2\2\u0177\u017a\3\2\2\2\u0178\u0176")
        buf.write("\3\2\2\2\u0178\u0179\3\2\2\2\u0179r\3\2\2\2\u017a\u0178")
        buf.write("\3\2\2\2\u017b\u017d\7B\2\2\u017c\u017e\t\5\2\2\u017d")
        buf.write("\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u017f\u0180\3\2\2\2\u0180t\3\2\2\2\u0181\u0183\7\60\2")
        buf.write("\2\u0182\u0181\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0187")
        buf.write("\3\2\2\2\u0184\u0186\t\2\2\2\u0185\u0184\3\2\2\2\u0186")
        buf.write("\u0189\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2")
        buf.write("\u0188v\3\2\2\2\u0189\u0187\3\2\2\2\u018a\u018c\t\6\2")
        buf.write("\2\u018b\u018d\t\7\2\2\u018c\u018b\3\2\2\2\u018c\u018d")
        buf.write("\3\2\2\2\u018d\u018f\3\2\2\2\u018e\u0190\t\2\2\2\u018f")
        buf.write("\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u018f\3\2\2\2")
        buf.write("\u0191\u0192\3\2\2\2\u0192x\3\2\2\2\u0193\u0194\7^\2\2")
        buf.write("\u0194\u01a2\7d\2\2\u0195\u0196\7^\2\2\u0196\u01a2\7h")
        buf.write("\2\2\u0197\u0198\7^\2\2\u0198\u01a2\7t\2\2\u0199\u019a")
        buf.write("\7^\2\2\u019a\u01a2\7p\2\2\u019b\u019c\7^\2\2\u019c\u01a2")
        buf.write("\7v\2\2\u019d\u019e\7^\2\2\u019e\u01a2\7$\2\2\u019f\u01a0")
        buf.write("\7^\2\2\u01a0\u01a2\7^\2\2\u01a1\u0193\3\2\2\2\u01a1\u0195")
        buf.write("\3\2\2\2\u01a1\u0197\3\2\2\2\u01a1\u0199\3\2\2\2\u01a1")
        buf.write("\u019b\3\2\2\2\u01a1\u019d\3\2\2\2\u01a1\u019f\3\2\2\2")
        buf.write("\u01a2z\3\2\2\2\u01a3\u01a8\n\b\2\2\u01a4\u01a8\5y=\2")
        buf.write("\u01a5\u01a6\7^\2\2\u01a6\u01a8\7$\2\2\u01a7\u01a3\3\2")
        buf.write("\2\2\u01a7\u01a4\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8|\3")
        buf.write("\2\2\2\u01a9\u01ab\t\t\2\2\u01aa\u01a9\3\2\2\2\u01ab\u01ac")
        buf.write("\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad")
        buf.write("\u01ae\3\2\2\2\u01ae\u01af\b?\3\2\u01af~\3\2\2\2\u01b0")
        buf.write("\u01b4\7$\2\2\u01b1\u01b3\5{>\2\u01b2\u01b1\3\2\2\2\u01b3")
        buf.write("\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2")
        buf.write("\u01b5\u01b7\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b7\u01b8\b")
        buf.write("@\4\2\u01b8\u0080\3\2\2\2\u01b9\u01bf\7$\2\2\u01ba\u01bb")
        buf.write("\7^\2\2\u01bb\u01be\t\n\2\2\u01bc\u01be\n\b\2\2\u01bd")
        buf.write("\u01ba\3\2\2\2\u01bd\u01bc\3\2\2\2\u01be\u01c1\3\2\2\2")
        buf.write("\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c2\3")
        buf.write("\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c3\7^\2\2\u01c3\u01c4")
        buf.write("\n\n\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c6\bA\5\2\u01c6")
        buf.write("\u0082\3\2\2\2\u01c7\u01c8\13\2\2\2\u01c8\u01c9\bB\6\2")
        buf.write("\u01c9\u0084\3\2\2\2\26\2\u0141\u0148\u014c\u0152\u015e")
        buf.write("\u016c\u0170\u0178\u017f\u0182\u0187\u018c\u0191\u01a1")
        buf.write("\u01a7\u01ac\u01b4\u01bd\u01bf\7\3\66\2\b\2\2\3@\3\3A")
        buf.write("\4\3B\5")
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
    AND = 28
    OR = 29
    EQ = 30
    ASSIGN = 31
    NEQ = 32
    LEQ = 33
    GEQ = 34
    DIFF = 35
    DECLARE = 36
    LE = 37
    GE = 38
    CONCAT = 39
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
    INTLIT = 51
    FLOATLIT = 52
    STRINGLIT = 53
    BLOCKCMT = 54
    LINECMT = 55
    ID = 56
    ATIDENTIFIER = 57
    WS = 58
    UNCLOSED_STRING = 59
    ILLEGAL_ESCAPE = 60
    ERROR_CHAR = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<-'", "'break'", "'continue'", "'if'", "'else'", "'for'", 
            "'true'", "'false'", "'int'", "'float'", "'bool'", "'string'", 
            "'return'", "'null'", "'class'", "'constructor'", "'var'", "'self'", 
            "'new'", "'void'", "'const'", "'func'", "'+'", "'-'", "'*'", 
            "'/'", "'\\'", "'&&'", "'||'", "'=='", "':='", "'!='", "'<='", 
            "'>='", "'!'", "'='", "'<'", "'>'", "'^'", "'%'", "'('", "')'", 
            "'['", "']'", "'.'", "','", "';'", "':'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", 
            "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
            "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", "PLUS", "MINUS", 
            "MULTIPLY", "DIVIDE_FLOAT", "DIVIDE_INT", "AND", "OR", "EQ", 
            "ASSIGN", "NEQ", "LEQ", "GEQ", "DIFF", "DECLARE", "LE", "GE", 
            "CONCAT", "MOD", "LRB", "RRB", "LSB", "RSB", "DOT", "CM", "SM", 
            "COLON", "LCB", "RCB", "INTLIT", "FLOATLIT", "STRINGLIT", "BLOCKCMT", 
            "LINECMT", "ID", "ATIDENTIFIER", "WS", "UNCLOSED_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", 
                  "FALSE", "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", 
                  "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", 
                  "CONST", "FUNC", "PLUS", "MINUS", "MULTIPLY", "DIVIDE_FLOAT", 
                  "DIVIDE_INT", "AND", "OR", "EQ", "ASSIGN", "NEQ", "LEQ", 
                  "GEQ", "DIFF", "DECLARE", "LE", "GE", "CONCAT", "MOD", 
                  "LRB", "RRB", "LSB", "RSB", "DOT", "CM", "SM", "COLON", 
                  "LCB", "RCB", "INTLIT", "FLOATLIT", "STRINGLIT", "BLOCKCMT", 
                  "LINECMT", "ID", "ATIDENTIFIER", "DEC", "EXP", "ESCAPESEQ", 
                  "CHAR_LIT", "WS", "UNCLOSED_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

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
            actions[52] = self.STRINGLIT_action 
            actions[62] = self.UNCLOSED_STRING_action 
            actions[63] = self.ILLEGAL_ESCAPE_action 
            actions[64] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSED_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:]; raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:]; raise IllegalEscape(self.text)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


