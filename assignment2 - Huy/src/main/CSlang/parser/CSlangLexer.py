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
        buf.write("\u01d5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3")
        buf.write(".\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\64\3\64\7\64\u0147\n\64\f\64\16\64\u014a\13\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\7\65\u0155")
        buf.write("\n\65\f\65\16\65\u0158\13\65\3\65\5\65\u015b\n\65\3\65")
        buf.write("\3\65\3\66\3\66\7\66\u0161\n\66\f\66\16\66\u0164\13\66")
        buf.write("\3\67\3\67\6\67\u0168\n\67\r\67\16\67\u0169\38\68\u016d")
        buf.write("\n8\r8\168\u016e\39\39\39\39\39\59\u0176\n9\39\39\59\u017a")
        buf.write("\n9\3:\6:\u017d\n:\r:\16:\u017e\3;\3;\7;\u0183\n;\f;\16")
        buf.write(";\u0186\13;\3<\3<\5<\u018a\n<\3<\6<\u018d\n<\r<\16<\u018e")
        buf.write("\3=\3=\5=\u0193\n=\3>\3>\7>\u0197\n>\f>\16>\u019a\13>")
        buf.write("\3>\3>\3>\3?\3?\3?\3?\5?\u01a3\n?\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\3@\3@\3@\3@\3@\3@\3@\5@\u01b3\n@\3A\6A\u01b6\nA\rA\16")
        buf.write("A\u01b7\3A\3A\3B\3B\7B\u01be\nB\fB\16B\u01c1\13B\3B\3")
        buf.write("B\3C\3C\3C\3C\7C\u01c9\nC\fC\16C\u01cc\13C\3C\3C\3C\3")
        buf.write("C\3C\3D\3D\3D\4\u0148\u0156\2E\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s\2u\2w\2y;{<}\2\177\2\u0081")
        buf.write("=\u0083>\u0085?\u0087@\3\2\f\3\3\f\f\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2\62;\4\2GGgg\4\2--//\t\2\f\f\17\17$$))GHQ")
        buf.write("Q^^\5\2\13\f\17\17\"\"\t\2))^^ddhhppttvv\6\2\f\f\17\17")
        buf.write("$$^^\2\u01e8\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
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
        buf.write("o\3\2\2\2\2q\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2\u0081\3\2")
        buf.write("\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\3")
        buf.write("\u0089\3\2\2\2\5\u008c\3\2\2\2\7\u0092\3\2\2\2\t\u0097")
        buf.write("\3\2\2\2\13\u009e\3\2\2\2\r\u00a2\3\2\2\2\17\u00a7\3\2")
        buf.write("\2\2\21\u00b0\3\2\2\2\23\u00b6\3\2\2\2\25\u00bd\3\2\2")
        buf.write("\2\27\u00c2\3\2\2\2\31\u00c5\3\2\2\2\33\u00c9\3\2\2\2")
        buf.write("\35\u00ce\3\2\2\2\37\u00d2\3\2\2\2!\u00d7\3\2\2\2#\u00dd")
        buf.write("\3\2\2\2%\u00e3\3\2\2\2\'\u00e8\3\2\2\2)\u00ec\3\2\2\2")
        buf.write("+\u00f1\3\2\2\2-\u00fd\3\2\2\2/\u0103\3\2\2\2\61\u0105")
        buf.write("\3\2\2\2\63\u0107\3\2\2\2\65\u0109\3\2\2\2\67\u010b\3")
        buf.write("\2\2\29\u010d\3\2\2\2;\u010f\3\2\2\2=\u0112\3\2\2\2?\u0115")
        buf.write("\3\2\2\2A\u0118\3\2\2\2C\u011a\3\2\2\2E\u011d\3\2\2\2")
        buf.write("G\u011f\3\2\2\2I\u0122\3\2\2\2K\u0124\3\2\2\2M\u0127\3")
        buf.write("\2\2\2O\u012a\3\2\2\2Q\u012c\3\2\2\2S\u012e\3\2\2\2U\u0130")
        buf.write("\3\2\2\2W\u0132\3\2\2\2Y\u0134\3\2\2\2[\u0136\3\2\2\2")
        buf.write("]\u0138\3\2\2\2_\u013a\3\2\2\2a\u013c\3\2\2\2c\u013e\3")
        buf.write("\2\2\2e\u0140\3\2\2\2g\u0142\3\2\2\2i\u0150\3\2\2\2k\u015e")
        buf.write("\3\2\2\2m\u0165\3\2\2\2o\u016c\3\2\2\2q\u0179\3\2\2\2")
        buf.write("s\u017c\3\2\2\2u\u0180\3\2\2\2w\u0187\3\2\2\2y\u0192\3")
        buf.write("\2\2\2{\u0194\3\2\2\2}\u01a2\3\2\2\2\177\u01b2\3\2\2\2")
        buf.write("\u0081\u01b5\3\2\2\2\u0083\u01bb\3\2\2\2\u0085\u01c4\3")
        buf.write("\2\2\2\u0087\u01d2\3\2\2\2\u0089\u008a\7>\2\2\u008a\u008b")
        buf.write("\7/\2\2\u008b\4\3\2\2\2\u008c\u008d\7d\2\2\u008d\u008e")
        buf.write("\7t\2\2\u008e\u008f\7g\2\2\u008f\u0090\7c\2\2\u0090\u0091")
        buf.write("\7m\2\2\u0091\6\3\2\2\2\u0092\u0093\7v\2\2\u0093\u0094")
        buf.write("\7t\2\2\u0094\u0095\7w\2\2\u0095\u0096\7g\2\2\u0096\b")
        buf.write("\3\2\2\2\u0097\u0098\7u\2\2\u0098\u0099\7v\2\2\u0099\u009a")
        buf.write("\7t\2\2\u009a\u009b\7k\2\2\u009b\u009c\7p\2\2\u009c\u009d")
        buf.write("\7i\2\2\u009d\n\3\2\2\2\u009e\u009f\7x\2\2\u009f\u00a0")
        buf.write("\7c\2\2\u00a0\u00a1\7t\2\2\u00a1\f\3\2\2\2\u00a2\u00a3")
        buf.write("\7h\2\2\u00a3\u00a4\7w\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6")
        buf.write("\7e\2\2\u00a6\16\3\2\2\2\u00a7\u00a8\7e\2\2\u00a8\u00a9")
        buf.write("\7q\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac")
        buf.write("\7k\2\2\u00ac\u00ad\7p\2\2\u00ad\u00ae\7w\2\2\u00ae\u00af")
        buf.write("\7g\2\2\u00af\20\3\2\2\2\u00b0\u00b1\7h\2\2\u00b1\u00b2")
        buf.write("\7c\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4\7u\2\2\u00b4\u00b5")
        buf.write("\7g\2\2\u00b5\22\3\2\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8")
        buf.write("\7g\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba\7w\2\2\u00ba\u00bb")
        buf.write("\7t\2\2\u00bb\u00bc\7p\2\2\u00bc\24\3\2\2\2\u00bd\u00be")
        buf.write("\7u\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0\7n\2\2\u00c0\u00c1")
        buf.write("\7h\2\2\u00c1\26\3\2\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4")
        buf.write("\7h\2\2\u00c4\30\3\2\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7")
        buf.write("\7p\2\2\u00c7\u00c8\7v\2\2\u00c8\32\3\2\2\2\u00c9\u00ca")
        buf.write("\7p\2\2\u00ca\u00cb\7w\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd")
        buf.write("\7n\2\2\u00cd\34\3\2\2\2\u00ce\u00cf\7p\2\2\u00cf\u00d0")
        buf.write("\7g\2\2\u00d0\u00d1\7y\2\2\u00d1\36\3\2\2\2\u00d2\u00d3")
        buf.write("\7g\2\2\u00d3\u00d4\7n\2\2\u00d4\u00d5\7u\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6 \3\2\2\2\u00d7\u00d8\7h\2\2\u00d8\u00d9")
        buf.write("\7n\2\2\u00d9\u00da\7q\2\2\u00da\u00db\7c\2\2\u00db\u00dc")
        buf.write("\7v\2\2\u00dc\"\3\2\2\2\u00dd\u00de\7e\2\2\u00de\u00df")
        buf.write("\7n\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1\7u\2\2\u00e1\u00e2")
        buf.write("\7u\2\2\u00e2$\3\2\2\2\u00e3\u00e4\7x\2\2\u00e4\u00e5")
        buf.write("\7q\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7\7f\2\2\u00e7&\3")
        buf.write("\2\2\2\u00e8\u00e9\7h\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb")
        buf.write("\7t\2\2\u00eb(\3\2\2\2\u00ec\u00ed\7d\2\2\u00ed\u00ee")
        buf.write("\7q\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7n\2\2\u00f0*\3")
        buf.write("\2\2\2\u00f1\u00f2\7e\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4")
        buf.write("\7p\2\2\u00f4\u00f5\7u\2\2\u00f5\u00f6\7v\2\2\u00f6\u00f7")
        buf.write("\7t\2\2\u00f7\u00f8\7w\2\2\u00f8\u00f9\7e\2\2\u00f9\u00fa")
        buf.write("\7v\2\2\u00fa\u00fb\7q\2\2\u00fb\u00fc\7t\2\2\u00fc,\3")
        buf.write("\2\2\2\u00fd\u00fe\7e\2\2\u00fe\u00ff\7q\2\2\u00ff\u0100")
        buf.write("\7p\2\2\u0100\u0101\7u\2\2\u0101\u0102\7v\2\2\u0102.\3")
        buf.write("\2\2\2\u0103\u0104\7-\2\2\u0104\60\3\2\2\2\u0105\u0106")
        buf.write("\7/\2\2\u0106\62\3\2\2\2\u0107\u0108\7,\2\2\u0108\64\3")
        buf.write("\2\2\2\u0109\u010a\7\61\2\2\u010a\66\3\2\2\2\u010b\u010c")
        buf.write("\7^\2\2\u010c8\3\2\2\2\u010d\u010e\7#\2\2\u010e:\3\2\2")
        buf.write("\2\u010f\u0110\7(\2\2\u0110\u0111\7(\2\2\u0111<\3\2\2")
        buf.write("\2\u0112\u0113\7~\2\2\u0113\u0114\7~\2\2\u0114>\3\2\2")
        buf.write("\2\u0115\u0116\7?\2\2\u0116\u0117\7?\2\2\u0117@\3\2\2")
        buf.write("\2\u0118\u0119\7?\2\2\u0119B\3\2\2\2\u011a\u011b\7#\2")
        buf.write("\2\u011b\u011c\7?\2\2\u011cD\3\2\2\2\u011d\u011e\7>\2")
        buf.write("\2\u011eF\3\2\2\2\u011f\u0120\7>\2\2\u0120\u0121\7?\2")
        buf.write("\2\u0121H\3\2\2\2\u0122\u0123\7@\2\2\u0123J\3\2\2\2\u0124")
        buf.write("\u0125\7@\2\2\u0125\u0126\7?\2\2\u0126L\3\2\2\2\u0127")
        buf.write("\u0128\7<\2\2\u0128\u0129\7?\2\2\u0129N\3\2\2\2\u012a")
        buf.write("\u012b\7`\2\2\u012bP\3\2\2\2\u012c\u012d\7\'\2\2\u012d")
        buf.write("R\3\2\2\2\u012e\u012f\7*\2\2\u012fT\3\2\2\2\u0130\u0131")
        buf.write("\7+\2\2\u0131V\3\2\2\2\u0132\u0133\7]\2\2\u0133X\3\2\2")
        buf.write("\2\u0134\u0135\7_\2\2\u0135Z\3\2\2\2\u0136\u0137\7\60")
        buf.write("\2\2\u0137\\\3\2\2\2\u0138\u0139\7.\2\2\u0139^\3\2\2\2")
        buf.write("\u013a\u013b\7=\2\2\u013b`\3\2\2\2\u013c\u013d\7<\2\2")
        buf.write("\u013db\3\2\2\2\u013e\u013f\7}\2\2\u013fd\3\2\2\2\u0140")
        buf.write("\u0141\7\177\2\2\u0141f\3\2\2\2\u0142\u0143\7\61\2\2\u0143")
        buf.write("\u0144\7,\2\2\u0144\u0148\3\2\2\2\u0145\u0147\13\2\2\2")
        buf.write("\u0146\u0145\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0149\3")
        buf.write("\2\2\2\u0148\u0146\3\2\2\2\u0149\u014b\3\2\2\2\u014a\u0148")
        buf.write("\3\2\2\2\u014b\u014c\7,\2\2\u014c\u014d\7\61\2\2\u014d")
        buf.write("\u014e\3\2\2\2\u014e\u014f\b\64\2\2\u014fh\3\2\2\2\u0150")
        buf.write("\u0151\7\61\2\2\u0151\u0152\7\61\2\2\u0152\u0156\3\2\2")
        buf.write("\2\u0153\u0155\13\2\2\2\u0154\u0153\3\2\2\2\u0155\u0158")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0156\u0154\3\2\2\2\u0157")
        buf.write("\u015a\3\2\2\2\u0158\u0156\3\2\2\2\u0159\u015b\t\2\2\2")
        buf.write("\u015a\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015d\b")
        buf.write("\65\2\2\u015dj\3\2\2\2\u015e\u0162\t\3\2\2\u015f\u0161")
        buf.write("\t\4\2\2\u0160\u015f\3\2\2\2\u0161\u0164\3\2\2\2\u0162")
        buf.write("\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163l\3\2\2\2\u0164")
        buf.write("\u0162\3\2\2\2\u0165\u0167\7B\2\2\u0166\u0168\t\4\2\2")
        buf.write("\u0167\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u0167\3")
        buf.write("\2\2\2\u0169\u016a\3\2\2\2\u016an\3\2\2\2\u016b\u016d")
        buf.write("\t\5\2\2\u016c\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016fp\3\2\2\2\u0170")
        buf.write("\u0171\5s:\2\u0171\u0172\5u;\2\u0172\u017a\3\2\2\2\u0173")
        buf.write("\u0175\5s:\2\u0174\u0176\5u;\2\u0175\u0174\3\2\2\2\u0175")
        buf.write("\u0176\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0178\5w<\2\u0178")
        buf.write("\u017a\3\2\2\2\u0179\u0170\3\2\2\2\u0179\u0173\3\2\2\2")
        buf.write("\u017ar\3\2\2\2\u017b\u017d\t\5\2\2\u017c\u017b\3\2\2")
        buf.write("\2\u017d\u017e\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f")
        buf.write("\3\2\2\2\u017ft\3\2\2\2\u0180\u0184\7\60\2\2\u0181\u0183")
        buf.write("\t\5\2\2\u0182\u0181\3\2\2\2\u0183\u0186\3\2\2\2\u0184")
        buf.write("\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185v\3\2\2\2\u0186")
        buf.write("\u0184\3\2\2\2\u0187\u0189\t\6\2\2\u0188\u018a\t\7\2\2")
        buf.write("\u0189\u0188\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018c\3")
        buf.write("\2\2\2\u018b\u018d\t\5\2\2\u018c\u018b\3\2\2\2\u018d\u018e")
        buf.write("\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f")
        buf.write("x\3\2\2\2\u0190\u0193\5\7\4\2\u0191\u0193\5\21\t\2\u0192")
        buf.write("\u0190\3\2\2\2\u0192\u0191\3\2\2\2\u0193z\3\2\2\2\u0194")
        buf.write("\u0198\7$\2\2\u0195\u0197\5}?\2\u0196\u0195\3\2\2\2\u0197")
        buf.write("\u019a\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199\u019b\3\2\2\2\u019a\u0198\3\2\2\2\u019b\u019c\7")
        buf.write("$\2\2\u019c\u019d\b>\3\2\u019d|\3\2\2\2\u019e\u01a3\n")
        buf.write("\b\2\2\u019f\u01a3\5\177@\2\u01a0\u01a1\7^\2\2\u01a1\u01a3")
        buf.write("\7$\2\2\u01a2\u019e\3\2\2\2\u01a2\u019f\3\2\2\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a3~\3\2\2\2\u01a4\u01a5\7^\2\2\u01a5")
        buf.write("\u01b3\7d\2\2\u01a6\u01a7\7^\2\2\u01a7\u01b3\7h\2\2\u01a8")
        buf.write("\u01a9\7^\2\2\u01a9\u01b3\7t\2\2\u01aa\u01ab\7^\2\2\u01ab")
        buf.write("\u01b3\7p\2\2\u01ac\u01ad\7^\2\2\u01ad\u01b3\7v\2\2\u01ae")
        buf.write("\u01af\7^\2\2\u01af\u01b3\7$\2\2\u01b0\u01b1\7^\2\2\u01b1")
        buf.write("\u01b3\7^\2\2\u01b2\u01a4\3\2\2\2\u01b2\u01a6\3\2\2\2")
        buf.write("\u01b2\u01a8\3\2\2\2\u01b2\u01aa\3\2\2\2\u01b2\u01ac\3")
        buf.write("\2\2\2\u01b2\u01ae\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b3\u0080")
        buf.write("\3\2\2\2\u01b4\u01b6\t\t\2\2\u01b5\u01b4\3\2\2\2\u01b6")
        buf.write("\u01b7\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2")
        buf.write("\u01b8\u01b9\3\2\2\2\u01b9\u01ba\bA\2\2\u01ba\u0082\3")
        buf.write("\2\2\2\u01bb\u01bf\7$\2\2\u01bc\u01be\5}?\2\u01bd\u01bc")
        buf.write("\3\2\2\2\u01be\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf")
        buf.write("\u01c0\3\2\2\2\u01c0\u01c2\3\2\2\2\u01c1\u01bf\3\2\2\2")
        buf.write("\u01c2\u01c3\bB\4\2\u01c3\u0084\3\2\2\2\u01c4\u01ca\7")
        buf.write("$\2\2\u01c5\u01c6\7^\2\2\u01c6\u01c9\t\n\2\2\u01c7\u01c9")
        buf.write("\n\13\2\2\u01c8\u01c5\3\2\2\2\u01c8\u01c7\3\2\2\2\u01c9")
        buf.write("\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2")
        buf.write("\u01cb\u01cd\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u01ce\7")
        buf.write("^\2\2\u01ce\u01cf\n\n\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1")
        buf.write("\bC\5\2\u01d1\u0086\3\2\2\2\u01d2\u01d3\13\2\2\2\u01d3")
        buf.write("\u01d4\bD\6\2\u01d4\u0088\3\2\2\2\27\2\u0148\u0156\u015a")
        buf.write("\u0162\u0169\u016e\u0175\u0179\u017e\u0184\u0189\u018e")
        buf.write("\u0192\u0198\u01a2\u01b2\u01b7\u01bf\u01c8\u01ca\7\b\2")
        buf.write("\2\3>\2\3B\3\3C\4\3D\5")
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
    BOOLLIT = 57
    STRLIT = 58
    WS = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61
    ERROR_CHAR = 62

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
            "BOOLLIT", "STRLIT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "BREAK", "TRUE", "STRING", "VAR", "FUNC", "CONTINUE", 
                  "FALSE", "RETURN", "SELF", "IF", "INT", "NULL", "NEW", 
                  "ELSE", "FLOAT", "CLASS", "VOID", "FOR", "BOOL", "CONSTRUCTOR", 
                  "CONST", "PLUS", "MINUS", "MULTIPLE", "DIVIDE_FLOAT", 
                  "DIVIDE_INT", "CHAMTHAN", "AND", "OR", "EQUAL", "DECLARE", 
                  "DIFFER", "SMOL", "SMOL_EQUAL", "BIG", "BIG_EQUAL", "ASSIGN", 
                  "CONCAT", "MOD", "LB", "RB", "LS", "RS", "DOT", "CM", 
                  "SM", "CL", "LC", "RC", "BLOCK_COMMENT", "LINE_COMMENT", 
                  "IDENTIFIER", "AT_ID", "INTLIT", "FLOATLIT", "INTPART", 
                  "DEC", "EXP", "BOOLLIT", "STRLIT", "CHARS", "ESC_SEQ", 
                  "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[60] = self.STRLIT_action 
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            actions[66] = self.ERROR_CHAR_action 
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
     


