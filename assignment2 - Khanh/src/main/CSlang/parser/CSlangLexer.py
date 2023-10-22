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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>")
        buf.write("\u01c5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\7\3\u008d\n\3\f\3\16\3\u0090\13")
        buf.write("\3\3\3\5\3\u0093\n\3\3\3\3\3\3\3\3\3\7\3\u0099\n\3\f\3")
        buf.write("\16\3\u009c\13\3\3\3\3\3\5\3\u00a0\n\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\65\3\65\6\65\u015c\n\65\r")
        buf.write("\65\16\65\u015d\3\66\3\66\7\66\u0162\n\66\f\66\16\66\u0165")
        buf.write("\13\66\3\67\6\67\u0168\n\67\r\67\16\67\u0169\38\38\39")
        buf.write("\39\79\u0170\n9\f9\169\u0173\139\3:\3:\5:\u0177\n:\3:")
        buf.write("\6:\u017a\n:\r:\16:\u017b\3;\3;\3;\3;\3;\5;\u0183\n;\3")
        buf.write(";\3;\5;\u0187\n;\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3")
        buf.write("<\3<\5<\u0197\n<\3=\3=\5=\u019b\n=\3>\3>\7>\u019f\n>\f")
        buf.write(">\16>\u01a2\13>\3>\3>\3>\3?\6?\u01a8\n?\r?\16?\u01a9\3")
        buf.write("?\3?\3@\3@\7@\u01b0\n@\f@\16@\u01b3\13@\3@\3@\3@\3@\3")
        buf.write("@\3A\3A\7A\u01bc\nA\fA\16A\u01bf\13A\3A\3A\3B\3B\3B\4")
        buf.write("\u008e\u009a\2C\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m\2o8q\2s\2u9w\2y\2{:};\177<\u0081=\u0083>\3\2")
        buf.write("\13\3\3\f\f\6\2\62;C\\aac|\5\2C\\aac|\3\2\62;\4\2GGgg")
        buf.write("\4\2--//\b\2\f\f\17\17$$GHQQ^^\5\2\13\f\17\17\"\"\t\2")
        buf.write("$$^^ddhhppttvv\2\u01d5\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("o\3\2\2\2\2u\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\3\u0085\3\2\2\2\5\u009f")
        buf.write("\3\2\2\2\7\u00a3\3\2\2\2\t\u00a9\3\2\2\2\13\u00b2\3\2")
        buf.write("\2\2\r\u00b5\3\2\2\2\17\u00ba\3\2\2\2\21\u00be\3\2\2\2")
        buf.write("\23\u00c3\3\2\2\2\25\u00c9\3\2\2\2\27\u00cd\3\2\2\2\31")
        buf.write("\u00d3\3\2\2\2\33\u00d8\3\2\2\2\35\u00df\3\2\2\2\37\u00e6")
        buf.write("\3\2\2\2!\u00eb\3\2\2\2#\u00f1\3\2\2\2%\u00fd\3\2\2\2")
        buf.write("\'\u0101\3\2\2\2)\u0106\3\2\2\2+\u010a\3\2\2\2-\u010f")
        buf.write("\3\2\2\2/\u0115\3\2\2\2\61\u011a\3\2\2\2\63\u011c\3\2")
        buf.write("\2\2\65\u011e\3\2\2\2\67\u0120\3\2\2\29\u0122\3\2\2\2")
        buf.write(";\u0124\3\2\2\2=\u0127\3\2\2\2?\u0129\3\2\2\2A\u012c\3")
        buf.write("\2\2\2C\u012f\3\2\2\2E\u0132\3\2\2\2G\u0135\3\2\2\2I\u0137")
        buf.write("\3\2\2\2K\u013a\3\2\2\2M\u013c\3\2\2\2O\u013f\3\2\2\2")
        buf.write("Q\u0141\3\2\2\2S\u0143\3\2\2\2U\u0145\3\2\2\2W\u0147\3")
        buf.write("\2\2\2Y\u0149\3\2\2\2[\u014b\3\2\2\2]\u014d\3\2\2\2_\u014f")
        buf.write("\3\2\2\2a\u0151\3\2\2\2c\u0153\3\2\2\2e\u0155\3\2\2\2")
        buf.write("g\u0157\3\2\2\2i\u0159\3\2\2\2k\u015f\3\2\2\2m\u0167\3")
        buf.write("\2\2\2o\u016b\3\2\2\2q\u016d\3\2\2\2s\u0174\3\2\2\2u\u0186")
        buf.write("\3\2\2\2w\u0196\3\2\2\2y\u019a\3\2\2\2{\u019c\3\2\2\2")
        buf.write("}\u01a7\3\2\2\2\177\u01ad\3\2\2\2\u0081\u01b9\3\2\2\2")
        buf.write("\u0083\u01c2\3\2\2\2\u0085\u0086\7>\2\2\u0086\u0087\7")
        buf.write("/\2\2\u0087\4\3\2\2\2\u0088\u0089\7\61\2\2\u0089\u008a")
        buf.write("\7\61\2\2\u008a\u008e\3\2\2\2\u008b\u008d\13\2\2\2\u008c")
        buf.write("\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008f\3\2\2\2")
        buf.write("\u008e\u008c\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3")
        buf.write("\2\2\2\u0091\u0093\t\2\2\2\u0092\u0091\3\2\2\2\u0093\u00a0")
        buf.write("\3\2\2\2\u0094\u0095\7\61\2\2\u0095\u0096\7,\2\2\u0096")
        buf.write("\u009a\3\2\2\2\u0097\u0099\13\2\2\2\u0098\u0097\3\2\2")
        buf.write("\2\u0099\u009c\3\2\2\2\u009a\u009b\3\2\2\2\u009a\u0098")
        buf.write("\3\2\2\2\u009b\u009d\3\2\2\2\u009c\u009a\3\2\2\2\u009d")
        buf.write("\u009e\7,\2\2\u009e\u00a0\7\61\2\2\u009f\u0088\3\2\2\2")
        buf.write("\u009f\u0094\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\b")
        buf.write("\3\2\2\u00a2\6\3\2\2\2\u00a3\u00a4\7d\2\2\u00a4\u00a5")
        buf.write("\7t\2\2\u00a5\u00a6\7g\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8")
        buf.write("\7m\2\2\u00a8\b\3\2\2\2\u00a9\u00aa\7e\2\2\u00aa\u00ab")
        buf.write("\7q\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad\7v\2\2\u00ad\u00ae")
        buf.write("\7k\2\2\u00ae\u00af\7p\2\2\u00af\u00b0\7w\2\2\u00b0\u00b1")
        buf.write("\7g\2\2\u00b1\n\3\2\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4")
        buf.write("\7h\2\2\u00b4\f\3\2\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7")
        buf.write("\7n\2\2\u00b7\u00b8\7u\2\2\u00b8\u00b9\7g\2\2\u00b9\16")
        buf.write("\3\2\2\2\u00ba\u00bb\7h\2\2\u00bb\u00bc\7q\2\2\u00bc\u00bd")
        buf.write("\7t\2\2\u00bd\20\3\2\2\2\u00be\u00bf\7v\2\2\u00bf\u00c0")
        buf.write("\7t\2\2\u00c0\u00c1\7w\2\2\u00c1\u00c2\7g\2\2\u00c2\22")
        buf.write("\3\2\2\2\u00c3\u00c4\7h\2\2\u00c4\u00c5\7c\2\2\u00c5\u00c6")
        buf.write("\7n\2\2\u00c6\u00c7\7u\2\2\u00c7\u00c8\7g\2\2\u00c8\24")
        buf.write("\3\2\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc")
        buf.write("\7v\2\2\u00cc\26\3\2\2\2\u00cd\u00ce\7h\2\2\u00ce\u00cf")
        buf.write("\7n\2\2\u00cf\u00d0\7q\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2")
        buf.write("\7v\2\2\u00d2\30\3\2\2\2\u00d3\u00d4\7d\2\2\u00d4\u00d5")
        buf.write("\7q\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7\7n\2\2\u00d7\32")
        buf.write("\3\2\2\2\u00d8\u00d9\7u\2\2\u00d9\u00da\7v\2\2\u00da\u00db")
        buf.write("\7t\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de")
        buf.write("\7i\2\2\u00de\34\3\2\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1")
        buf.write("\7g\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3\7w\2\2\u00e3\u00e4")
        buf.write("\7t\2\2\u00e4\u00e5\7p\2\2\u00e5\36\3\2\2\2\u00e6\u00e7")
        buf.write("\7p\2\2\u00e7\u00e8\7w\2\2\u00e8\u00e9\7n\2\2\u00e9\u00ea")
        buf.write("\7n\2\2\u00ea \3\2\2\2\u00eb\u00ec\7e\2\2\u00ec\u00ed")
        buf.write("\7n\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef\7u\2\2\u00ef\u00f0")
        buf.write("\7u\2\2\u00f0\"\3\2\2\2\u00f1\u00f2\7e\2\2\u00f2\u00f3")
        buf.write("\7q\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5\7u\2\2\u00f5\u00f6")
        buf.write("\7v\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8\7w\2\2\u00f8\u00f9")
        buf.write("\7e\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb\7q\2\2\u00fb\u00fc")
        buf.write("\7t\2\2\u00fc$\3\2\2\2\u00fd\u00fe\7x\2\2\u00fe\u00ff")
        buf.write("\7c\2\2\u00ff\u0100\7t\2\2\u0100&\3\2\2\2\u0101\u0102")
        buf.write("\7u\2\2\u0102\u0103\7g\2\2\u0103\u0104\7n\2\2\u0104\u0105")
        buf.write("\7h\2\2\u0105(\3\2\2\2\u0106\u0107\7p\2\2\u0107\u0108")
        buf.write("\7g\2\2\u0108\u0109\7y\2\2\u0109*\3\2\2\2\u010a\u010b")
        buf.write("\7x\2\2\u010b\u010c\7q\2\2\u010c\u010d\7k\2\2\u010d\u010e")
        buf.write("\7f\2\2\u010e,\3\2\2\2\u010f\u0110\7e\2\2\u0110\u0111")
        buf.write("\7q\2\2\u0111\u0112\7p\2\2\u0112\u0113\7u\2\2\u0113\u0114")
        buf.write("\7v\2\2\u0114.\3\2\2\2\u0115\u0116\7h\2\2\u0116\u0117")
        buf.write("\7w\2\2\u0117\u0118\7p\2\2\u0118\u0119\7e\2\2\u0119\60")
        buf.write("\3\2\2\2\u011a\u011b\7-\2\2\u011b\62\3\2\2\2\u011c\u011d")
        buf.write("\7/\2\2\u011d\64\3\2\2\2\u011e\u011f\7,\2\2\u011f\66\3")
        buf.write("\2\2\2\u0120\u0121\7\61\2\2\u01218\3\2\2\2\u0122\u0123")
        buf.write("\7^\2\2\u0123:\3\2\2\2\u0124\u0125\7#\2\2\u0125\u0126")
        buf.write("\7?\2\2\u0126<\3\2\2\2\u0127\u0128\7#\2\2\u0128>\3\2\2")
        buf.write("\2\u0129\u012a\7(\2\2\u012a\u012b\7(\2\2\u012b@\3\2\2")
        buf.write("\2\u012c\u012d\7~\2\2\u012d\u012e\7~\2\2\u012eB\3\2\2")
        buf.write("\2\u012f\u0130\7?\2\2\u0130\u0131\7?\2\2\u0131D\3\2\2")
        buf.write("\2\u0132\u0133\7<\2\2\u0133\u0134\7?\2\2\u0134F\3\2\2")
        buf.write("\2\u0135\u0136\7?\2\2\u0136H\3\2\2\2\u0137\u0138\7>\2")
        buf.write("\2\u0138\u0139\7?\2\2\u0139J\3\2\2\2\u013a\u013b\7>\2")
        buf.write("\2\u013bL\3\2\2\2\u013c\u013d\7@\2\2\u013d\u013e\7?\2")
        buf.write("\2\u013eN\3\2\2\2\u013f\u0140\7@\2\2\u0140P\3\2\2\2\u0141")
        buf.write("\u0142\7`\2\2\u0142R\3\2\2\2\u0143\u0144\7\'\2\2\u0144")
        buf.write("T\3\2\2\2\u0145\u0146\7*\2\2\u0146V\3\2\2\2\u0147\u0148")
        buf.write("\7+\2\2\u0148X\3\2\2\2\u0149\u014a\7]\2\2\u014aZ\3\2\2")
        buf.write("\2\u014b\u014c\7_\2\2\u014c\\\3\2\2\2\u014d\u014e\7\60")
        buf.write("\2\2\u014e^\3\2\2\2\u014f\u0150\7.\2\2\u0150`\3\2\2\2")
        buf.write("\u0151\u0152\7=\2\2\u0152b\3\2\2\2\u0153\u0154\7<\2\2")
        buf.write("\u0154d\3\2\2\2\u0155\u0156\7}\2\2\u0156f\3\2\2\2\u0157")
        buf.write("\u0158\7\177\2\2\u0158h\3\2\2\2\u0159\u015b\7B\2\2\u015a")
        buf.write("\u015c\t\3\2\2\u015b\u015a\3\2\2\2\u015c\u015d\3\2\2\2")
        buf.write("\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015ej\3\2\2")
        buf.write("\2\u015f\u0163\t\4\2\2\u0160\u0162\t\3\2\2\u0161\u0160")
        buf.write("\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3\2\2\2\u0163")
        buf.write("\u0164\3\2\2\2\u0164l\3\2\2\2\u0165\u0163\3\2\2\2\u0166")
        buf.write("\u0168\t\5\2\2\u0167\u0166\3\2\2\2\u0168\u0169\3\2\2\2")
        buf.write("\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016an\3\2\2")
        buf.write("\2\u016b\u016c\5m\67\2\u016cp\3\2\2\2\u016d\u0171\7\60")
        buf.write("\2\2\u016e\u0170\5m\67\2\u016f\u016e\3\2\2\2\u0170\u0173")
        buf.write("\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172")
        buf.write("r\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u0176\t\6\2\2\u0175")
        buf.write("\u0177\t\7\2\2\u0176\u0175\3\2\2\2\u0176\u0177\3\2\2\2")
        buf.write("\u0177\u0179\3\2\2\2\u0178\u017a\5m\67\2\u0179\u0178\3")
        buf.write("\2\2\2\u017a\u017b\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c")
        buf.write("\3\2\2\2\u017ct\3\2\2\2\u017d\u017e\5m\67\2\u017e\u017f")
        buf.write("\5q9\2\u017f\u0187\3\2\2\2\u0180\u0182\5m\67\2\u0181\u0183")
        buf.write("\5q9\2\u0182\u0181\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184")
        buf.write("\3\2\2\2\u0184\u0185\5s:\2\u0185\u0187\3\2\2\2\u0186\u017d")
        buf.write("\3\2\2\2\u0186\u0180\3\2\2\2\u0187v\3\2\2\2\u0188\u0189")
        buf.write("\7^\2\2\u0189\u0197\7d\2\2\u018a\u018b\7^\2\2\u018b\u0197")
        buf.write("\7h\2\2\u018c\u018d\7^\2\2\u018d\u0197\7t\2\2\u018e\u018f")
        buf.write("\7^\2\2\u018f\u0197\7p\2\2\u0190\u0191\7^\2\2\u0191\u0197")
        buf.write("\7v\2\2\u0192\u0193\7^\2\2\u0193\u0197\7$\2\2\u0194\u0195")
        buf.write("\7^\2\2\u0195\u0197\7^\2\2\u0196\u0188\3\2\2\2\u0196\u018a")
        buf.write("\3\2\2\2\u0196\u018c\3\2\2\2\u0196\u018e\3\2\2\2\u0196")
        buf.write("\u0190\3\2\2\2\u0196\u0192\3\2\2\2\u0196\u0194\3\2\2\2")
        buf.write("\u0197x\3\2\2\2\u0198\u019b\n\b\2\2\u0199\u019b\5w<\2")
        buf.write("\u019a\u0198\3\2\2\2\u019a\u0199\3\2\2\2\u019bz\3\2\2")
        buf.write("\2\u019c\u01a0\7$\2\2\u019d\u019f\5y=\2\u019e\u019d\3")
        buf.write("\2\2\2\u019f\u01a2\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u01a1")
        buf.write("\3\2\2\2\u01a1\u01a3\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a3")
        buf.write("\u01a4\7$\2\2\u01a4\u01a5\b>\3\2\u01a5|\3\2\2\2\u01a6")
        buf.write("\u01a8\t\t\2\2\u01a7\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2")
        buf.write("\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\3")
        buf.write("\2\2\2\u01ab\u01ac\b?\2\2\u01ac~\3\2\2\2\u01ad\u01b1\7")
        buf.write("$\2\2\u01ae\u01b0\5y=\2\u01af\u01ae\3\2\2\2\u01b0\u01b3")
        buf.write("\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2")
        buf.write("\u01b4\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4\u01b5\7^\2\2")
        buf.write("\u01b5\u01b6\n\n\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8\b")
        buf.write("@\4\2\u01b8\u0080\3\2\2\2\u01b9\u01bd\7$\2\2\u01ba\u01bc")
        buf.write("\5y=\2\u01bb\u01ba\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd\u01bb")
        buf.write("\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01c0\3\2\2\2\u01bf")
        buf.write("\u01bd\3\2\2\2\u01c0\u01c1\bA\5\2\u01c1\u0082\3\2\2\2")
        buf.write("\u01c2\u01c3\13\2\2\2\u01c3\u01c4\bB\6\2\u01c4\u0084\3")
        buf.write("\2\2\2\25\2\u008e\u0092\u009a\u009f\u015d\u0163\u0169")
        buf.write("\u0171\u0176\u017b\u0182\u0186\u0196\u019a\u01a0\u01a9")
        buf.write("\u01b1\u01bd\7\b\2\2\3>\2\3@\3\3A\4\3B\5")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    COMMENT = 2
    BREAK = 3
    CONTINUE = 4
    IF = 5
    ELSE = 6
    FOR = 7
    TRUE = 8
    FALSE = 9
    INT = 10
    FLOAT = 11
    BOOL = 12
    STRING = 13
    RETURN = 14
    NULL = 15
    CLASS = 16
    CONSTRUCTOR = 17
    VAR = 18
    SELF = 19
    NEW = 20
    VOID = 21
    CONST = 22
    FUNC = 23
    PLUS = 24
    MINUS = 25
    MULTI = 26
    DIVFLO = 27
    DIVINT = 28
    DIFFROM = 29
    DIFF = 30
    AND = 31
    OR = 32
    COMPEQ = 33
    ASSIGN = 34
    EQUAL = 35
    LESSEQ = 36
    LESS = 37
    MOREEQ = 38
    MOR = 39
    SPACING = 40
    MODU = 41
    LB = 42
    RB = 43
    SLB = 44
    SRB = 45
    DOT = 46
    CM = 47
    SC = 48
    COLON = 49
    LCB = 50
    RCB = 51
    ATIDENTIFIER = 52
    IDENTIFIER = 53
    INTLIT = 54
    FLOATLIT = 55
    STRINGLIT = 56
    WS = 57
    ILLEGAL_ESCAPE = 58
    UNCLOSED_STRING = 59
    ERROR_CHAR = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<-'", "'break'", "'continue'", "'if'", "'else'", "'for'", 
            "'true'", "'false'", "'int'", "'float'", "'bool'", "'string'", 
            "'return'", "'null'", "'class'", "'constructor'", "'var'", "'self'", 
            "'new'", "'void'", "'const'", "'func'", "'+'", "'-'", "'*'", 
            "'/'", "'\\'", "'!='", "'!'", "'&&'", "'||'", "'=='", "':='", 
            "'='", "'<='", "'<'", "'>='", "'>'", "'^'", "'%'", "'('", "')'", 
            "'['", "']'", "'.'", "','", "';'", "':'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", 
            "FALSE", "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", 
            "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", "CONST", 
            "FUNC", "PLUS", "MINUS", "MULTI", "DIVFLO", "DIVINT", "DIFFROM", 
            "DIFF", "AND", "OR", "COMPEQ", "ASSIGN", "EQUAL", "LESSEQ", 
            "LESS", "MOREEQ", "MOR", "SPACING", "MODU", "LB", "RB", "SLB", 
            "SRB", "DOT", "CM", "SC", "COLON", "LCB", "RCB", "ATIDENTIFIER", 
            "IDENTIFIER", "INTLIT", "FLOATLIT", "STRINGLIT", "WS", "ILLEGAL_ESCAPE", 
            "UNCLOSED_STRING", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "COMMENT", "BREAK", "CONTINUE", "IF", "ELSE", 
                  "FOR", "TRUE", "FALSE", "INT", "FLOAT", "BOOL", "STRING", 
                  "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", 
                  "NEW", "VOID", "CONST", "FUNC", "PLUS", "MINUS", "MULTI", 
                  "DIVFLO", "DIVINT", "DIFFROM", "DIFF", "AND", "OR", "COMPEQ", 
                  "ASSIGN", "EQUAL", "LESSEQ", "LESS", "MOREEQ", "MOR", 
                  "SPACING", "MODU", "LB", "RB", "SLB", "SRB", "DOT", "CM", 
                  "SC", "COLON", "LCB", "RCB", "ATIDENTIFIER", "IDENTIFIER", 
                  "Int", "INTLIT", "Decimal", "Exponent", "FLOATLIT", "ESCSEQ", 
                  "CHARLIT", "STRINGLIT", "WS", "ILLEGAL_ESCAPE", "UNCLOSED_STRING", 
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
            actions[60] = self.STRINGLIT_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            actions[63] = self.UNCLOSED_STRING_action 
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
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = self.text[1:]
                raise IllegalEscape(self.text)

     

    def UNCLOSED_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             
                self.text = self.text[1:]
                raise UncloseString(self.text)

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


