# Generated from d:\btl1-nlnnlt\assignment1\src\main\CSlang\parser\CSlang.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01e2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%")
        buf.write("\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-")
        buf.write("\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3")
        buf.write("\64\6\64\u0144\n\64\r\64\16\64\u0145\3\65\3\65\3\65\3")
        buf.write("\65\3\65\5\65\u014d\n\65\3\65\3\65\5\65\u0151\n\65\3\66")
        buf.write("\3\66\7\66\u0155\n\66\f\66\16\66\u0158\13\66\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\3\67\3\67\5\67\u0162\n\67\3\67\3")
        buf.write("\67\3\67\3\67\3\67\3\67\38\38\38\38\38\78\u016f\n8\f8")
        buf.write("\168\u0172\138\38\58\u0175\n8\38\38\39\39\79\u017b\n9")
        buf.write("\f9\169\u017e\139\39\39\69\u0182\n9\r9\169\u0183\39\5")
        buf.write("9\u0187\n9\3:\3:\7:\u018b\n:\f:\16:\u018e\13:\3;\3;\6")
        buf.write(";\u0192\n;\r;\16;\u0193\3<\3<\7<\u0198\n<\f<\16<\u019b")
        buf.write("\13<\3=\5=\u019e\n=\3=\6=\u01a1\n=\r=\16=\u01a2\3>\3>")
        buf.write("\3>\6>\u01a8\n>\r>\16>\u01a9\3?\3?\3?\3?\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\3?\3?\3?\5?\u01ba\n?\3@\3@\3@\3@\5@\u01c0\n@\3")
        buf.write("A\6A\u01c3\nA\rA\16A\u01c4\3A\3A\3B\3B\7B\u01cb\nB\fB")
        buf.write("\16B\u01ce\13B\3B\3B\3C\3C\3C\3C\7C\u01d6\nC\fC\16C\u01d9")
        buf.write("\13C\3C\3C\3C\3C\3C\3D\3D\3D\3\u0170\2E\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y\2{\2}\2\177")
        buf.write("\2\u0081>\u0083?\u0085@\u0087A\3\2\r\3\2\62;\3\3\f\f\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\3\2\63;\4\2GGgg\4\2--//\t\2\f")
        buf.write("\f\17\17$$))GHQQ^^\5\2\13\f\17\17\"\"\t\2))^^ddhhpptt")
        buf.write("vv\6\2\f\f\17\17$$^^\2\u01f9\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\3\u0089\3\2\2\2\5\u008c\3\2\2")
        buf.write("\2\7\u0092\3\2\2\2\t\u009b\3\2\2\2\13\u009e\3\2\2\2\r")
        buf.write("\u00a3\3\2\2\2\17\u00a7\3\2\2\2\21\u00ac\3\2\2\2\23\u00b2")
        buf.write("\3\2\2\2\25\u00b6\3\2\2\2\27\u00bc\3\2\2\2\31\u00c1\3")
        buf.write("\2\2\2\33\u00c8\3\2\2\2\35\u00cf\3\2\2\2\37\u00d4\3\2")
        buf.write("\2\2!\u00da\3\2\2\2#\u00e6\3\2\2\2%\u00ea\3\2\2\2\'\u00ef")
        buf.write("\3\2\2\2)\u00f3\3\2\2\2+\u00f8\3\2\2\2-\u00fe\3\2\2\2")
        buf.write("/\u0103\3\2\2\2\61\u0105\3\2\2\2\63\u0107\3\2\2\2\65\u0109")
        buf.write("\3\2\2\2\67\u010b\3\2\2\29\u010d\3\2\2\2;\u0110\3\2\2")
        buf.write("\2=\u0113\3\2\2\2?\u0116\3\2\2\2A\u0119\3\2\2\2C\u011c")
        buf.write("\3\2\2\2E\u011f\3\2\2\2G\u0122\3\2\2\2I\u0124\3\2\2\2")
        buf.write("K\u0126\3\2\2\2M\u0128\3\2\2\2O\u012a\3\2\2\2Q\u012c\3")
        buf.write("\2\2\2S\u012e\3\2\2\2U\u0130\3\2\2\2W\u0132\3\2\2\2Y\u0134")
        buf.write("\3\2\2\2[\u0136\3\2\2\2]\u0138\3\2\2\2_\u013a\3\2\2\2")
        buf.write("a\u013c\3\2\2\2c\u013e\3\2\2\2e\u0140\3\2\2\2g\u0143\3")
        buf.write("\2\2\2i\u0150\3\2\2\2k\u0152\3\2\2\2m\u015c\3\2\2\2o\u0169")
        buf.write("\3\2\2\2q\u0186\3\2\2\2s\u0188\3\2\2\2u\u018f\3\2\2\2")
        buf.write("w\u0195\3\2\2\2y\u019d\3\2\2\2{\u01a4\3\2\2\2}\u01b9\3")
        buf.write("\2\2\2\177\u01bf\3\2\2\2\u0081\u01c2\3\2\2\2\u0083\u01c8")
        buf.write("\3\2\2\2\u0085\u01d1\3\2\2\2\u0087\u01df\3\2\2\2\u0089")
        buf.write("\u008a\7>\2\2\u008a\u008b\7/\2\2\u008b\4\3\2\2\2\u008c")
        buf.write("\u008d\7d\2\2\u008d\u008e\7t\2\2\u008e\u008f\7g\2\2\u008f")
        buf.write("\u0090\7c\2\2\u0090\u0091\7m\2\2\u0091\6\3\2\2\2\u0092")
        buf.write("\u0093\7e\2\2\u0093\u0094\7q\2\2\u0094\u0095\7p\2\2\u0095")
        buf.write("\u0096\7v\2\2\u0096\u0097\7k\2\2\u0097\u0098\7p\2\2\u0098")
        buf.write("\u0099\7w\2\2\u0099\u009a\7g\2\2\u009a\b\3\2\2\2\u009b")
        buf.write("\u009c\7k\2\2\u009c\u009d\7h\2\2\u009d\n\3\2\2\2\u009e")
        buf.write("\u009f\7g\2\2\u009f\u00a0\7n\2\2\u00a0\u00a1\7u\2\2\u00a1")
        buf.write("\u00a2\7g\2\2\u00a2\f\3\2\2\2\u00a3\u00a4\7h\2\2\u00a4")
        buf.write("\u00a5\7q\2\2\u00a5\u00a6\7t\2\2\u00a6\16\3\2\2\2\u00a7")
        buf.write("\u00a8\7v\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa\7w\2\2\u00aa")
        buf.write("\u00ab\7g\2\2\u00ab\20\3\2\2\2\u00ac\u00ad\7h\2\2\u00ad")
        buf.write("\u00ae\7c\2\2\u00ae\u00af\7n\2\2\u00af\u00b0\7u\2\2\u00b0")
        buf.write("\u00b1\7g\2\2\u00b1\22\3\2\2\2\u00b2\u00b3\7k\2\2\u00b3")
        buf.write("\u00b4\7p\2\2\u00b4\u00b5\7v\2\2\u00b5\24\3\2\2\2\u00b6")
        buf.write("\u00b7\7h\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9\7q\2\2\u00b9")
        buf.write("\u00ba\7c\2\2\u00ba\u00bb\7v\2\2\u00bb\26\3\2\2\2\u00bc")
        buf.write("\u00bd\7d\2\2\u00bd\u00be\7q\2\2\u00be\u00bf\7q\2\2\u00bf")
        buf.write("\u00c0\7n\2\2\u00c0\30\3\2\2\2\u00c1\u00c2\7u\2\2\u00c2")
        buf.write("\u00c3\7v\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5\7k\2\2\u00c5")
        buf.write("\u00c6\7p\2\2\u00c6\u00c7\7i\2\2\u00c7\32\3\2\2\2\u00c8")
        buf.write("\u00c9\7t\2\2\u00c9\u00ca\7g\2\2\u00ca\u00cb\7v\2\2\u00cb")
        buf.write("\u00cc\7w\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce\7p\2\2\u00ce")
        buf.write("\34\3\2\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1\7w\2\2\u00d1")
        buf.write("\u00d2\7n\2\2\u00d2\u00d3\7n\2\2\u00d3\36\3\2\2\2\u00d4")
        buf.write("\u00d5\7e\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7\7c\2\2\u00d7")
        buf.write("\u00d8\7u\2\2\u00d8\u00d9\7u\2\2\u00d9 \3\2\2\2\u00da")
        buf.write("\u00db\7e\2\2\u00db\u00dc\7q\2\2\u00dc\u00dd\7p\2\2\u00dd")
        buf.write("\u00de\7u\2\2\u00de\u00df\7v\2\2\u00df\u00e0\7t\2\2\u00e0")
        buf.write("\u00e1\7w\2\2\u00e1\u00e2\7e\2\2\u00e2\u00e3\7v\2\2\u00e3")
        buf.write("\u00e4\7q\2\2\u00e4\u00e5\7t\2\2\u00e5\"\3\2\2\2\u00e6")
        buf.write("\u00e7\7x\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9\7t\2\2\u00e9")
        buf.write("$\3\2\2\2\u00ea\u00eb\7u\2\2\u00eb\u00ec\7g\2\2\u00ec")
        buf.write("\u00ed\7n\2\2\u00ed\u00ee\7h\2\2\u00ee&\3\2\2\2\u00ef")
        buf.write("\u00f0\7p\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2\7y\2\2\u00f2")
        buf.write("(\3\2\2\2\u00f3\u00f4\7x\2\2\u00f4\u00f5\7q\2\2\u00f5")
        buf.write("\u00f6\7k\2\2\u00f6\u00f7\7f\2\2\u00f7*\3\2\2\2\u00f8")
        buf.write("\u00f9\7e\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb\7p\2\2\u00fb")
        buf.write("\u00fc\7u\2\2\u00fc\u00fd\7v\2\2\u00fd,\3\2\2\2\u00fe")
        buf.write("\u00ff\7h\2\2\u00ff\u0100\7w\2\2\u0100\u0101\7p\2\2\u0101")
        buf.write("\u0102\7e\2\2\u0102.\3\2\2\2\u0103\u0104\7-\2\2\u0104")
        buf.write("\60\3\2\2\2\u0105\u0106\7/\2\2\u0106\62\3\2\2\2\u0107")
        buf.write("\u0108\7,\2\2\u0108\64\3\2\2\2\u0109\u010a\7\61\2\2\u010a")
        buf.write("\66\3\2\2\2\u010b\u010c\7^\2\2\u010c8\3\2\2\2\u010d\u010e")
        buf.write("\7(\2\2\u010e\u010f\7(\2\2\u010f:\3\2\2\2\u0110\u0111")
        buf.write("\7~\2\2\u0111\u0112\7~\2\2\u0112<\3\2\2\2\u0113\u0114")
        buf.write("\7?\2\2\u0114\u0115\7?\2\2\u0115>\3\2\2\2\u0116\u0117")
        buf.write("\7<\2\2\u0117\u0118\7?\2\2\u0118@\3\2\2\2\u0119\u011a")
        buf.write("\7#\2\2\u011a\u011b\7?\2\2\u011bB\3\2\2\2\u011c\u011d")
        buf.write("\7>\2\2\u011d\u011e\7?\2\2\u011eD\3\2\2\2\u011f\u0120")
        buf.write("\7@\2\2\u0120\u0121\7?\2\2\u0121F\3\2\2\2\u0122\u0123")
        buf.write("\7#\2\2\u0123H\3\2\2\2\u0124\u0125\7?\2\2\u0125J\3\2\2")
        buf.write("\2\u0126\u0127\7>\2\2\u0127L\3\2\2\2\u0128\u0129\7@\2")
        buf.write("\2\u0129N\3\2\2\2\u012a\u012b\7`\2\2\u012bP\3\2\2\2\u012c")
        buf.write("\u012d\7\'\2\2\u012dR\3\2\2\2\u012e\u012f\7*\2\2\u012f")
        buf.write("T\3\2\2\2\u0130\u0131\7+\2\2\u0131V\3\2\2\2\u0132\u0133")
        buf.write("\7]\2\2\u0133X\3\2\2\2\u0134\u0135\7_\2\2\u0135Z\3\2\2")
        buf.write("\2\u0136\u0137\7\60\2\2\u0137\\\3\2\2\2\u0138\u0139\7")
        buf.write(".\2\2\u0139^\3\2\2\2\u013a\u013b\7=\2\2\u013b`\3\2\2\2")
        buf.write("\u013c\u013d\7<\2\2\u013db\3\2\2\2\u013e\u013f\7}\2\2")
        buf.write("\u013fd\3\2\2\2\u0140\u0141\7\177\2\2\u0141f\3\2\2\2\u0142")
        buf.write("\u0144\t\2\2\2\u0143\u0142\3\2\2\2\u0144\u0145\3\2\2\2")
        buf.write("\u0145\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146h\3\2\2")
        buf.write("\2\u0147\u0148\5g\64\2\u0148\u0149\5y=\2\u0149\u0151\3")
        buf.write("\2\2\2\u014a\u014c\5g\64\2\u014b\u014d\5y=\2\u014c\u014b")
        buf.write("\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014e\3\2\2\2\u014e")
        buf.write("\u014f\5{>\2\u014f\u0151\3\2\2\2\u0150\u0147\3\2\2\2\u0150")
        buf.write("\u014a\3\2\2\2\u0151j\3\2\2\2\u0152\u0156\7$\2\2\u0153")
        buf.write("\u0155\5\177@\2\u0154\u0153\3\2\2\2\u0155\u0158\3\2\2")
        buf.write("\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0159")
        buf.write("\3\2\2\2\u0158\u0156\3\2\2\2\u0159\u015a\7$\2\2\u015a")
        buf.write("\u015b\b\66\2\2\u015bl\3\2\2\2\u015c\u015d\7\61\2\2\u015d")
        buf.write("\u015e\7\61\2\2\u015e\u015f\7,\2\2\u015f\u0161\3\2\2\2")
        buf.write("\u0160\u0162\13\2\2\2\u0161\u0160\3\2\2\2\u0161\u0162")
        buf.write("\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0164\7,\2\2\u0164")
        buf.write("\u0165\7\61\2\2\u0165\u0166\7\61\2\2\u0166\u0167\3\2\2")
        buf.write("\2\u0167\u0168\b\67\3\2\u0168n\3\2\2\2\u0169\u016a\7\61")
        buf.write("\2\2\u016a\u016b\7\61\2\2\u016b\u016c\7\61\2\2\u016c\u0170")
        buf.write("\3\2\2\2\u016d\u016f\13\2\2\2\u016e\u016d\3\2\2\2\u016f")
        buf.write("\u0172\3\2\2\2\u0170\u0171\3\2\2\2\u0170\u016e\3\2\2\2")
        buf.write("\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0173\u0175\t")
        buf.write("\3\2\2\u0174\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177")
        buf.write("\b8\3\2\u0177p\3\2\2\2\u0178\u017c\t\4\2\2\u0179\u017b")
        buf.write("\t\5\2\2\u017a\u0179\3\2\2\2\u017b\u017e\3\2\2\2\u017c")
        buf.write("\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u0187\3\2\2\2")
        buf.write("\u017e\u017c\3\2\2\2\u017f\u0181\7B\2\2\u0180\u0182\t")
        buf.write("\5\2\2\u0181\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0181")
        buf.write("\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0187\3\2\2\2\u0185")
        buf.write("\u0187\5%\23\2\u0186\u0178\3\2\2\2\u0186\u017f\3\2\2\2")
        buf.write("\u0186\u0185\3\2\2\2\u0187r\3\2\2\2\u0188\u018c\t\4\2")
        buf.write("\2\u0189\u018b\t\5\2\2\u018a\u0189\3\2\2\2\u018b\u018e")
        buf.write("\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d")
        buf.write("t\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0191\7B\2\2\u0190")
        buf.write("\u0192\t\5\2\2\u0191\u0190\3\2\2\2\u0192\u0193\3\2\2\2")
        buf.write("\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194v\3\2\2")
        buf.write("\2\u0195\u0199\t\6\2\2\u0196\u0198\t\2\2\2\u0197\u0196")
        buf.write("\3\2\2\2\u0198\u019b\3\2\2\2\u0199\u0197\3\2\2\2\u0199")
        buf.write("\u019a\3\2\2\2\u019ax\3\2\2\2\u019b\u0199\3\2\2\2\u019c")
        buf.write("\u019e\7\60\2\2\u019d\u019c\3\2\2\2\u019d\u019e\3\2\2")
        buf.write("\2\u019e\u01a0\3\2\2\2\u019f\u01a1\t\2\2\2\u01a0\u019f")
        buf.write("\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2")
        buf.write("\u01a3\3\2\2\2\u01a3z\3\2\2\2\u01a4\u01a5\t\7\2\2\u01a5")
        buf.write("\u01a7\t\b\2\2\u01a6\u01a8\t\2\2\2\u01a7\u01a6\3\2\2\2")
        buf.write("\u01a8\u01a9\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3")
        buf.write("\2\2\2\u01aa|\3\2\2\2\u01ab\u01ac\7^\2\2\u01ac\u01ba\7")
        buf.write("d\2\2\u01ad\u01ae\7^\2\2\u01ae\u01ba\7h\2\2\u01af\u01b0")
        buf.write("\7^\2\2\u01b0\u01ba\7t\2\2\u01b1\u01b2\7^\2\2\u01b2\u01ba")
        buf.write("\7p\2\2\u01b3\u01b4\7^\2\2\u01b4\u01ba\7v\2\2\u01b5\u01b6")
        buf.write("\7^\2\2\u01b6\u01ba\7$\2\2\u01b7\u01b8\7^\2\2\u01b8\u01ba")
        buf.write("\7^\2\2\u01b9\u01ab\3\2\2\2\u01b9\u01ad\3\2\2\2\u01b9")
        buf.write("\u01af\3\2\2\2\u01b9\u01b1\3\2\2\2\u01b9\u01b3\3\2\2\2")
        buf.write("\u01b9\u01b5\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba~\3\2\2")
        buf.write("\2\u01bb\u01c0\n\t\2\2\u01bc\u01c0\5}?\2\u01bd\u01be\7")
        buf.write("^\2\2\u01be\u01c0\7$\2\2\u01bf\u01bb\3\2\2\2\u01bf\u01bc")
        buf.write("\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0\u0080\3\2\2\2\u01c1")
        buf.write("\u01c3\t\n\2\2\u01c2\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2")
        buf.write("\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c6\3")
        buf.write("\2\2\2\u01c6\u01c7\bA\3\2\u01c7\u0082\3\2\2\2\u01c8\u01cc")
        buf.write("\7$\2\2\u01c9\u01cb\5\177@\2\u01ca\u01c9\3\2\2\2\u01cb")
        buf.write("\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2")
        buf.write("\u01cd\u01cf\3\2\2\2\u01ce\u01cc\3\2\2\2\u01cf\u01d0\b")
        buf.write("B\4\2\u01d0\u0084\3\2\2\2\u01d1\u01d7\7$\2\2\u01d2\u01d3")
        buf.write("\7^\2\2\u01d3\u01d6\t\13\2\2\u01d4\u01d6\n\f\2\2\u01d5")
        buf.write("\u01d2\3\2\2\2\u01d5\u01d4\3\2\2\2\u01d6\u01d9\3\2\2\2")
        buf.write("\u01d7\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01da\3")
        buf.write("\2\2\2\u01d9\u01d7\3\2\2\2\u01da\u01db\7^\2\2\u01db\u01dc")
        buf.write("\n\13\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01de\bC\5\2\u01de")
        buf.write("\u0086\3\2\2\2\u01df\u01e0\13\2\2\2\u01e0\u01e1\bD\6\2")
        buf.write("\u01e1\u0088\3\2\2\2\31\2\u0145\u014c\u0150\u0156\u0161")
        buf.write("\u0170\u0174\u017c\u0183\u0186\u018c\u0193\u0199\u019d")
        buf.write("\u01a2\u01a9\u01b9\u01bf\u01c4\u01cc\u01d5\u01d7\7\3\66")
        buf.write("\2\b\2\2\3B\3\3C\4\3D\5")
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
    EQUAL = 30
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
    IDENTIFIER = 56
    ID = 57
    ATIDENTIFIER = 58
    ARRAYSIZE = 59
    WS = 60
    UNCLOSED_STRING = 61
    ILLEGAL_ESCAPE = 62
    ERROR_CHAR = 63

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
            "MULTIPLY", "DIVIDE_FLOAT", "DIVIDE_INT", "AND", "OR", "EQUAL", 
            "ASSIGN", "NEQ", "LEQ", "GEQ", "DIFF", "DECLARE", "LE", "GE", 
            "CONCAT", "MOD", "LRB", "RRB", "LSB", "RSB", "DOT", "CM", "SM", 
            "COLON", "LCB", "RCB", "INTLIT", "FLOATLIT", "STRINGLIT", "BLOCKCMT", 
            "LINECMT", "IDENTIFIER", "ID", "ATIDENTIFIER", "ARRAYSIZE", 
            "WS", "UNCLOSED_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", 
                  "FALSE", "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", 
                  "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", 
                  "CONST", "FUNC", "PLUS", "MINUS", "MULTIPLY", "DIVIDE_FLOAT", 
                  "DIVIDE_INT", "AND", "OR", "EQUAL", "ASSIGN", "NEQ", "LEQ", 
                  "GEQ", "DIFF", "DECLARE", "LE", "GE", "CONCAT", "MOD", 
                  "LRB", "RRB", "LSB", "RSB", "DOT", "CM", "SM", "COLON", 
                  "LCB", "RCB", "INTLIT", "FLOATLIT", "STRINGLIT", "BLOCKCMT", 
                  "LINECMT", "IDENTIFIER", "ID", "ATIDENTIFIER", "ARRAYSIZE", 
                  "DEC", "EXP", "ESCAPESEQ", "CHAR_LIT", "WS", "UNCLOSED_STRING", 
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
            actions[52] = self.STRINGLIT_action 
            actions[64] = self.UNCLOSED_STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            actions[66] = self.ERROR_CHAR_action 
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
     


