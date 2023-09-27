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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01f4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3")
        buf.write("$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3")
        buf.write("-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\5\64\u0147\n\64\3\64\3\64\7\64\u014b\n\64")
        buf.write("\f\64\16\64\u014e\13\64\5\64\u0150\n\64\3\65\3\65\3\65")
        buf.write("\3\65\3\65\5\65\u0157\n\65\3\65\3\65\5\65\u015b\n\65\3")
        buf.write("\66\5\66\u015e\n\66\3\66\6\66\u0161\n\66\r\66\16\66\u0162")
        buf.write("\3\67\3\67\3\67\6\67\u0168\n\67\r\67\16\67\u0169\38\3")
        buf.write("8\58\u016e\n8\39\39\39\39\39\39\39\39\39\39\39\39\39\3")
        buf.write("9\59\u017e\n9\3:\3:\3:\3:\5:\u0184\n:\3;\3;\7;\u0188\n")
        buf.write(";\f;\16;\u018b\13;\3;\3;\3;\3<\3<\3<\3<\3<\5<\u0195\n")
        buf.write("<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\7=\u01a2\n=\f=\16=")
        buf.write("\u01a5\13=\3=\5=\u01a8\n=\3=\3=\3>\3>\7>\u01ae\n>\f>\16")
        buf.write(">\u01b1\13>\3>\3>\6>\u01b5\n>\r>\16>\u01b6\3>\5>\u01ba")
        buf.write("\n>\3?\3?\7?\u01be\n?\f?\16?\u01c1\13?\3@\3@\6@\u01c5")
        buf.write("\n@\r@\16@\u01c6\3A\3A\7A\u01cb\nA\fA\16A\u01ce\13A\3")
        buf.write("B\6B\u01d1\nB\rB\16B\u01d2\3B\3B\3C\3C\3C\3D\3D\3D\3D")
        buf.write("\3D\3D\7D\u01e0\nD\fD\16D\u01e3\13D\3D\3D\3E\3E\3E\3E")
        buf.write("\7E\u01eb\nE\fE\16E\u01ee\13E\3E\3E\3E\3E\3E\3\u01a3\2")
        buf.write("F\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\2m\2o\67q\2")
        buf.write("s\2u8w9y:{;}<\177=\u0081>\u0083?\u0085@\u0087A\u0089B")
        buf.write("\3\2\16\3\2\63;\3\2\62;\4\2GGgg\4\2--//\t\2\f\f\17\17")
        buf.write("$$))GHQQ^^\3\3\f\f\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f")
        buf.write("\17\17\"\"\t\2))^^ddhhppttvv\6\2\13\f\17\17$$^^\6\2\f")
        buf.write("\f\17\17$$^^\2\u0210\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2o\3\2\2\2\2u\3\2")
        buf.write("\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\3\u008b\3\2\2\2\5\u008e")
        buf.write("\3\2\2\2\7\u0094\3\2\2\2\t\u009d\3\2\2\2\13\u00a0\3\2")
        buf.write("\2\2\r\u00a5\3\2\2\2\17\u00a9\3\2\2\2\21\u00ae\3\2\2\2")
        buf.write("\23\u00b4\3\2\2\2\25\u00b8\3\2\2\2\27\u00be\3\2\2\2\31")
        buf.write("\u00c3\3\2\2\2\33\u00ca\3\2\2\2\35\u00d1\3\2\2\2\37\u00d6")
        buf.write("\3\2\2\2!\u00dc\3\2\2\2#\u00e8\3\2\2\2%\u00ec\3\2\2\2")
        buf.write("\'\u00f1\3\2\2\2)\u00f5\3\2\2\2+\u00fa\3\2\2\2-\u0100")
        buf.write("\3\2\2\2/\u0105\3\2\2\2\61\u0107\3\2\2\2\63\u0109\3\2")
        buf.write("\2\2\65\u010b\3\2\2\2\67\u010d\3\2\2\29\u010f\3\2\2\2")
        buf.write(";\u0112\3\2\2\2=\u0115\3\2\2\2?\u0118\3\2\2\2A\u011b\3")
        buf.write("\2\2\2C\u011e\3\2\2\2E\u0121\3\2\2\2G\u0124\3\2\2\2I\u0126")
        buf.write("\3\2\2\2K\u0128\3\2\2\2M\u012a\3\2\2\2O\u012c\3\2\2\2")
        buf.write("Q\u012e\3\2\2\2S\u0130\3\2\2\2U\u0132\3\2\2\2W\u0134\3")
        buf.write("\2\2\2Y\u0136\3\2\2\2[\u0138\3\2\2\2]\u013a\3\2\2\2_\u013c")
        buf.write("\3\2\2\2a\u013e\3\2\2\2c\u0140\3\2\2\2e\u0142\3\2\2\2")
        buf.write("g\u014f\3\2\2\2i\u015a\3\2\2\2k\u015d\3\2\2\2m\u0164\3")
        buf.write("\2\2\2o\u016d\3\2\2\2q\u017d\3\2\2\2s\u0183\3\2\2\2u\u0185")
        buf.write("\3\2\2\2w\u018f\3\2\2\2y\u019c\3\2\2\2{\u01b9\3\2\2\2")
        buf.write("}\u01bb\3\2\2\2\177\u01c2\3\2\2\2\u0081\u01c8\3\2\2\2")
        buf.write("\u0083\u01d0\3\2\2\2\u0085\u01d6\3\2\2\2\u0087\u01d9\3")
        buf.write("\2\2\2\u0089\u01e6\3\2\2\2\u008b\u008c\7>\2\2\u008c\u008d")
        buf.write("\7/\2\2\u008d\4\3\2\2\2\u008e\u008f\7d\2\2\u008f\u0090")
        buf.write("\7t\2\2\u0090\u0091\7g\2\2\u0091\u0092\7c\2\2\u0092\u0093")
        buf.write("\7m\2\2\u0093\6\3\2\2\2\u0094\u0095\7e\2\2\u0095\u0096")
        buf.write("\7q\2\2\u0096\u0097\7p\2\2\u0097\u0098\7v\2\2\u0098\u0099")
        buf.write("\7k\2\2\u0099\u009a\7p\2\2\u009a\u009b\7w\2\2\u009b\u009c")
        buf.write("\7g\2\2\u009c\b\3\2\2\2\u009d\u009e\7k\2\2\u009e\u009f")
        buf.write("\7h\2\2\u009f\n\3\2\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2")
        buf.write("\7n\2\2\u00a2\u00a3\7u\2\2\u00a3\u00a4\7g\2\2\u00a4\f")
        buf.write("\3\2\2\2\u00a5\u00a6\7h\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8")
        buf.write("\7t\2\2\u00a8\16\3\2\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab")
        buf.write("\7t\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad\7g\2\2\u00ad\20")
        buf.write("\3\2\2\2\u00ae\u00af\7h\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1")
        buf.write("\7n\2\2\u00b1\u00b2\7u\2\2\u00b2\u00b3\7g\2\2\u00b3\22")
        buf.write("\3\2\2\2\u00b4\u00b5\7k\2\2\u00b5\u00b6\7p\2\2\u00b6\u00b7")
        buf.write("\7v\2\2\u00b7\24\3\2\2\2\u00b8\u00b9\7h\2\2\u00b9\u00ba")
        buf.write("\7n\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd")
        buf.write("\7v\2\2\u00bd\26\3\2\2\2\u00be\u00bf\7d\2\2\u00bf\u00c0")
        buf.write("\7q\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2\7n\2\2\u00c2\30")
        buf.write("\3\2\2\2\u00c3\u00c4\7u\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6")
        buf.write("\7t\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9")
        buf.write("\7i\2\2\u00c9\32\3\2\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc")
        buf.write("\7g\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce\7w\2\2\u00ce\u00cf")
        buf.write("\7t\2\2\u00cf\u00d0\7p\2\2\u00d0\34\3\2\2\2\u00d1\u00d2")
        buf.write("\7p\2\2\u00d2\u00d3\7w\2\2\u00d3\u00d4\7n\2\2\u00d4\u00d5")
        buf.write("\7n\2\2\u00d5\36\3\2\2\2\u00d6\u00d7\7e\2\2\u00d7\u00d8")
        buf.write("\7n\2\2\u00d8\u00d9\7c\2\2\u00d9\u00da\7u\2\2\u00da\u00db")
        buf.write("\7u\2\2\u00db \3\2\2\2\u00dc\u00dd\7e\2\2\u00dd\u00de")
        buf.write("\7q\2\2\u00de\u00df\7p\2\2\u00df\u00e0\7u\2\2\u00e0\u00e1")
        buf.write("\7v\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3\7w\2\2\u00e3\u00e4")
        buf.write("\7e\2\2\u00e4\u00e5\7v\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7")
        buf.write("\7t\2\2\u00e7\"\3\2\2\2\u00e8\u00e9\7x\2\2\u00e9\u00ea")
        buf.write("\7c\2\2\u00ea\u00eb\7t\2\2\u00eb$\3\2\2\2\u00ec\u00ed")
        buf.write("\7u\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef\7n\2\2\u00ef\u00f0")
        buf.write("\7h\2\2\u00f0&\3\2\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3")
        buf.write("\7g\2\2\u00f3\u00f4\7y\2\2\u00f4(\3\2\2\2\u00f5\u00f6")
        buf.write("\7x\2\2\u00f6\u00f7\7q\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9")
        buf.write("\7f\2\2\u00f9*\3\2\2\2\u00fa\u00fb\7e\2\2\u00fb\u00fc")
        buf.write("\7q\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7u\2\2\u00fe\u00ff")
        buf.write("\7v\2\2\u00ff,\3\2\2\2\u0100\u0101\7h\2\2\u0101\u0102")
        buf.write("\7w\2\2\u0102\u0103\7p\2\2\u0103\u0104\7e\2\2\u0104.\3")
        buf.write("\2\2\2\u0105\u0106\7-\2\2\u0106\60\3\2\2\2\u0107\u0108")
        buf.write("\7/\2\2\u0108\62\3\2\2\2\u0109\u010a\7,\2\2\u010a\64\3")
        buf.write("\2\2\2\u010b\u010c\7\61\2\2\u010c\66\3\2\2\2\u010d\u010e")
        buf.write("\7^\2\2\u010e8\3\2\2\2\u010f\u0110\7(\2\2\u0110\u0111")
        buf.write("\7(\2\2\u0111:\3\2\2\2\u0112\u0113\7~\2\2\u0113\u0114")
        buf.write("\7~\2\2\u0114<\3\2\2\2\u0115\u0116\7?\2\2\u0116\u0117")
        buf.write("\7?\2\2\u0117>\3\2\2\2\u0118\u0119\7<\2\2\u0119\u011a")
        buf.write("\7?\2\2\u011a@\3\2\2\2\u011b\u011c\7#\2\2\u011c\u011d")
        buf.write("\7?\2\2\u011dB\3\2\2\2\u011e\u011f\7>\2\2\u011f\u0120")
        buf.write("\7?\2\2\u0120D\3\2\2\2\u0121\u0122\7@\2\2\u0122\u0123")
        buf.write("\7?\2\2\u0123F\3\2\2\2\u0124\u0125\7#\2\2\u0125H\3\2\2")
        buf.write("\2\u0126\u0127\7?\2\2\u0127J\3\2\2\2\u0128\u0129\7>\2")
        buf.write("\2\u0129L\3\2\2\2\u012a\u012b\7@\2\2\u012bN\3\2\2\2\u012c")
        buf.write("\u012d\7`\2\2\u012dP\3\2\2\2\u012e\u012f\7\'\2\2\u012f")
        buf.write("R\3\2\2\2\u0130\u0131\7*\2\2\u0131T\3\2\2\2\u0132\u0133")
        buf.write("\7+\2\2\u0133V\3\2\2\2\u0134\u0135\7]\2\2\u0135X\3\2\2")
        buf.write("\2\u0136\u0137\7_\2\2\u0137Z\3\2\2\2\u0138\u0139\7\60")
        buf.write("\2\2\u0139\\\3\2\2\2\u013a\u013b\7.\2\2\u013b^\3\2\2\2")
        buf.write("\u013c\u013d\7=\2\2\u013d`\3\2\2\2\u013e\u013f\7<\2\2")
        buf.write("\u013fb\3\2\2\2\u0140\u0141\7}\2\2\u0141d\3\2\2\2\u0142")
        buf.write("\u0143\7\177\2\2\u0143f\3\2\2\2\u0144\u0150\7\62\2\2\u0145")
        buf.write("\u0147\7/\2\2\u0146\u0145\3\2\2\2\u0146\u0147\3\2\2\2")
        buf.write("\u0147\u0148\3\2\2\2\u0148\u014c\t\2\2\2\u0149\u014b\t")
        buf.write("\3\2\2\u014a\u0149\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a")
        buf.write("\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u0150\3\2\2\2\u014e")
        buf.write("\u014c\3\2\2\2\u014f\u0144\3\2\2\2\u014f\u0146\3\2\2\2")
        buf.write("\u0150h\3\2\2\2\u0151\u0152\5g\64\2\u0152\u0153\5k\66")
        buf.write("\2\u0153\u015b\3\2\2\2\u0154\u0156\5g\64\2\u0155\u0157")
        buf.write("\5k\66\2\u0156\u0155\3\2\2\2\u0156\u0157\3\2\2\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u0159\5m\67\2\u0159\u015b\3\2\2\2")
        buf.write("\u015a\u0151\3\2\2\2\u015a\u0154\3\2\2\2\u015bj\3\2\2")
        buf.write("\2\u015c\u015e\7\60\2\2\u015d\u015c\3\2\2\2\u015d\u015e")
        buf.write("\3\2\2\2\u015e\u0160\3\2\2\2\u015f\u0161\t\3\2\2\u0160")
        buf.write("\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0160\3\2\2\2")
        buf.write("\u0162\u0163\3\2\2\2\u0163l\3\2\2\2\u0164\u0165\t\4\2")
        buf.write("\2\u0165\u0167\t\5\2\2\u0166\u0168\t\3\2\2\u0167\u0166")
        buf.write("\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u0167\3\2\2\2\u0169")
        buf.write("\u016a\3\2\2\2\u016an\3\2\2\2\u016b\u016e\5\17\b\2\u016c")
        buf.write("\u016e\5\21\t\2\u016d\u016b\3\2\2\2\u016d\u016c\3\2\2")
        buf.write("\2\u016ep\3\2\2\2\u016f\u0170\7^\2\2\u0170\u017e\7d\2")
        buf.write("\2\u0171\u0172\7^\2\2\u0172\u017e\7h\2\2\u0173\u0174\7")
        buf.write("^\2\2\u0174\u017e\7t\2\2\u0175\u0176\7^\2\2\u0176\u017e")
        buf.write("\7p\2\2\u0177\u0178\7^\2\2\u0178\u017e\7v\2\2\u0179\u017a")
        buf.write("\7^\2\2\u017a\u017e\7$\2\2\u017b\u017c\7^\2\2\u017c\u017e")
        buf.write("\7^\2\2\u017d\u016f\3\2\2\2\u017d\u0171\3\2\2\2\u017d")
        buf.write("\u0173\3\2\2\2\u017d\u0175\3\2\2\2\u017d\u0177\3\2\2\2")
        buf.write("\u017d\u0179\3\2\2\2\u017d\u017b\3\2\2\2\u017er\3\2\2")
        buf.write("\2\u017f\u0184\n\6\2\2\u0180\u0184\5q9\2\u0181\u0182\7")
        buf.write(")\2\2\u0182\u0184\7$\2\2\u0183\u017f\3\2\2\2\u0183\u0180")
        buf.write("\3\2\2\2\u0183\u0181\3\2\2\2\u0184t\3\2\2\2\u0185\u0189")
        buf.write("\7$\2\2\u0186\u0188\5s:\2\u0187\u0186\3\2\2\2\u0188\u018b")
        buf.write("\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a")
        buf.write("\u018c\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u018d\7$\2\2")
        buf.write("\u018d\u018e\b;\2\2\u018ev\3\2\2\2\u018f\u0190\7\61\2")
        buf.write("\2\u0190\u0191\7\61\2\2\u0191\u0192\7,\2\2\u0192\u0194")
        buf.write("\3\2\2\2\u0193\u0195\13\2\2\2\u0194\u0193\3\2\2\2\u0194")
        buf.write("\u0195\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197\7,\2\2")
        buf.write("\u0197\u0198\7\61\2\2\u0198\u0199\7\61\2\2\u0199\u019a")
        buf.write("\3\2\2\2\u019a\u019b\b<\3\2\u019bx\3\2\2\2\u019c\u019d")
        buf.write("\7\61\2\2\u019d\u019e\7\61\2\2\u019e\u019f\7\61\2\2\u019f")
        buf.write("\u01a3\3\2\2\2\u01a0\u01a2\13\2\2\2\u01a1\u01a0\3\2\2")
        buf.write("\2\u01a2\u01a5\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a3\u01a1")
        buf.write("\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6")
        buf.write("\u01a8\t\7\2\2\u01a7\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2")
        buf.write("\u01a9\u01aa\b=\3\2\u01aaz\3\2\2\2\u01ab\u01af\t\b\2\2")
        buf.write("\u01ac\u01ae\t\t\2\2\u01ad\u01ac\3\2\2\2\u01ae\u01b1\3")
        buf.write("\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01ba")
        buf.write("\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b4\7B\2\2\u01b3")
        buf.write("\u01b5\t\t\2\2\u01b4\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2")
        buf.write("\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01ba\3")
        buf.write("\2\2\2\u01b8\u01ba\5%\23\2\u01b9\u01ab\3\2\2\2\u01b9\u01b2")
        buf.write("\3\2\2\2\u01b9\u01b8\3\2\2\2\u01ba|\3\2\2\2\u01bb\u01bf")
        buf.write("\t\b\2\2\u01bc\u01be\t\t\2\2\u01bd\u01bc\3\2\2\2\u01be")
        buf.write("\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2")
        buf.write("\u01c0~\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c4\7B\2\2")
        buf.write("\u01c3\u01c5\t\t\2\2\u01c4\u01c3\3\2\2\2\u01c5\u01c6\3")
        buf.write("\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u0080")
        buf.write("\3\2\2\2\u01c8\u01cc\t\2\2\2\u01c9\u01cb\t\3\2\2\u01ca")
        buf.write("\u01c9\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2")
        buf.write("\u01cc\u01cd\3\2\2\2\u01cd\u0082\3\2\2\2\u01ce\u01cc\3")
        buf.write("\2\2\2\u01cf\u01d1\t\n\2\2\u01d0\u01cf\3\2\2\2\u01d1\u01d2")
        buf.write("\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3")
        buf.write("\u01d4\3\2\2\2\u01d4\u01d5\bB\3\2\u01d5\u0084\3\2\2\2")
        buf.write("\u01d6\u01d7\13\2\2\2\u01d7\u01d8\bC\4\2\u01d8\u0086\3")
        buf.write("\2\2\2\u01d9\u01e1\7$\2\2\u01da\u01db\7)\2\2\u01db\u01e0")
        buf.write("\7$\2\2\u01dc\u01dd\7^\2\2\u01dd\u01e0\t\13\2\2\u01de")
        buf.write("\u01e0\n\f\2\2\u01df\u01da\3\2\2\2\u01df\u01dc\3\2\2\2")
        buf.write("\u01df\u01de\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3")
        buf.write("\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e4\3\2\2\2\u01e3\u01e1")
        buf.write("\3\2\2\2\u01e4\u01e5\bD\5\2\u01e5\u0088\3\2\2\2\u01e6")
        buf.write("\u01ec\7$\2\2\u01e7\u01e8\7^\2\2\u01e8\u01eb\t\13\2\2")
        buf.write("\u01e9\u01eb\n\r\2\2\u01ea\u01e7\3\2\2\2\u01ea\u01e9\3")
        buf.write("\2\2\2\u01eb\u01ee\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01ed")
        buf.write("\3\2\2\2\u01ed\u01ef\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ef")
        buf.write("\u01f0\7^\2\2\u01f0\u01f1\n\13\2\2\u01f1\u01f2\3\2\2\2")
        buf.write("\u01f2\u01f3\bE\6\2\u01f3\u008a\3\2\2\2\35\2\u0146\u014c")
        buf.write("\u014f\u0156\u015a\u015d\u0162\u0169\u016d\u017d\u0183")
        buf.write("\u0189\u0194\u01a3\u01a7\u01af\u01b6\u01b9\u01bf\u01c6")
        buf.write("\u01cc\u01d2\u01df\u01e1\u01ea\u01ec\7\3;\2\b\2\2\3C\3")
        buf.write("\3D\4\3E\5")
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
    BOOLLIT = 53
    STRINGLIT = 54
    BLOCKCMT = 55
    LINECMT = 56
    IDENTIFIER = 57
    ID = 58
    ATIDENTIFIER = 59
    ARRAYSIZE = 60
    WS = 61
    ERROR_CHAR = 62
    UNCLOSED_STRING = 63
    ILLEGAL_ESCAPE = 64

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
            "COLON", "LCB", "RCB", "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", 
            "BLOCKCMT", "LINECMT", "IDENTIFIER", "ID", "ATIDENTIFIER", "ARRAYSIZE", 
            "WS", "ERROR_CHAR", "UNCLOSED_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", 
                  "FALSE", "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", 
                  "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", 
                  "CONST", "FUNC", "PLUS", "MINUS", "MULTIPLY", "DIVIDE_FLOAT", 
                  "DIVIDE_INT", "AND", "OR", "EQUAL", "ASSIGN", "NEQ", "LEQ", 
                  "GEQ", "DIFF", "DECLARE", "LE", "GE", "CONCAT", "MOD", 
                  "LRB", "RRB", "LSB", "RSB", "DOT", "CM", "SM", "COLON", 
                  "LCB", "RCB", "INTLIT", "FLOATLIT", "DEC", "EXP", "BOOLLIT", 
                  "ESCAPESEQ", "CHAR_LIT", "STRINGLIT", "BLOCKCMT", "LINECMT", 
                  "IDENTIFIER", "ID", "ATIDENTIFIER", "ARRAYSIZE", "WS", 
                  "ERROR_CHAR", "UNCLOSED_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[57] = self.STRINGLIT_action 
            actions[65] = self.ERROR_CHAR_action 
            actions[66] = self.UNCLOSED_STRING_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSED_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:]; raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text[1:]; raise IllegalEscape(self.text)
     


