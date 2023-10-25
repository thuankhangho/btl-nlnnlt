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
        buf.write("\u01cf\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/")
        buf.write("\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\7\64\u0145\n\64\f\64\16\64\u0148\13\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\7\65\u0153\n")
        buf.write("\65\f\65\16\65\u0156\13\65\3\65\5\65\u0159\n\65\3\65\3")
        buf.write("\65\3\66\3\66\7\66\u015f\n\66\f\66\16\66\u0162\13\66\3")
        buf.write("\67\3\67\6\67\u0166\n\67\r\67\16\67\u0167\38\68\u016b")
        buf.write("\n8\r8\168\u016c\39\39\39\39\39\59\u0174\n9\39\39\59\u0178")
        buf.write("\n9\3:\6:\u017b\n:\r:\16:\u017c\3;\3;\7;\u0181\n;\f;\16")
        buf.write(";\u0184\13;\3<\3<\5<\u0188\n<\3<\6<\u018b\n<\r<\16<\u018c")
        buf.write("\3=\3=\7=\u0191\n=\f=\16=\u0194\13=\3=\3=\3=\3>\3>\3>")
        buf.write("\3>\5>\u019d\n>\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3")
        buf.write("?\3?\5?\u01ad\n?\3@\6@\u01b0\n@\r@\16@\u01b1\3@\3@\3A")
        buf.write("\3A\7A\u01b8\nA\fA\16A\u01bb\13A\3A\3A\3B\3B\3B\3B\7B")
        buf.write("\u01c3\nB\fB\16B\u01c6\13B\3B\3B\3B\3B\3B\3C\3C\3C\4\u0146")
        buf.write("\u0154\2D\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s\2u\2w\2y;{\2}\2\177<\u0081=\u0083>\u0085?\3")
        buf.write("\2\f\3\3\f\f\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGg")
        buf.write("g\4\2--//\t\2\f\f\17\17$$))GHQQ^^\5\2\13\f\17\17\"\"\t")
        buf.write("\2))^^ddhhppttvv\6\2\f\f\17\17$$^^\2\u01e1\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2y")
        buf.write("\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2")
        buf.write("\2\u0085\3\2\2\2\3\u0087\3\2\2\2\5\u008a\3\2\2\2\7\u0090")
        buf.write("\3\2\2\2\t\u0095\3\2\2\2\13\u009c\3\2\2\2\r\u00a0\3\2")
        buf.write("\2\2\17\u00a5\3\2\2\2\21\u00ae\3\2\2\2\23\u00b4\3\2\2")
        buf.write("\2\25\u00bb\3\2\2\2\27\u00c0\3\2\2\2\31\u00c3\3\2\2\2")
        buf.write("\33\u00c7\3\2\2\2\35\u00cc\3\2\2\2\37\u00d0\3\2\2\2!\u00d5")
        buf.write("\3\2\2\2#\u00db\3\2\2\2%\u00e1\3\2\2\2\'\u00e6\3\2\2\2")
        buf.write(")\u00ea\3\2\2\2+\u00ef\3\2\2\2-\u00fb\3\2\2\2/\u0101\3")
        buf.write("\2\2\2\61\u0103\3\2\2\2\63\u0105\3\2\2\2\65\u0107\3\2")
        buf.write("\2\2\67\u0109\3\2\2\29\u010b\3\2\2\2;\u010d\3\2\2\2=\u0110")
        buf.write("\3\2\2\2?\u0113\3\2\2\2A\u0116\3\2\2\2C\u0118\3\2\2\2")
        buf.write("E\u011b\3\2\2\2G\u011d\3\2\2\2I\u0120\3\2\2\2K\u0122\3")
        buf.write("\2\2\2M\u0125\3\2\2\2O\u0128\3\2\2\2Q\u012a\3\2\2\2S\u012c")
        buf.write("\3\2\2\2U\u012e\3\2\2\2W\u0130\3\2\2\2Y\u0132\3\2\2\2")
        buf.write("[\u0134\3\2\2\2]\u0136\3\2\2\2_\u0138\3\2\2\2a\u013a\3")
        buf.write("\2\2\2c\u013c\3\2\2\2e\u013e\3\2\2\2g\u0140\3\2\2\2i\u014e")
        buf.write("\3\2\2\2k\u015c\3\2\2\2m\u0163\3\2\2\2o\u016a\3\2\2\2")
        buf.write("q\u0177\3\2\2\2s\u017a\3\2\2\2u\u017e\3\2\2\2w\u0185\3")
        buf.write("\2\2\2y\u018e\3\2\2\2{\u019c\3\2\2\2}\u01ac\3\2\2\2\177")
        buf.write("\u01af\3\2\2\2\u0081\u01b5\3\2\2\2\u0083\u01be\3\2\2\2")
        buf.write("\u0085\u01cc\3\2\2\2\u0087\u0088\7>\2\2\u0088\u0089\7")
        buf.write("/\2\2\u0089\4\3\2\2\2\u008a\u008b\7d\2\2\u008b\u008c\7")
        buf.write("t\2\2\u008c\u008d\7g\2\2\u008d\u008e\7c\2\2\u008e\u008f")
        buf.write("\7m\2\2\u008f\6\3\2\2\2\u0090\u0091\7v\2\2\u0091\u0092")
        buf.write("\7t\2\2\u0092\u0093\7w\2\2\u0093\u0094\7g\2\2\u0094\b")
        buf.write("\3\2\2\2\u0095\u0096\7u\2\2\u0096\u0097\7v\2\2\u0097\u0098")
        buf.write("\7t\2\2\u0098\u0099\7k\2\2\u0099\u009a\7p\2\2\u009a\u009b")
        buf.write("\7i\2\2\u009b\n\3\2\2\2\u009c\u009d\7x\2\2\u009d\u009e")
        buf.write("\7c\2\2\u009e\u009f\7t\2\2\u009f\f\3\2\2\2\u00a0\u00a1")
        buf.write("\7h\2\2\u00a1\u00a2\7w\2\2\u00a2\u00a3\7p\2\2\u00a3\u00a4")
        buf.write("\7e\2\2\u00a4\16\3\2\2\2\u00a5\u00a6\7e\2\2\u00a6\u00a7")
        buf.write("\7q\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa")
        buf.write("\7k\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad")
        buf.write("\7g\2\2\u00ad\20\3\2\2\2\u00ae\u00af\7h\2\2\u00af\u00b0")
        buf.write("\7c\2\2\u00b0\u00b1\7n\2\2\u00b1\u00b2\7u\2\2\u00b2\u00b3")
        buf.write("\7g\2\2\u00b3\22\3\2\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6")
        buf.write("\7g\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8\7w\2\2\u00b8\u00b9")
        buf.write("\7t\2\2\u00b9\u00ba\7p\2\2\u00ba\24\3\2\2\2\u00bb\u00bc")
        buf.write("\7u\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be\7n\2\2\u00be\u00bf")
        buf.write("\7h\2\2\u00bf\26\3\2\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2")
        buf.write("\7h\2\2\u00c2\30\3\2\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5")
        buf.write("\7p\2\2\u00c5\u00c6\7v\2\2\u00c6\32\3\2\2\2\u00c7\u00c8")
        buf.write("\7p\2\2\u00c8\u00c9\7w\2\2\u00c9\u00ca\7n\2\2\u00ca\u00cb")
        buf.write("\7n\2\2\u00cb\34\3\2\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce")
        buf.write("\7g\2\2\u00ce\u00cf\7y\2\2\u00cf\36\3\2\2\2\u00d0\u00d1")
        buf.write("\7g\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7u\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4 \3\2\2\2\u00d5\u00d6\7h\2\2\u00d6\u00d7")
        buf.write("\7n\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7c\2\2\u00d9\u00da")
        buf.write("\7v\2\2\u00da\"\3\2\2\2\u00db\u00dc\7e\2\2\u00dc\u00dd")
        buf.write("\7n\2\2\u00dd\u00de\7c\2\2\u00de\u00df\7u\2\2\u00df\u00e0")
        buf.write("\7u\2\2\u00e0$\3\2\2\2\u00e1\u00e2\7x\2\2\u00e2\u00e3")
        buf.write("\7q\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5\7f\2\2\u00e5&\3")
        buf.write("\2\2\2\u00e6\u00e7\7h\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9")
        buf.write("\7t\2\2\u00e9(\3\2\2\2\u00ea\u00eb\7d\2\2\u00eb\u00ec")
        buf.write("\7q\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee\7n\2\2\u00ee*\3")
        buf.write("\2\2\2\u00ef\u00f0\7e\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2")
        buf.write("\7p\2\2\u00f2\u00f3\7u\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5")
        buf.write("\7t\2\2\u00f5\u00f6\7w\2\2\u00f6\u00f7\7e\2\2\u00f7\u00f8")
        buf.write("\7v\2\2\u00f8\u00f9\7q\2\2\u00f9\u00fa\7t\2\2\u00fa,\3")
        buf.write("\2\2\2\u00fb\u00fc\7e\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe")
        buf.write("\7p\2\2\u00fe\u00ff\7u\2\2\u00ff\u0100\7v\2\2\u0100.\3")
        buf.write("\2\2\2\u0101\u0102\7-\2\2\u0102\60\3\2\2\2\u0103\u0104")
        buf.write("\7/\2\2\u0104\62\3\2\2\2\u0105\u0106\7,\2\2\u0106\64\3")
        buf.write("\2\2\2\u0107\u0108\7\61\2\2\u0108\66\3\2\2\2\u0109\u010a")
        buf.write("\7^\2\2\u010a8\3\2\2\2\u010b\u010c\7#\2\2\u010c:\3\2\2")
        buf.write("\2\u010d\u010e\7(\2\2\u010e\u010f\7(\2\2\u010f<\3\2\2")
        buf.write("\2\u0110\u0111\7~\2\2\u0111\u0112\7~\2\2\u0112>\3\2\2")
        buf.write("\2\u0113\u0114\7?\2\2\u0114\u0115\7?\2\2\u0115@\3\2\2")
        buf.write("\2\u0116\u0117\7?\2\2\u0117B\3\2\2\2\u0118\u0119\7#\2")
        buf.write("\2\u0119\u011a\7?\2\2\u011aD\3\2\2\2\u011b\u011c\7>\2")
        buf.write("\2\u011cF\3\2\2\2\u011d\u011e\7>\2\2\u011e\u011f\7?\2")
        buf.write("\2\u011fH\3\2\2\2\u0120\u0121\7@\2\2\u0121J\3\2\2\2\u0122")
        buf.write("\u0123\7@\2\2\u0123\u0124\7?\2\2\u0124L\3\2\2\2\u0125")
        buf.write("\u0126\7<\2\2\u0126\u0127\7?\2\2\u0127N\3\2\2\2\u0128")
        buf.write("\u0129\7`\2\2\u0129P\3\2\2\2\u012a\u012b\7\'\2\2\u012b")
        buf.write("R\3\2\2\2\u012c\u012d\7*\2\2\u012dT\3\2\2\2\u012e\u012f")
        buf.write("\7+\2\2\u012fV\3\2\2\2\u0130\u0131\7]\2\2\u0131X\3\2\2")
        buf.write("\2\u0132\u0133\7_\2\2\u0133Z\3\2\2\2\u0134\u0135\7\60")
        buf.write("\2\2\u0135\\\3\2\2\2\u0136\u0137\7.\2\2\u0137^\3\2\2\2")
        buf.write("\u0138\u0139\7=\2\2\u0139`\3\2\2\2\u013a\u013b\7<\2\2")
        buf.write("\u013bb\3\2\2\2\u013c\u013d\7}\2\2\u013dd\3\2\2\2\u013e")
        buf.write("\u013f\7\177\2\2\u013ff\3\2\2\2\u0140\u0141\7\61\2\2\u0141")
        buf.write("\u0142\7,\2\2\u0142\u0146\3\2\2\2\u0143\u0145\13\2\2\2")
        buf.write("\u0144\u0143\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0147\3")
        buf.write("\2\2\2\u0146\u0144\3\2\2\2\u0147\u0149\3\2\2\2\u0148\u0146")
        buf.write("\3\2\2\2\u0149\u014a\7,\2\2\u014a\u014b\7\61\2\2\u014b")
        buf.write("\u014c\3\2\2\2\u014c\u014d\b\64\2\2\u014dh\3\2\2\2\u014e")
        buf.write("\u014f\7\61\2\2\u014f\u0150\7\61\2\2\u0150\u0154\3\2\2")
        buf.write("\2\u0151\u0153\13\2\2\2\u0152\u0151\3\2\2\2\u0153\u0156")
        buf.write("\3\2\2\2\u0154\u0155\3\2\2\2\u0154\u0152\3\2\2\2\u0155")
        buf.write("\u0158\3\2\2\2\u0156\u0154\3\2\2\2\u0157\u0159\t\2\2\2")
        buf.write("\u0158\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015b\b")
        buf.write("\65\2\2\u015bj\3\2\2\2\u015c\u0160\t\3\2\2\u015d\u015f")
        buf.write("\t\4\2\2\u015e\u015d\3\2\2\2\u015f\u0162\3\2\2\2\u0160")
        buf.write("\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161l\3\2\2\2\u0162")
        buf.write("\u0160\3\2\2\2\u0163\u0165\7B\2\2\u0164\u0166\t\4\2\2")
        buf.write("\u0165\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0165\3")
        buf.write("\2\2\2\u0167\u0168\3\2\2\2\u0168n\3\2\2\2\u0169\u016b")
        buf.write("\t\5\2\2\u016a\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016dp\3\2\2\2\u016e")
        buf.write("\u016f\5s:\2\u016f\u0170\5u;\2\u0170\u0178\3\2\2\2\u0171")
        buf.write("\u0173\5s:\2\u0172\u0174\5u;\2\u0173\u0172\3\2\2\2\u0173")
        buf.write("\u0174\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\5w<\2\u0176")
        buf.write("\u0178\3\2\2\2\u0177\u016e\3\2\2\2\u0177\u0171\3\2\2\2")
        buf.write("\u0178r\3\2\2\2\u0179\u017b\t\5\2\2\u017a\u0179\3\2\2")
        buf.write("\2\u017b\u017c\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d")
        buf.write("\3\2\2\2\u017dt\3\2\2\2\u017e\u0182\7\60\2\2\u017f\u0181")
        buf.write("\t\5\2\2\u0180\u017f\3\2\2\2\u0181\u0184\3\2\2\2\u0182")
        buf.write("\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183v\3\2\2\2\u0184")
        buf.write("\u0182\3\2\2\2\u0185\u0187\t\6\2\2\u0186\u0188\t\7\2\2")
        buf.write("\u0187\u0186\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u018a\3")
        buf.write("\2\2\2\u0189\u018b\t\5\2\2\u018a\u0189\3\2\2\2\u018b\u018c")
        buf.write("\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d")
        buf.write("x\3\2\2\2\u018e\u0192\7$\2\2\u018f\u0191\5{>\2\u0190\u018f")
        buf.write("\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3\2\2\2\u0192")
        buf.write("\u0193\3\2\2\2\u0193\u0195\3\2\2\2\u0194\u0192\3\2\2\2")
        buf.write("\u0195\u0196\7$\2\2\u0196\u0197\b=\3\2\u0197z\3\2\2\2")
        buf.write("\u0198\u019d\n\b\2\2\u0199\u019d\5}?\2\u019a\u019b\7^")
        buf.write("\2\2\u019b\u019d\7$\2\2\u019c\u0198\3\2\2\2\u019c\u0199")
        buf.write("\3\2\2\2\u019c\u019a\3\2\2\2\u019d|\3\2\2\2\u019e\u019f")
        buf.write("\7^\2\2\u019f\u01ad\7d\2\2\u01a0\u01a1\7^\2\2\u01a1\u01ad")
        buf.write("\7h\2\2\u01a2\u01a3\7^\2\2\u01a3\u01ad\7t\2\2\u01a4\u01a5")
        buf.write("\7^\2\2\u01a5\u01ad\7p\2\2\u01a6\u01a7\7^\2\2\u01a7\u01ad")
        buf.write("\7v\2\2\u01a8\u01a9\7^\2\2\u01a9\u01ad\7$\2\2\u01aa\u01ab")
        buf.write("\7^\2\2\u01ab\u01ad\7^\2\2\u01ac\u019e\3\2\2\2\u01ac\u01a0")
        buf.write("\3\2\2\2\u01ac\u01a2\3\2\2\2\u01ac\u01a4\3\2\2\2\u01ac")
        buf.write("\u01a6\3\2\2\2\u01ac\u01a8\3\2\2\2\u01ac\u01aa\3\2\2\2")
        buf.write("\u01ad~\3\2\2\2\u01ae\u01b0\t\t\2\2\u01af\u01ae\3\2\2")
        buf.write("\2\u01b0\u01b1\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2")
        buf.write("\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b4\b@\2\2\u01b4")
        buf.write("\u0080\3\2\2\2\u01b5\u01b9\7$\2\2\u01b6\u01b8\5{>\2\u01b7")
        buf.write("\u01b6\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2")
        buf.write("\u01b9\u01ba\3\2\2\2\u01ba\u01bc\3\2\2\2\u01bb\u01b9\3")
        buf.write("\2\2\2\u01bc\u01bd\bA\4\2\u01bd\u0082\3\2\2\2\u01be\u01c4")
        buf.write("\7$\2\2\u01bf\u01c0\7^\2\2\u01c0\u01c3\t\n\2\2\u01c1\u01c3")
        buf.write("\n\13\2\2\u01c2\u01bf\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3")
        buf.write("\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2")
        buf.write("\u01c5\u01c7\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01c8\7")
        buf.write("^\2\2\u01c8\u01c9\n\n\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb")
        buf.write("\bB\5\2\u01cb\u0084\3\2\2\2\u01cc\u01cd\13\2\2\2\u01cd")
        buf.write("\u01ce\bC\6\2\u01ce\u0086\3\2\2\2\26\2\u0146\u0154\u0158")
        buf.write("\u0160\u0167\u016c\u0173\u0177\u017c\u0182\u0187\u018c")
        buf.write("\u0192\u019c\u01ac\u01b1\u01b9\u01c2\u01c4\7\b\2\2\3=")
        buf.write("\2\3A\3\3B\4\3C\5")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    BREAK = 2
    TRUE = 3
    STRING = 4
    VAR = 5
    FUNC = 6
    CONTINUE = 7
    FALSE = 8
    RETURN = 9
    SELF = 10
    IF = 11
    INT = 12
    NULL = 13
    NEW = 14
    ELSE = 15
    FLOAT = 16
    CLASS = 17
    VOID = 18
    FOR = 19
    BOOL = 20
    CONSTRUCTOR = 21
    CONST = 22
    PLUS = 23
    MINUS = 24
    MULTIPLE = 25
    DIVIDE_FLOAT = 26
    DIVIDE_INT = 27
    CHAMTHAN = 28
    AND = 29
    OR = 30
    EQUAL = 31
    DECLARE = 32
    DIFFER = 33
    SMOL = 34
    SMOL_EQUAL = 35
    BIG = 36
    BIG_EQUAL = 37
    ASSIGN = 38
    CONCAT = 39
    MOD = 40
    LB = 41
    RB = 42
    LS = 43
    RS = 44
    DOT = 45
    CM = 46
    SM = 47
    CL = 48
    LC = 49
    RC = 50
    BLOCK_COMMENT = 51
    LINE_COMMENT = 52
    IDENTIFIER = 53
    AT_ID = 54
    INTLIT = 55
    FLOATLIT = 56
    STRLIT = 57
    WS = 58
    UNCLOSE_STRING = 59
    ILLEGAL_ESCAPE = 60
    ERROR_CHAR = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<-'", "'break'", "'true'", "'string'", "'var'", "'func'", 
            "'continue'", "'false'", "'return'", "'self'", "'if'", "'int'", 
            "'null'", "'new'", "'else'", "'float'", "'class'", "'void'", 
            "'for'", "'bool'", "'constructor'", "'const'", "'+'", "'-'", 
            "'*'", "'/'", "'\\'", "'!'", "'&&'", "'||'", "'=='", "'='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "':='", "'^'", "'%'", 
            "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", "'{'", 
            "'}'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "TRUE", "STRING", "VAR", "FUNC", "CONTINUE", "FALSE", 
            "RETURN", "SELF", "IF", "INT", "NULL", "NEW", "ELSE", "FLOAT", 
            "CLASS", "VOID", "FOR", "BOOL", "CONSTRUCTOR", "CONST", "PLUS", 
            "MINUS", "MULTIPLE", "DIVIDE_FLOAT", "DIVIDE_INT", "CHAMTHAN", 
            "AND", "OR", "EQUAL", "DECLARE", "DIFFER", "SMOL", "SMOL_EQUAL", 
            "BIG", "BIG_EQUAL", "ASSIGN", "CONCAT", "MOD", "LB", "RB", "LS", 
            "RS", "DOT", "CM", "SM", "CL", "LC", "RC", "BLOCK_COMMENT", 
            "LINE_COMMENT", "IDENTIFIER", "AT_ID", "INTLIT", "FLOATLIT", 
            "STRLIT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "BREAK", "TRUE", "STRING", "VAR", "FUNC", "CONTINUE", 
                  "FALSE", "RETURN", "SELF", "IF", "INT", "NULL", "NEW", 
                  "ELSE", "FLOAT", "CLASS", "VOID", "FOR", "BOOL", "CONSTRUCTOR", 
                  "CONST", "PLUS", "MINUS", "MULTIPLE", "DIVIDE_FLOAT", 
                  "DIVIDE_INT", "CHAMTHAN", "AND", "OR", "EQUAL", "DECLARE", 
                  "DIFFER", "SMOL", "SMOL_EQUAL", "BIG", "BIG_EQUAL", "ASSIGN", 
                  "CONCAT", "MOD", "LB", "RB", "LS", "RS", "DOT", "CM", 
                  "SM", "CL", "LC", "RC", "BLOCK_COMMENT", "LINE_COMMENT", 
                  "IDENTIFIER", "AT_ID", "INTLIT", "FLOATLIT", "INTPART", 
                  "DEC", "EXP", "STRLIT", "CHARS", "ESC_SEQ", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[59] = self.STRLIT_action 
            actions[63] = self.UNCLOSE_STRING_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
            actions[65] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text=self.text[1:]; raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:]; raise IllegalEscape(self.text)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


