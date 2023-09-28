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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u01d3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\6\64")
        buf.write("\u0142\n\64\r\64\16\64\u0143\3\65\3\65\3\65\3\65\3\65")
        buf.write("\5\65\u014b\n\65\3\65\3\65\5\65\u014f\n\65\3\66\3\66\7")
        buf.write("\66\u0153\n\66\f\66\16\66\u0156\13\66\3\66\3\66\3\66\3")
        buf.write("\67\3\67\3\67\3\67\3\67\7\67\u0160\n\67\f\67\16\67\u0163")
        buf.write("\13\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\7")
        buf.write("8\u0170\n8\f8\168\u0173\138\38\58\u0176\n8\38\38\39\3")
        buf.write("9\79\u017c\n9\f9\169\u017f\139\3:\3:\6:\u0183\n:\r:\16")
        buf.write(":\u0184\3;\3;\7;\u0189\n;\f;\16;\u018c\13;\3<\5<\u018f")
        buf.write("\n<\3<\6<\u0192\n<\r<\16<\u0193\3=\3=\3=\6=\u0199\n=\r")
        buf.write("=\16=\u019a\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>")
        buf.write("\5>\u01ab\n>\3?\3?\3?\3?\5?\u01b1\n?\3@\6@\u01b4\n@\r")
        buf.write("@\16@\u01b5\3@\3@\3A\3A\7A\u01bc\nA\fA\16A\u01bf\13A\3")
        buf.write("A\3A\3B\3B\3B\3B\7B\u01c7\nB\fB\16B\u01ca\13B\3B\3B\3")
        buf.write("B\3B\3B\3C\3C\3C\4\u0161\u0171\2D\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u<w\2y\2{\2}\2\177=\u0081")
        buf.write(">\u0083?\u0085@\3\2\r\3\2\62;\3\3\f\f\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2\63;\4\2GGgg\4\2--//\t\2\f\f\17\17$$))GHQ")
        buf.write("Q^^\5\2\13\f\17\17\"\"\t\2))^^ddhhppttvv\6\2\f\f\17\17")
        buf.write("$$^^\2\u01e6\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\3\u0087")
        buf.write("\3\2\2\2\5\u008a\3\2\2\2\7\u0090\3\2\2\2\t\u0099\3\2\2")
        buf.write("\2\13\u009c\3\2\2\2\r\u00a1\3\2\2\2\17\u00a5\3\2\2\2\21")
        buf.write("\u00aa\3\2\2\2\23\u00b0\3\2\2\2\25\u00b4\3\2\2\2\27\u00ba")
        buf.write("\3\2\2\2\31\u00bf\3\2\2\2\33\u00c6\3\2\2\2\35\u00cd\3")
        buf.write("\2\2\2\37\u00d2\3\2\2\2!\u00d8\3\2\2\2#\u00e4\3\2\2\2")
        buf.write("%\u00e8\3\2\2\2\'\u00ed\3\2\2\2)\u00f1\3\2\2\2+\u00f6")
        buf.write("\3\2\2\2-\u00fc\3\2\2\2/\u0101\3\2\2\2\61\u0103\3\2\2")
        buf.write("\2\63\u0105\3\2\2\2\65\u0107\3\2\2\2\67\u0109\3\2\2\2")
        buf.write("9\u010b\3\2\2\2;\u010e\3\2\2\2=\u0111\3\2\2\2?\u0114\3")
        buf.write("\2\2\2A\u0117\3\2\2\2C\u011a\3\2\2\2E\u011d\3\2\2\2G\u0120")
        buf.write("\3\2\2\2I\u0122\3\2\2\2K\u0124\3\2\2\2M\u0126\3\2\2\2")
        buf.write("O\u0128\3\2\2\2Q\u012a\3\2\2\2S\u012c\3\2\2\2U\u012e\3")
        buf.write("\2\2\2W\u0130\3\2\2\2Y\u0132\3\2\2\2[\u0134\3\2\2\2]\u0136")
        buf.write("\3\2\2\2_\u0138\3\2\2\2a\u013a\3\2\2\2c\u013c\3\2\2\2")
        buf.write("e\u013e\3\2\2\2g\u0141\3\2\2\2i\u014e\3\2\2\2k\u0150\3")
        buf.write("\2\2\2m\u015a\3\2\2\2o\u016a\3\2\2\2q\u0179\3\2\2\2s\u0180")
        buf.write("\3\2\2\2u\u0186\3\2\2\2w\u018e\3\2\2\2y\u0195\3\2\2\2")
        buf.write("{\u01aa\3\2\2\2}\u01b0\3\2\2\2\177\u01b3\3\2\2\2\u0081")
        buf.write("\u01b9\3\2\2\2\u0083\u01c2\3\2\2\2\u0085\u01d0\3\2\2\2")
        buf.write("\u0087\u0088\7>\2\2\u0088\u0089\7/\2\2\u0089\4\3\2\2\2")
        buf.write("\u008a\u008b\7d\2\2\u008b\u008c\7t\2\2\u008c\u008d\7g")
        buf.write("\2\2\u008d\u008e\7c\2\2\u008e\u008f\7m\2\2\u008f\6\3\2")
        buf.write("\2\2\u0090\u0091\7e\2\2\u0091\u0092\7q\2\2\u0092\u0093")
        buf.write("\7p\2\2\u0093\u0094\7v\2\2\u0094\u0095\7k\2\2\u0095\u0096")
        buf.write("\7p\2\2\u0096\u0097\7w\2\2\u0097\u0098\7g\2\2\u0098\b")
        buf.write("\3\2\2\2\u0099\u009a\7k\2\2\u009a\u009b\7h\2\2\u009b\n")
        buf.write("\3\2\2\2\u009c\u009d\7g\2\2\u009d\u009e\7n\2\2\u009e\u009f")
        buf.write("\7u\2\2\u009f\u00a0\7g\2\2\u00a0\f\3\2\2\2\u00a1\u00a2")
        buf.write("\7h\2\2\u00a2\u00a3\7q\2\2\u00a3\u00a4\7t\2\2\u00a4\16")
        buf.write("\3\2\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8")
        buf.write("\7w\2\2\u00a8\u00a9\7g\2\2\u00a9\20\3\2\2\2\u00aa\u00ab")
        buf.write("\7h\2\2\u00ab\u00ac\7c\2\2\u00ac\u00ad\7n\2\2\u00ad\u00ae")
        buf.write("\7u\2\2\u00ae\u00af\7g\2\2\u00af\22\3\2\2\2\u00b0\u00b1")
        buf.write("\7k\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3\7v\2\2\u00b3\24")
        buf.write("\3\2\2\2\u00b4\u00b5\7h\2\2\u00b5\u00b6\7n\2\2\u00b6\u00b7")
        buf.write("\7q\2\2\u00b7\u00b8\7c\2\2\u00b8\u00b9\7v\2\2\u00b9\26")
        buf.write("\3\2\2\2\u00ba\u00bb\7d\2\2\u00bb\u00bc\7q\2\2\u00bc\u00bd")
        buf.write("\7q\2\2\u00bd\u00be\7n\2\2\u00be\30\3\2\2\2\u00bf\u00c0")
        buf.write("\7u\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3")
        buf.write("\7k\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5\7i\2\2\u00c5\32")
        buf.write("\3\2\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9")
        buf.write("\7v\2\2\u00c9\u00ca\7w\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\34\3\2\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf")
        buf.write("\7w\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1\7n\2\2\u00d1\36")
        buf.write("\3\2\2\2\u00d2\u00d3\7e\2\2\u00d3\u00d4\7n\2\2\u00d4\u00d5")
        buf.write("\7c\2\2\u00d5\u00d6\7u\2\2\u00d6\u00d7\7u\2\2\u00d7 \3")
        buf.write("\2\2\2\u00d8\u00d9\7e\2\2\u00d9\u00da\7q\2\2\u00da\u00db")
        buf.write("\7p\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd\7v\2\2\u00dd\u00de")
        buf.write("\7t\2\2\u00de\u00df\7w\2\2\u00df\u00e0\7e\2\2\u00e0\u00e1")
        buf.write("\7v\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3\7t\2\2\u00e3\"")
        buf.write("\3\2\2\2\u00e4\u00e5\7x\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7")
        buf.write("\7t\2\2\u00e7$\3\2\2\2\u00e8\u00e9\7u\2\2\u00e9\u00ea")
        buf.write("\7g\2\2\u00ea\u00eb\7n\2\2\u00eb\u00ec\7h\2\2\u00ec&\3")
        buf.write("\2\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0")
        buf.write("\7y\2\2\u00f0(\3\2\2\2\u00f1\u00f2\7x\2\2\u00f2\u00f3")
        buf.write("\7q\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7f\2\2\u00f5*\3")
        buf.write("\2\2\2\u00f6\u00f7\7e\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9")
        buf.write("\7p\2\2\u00f9\u00fa\7u\2\2\u00fa\u00fb\7v\2\2\u00fb,\3")
        buf.write("\2\2\2\u00fc\u00fd\7h\2\2\u00fd\u00fe\7w\2\2\u00fe\u00ff")
        buf.write("\7p\2\2\u00ff\u0100\7e\2\2\u0100.\3\2\2\2\u0101\u0102")
        buf.write("\7-\2\2\u0102\60\3\2\2\2\u0103\u0104\7/\2\2\u0104\62\3")
        buf.write("\2\2\2\u0105\u0106\7,\2\2\u0106\64\3\2\2\2\u0107\u0108")
        buf.write("\7\61\2\2\u0108\66\3\2\2\2\u0109\u010a\7^\2\2\u010a8\3")
        buf.write("\2\2\2\u010b\u010c\7(\2\2\u010c\u010d\7(\2\2\u010d:\3")
        buf.write("\2\2\2\u010e\u010f\7~\2\2\u010f\u0110\7~\2\2\u0110<\3")
        buf.write("\2\2\2\u0111\u0112\7?\2\2\u0112\u0113\7?\2\2\u0113>\3")
        buf.write("\2\2\2\u0114\u0115\7<\2\2\u0115\u0116\7?\2\2\u0116@\3")
        buf.write("\2\2\2\u0117\u0118\7#\2\2\u0118\u0119\7?\2\2\u0119B\3")
        buf.write("\2\2\2\u011a\u011b\7>\2\2\u011b\u011c\7?\2\2\u011cD\3")
        buf.write("\2\2\2\u011d\u011e\7@\2\2\u011e\u011f\7?\2\2\u011fF\3")
        buf.write("\2\2\2\u0120\u0121\7#\2\2\u0121H\3\2\2\2\u0122\u0123\7")
        buf.write("?\2\2\u0123J\3\2\2\2\u0124\u0125\7>\2\2\u0125L\3\2\2\2")
        buf.write("\u0126\u0127\7@\2\2\u0127N\3\2\2\2\u0128\u0129\7`\2\2")
        buf.write("\u0129P\3\2\2\2\u012a\u012b\7\'\2\2\u012bR\3\2\2\2\u012c")
        buf.write("\u012d\7*\2\2\u012dT\3\2\2\2\u012e\u012f\7+\2\2\u012f")
        buf.write("V\3\2\2\2\u0130\u0131\7]\2\2\u0131X\3\2\2\2\u0132\u0133")
        buf.write("\7_\2\2\u0133Z\3\2\2\2\u0134\u0135\7\60\2\2\u0135\\\3")
        buf.write("\2\2\2\u0136\u0137\7.\2\2\u0137^\3\2\2\2\u0138\u0139\7")
        buf.write("=\2\2\u0139`\3\2\2\2\u013a\u013b\7<\2\2\u013bb\3\2\2\2")
        buf.write("\u013c\u013d\7}\2\2\u013dd\3\2\2\2\u013e\u013f\7\177\2")
        buf.write("\2\u013ff\3\2\2\2\u0140\u0142\t\2\2\2\u0141\u0140\3\2")
        buf.write("\2\2\u0142\u0143\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144")
        buf.write("\3\2\2\2\u0144h\3\2\2\2\u0145\u0146\5g\64\2\u0146\u0147")
        buf.write("\5w<\2\u0147\u014f\3\2\2\2\u0148\u014a\5g\64\2\u0149\u014b")
        buf.write("\5w<\2\u014a\u0149\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014c")
        buf.write("\3\2\2\2\u014c\u014d\5y=\2\u014d\u014f\3\2\2\2\u014e\u0145")
        buf.write("\3\2\2\2\u014e\u0148\3\2\2\2\u014fj\3\2\2\2\u0150\u0154")
        buf.write("\7$\2\2\u0151\u0153\5}?\2\u0152\u0151\3\2\2\2\u0153\u0156")
        buf.write("\3\2\2\2\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155")
        buf.write("\u0157\3\2\2\2\u0156\u0154\3\2\2\2\u0157\u0158\7$\2\2")
        buf.write("\u0158\u0159\b\66\2\2\u0159l\3\2\2\2\u015a\u015b\7\61")
        buf.write("\2\2\u015b\u015c\7\61\2\2\u015c\u015d\7,\2\2\u015d\u0161")
        buf.write("\3\2\2\2\u015e\u0160\13\2\2\2\u015f\u015e\3\2\2\2\u0160")
        buf.write("\u0163\3\2\2\2\u0161\u0162\3\2\2\2\u0161\u015f\3\2\2\2")
        buf.write("\u0162\u0164\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0165\7")
        buf.write(",\2\2\u0165\u0166\7\61\2\2\u0166\u0167\7\61\2\2\u0167")
        buf.write("\u0168\3\2\2\2\u0168\u0169\b\67\3\2\u0169n\3\2\2\2\u016a")
        buf.write("\u016b\7\61\2\2\u016b\u016c\7\61\2\2\u016c\u016d\7\61")
        buf.write("\2\2\u016d\u0171\3\2\2\2\u016e\u0170\13\2\2\2\u016f\u016e")
        buf.write("\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u0172\3\2\2\2\u0171")
        buf.write("\u016f\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2")
        buf.write("\u0174\u0176\t\3\2\2\u0175\u0174\3\2\2\2\u0176\u0177\3")
        buf.write("\2\2\2\u0177\u0178\b8\3\2\u0178p\3\2\2\2\u0179\u017d\t")
        buf.write("\4\2\2\u017a\u017c\t\5\2\2\u017b\u017a\3\2\2\2\u017c\u017f")
        buf.write("\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e")
        buf.write("r\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0182\7B\2\2\u0181")
        buf.write("\u0183\t\5\2\2\u0182\u0181\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185t\3\2\2")
        buf.write("\2\u0186\u018a\t\6\2\2\u0187\u0189\t\2\2\2\u0188\u0187")
        buf.write("\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u0188\3\2\2\2\u018a")
        buf.write("\u018b\3\2\2\2\u018bv\3\2\2\2\u018c\u018a\3\2\2\2\u018d")
        buf.write("\u018f\7\60\2\2\u018e\u018d\3\2\2\2\u018e\u018f\3\2\2")
        buf.write("\2\u018f\u0191\3\2\2\2\u0190\u0192\t\2\2\2\u0191\u0190")
        buf.write("\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0191\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194x\3\2\2\2\u0195\u0196\t\7\2\2\u0196")
        buf.write("\u0198\t\b\2\2\u0197\u0199\t\2\2\2\u0198\u0197\3\2\2\2")
        buf.write("\u0199\u019a\3\2\2\2\u019a\u0198\3\2\2\2\u019a\u019b\3")
        buf.write("\2\2\2\u019bz\3\2\2\2\u019c\u019d\7^\2\2\u019d\u01ab\7")
        buf.write("d\2\2\u019e\u019f\7^\2\2\u019f\u01ab\7h\2\2\u01a0\u01a1")
        buf.write("\7^\2\2\u01a1\u01ab\7t\2\2\u01a2\u01a3\7^\2\2\u01a3\u01ab")
        buf.write("\7p\2\2\u01a4\u01a5\7^\2\2\u01a5\u01ab\7v\2\2\u01a6\u01a7")
        buf.write("\7^\2\2\u01a7\u01ab\7$\2\2\u01a8\u01a9\7^\2\2\u01a9\u01ab")
        buf.write("\7^\2\2\u01aa\u019c\3\2\2\2\u01aa\u019e\3\2\2\2\u01aa")
        buf.write("\u01a0\3\2\2\2\u01aa\u01a2\3\2\2\2\u01aa\u01a4\3\2\2\2")
        buf.write("\u01aa\u01a6\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab|\3\2\2")
        buf.write("\2\u01ac\u01b1\n\t\2\2\u01ad\u01b1\5{>\2\u01ae\u01af\7")
        buf.write("^\2\2\u01af\u01b1\7$\2\2\u01b0\u01ac\3\2\2\2\u01b0\u01ad")
        buf.write("\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1~\3\2\2\2\u01b2\u01b4")
        buf.write("\t\n\2\2\u01b3\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5")
        buf.write("\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b7\3\2\2\2")
        buf.write("\u01b7\u01b8\b@\3\2\u01b8\u0080\3\2\2\2\u01b9\u01bd\7")
        buf.write("$\2\2\u01ba\u01bc\5}?\2\u01bb\u01ba\3\2\2\2\u01bc\u01bf")
        buf.write("\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be")
        buf.write("\u01c0\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0\u01c1\bA\4\2")
        buf.write("\u01c1\u0082\3\2\2\2\u01c2\u01c8\7$\2\2\u01c3\u01c4\7")
        buf.write("^\2\2\u01c4\u01c7\t\13\2\2\u01c5\u01c7\n\f\2\2\u01c6\u01c3")
        buf.write("\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8")
        buf.write("\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01cb\3\2\2\2")
        buf.write("\u01ca\u01c8\3\2\2\2\u01cb\u01cc\7^\2\2\u01cc\u01cd\n")
        buf.write("\13\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cf\bB\5\2\u01cf\u0084")
        buf.write("\3\2\2\2\u01d0\u01d1\13\2\2\2\u01d1\u01d2\bC\6\2\u01d2")
        buf.write("\u0086\3\2\2\2\26\2\u0143\u014a\u014e\u0154\u0161\u0171")
        buf.write("\u0175\u017d\u0184\u018a\u018e\u0193\u019a\u01aa\u01b0")
        buf.write("\u01b5\u01bd\u01c6\u01c8\7\3\66\2\b\2\2\3A\3\3B\4\3C\5")
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
    ARRAYSIZE = 58
    WS = 59
    UNCLOSED_STRING = 60
    ILLEGAL_ESCAPE = 61
    ERROR_CHAR = 62

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
            "LINECMT", "ID", "ATIDENTIFIER", "ARRAYSIZE", "WS", "UNCLOSED_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", 
                  "FALSE", "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", 
                  "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", 
                  "CONST", "FUNC", "PLUS", "MINUS", "MULTIPLY", "DIVIDE_FLOAT", 
                  "DIVIDE_INT", "AND", "OR", "EQ", "ASSIGN", "NEQ", "LEQ", 
                  "GEQ", "DIFF", "DECLARE", "LE", "GE", "CONCAT", "MOD", 
                  "LRB", "RRB", "LSB", "RSB", "DOT", "CM", "SM", "COLON", 
                  "LCB", "RCB", "INTLIT", "FLOATLIT", "STRINGLIT", "BLOCKCMT", 
                  "LINECMT", "ID", "ATIDENTIFIER", "ARRAYSIZE", "DEC", "EXP", 
                  "ESCAPESEQ", "CHAR_LIT", "WS", "UNCLOSED_STRING", "ILLEGAL_ESCAPE", 
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
            actions[63] = self.UNCLOSED_STRING_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
            actions[65] = self.ERROR_CHAR_action 
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
     


