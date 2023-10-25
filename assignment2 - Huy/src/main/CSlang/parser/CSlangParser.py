# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3>")
        buf.write("\u022d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0082\n")
        buf.write("\3\3\4\3\4\5\4\u0086\n\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\5\5\u0091\n\5\3\6\3\6\5\6\u0095\n\6\3\7\3\7\3\b")
        buf.write("\3\b\5\b\u009b\n\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\5\13\u00ac\n\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00b7\n\f\3\f\3\f\3\f")
        buf.write("\3\f\5\f\u00bd\n\f\3\r\3\r\3\16\3\16\3\16\3\16\5\16\u00c5")
        buf.write("\n\16\3\17\3\17\3\20\3\20\5\20\u00cb\n\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\5\21\u00d5\n\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\5\23\u00e2")
        buf.write("\n\23\3\24\3\24\5\24\u00e6\n\24\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\5\25\u00f1\n\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u00fd\n\26\3")
        buf.write("\27\3\27\3\30\3\30\3\30\3\30\3\30\5\30\u0106\n\30\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\5\32\u0111\n")
        buf.write("\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\5\37\u0120\n\37\3 \3 \3 \3 \3 \5 \u0127")
        buf.write("\n \3!\3!\3!\3!\3!\3!\3!\7!\u0130\n!\f!\16!\u0133\13!")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u013c\n\"\f\"\16\"\u013f")
        buf.write("\13\"\3#\3#\3#\3#\3#\3#\3#\7#\u0148\n#\f#\16#\u014b\13")
        buf.write("#\3$\3$\3$\5$\u0150\n$\3%\3%\3%\5%\u0155\n%\3&\3&\3&\3")
        buf.write("&\3&\3&\5&\u015d\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0166")
        buf.write("\n\'\3\'\3\'\3\'\3\'\5\'\u016c\n\'\3\'\3\'\3\'\3\'\7\'")
        buf.write("\u0172\n\'\f\'\16\'\u0175\13\'\3(\3(\5(\u0179\n(\3(\3")
        buf.write("(\5(\u017d\n(\3(\3(\5(\u0181\n(\3(\3(\5(\u0185\n(\3(\3")
        buf.write("(\3(\3(\3(\5(\u018c\n(\3)\3)\5)\u0190\n)\3*\3*\3*\3*\3")
        buf.write("*\5*\u0197\n*\3+\3+\3+\5+\u019c\n+\3,\3,\3,\3,\3,\3,\3")
        buf.write("-\3-\5-\u01a6\n-\3.\3.\3.\3.\3.\5.\u01ad\n.\3/\3/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\60\5\60\u01b7\n\60\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\5\61\u01c2\n\61\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u01cd\n\62\3")
        buf.write("\63\3\63\5\63\u01d1\n\63\3\63\5\63\u01d4\n\63\3\63\3\63")
        buf.write("\3\63\3\63\3\64\3\64\5\64\u01dc\n\64\3\64\3\64\3\64\3")
        buf.write("\64\5\64\u01e2\n\64\3\65\3\65\5\65\u01e6\n\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\5\66\u01ed\n\66\3\66\3\66\3\66\3\66\5")
        buf.write("\66\u01f3\n\66\5\66\u01f5\n\66\3\67\3\67\5\67\u01f9\n")
        buf.write("\67\3\67\3\67\3\67\5\67\u01fe\n\67\3\67\3\67\5\67\u0202")
        buf.write("\n\67\3\67\3\67\3\67\5\67\u0207\n\67\5\67\u0209\n\67\3")
        buf.write("8\38\38\38\38\38\38\38\39\39\39\3:\3:\3:\3;\3;\3;\5;\u021c")
        buf.write("\n;\3;\3;\3<\3<\5<\u0222\n<\3<\3<\3<\3<\3<\3<\3=\3=\3")
        buf.write("=\3=\2\6@BDL>\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 ")
        buf.write("\"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtv")
        buf.write("x\2\n\4\2\24\24\30\30\3\2\f\17\3\2\66\67\3\2\n\13\5\2")
        buf.write("\37\37##&)\3\2!\"\3\2\32\33\4\2\34\36++\2\u0236\2z\3\2")
        buf.write("\2\2\4\u0081\3\2\2\2\6\u0083\3\2\2\2\b\u0090\3\2\2\2\n")
        buf.write("\u0094\3\2\2\2\f\u0096\3\2\2\2\16\u009a\3\2\2\2\20\u009c")
        buf.write("\3\2\2\2\22\u00a0\3\2\2\2\24\u00ab\3\2\2\2\26\u00bc\3")
        buf.write("\2\2\2\30\u00be\3\2\2\2\32\u00c4\3\2\2\2\34\u00c6\3\2")
        buf.write("\2\2\36\u00ca\3\2\2\2 \u00cc\3\2\2\2\"\u00d8\3\2\2\2$")
        buf.write("\u00e1\3\2\2\2&\u00e5\3\2\2\2(\u00f0\3\2\2\2*\u00fc\3")
        buf.write("\2\2\2,\u00fe\3\2\2\2.\u0105\3\2\2\2\60\u0107\3\2\2\2")
        buf.write("\62\u0110\3\2\2\2\64\u0112\3\2\2\2\66\u0114\3\2\2\28\u0116")
        buf.write("\3\2\2\2:\u0118\3\2\2\2<\u011f\3\2\2\2>\u0126\3\2\2\2")
        buf.write("@\u0128\3\2\2\2B\u0134\3\2\2\2D\u0140\3\2\2\2F\u014f\3")
        buf.write("\2\2\2H\u0154\3\2\2\2J\u015c\3\2\2\2L\u015e\3\2\2\2N\u018b")
        buf.write("\3\2\2\2P\u018f\3\2\2\2R\u0196\3\2\2\2T\u019b\3\2\2\2")
        buf.write("V\u019d\3\2\2\2X\u01a5\3\2\2\2Z\u01ac\3\2\2\2\\\u01ae")
        buf.write("\3\2\2\2^\u01b6\3\2\2\2`\u01c1\3\2\2\2b\u01c3\3\2\2\2")
        buf.write("d\u01d3\3\2\2\2f\u01d9\3\2\2\2h\u01e3\3\2\2\2j\u01ea\3")
        buf.write("\2\2\2l\u01f6\3\2\2\2n\u020a\3\2\2\2p\u0212\3\2\2\2r\u0215")
        buf.write("\3\2\2\2t\u0218\3\2\2\2v\u0221\3\2\2\2x\u0229\3\2\2\2")
        buf.write("z{\5\4\3\2{|\7\2\2\3|\3\3\2\2\2}~\5\6\4\2~\177\5\4\3\2")
        buf.write("\177\u0082\3\2\2\2\u0080\u0082\3\2\2\2\u0081}\3\2\2\2")
        buf.write("\u0081\u0080\3\2\2\2\u0082\5\3\2\2\2\u0083\u0085\7\22")
        buf.write("\2\2\u0084\u0086\5x=\2\u0085\u0084\3\2\2\2\u0085\u0086")
        buf.write("\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\7\67\2\2\u0088")
        buf.write("\u0089\7\64\2\2\u0089\u008a\5\b\5\2\u008a\u008b\7\65\2")
        buf.write("\2\u008b\7\3\2\2\2\u008c\u008d\5\n\6\2\u008d\u008e\5\b")
        buf.write("\5\2\u008e\u0091\3\2\2\2\u008f\u0091\3\2\2\2\u0090\u008c")
        buf.write("\3\2\2\2\u0090\u008f\3\2\2\2\u0091\t\3\2\2\2\u0092\u0095")
        buf.write("\5\16\b\2\u0093\u0095\5\36\20\2\u0094\u0092\3\2\2\2\u0094")
        buf.write("\u0093\3\2\2\2\u0095\13\3\2\2\2\u0096\u0097\t\2\2\2\u0097")
        buf.write("\r\3\2\2\2\u0098\u009b\5\20\t\2\u0099\u009b\5\22\n\2\u009a")
        buf.write("\u0098\3\2\2\2\u009a\u0099\3\2\2\2\u009b\17\3\2\2\2\u009c")
        buf.write("\u009d\5\f\7\2\u009d\u009e\5\26\f\2\u009e\u009f\7\62\2")
        buf.write("\2\u009f\21\3\2\2\2\u00a0\u00a1\5\f\7\2\u00a1\u00a2\5")
        buf.write("\24\13\2\u00a2\u00a3\7\63\2\2\u00a3\u00a4\5\30\r\2\u00a4")
        buf.write("\u00a5\7\62\2\2\u00a5\23\3\2\2\2\u00a6\u00a7\5\34\17\2")
        buf.write("\u00a7\u00a8\7\61\2\2\u00a8\u00a9\5\24\13\2\u00a9\u00ac")
        buf.write("\3\2\2\2\u00aa\u00ac\5\34\17\2\u00ab\u00a6\3\2\2\2\u00ab")
        buf.write("\u00aa\3\2\2\2\u00ac\25\3\2\2\2\u00ad\u00ae\5\34\17\2")
        buf.write("\u00ae\u00af\7\61\2\2\u00af\u00b0\5\26\f\2\u00b0\u00b1")
        buf.write("\7\61\2\2\u00b1\u00b2\5<\37\2\u00b2\u00bd\3\2\2\2\u00b3")
        buf.write("\u00b4\5\34\17\2\u00b4\u00b6\7\63\2\2\u00b5\u00b7\5\60")
        buf.write("\31\2\u00b6\u00b5\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8")
        buf.write("\3\2\2\2\u00b8\u00b9\5\30\r\2\u00b9\u00ba\7%\2\2\u00ba")
        buf.write("\u00bb\5<\37\2\u00bb\u00bd\3\2\2\2\u00bc\u00ad\3\2\2\2")
        buf.write("\u00bc\u00b3\3\2\2\2\u00bd\27\3\2\2\2\u00be\u00bf\t\3")
        buf.write("\2\2\u00bf\31\3\2\2\2\u00c0\u00c1\7\67\2\2\u00c1\u00c2")
        buf.write("\7\61\2\2\u00c2\u00c5\5\32\16\2\u00c3\u00c5\7\67\2\2\u00c4")
        buf.write("\u00c0\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5\33\3\2\2\2\u00c6")
        buf.write("\u00c7\t\4\2\2\u00c7\35\3\2\2\2\u00c8\u00cb\5 \21\2\u00c9")
        buf.write("\u00cb\5\"\22\2\u00ca\u00c8\3\2\2\2\u00ca\u00c9\3\2\2")
        buf.write("\2\u00cb\37\3\2\2\2\u00cc\u00cd\7\31\2\2\u00cd\u00ce\5")
        buf.write("\34\17\2\u00ce\u00cf\7,\2\2\u00cf\u00d0\5$\23\2\u00d0")
        buf.write("\u00d1\7-\2\2\u00d1\u00d4\7\63\2\2\u00d2\u00d5\5\30\r")
        buf.write("\2\u00d3\u00d5\7\27\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d3")
        buf.write("\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7\5\\/\2\u00d7")
        buf.write("!\3\2\2\2\u00d8\u00d9\7\31\2\2\u00d9\u00da\7\23\2\2\u00da")
        buf.write("\u00db\7,\2\2\u00db\u00dc\5$\23\2\u00dc\u00dd\7-\2\2\u00dd")
        buf.write("\u00de\5\\/\2\u00de#\3\2\2\2\u00df\u00e2\5&\24\2\u00e0")
        buf.write("\u00e2\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e0\3\2\2\2")
        buf.write("\u00e2%\3\2\2\2\u00e3\u00e6\5(\25\2\u00e4\u00e6\5*\26")
        buf.write("\2\u00e5\u00e3\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6\'\3\2")
        buf.write("\2\2\u00e7\u00e8\7\67\2\2\u00e8\u00e9\7\63\2\2\u00e9\u00ea")
        buf.write("\5\30\r\2\u00ea\u00eb\7\61\2\2\u00eb\u00ec\5(\25\2\u00ec")
        buf.write("\u00f1\3\2\2\2\u00ed\u00ee\7\67\2\2\u00ee\u00ef\7\63\2")
        buf.write("\2\u00ef\u00f1\5\30\r\2\u00f0\u00e7\3\2\2\2\u00f0\u00ed")
        buf.write("\3\2\2\2\u00f1)\3\2\2\2\u00f2\u00f3\5\32\16\2\u00f3\u00f4")
        buf.write("\7\63\2\2\u00f4\u00f5\5\30\r\2\u00f5\u00f6\7\61\2\2\u00f6")
        buf.write("\u00f7\5*\26\2\u00f7\u00fd\3\2\2\2\u00f8\u00f9\5\32\16")
        buf.write("\2\u00f9\u00fa\7\63\2\2\u00fa\u00fb\5\30\r\2\u00fb\u00fd")
        buf.write("\3\2\2\2\u00fc\u00f2\3\2\2\2\u00fc\u00f8\3\2\2\2\u00fd")
        buf.write("+\3\2\2\2\u00fe\u00ff\t\5\2\2\u00ff-\3\2\2\2\u0100\u0106")
        buf.write("\78\2\2\u0101\u0106\79\2\2\u0102\u0106\5,\27\2\u0103\u0106")
        buf.write("\7:\2\2\u0104\u0106\5\60\31\2\u0105\u0100\3\2\2\2\u0105")
        buf.write("\u0101\3\2\2\2\u0105\u0102\3\2\2\2\u0105\u0103\3\2\2\2")
        buf.write("\u0105\u0104\3\2\2\2\u0106/\3\2\2\2\u0107\u0108\7.\2\2")
        buf.write("\u0108\u0109\5\62\32\2\u0109\u010a\7/\2\2\u010a\61\3\2")
        buf.write("\2\2\u010b\u010c\5.\30\2\u010c\u010d\7\61\2\2\u010d\u010e")
        buf.write("\5\62\32\2\u010e\u0111\3\2\2\2\u010f\u0111\5.\30\2\u0110")
        buf.write("\u010b\3\2\2\2\u0110\u010f\3\2\2\2\u0111\63\3\2\2\2\u0112")
        buf.write("\u0113\t\6\2\2\u0113\65\3\2\2\2\u0114\u0115\t\7\2\2\u0115")
        buf.write("\67\3\2\2\2\u0116\u0117\t\b\2\2\u01179\3\2\2\2\u0118\u0119")
        buf.write("\t\t\2\2\u0119;\3\2\2\2\u011a\u011b\5> \2\u011b\u011c")
        buf.write("\7*\2\2\u011c\u011d\5> \2\u011d\u0120\3\2\2\2\u011e\u0120")
        buf.write("\5> \2\u011f\u011a\3\2\2\2\u011f\u011e\3\2\2\2\u0120=")
        buf.write("\3\2\2\2\u0121\u0122\5@!\2\u0122\u0123\5\64\33\2\u0123")
        buf.write("\u0124\5@!\2\u0124\u0127\3\2\2\2\u0125\u0127\5@!\2\u0126")
        buf.write("\u0121\3\2\2\2\u0126\u0125\3\2\2\2\u0127?\3\2\2\2\u0128")
        buf.write("\u0129\b!\1\2\u0129\u012a\5B\"\2\u012a\u0131\3\2\2\2\u012b")
        buf.write("\u012c\f\4\2\2\u012c\u012d\5\66\34\2\u012d\u012e\5B\"")
        buf.write("\2\u012e\u0130\3\2\2\2\u012f\u012b\3\2\2\2\u0130\u0133")
        buf.write("\3\2\2\2\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132")
        buf.write("A\3\2\2\2\u0133\u0131\3\2\2\2\u0134\u0135\b\"\1\2\u0135")
        buf.write("\u0136\5D#\2\u0136\u013d\3\2\2\2\u0137\u0138\f\4\2\2\u0138")
        buf.write("\u0139\58\35\2\u0139\u013a\5D#\2\u013a\u013c\3\2\2\2\u013b")
        buf.write("\u0137\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b\3\2\2\2")
        buf.write("\u013d\u013e\3\2\2\2\u013eC\3\2\2\2\u013f\u013d\3\2\2")
        buf.write("\2\u0140\u0141\b#\1\2\u0141\u0142\5F$\2\u0142\u0149\3")
        buf.write("\2\2\2\u0143\u0144\f\4\2\2\u0144\u0145\5:\36\2\u0145\u0146")
        buf.write("\5F$\2\u0146\u0148\3\2\2\2\u0147\u0143\3\2\2\2\u0148\u014b")
        buf.write("\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a")
        buf.write("E\3\2\2\2\u014b\u0149\3\2\2\2\u014c\u014d\7 \2\2\u014d")
        buf.write("\u0150\5F$\2\u014e\u0150\5H%\2\u014f\u014c\3\2\2\2\u014f")
        buf.write("\u014e\3\2\2\2\u0150G\3\2\2\2\u0151\u0152\7\33\2\2\u0152")
        buf.write("\u0155\5H%\2\u0153\u0155\5J&\2\u0154\u0151\3\2\2\2\u0154")
        buf.write("\u0153\3\2\2\2\u0155I\3\2\2\2\u0156\u0157\5L\'\2\u0157")
        buf.write("\u0158\7.\2\2\u0158\u0159\5<\37\2\u0159\u015a\7/\2\2\u015a")
        buf.write("\u015d\3\2\2\2\u015b\u015d\5L\'\2\u015c\u0156\3\2\2\2")
        buf.write("\u015c\u015b\3\2\2\2\u015dK\3\2\2\2\u015e\u015f\b\'\1")
        buf.write("\2\u015f\u0160\5N(\2\u0160\u0173\3\2\2\2\u0161\u0162\f")
        buf.write("\5\2\2\u0162\u0163\7\60\2\2\u0163\u0165\7\67\2\2\u0164")
        buf.write("\u0166\5\60\31\2\u0165\u0164\3\2\2\2\u0165\u0166\3\2\2")
        buf.write("\2\u0166\u0172\3\2\2\2\u0167\u0168\f\4\2\2\u0168\u0169")
        buf.write("\7\60\2\2\u0169\u016b\7\67\2\2\u016a\u016c\5\60\31\2\u016b")
        buf.write("\u016a\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016d\3\2\2\2")
        buf.write("\u016d\u016e\7,\2\2\u016e\u016f\5X-\2\u016f\u0170\7-\2")
        buf.write("\2\u0170\u0172\3\2\2\2\u0171\u0161\3\2\2\2\u0171\u0167")
        buf.write("\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2\u0173")
        buf.write("\u0174\3\2\2\2\u0174M\3\2\2\2\u0175\u0173\3\2\2\2\u0176")
        buf.write("\u0177\7\67\2\2\u0177\u0179\7\60\2\2\u0178\u0176\3\2\2")
        buf.write("\2\u0178\u0179\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u017c")
        buf.write("\7\66\2\2\u017b\u017d\5\60\31\2\u017c\u017b\3\2\2\2\u017c")
        buf.write("\u017d\3\2\2\2\u017d\u018c\3\2\2\2\u017e\u017f\7\67\2")
        buf.write("\2\u017f\u0181\7\60\2\2\u0180\u017e\3\2\2\2\u0180\u0181")
        buf.write("\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0184\7\66\2\2\u0183")
        buf.write("\u0185\5\60\31\2\u0184\u0183\3\2\2\2\u0184\u0185\3\2\2")
        buf.write("\2\u0185\u0186\3\2\2\2\u0186\u0187\7,\2\2\u0187\u0188")
        buf.write("\5X-\2\u0188\u0189\7-\2\2\u0189\u018c\3\2\2\2\u018a\u018c")
        buf.write("\5P)\2\u018b\u0178\3\2\2\2\u018b\u0180\3\2\2\2\u018b\u018a")
        buf.write("\3\2\2\2\u018cO\3\2\2\2\u018d\u0190\5V,\2\u018e\u0190")
        buf.write("\5R*\2\u018f\u018d\3\2\2\2\u018f\u018e\3\2\2\2\u0190Q")
        buf.write("\3\2\2\2\u0191\u0192\7,\2\2\u0192\u0193\5<\37\2\u0193")
        buf.write("\u0194\7-\2\2\u0194\u0197\3\2\2\2\u0195\u0197\5T+\2\u0196")
        buf.write("\u0191\3\2\2\2\u0196\u0195\3\2\2\2\u0197S\3\2\2\2\u0198")
        buf.write("\u019c\5.\30\2\u0199\u019c\5\34\17\2\u019a\u019c\7\25")
        buf.write("\2\2\u019b\u0198\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019a")
        buf.write("\3\2\2\2\u019cU\3\2\2\2\u019d\u019e\7\26\2\2\u019e\u019f")
        buf.write("\5\34\17\2\u019f\u01a0\7,\2\2\u01a0\u01a1\5X-\2\u01a1")
        buf.write("\u01a2\7-\2\2\u01a2W\3\2\2\2\u01a3\u01a6\5Z.\2\u01a4\u01a6")
        buf.write("\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a6")
        buf.write("Y\3\2\2\2\u01a7\u01a8\5<\37\2\u01a8\u01a9\7\61\2\2\u01a9")
        buf.write("\u01aa\5Z.\2\u01aa\u01ad\3\2\2\2\u01ab\u01ad\5<\37\2\u01ac")
        buf.write("\u01a7\3\2\2\2\u01ac\u01ab\3\2\2\2\u01ad[\3\2\2\2\u01ae")
        buf.write("\u01af\7\64\2\2\u01af\u01b0\5^\60\2\u01b0\u01b1\7\65\2")
        buf.write("\2\u01b1]\3\2\2\2\u01b2\u01b3\5`\61\2\u01b3\u01b4\5^\60")
        buf.write("\2\u01b4\u01b7\3\2\2\2\u01b5\u01b7\3\2\2\2\u01b6\u01b2")
        buf.write("\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7_\3\2\2\2\u01b8\u01c2")
        buf.write("\5b\62\2\u01b9\u01c2\5d\63\2\u01ba\u01c2\5f\64\2\u01bb")
        buf.write("\u01c2\5n8\2\u01bc\u01c2\5p9\2\u01bd\u01c2\5r:\2\u01be")
        buf.write("\u01c2\5t;\2\u01bf\u01c2\5v<\2\u01c0\u01c2\5\\/\2\u01c1")
        buf.write("\u01b8\3\2\2\2\u01c1\u01b9\3\2\2\2\u01c1\u01ba\3\2\2\2")
        buf.write("\u01c1\u01bb\3\2\2\2\u01c1\u01bc\3\2\2\2\u01c1\u01bd\3")
        buf.write("\2\2\2\u01c1\u01be\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c0")
        buf.write("\3\2\2\2\u01c2a\3\2\2\2\u01c3\u01cc\t\2\2\2\u01c4\u01c5")
        buf.write("\5\24\13\2\u01c5\u01c6\7\63\2\2\u01c6\u01c7\5\30\r\2\u01c7")
        buf.write("\u01c8\7\62\2\2\u01c8\u01cd\3\2\2\2\u01c9\u01ca\5\26\f")
        buf.write("\2\u01ca\u01cb\7\62\2\2\u01cb\u01cd\3\2\2\2\u01cc\u01c4")
        buf.write("\3\2\2\2\u01cc\u01c9\3\2\2\2\u01cdc\3\2\2\2\u01ce\u01d0")
        buf.write("\5\34\17\2\u01cf\u01d1\5\60\31\2\u01d0\u01cf\3\2\2\2\u01d0")
        buf.write("\u01d1\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d4\5v<\2\u01d3")
        buf.write("\u01ce\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2")
        buf.write("\u01d5\u01d6\7$\2\2\u01d6\u01d7\5<\37\2\u01d7\u01d8\7")
        buf.write("\62\2\2\u01d8e\3\2\2\2\u01d9\u01db\7\7\2\2\u01da\u01dc")
        buf.write("\5\\/\2\u01db\u01da\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc")
        buf.write("\u01dd\3\2\2\2\u01dd\u01de\5<\37\2\u01de\u01e1\5\\/\2")
        buf.write("\u01df\u01e0\7\b\2\2\u01e0\u01e2\5\\/\2\u01e1\u01df\3")
        buf.write("\2\2\2\u01e1\u01e2\3\2\2\2\u01e2g\3\2\2\2\u01e3\u01e5")
        buf.write("\7\67\2\2\u01e4\u01e6\5\60\31\2\u01e5\u01e4\3\2\2\2\u01e5")
        buf.write("\u01e6\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e8\7$\2\2")
        buf.write("\u01e8\u01e9\78\2\2\u01e9i\3\2\2\2\u01ea\u01ec\7\67\2")
        buf.write("\2\u01eb\u01ed\5\60\31\2\u01ec\u01eb\3\2\2\2\u01ec\u01ed")
        buf.write("\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01f4\5\64\33\2\u01ef")
        buf.write("\u01f5\78\2\2\u01f0\u01f2\7\67\2\2\u01f1\u01f3\5\60\31")
        buf.write("\2\u01f2\u01f1\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f5")
        buf.write("\3\2\2\2\u01f4\u01ef\3\2\2\2\u01f4\u01f0\3\2\2\2\u01f5")
        buf.write("k\3\2\2\2\u01f6\u01f8\7\67\2\2\u01f7\u01f9\5\60\31\2\u01f8")
        buf.write("\u01f7\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fa\3\2\2\2")
        buf.write("\u01fa\u01fb\7$\2\2\u01fb\u01fd\7\67\2\2\u01fc\u01fe\5")
        buf.write("\60\31\2\u01fd\u01fc\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe")
        buf.write("\u0201\3\2\2\2\u01ff\u0202\58\35\2\u0200\u0202\5:\36\2")
        buf.write("\u0201\u01ff\3\2\2\2\u0201\u0200\3\2\2\2\u0202\u0208\3")
        buf.write("\2\2\2\u0203\u0209\78\2\2\u0204\u0206\7\67\2\2\u0205\u0207")
        buf.write("\5\60\31\2\u0206\u0205\3\2\2\2\u0206\u0207\3\2\2\2\u0207")
        buf.write("\u0209\3\2\2\2\u0208\u0203\3\2\2\2\u0208\u0204\3\2\2\2")
        buf.write("\u0209m\3\2\2\2\u020a\u020b\7\t\2\2\u020b\u020c\5h\65")
        buf.write("\2\u020c\u020d\7\62\2\2\u020d\u020e\5j\66\2\u020e\u020f")
        buf.write("\7\62\2\2\u020f\u0210\5l\67\2\u0210\u0211\5\\/\2\u0211")
        buf.write("o\3\2\2\2\u0212\u0213\7\5\2\2\u0213\u0214\7\62\2\2\u0214")
        buf.write("q\3\2\2\2\u0215\u0216\7\6\2\2\u0216\u0217\7\62\2\2\u0217")
        buf.write("s\3\2\2\2\u0218\u021b\7\20\2\2\u0219\u021c\5<\37\2\u021a")
        buf.write("\u021c\5\34\17\2\u021b\u0219\3\2\2\2\u021b\u021a\3\2\2")
        buf.write("\2\u021b\u021c\3\2\2\2\u021c\u021d\3\2\2\2\u021d\u021e")
        buf.write("\7\62\2\2\u021eu\3\2\2\2\u021f\u0220\7\67\2\2\u0220\u0222")
        buf.write("\7\60\2\2\u0221\u021f\3\2\2\2\u0221\u0222\3\2\2\2\u0222")
        buf.write("\u0223\3\2\2\2\u0223\u0224\7\66\2\2\u0224\u0225\7,\2\2")
        buf.write("\u0225\u0226\5X-\2\u0226\u0227\7-\2\2\u0227\u0228\7\62")
        buf.write("\2\2\u0228w\3\2\2\2\u0229\u022a\7\67\2\2\u022a\u022b\7")
        buf.write("\3\2\2\u022by\3\2\2\2;\u0081\u0085\u0090\u0094\u009a\u00ab")
        buf.write("\u00b6\u00bc\u00c4\u00ca\u00d4\u00e1\u00e5\u00f0\u00fc")
        buf.write("\u0105\u0110\u011f\u0126\u0131\u013d\u0149\u014f\u0154")
        buf.write("\u015c\u0165\u016b\u0171\u0173\u0178\u017c\u0180\u0184")
        buf.write("\u018b\u018f\u0196\u019b\u01a5\u01ac\u01b6\u01c1\u01cc")
        buf.write("\u01d0\u01d3\u01db\u01e1\u01e5\u01ec\u01f2\u01f4\u01f8")
        buf.write("\u01fd\u0201\u0206\u0208\u021b\u0221")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<-'", "<INVALID>", "'break'", "'continue'", 
                     "'if'", "'else'", "'for'", "'true'", "'false'", "'int'", 
                     "'float'", "'bool'", "'string'", "'return'", "'null'", 
                     "'class'", "'constructor'", "'var'", "'self'", "'new'", 
                     "'void'", "'const'", "'func'", "'+'", "'-'", "'*'", 
                     "'/'", "'\\'", "'!='", "'!'", "'&&'", "'||'", "'=='", 
                     "':='", "'='", "'<='", "'<'", "'>='", "'>'", "'^'", 
                     "'%'", "'('", "')'", "'['", "']'", "'.'", "','", "';'", 
                     "':'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "COMMENT", "BREAK", "CONTINUE", 
                      "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", "FLOAT", 
                      "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
                      "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", "PLUS", 
                      "MINUS", "MULTI", "DIVFLO", "DIVINT", "DIFFROM", "DIFF", 
                      "AND", "OR", "COMPEQ", "ASSIGN", "EQUAL", "LESSEQ", 
                      "LESS", "MOREEQ", "MOR", "SPACING", "MODU", "LB", 
                      "RB", "SLB", "SRB", "DOT", "CM", "SC", "COLON", "LCB", 
                      "RCB", "ATIDENTIFIER", "IDENTIFIER", "INTLIT", "FLOATLIT", 
                      "STRINGLIT", "WS", "ILLEGAL_ESCAPE", "UNCLOSED_STRING", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classi = 1
    RULE_classdecl = 2
    RULE_body = 3
    RULE_member = 4
    RULE_hder = 5
    RULE_attr = 6
    RULE_attrdc = 7
    RULE_attrndc = 8
    RULE_attrlist = 9
    RULE_attlist = 10
    RULE_typ = 11
    RULE_idenNoAtlist = 12
    RULE_iden = 13
    RULE_methd = 14
    RULE_funct = 15
    RULE_functcons = 16
    RULE_paramlist = 17
    RULE_paramprime = 18
    RULE_param1 = 19
    RULE_param2 = 20
    RULE_boolit = 21
    RULE_lits = 22
    RULE_array = 23
    RULE_arraylist = 24
    RULE_operators = 25
    RULE_logical = 26
    RULE_adding = 27
    RULE_multiplying = 28
    RULE_expr = 29
    RULE_expr1 = 30
    RULE_expr2 = 31
    RULE_expr3 = 32
    RULE_expr4 = 33
    RULE_expr5 = 34
    RULE_expr6 = 35
    RULE_expr7 = 36
    RULE_expr8 = 37
    RULE_expr9 = 38
    RULE_expr10 = 39
    RULE_expr11 = 40
    RULE_expr12 = 41
    RULE_new = 42
    RULE_exprlist = 43
    RULE_exprlst = 44
    RULE_blkstate = 45
    RULE_stmtlist = 46
    RULE_stmt = 47
    RULE_declstmt = 48
    RULE_assstmt = 49
    RULE_ifstmt = 50
    RULE_initstmt = 51
    RULE_condstmt = 52
    RULE_poststmt = 53
    RULE_forstmt = 54
    RULE_breakstmt = 55
    RULE_contstmt = 56
    RULE_retstmt = 57
    RULE_metdinvoke = 58
    RULE_superpart = 59

    ruleNames =  [ "program", "classi", "classdecl", "body", "member", "hder", 
                   "attr", "attrdc", "attrndc", "attrlist", "attlist", "typ", 
                   "idenNoAtlist", "iden", "methd", "funct", "functcons", 
                   "paramlist", "paramprime", "param1", "param2", "boolit", 
                   "lits", "array", "arraylist", "operators", "logical", 
                   "adding", "multiplying", "expr", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "expr7", "expr8", "expr9", 
                   "expr10", "expr11", "expr12", "new", "exprlist", "exprlst", 
                   "blkstate", "stmtlist", "stmt", "declstmt", "assstmt", 
                   "ifstmt", "initstmt", "condstmt", "poststmt", "forstmt", 
                   "breakstmt", "contstmt", "retstmt", "metdinvoke", "superpart" ]

    EOF = Token.EOF
    T__0=1
    COMMENT=2
    BREAK=3
    CONTINUE=4
    IF=5
    ELSE=6
    FOR=7
    TRUE=8
    FALSE=9
    INT=10
    FLOAT=11
    BOOL=12
    STRING=13
    RETURN=14
    NULL=15
    CLASS=16
    CONSTRUCTOR=17
    VAR=18
    SELF=19
    NEW=20
    VOID=21
    CONST=22
    FUNC=23
    PLUS=24
    MINUS=25
    MULTI=26
    DIVFLO=27
    DIVINT=28
    DIFFROM=29
    DIFF=30
    AND=31
    OR=32
    COMPEQ=33
    ASSIGN=34
    EQUAL=35
    LESSEQ=36
    LESS=37
    MOREEQ=38
    MOR=39
    SPACING=40
    MODU=41
    LB=42
    RB=43
    SLB=44
    SRB=45
    DOT=46
    CM=47
    SC=48
    COLON=49
    LCB=50
    RCB=51
    ATIDENTIFIER=52
    IDENTIFIER=53
    INTLIT=54
    FLOATLIT=55
    STRINGLIT=56
    WS=57
    ILLEGAL_ESCAPE=58
    UNCLOSED_STRING=59
    ERROR_CHAR=60

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classi(self):
            return self.getTypedRuleContext(CSlangParser.ClassiContext,0)


        def EOF(self):
            return self.getToken(CSlangParser.EOF, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.classi()
            self.state = 121
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecl(self):
            return self.getTypedRuleContext(CSlangParser.ClassdeclContext,0)


        def classi(self):
            return self.getTypedRuleContext(CSlangParser.ClassiContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_classi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassi" ):
                return visitor.visitClassi(self)
            else:
                return visitor.visitChildren(self)




    def classi(self):

        localctx = CSlangParser.ClassiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classi)
        try:
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.classdecl()
                self.state = 124
                self.classi()
                pass
            elif token in [CSlangParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CSlangParser.CLASS, 0)

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def LCB(self):
            return self.getToken(CSlangParser.LCB, 0)

        def body(self):
            return self.getTypedRuleContext(CSlangParser.BodyContext,0)


        def RCB(self):
            return self.getToken(CSlangParser.RCB, 0)

        def superpart(self):
            return self.getTypedRuleContext(CSlangParser.SuperpartContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_classdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecl" ):
                return visitor.visitClassdecl(self)
            else:
                return visitor.visitChildren(self)




    def classdecl(self):

        localctx = CSlangParser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(CSlangParser.CLASS)
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 130
                self.superpart()


            self.state = 133
            self.match(CSlangParser.IDENTIFIER)
            self.state = 134
            self.match(CSlangParser.LCB)
            self.state = 135
            self.body()
            self.state = 136
            self.match(CSlangParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(CSlangParser.MemberContext,0)


        def body(self):
            return self.getTypedRuleContext(CSlangParser.BodyContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = CSlangParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_body)
        try:
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.member()
                self.state = 139
                self.body()
                pass
            elif token in [CSlangParser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr(self):
            return self.getTypedRuleContext(CSlangParser.AttrContext,0)


        def methd(self):
            return self.getTypedRuleContext(CSlangParser.MethdContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = CSlangParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_member)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.attr()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.methd()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_hder

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHder" ):
                return visitor.visitHder(self)
            else:
                return visitor.visitChildren(self)




    def hder(self):

        localctx = CSlangParser.HderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_hder)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrdc(self):
            return self.getTypedRuleContext(CSlangParser.AttrdcContext,0)


        def attrndc(self):
            return self.getTypedRuleContext(CSlangParser.AttrndcContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr" ):
                return visitor.visitAttr(self)
            else:
                return visitor.visitChildren(self)




    def attr(self):

        localctx = CSlangParser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attr)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.attrdc()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.attrndc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrdcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hder(self):
            return self.getTypedRuleContext(CSlangParser.HderContext,0)


        def attlist(self):
            return self.getTypedRuleContext(CSlangParser.AttlistContext,0)


        def SC(self):
            return self.getToken(CSlangParser.SC, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attrdc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrdc" ):
                return visitor.visitAttrdc(self)
            else:
                return visitor.visitChildren(self)




    def attrdc(self):

        localctx = CSlangParser.AttrdcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attrdc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.hder()
            self.state = 155
            self.attlist()
            self.state = 156
            self.match(CSlangParser.SC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrndcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hder(self):
            return self.getTypedRuleContext(CSlangParser.HderContext,0)


        def attrlist(self):
            return self.getTypedRuleContext(CSlangParser.AttrlistContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def SC(self):
            return self.getToken(CSlangParser.SC, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attrndc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrndc" ):
                return visitor.visitAttrndc(self)
            else:
                return visitor.visitChildren(self)




    def attrndc(self):

        localctx = CSlangParser.AttrndcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attrndc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.hder()
            self.state = 159
            self.attrlist()
            self.state = 160
            self.match(CSlangParser.COLON)
            self.state = 161
            self.typ()
            self.state = 162
            self.match(CSlangParser.SC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iden(self):
            return self.getTypedRuleContext(CSlangParser.IdenContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def attrlist(self):
            return self.getTypedRuleContext(CSlangParser.AttrlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attrlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrlist" ):
                return visitor.visitAttrlist(self)
            else:
                return visitor.visitChildren(self)




    def attrlist(self):

        localctx = CSlangParser.AttrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attrlist)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.iden()
                self.state = 165
                self.match(CSlangParser.CM)
                self.state = 166
                self.attrlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.iden()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iden(self):
            return self.getTypedRuleContext(CSlangParser.IdenContext,0)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def attlist(self):
            return self.getTypedRuleContext(CSlangParser.AttlistContext,0)


        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def EQUAL(self):
            return self.getToken(CSlangParser.EQUAL, 0)

        def array(self):
            return self.getTypedRuleContext(CSlangParser.ArrayContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttlist" ):
                return visitor.visitAttlist(self)
            else:
                return visitor.visitChildren(self)




    def attlist(self):

        localctx = CSlangParser.AttlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attlist)
        self._la = 0 # Token type
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.iden()
                self.state = 172
                self.match(CSlangParser.CM)
                self.state = 173
                self.attlist()
                self.state = 174
                self.match(CSlangParser.CM)
                self.state = 175
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.iden()
                self.state = 178
                self.match(CSlangParser.COLON)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.SLB:
                    self.state = 179
                    self.array()


                self.state = 182
                self.typ()
                self.state = 183
                self.match(CSlangParser.EQUAL)
                self.state = 184
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = CSlangParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.INT) | (1 << CSlangParser.FLOAT) | (1 << CSlangParser.BOOL) | (1 << CSlangParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdenNoAtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def idenNoAtlist(self):
            return self.getTypedRuleContext(CSlangParser.IdenNoAtlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_idenNoAtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdenNoAtlist" ):
                return visitor.visitIdenNoAtlist(self)
            else:
                return visitor.visitChildren(self)




    def idenNoAtlist(self):

        localctx = CSlangParser.IdenNoAtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_idenNoAtlist)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.match(CSlangParser.IDENTIFIER)
                self.state = 191
                self.match(CSlangParser.CM)
                self.state = 192
                self.idenNoAtlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(CSlangParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATIDENTIFIER(self):
            return self.getToken(CSlangParser.ATIDENTIFIER, 0)

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_iden

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIden" ):
                return visitor.visitIden(self)
            else:
                return visitor.visitChildren(self)




    def iden(self):

        localctx = CSlangParser.IdenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_iden)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ATIDENTIFIER or _la==CSlangParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funct(self):
            return self.getTypedRuleContext(CSlangParser.FunctContext,0)


        def functcons(self):
            return self.getTypedRuleContext(CSlangParser.FunctconsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_methd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethd" ):
                return visitor.visitMethd(self)
            else:
                return visitor.visitChildren(self)




    def methd(self):

        localctx = CSlangParser.MethdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_methd)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.funct()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.functcons()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def iden(self):
            return self.getTypedRuleContext(CSlangParser.IdenContext,0)


        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(CSlangParser.ParamlistContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def blkstate(self):
            return self.getTypedRuleContext(CSlangParser.BlkstateContext,0)


        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_funct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunct" ):
                return visitor.visitFunct(self)
            else:
                return visitor.visitChildren(self)




    def funct(self):

        localctx = CSlangParser.FunctContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_funct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(CSlangParser.FUNC)
            self.state = 203
            self.iden()
            self.state = 204
            self.match(CSlangParser.LB)
            self.state = 205
            self.paramlist()
            self.state = 206
            self.match(CSlangParser.RB)
            self.state = 207
            self.match(CSlangParser.COLON)
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING]:
                self.state = 208
                self.typ()
                pass
            elif token in [CSlangParser.VOID]:
                self.state = 209
                self.match(CSlangParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 212
            self.blkstate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctconsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def CONSTRUCTOR(self):
            return self.getToken(CSlangParser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(CSlangParser.ParamlistContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def blkstate(self):
            return self.getTypedRuleContext(CSlangParser.BlkstateContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_functcons

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctcons" ):
                return visitor.visitFunctcons(self)
            else:
                return visitor.visitChildren(self)




    def functcons(self):

        localctx = CSlangParser.FunctconsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_functcons)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(CSlangParser.FUNC)
            self.state = 215
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 216
            self.match(CSlangParser.LB)
            self.state = 217
            self.paramlist()
            self.state = 218
            self.match(CSlangParser.RB)
            self.state = 219
            self.blkstate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramprime(self):
            return self.getTypedRuleContext(CSlangParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = CSlangParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_paramlist)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.paramprime()
                pass
            elif token in [CSlangParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param1(self):
            return self.getTypedRuleContext(CSlangParser.Param1Context,0)


        def param2(self):
            return self.getTypedRuleContext(CSlangParser.Param2Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_paramprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamprime" ):
                return visitor.visitParamprime(self)
            else:
                return visitor.visitChildren(self)




    def paramprime(self):

        localctx = CSlangParser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_paramprime)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.param1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.param2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def param1(self):
            return self.getTypedRuleContext(CSlangParser.Param1Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_param1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam1" ):
                return visitor.visitParam1(self)
            else:
                return visitor.visitChildren(self)




    def param1(self):

        localctx = CSlangParser.Param1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_param1)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(CSlangParser.IDENTIFIER)
                self.state = 230
                self.match(CSlangParser.COLON)
                self.state = 231
                self.typ()
                self.state = 232
                self.match(CSlangParser.CM)
                self.state = 233
                self.param1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(CSlangParser.IDENTIFIER)
                self.state = 236
                self.match(CSlangParser.COLON)
                self.state = 237
                self.typ()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idenNoAtlist(self):
            return self.getTypedRuleContext(CSlangParser.IdenNoAtlistContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def param2(self):
            return self.getTypedRuleContext(CSlangParser.Param2Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_param2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam2" ):
                return visitor.visitParam2(self)
            else:
                return visitor.visitChildren(self)




    def param2(self):

        localctx = CSlangParser.Param2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_param2)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.idenNoAtlist()
                self.state = 241
                self.match(CSlangParser.COLON)
                self.state = 242
                self.typ()
                self.state = 243
                self.match(CSlangParser.CM)
                self.state = 244
                self.param2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.idenNoAtlist()
                self.state = 247
                self.match(CSlangParser.COLON)
                self.state = 248
                self.typ()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(CSlangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSlangParser.FALSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_boolit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolit" ):
                return visitor.visitBoolit(self)
            else:
                return visitor.visitChildren(self)




    def boolit(self):

        localctx = CSlangParser.BoolitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_boolit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            _la = self._input.LA(1)
            if not(_la==CSlangParser.TRUE or _la==CSlangParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(CSlangParser.FLOATLIT, 0)

        def boolit(self):
            return self.getTypedRuleContext(CSlangParser.BoolitContext,0)


        def STRINGLIT(self):
            return self.getToken(CSlangParser.STRINGLIT, 0)

        def array(self):
            return self.getTypedRuleContext(CSlangParser.ArrayContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_lits

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLits" ):
                return visitor.visitLits(self)
            else:
                return visitor.visitChildren(self)




    def lits(self):

        localctx = CSlangParser.LitsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_lits)
        try:
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 256
                self.boolit()
                pass
            elif token in [CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 257
                self.match(CSlangParser.STRINGLIT)
                pass
            elif token in [CSlangParser.SLB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 258
                self.array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLB(self):
            return self.getToken(CSlangParser.SLB, 0)

        def arraylist(self):
            return self.getTypedRuleContext(CSlangParser.ArraylistContext,0)


        def SRB(self):
            return self.getToken(CSlangParser.SRB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = CSlangParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(CSlangParser.SLB)
            self.state = 262
            self.arraylist()
            self.state = 263
            self.match(CSlangParser.SRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lits(self):
            return self.getTypedRuleContext(CSlangParser.LitsContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def arraylist(self):
            return self.getTypedRuleContext(CSlangParser.ArraylistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_arraylist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylist" ):
                return visitor.visitArraylist(self)
            else:
                return visitor.visitChildren(self)




    def arraylist(self):

        localctx = CSlangParser.ArraylistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_arraylist)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.lits()
                self.state = 266
                self.match(CSlangParser.CM)
                self.state = 267
                self.arraylist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.lits()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPEQ(self):
            return self.getToken(CSlangParser.COMPEQ, 0)

        def DIFFROM(self):
            return self.getToken(CSlangParser.DIFFROM, 0)

        def LESS(self):
            return self.getToken(CSlangParser.LESS, 0)

        def MOR(self):
            return self.getToken(CSlangParser.MOR, 0)

        def LESSEQ(self):
            return self.getToken(CSlangParser.LESSEQ, 0)

        def MOREEQ(self):
            return self.getToken(CSlangParser.MOREEQ, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperators" ):
                return visitor.visitOperators(self)
            else:
                return visitor.visitChildren(self)




    def operators(self):

        localctx = CSlangParser.OperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.DIFFROM) | (1 << CSlangParser.COMPEQ) | (1 << CSlangParser.LESSEQ) | (1 << CSlangParser.LESS) | (1 << CSlangParser.MOREEQ) | (1 << CSlangParser.MOR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(CSlangParser.AND, 0)

        def OR(self):
            return self.getToken(CSlangParser.OR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_logical

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical" ):
                return visitor.visitLogical(self)
            else:
                return visitor.visitChildren(self)




    def logical(self):

        localctx = CSlangParser.LogicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            _la = self._input.LA(1)
            if not(_la==CSlangParser.AND or _la==CSlangParser.OR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(CSlangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(CSlangParser.MINUS, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_adding

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding" ):
                return visitor.visitAdding(self)
            else:
                return visitor.visitChildren(self)




    def adding(self):

        localctx = CSlangParser.AddingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            _la = self._input.LA(1)
            if not(_la==CSlangParser.PLUS or _la==CSlangParser.MINUS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplyingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTI(self):
            return self.getToken(CSlangParser.MULTI, 0)

        def DIVFLO(self):
            return self.getToken(CSlangParser.DIVFLO, 0)

        def DIVINT(self):
            return self.getToken(CSlangParser.DIVINT, 0)

        def MODU(self):
            return self.getToken(CSlangParser.MODU, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_multiplying

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying" ):
                return visitor.visitMultiplying(self)
            else:
                return visitor.visitChildren(self)




    def multiplying(self):

        localctx = CSlangParser.MultiplyingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MULTI) | (1 << CSlangParser.DIVFLO) | (1 << CSlangParser.DIVINT) | (1 << CSlangParser.MODU))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr1Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr1Context,i)


        def SPACING(self):
            return self.getToken(CSlangParser.SPACING, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CSlangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr)
        try:
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.expr1()
                self.state = 281
                self.match(CSlangParser.SPACING)
                self.state = 282
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr2Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr2Context,i)


        def operators(self):
            return self.getTypedRuleContext(CSlangParser.OperatorsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = CSlangParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr1)
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.expr2(0)
                self.state = 288
                self.operators()
                self.state = 289
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(CSlangParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(CSlangParser.Expr2Context,0)


        def logical(self):
            return self.getTypedRuleContext(CSlangParser.LogicalContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 303
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 297
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 298
                    self.logical()
                    self.state = 299
                    self.expr3(0) 
                self.state = 305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(CSlangParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(CSlangParser.Expr3Context,0)


        def adding(self):
            return self.getTypedRuleContext(CSlangParser.AddingContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 309
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 310
                    self.adding()
                    self.state = 311
                    self.expr4(0) 
                self.state = 317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(CSlangParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(CSlangParser.Expr4Context,0)


        def multiplying(self):
            return self.getTypedRuleContext(CSlangParser.MultiplyingContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 327
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 321
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 322
                    self.multiplying()
                    self.state = 323
                    self.expr5() 
                self.state = 329
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIFF(self):
            return self.getToken(CSlangParser.DIFF, 0)

        def expr5(self):
            return self.getTypedRuleContext(CSlangParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(CSlangParser.Expr6Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = CSlangParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expr5)
        try:
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.DIFF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.match(CSlangParser.DIFF)
                self.state = 331
                self.expr5()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.LB, CSlangParser.SLB, CSlangParser.ATIDENTIFIER, CSlangParser.IDENTIFIER, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(CSlangParser.MINUS, 0)

        def expr6(self):
            return self.getTypedRuleContext(CSlangParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(CSlangParser.Expr7Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = CSlangParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr6)
        try:
            self.state = 338
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.match(CSlangParser.MINUS)
                self.state = 336
                self.expr6()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LB, CSlangParser.SLB, CSlangParser.ATIDENTIFIER, CSlangParser.IDENTIFIER, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def SLB(self):
            return self.getToken(CSlangParser.SLB, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def SRB(self):
            return self.getToken(CSlangParser.SRB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = CSlangParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr7)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.expr8(0)
                self.state = 341
                self.match(CSlangParser.SLB)
                self.state = 342
                self.expr()
                self.state = 343
                self.match(CSlangParser.SRB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.expr8(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(CSlangParser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def array(self):
            return self.getTypedRuleContext(CSlangParser.ArrayContext,0)


        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(CSlangParser.ExprlistContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr8, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 369
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 367
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 351
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 352
                        self.match(CSlangParser.DOT)
                        self.state = 353
                        self.match(CSlangParser.IDENTIFIER)
                        self.state = 355
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                        if la_ == 1:
                            self.state = 354
                            self.array()


                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 357
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 358
                        self.match(CSlangParser.DOT)
                        self.state = 359
                        self.match(CSlangParser.IDENTIFIER)
                        self.state = 361
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==CSlangParser.SLB:
                            self.state = 360
                            self.array()


                        self.state = 363
                        self.match(CSlangParser.LB)
                        self.state = 364
                        self.exprlist()
                        self.state = 365
                        self.match(CSlangParser.RB)
                        pass

             
                self.state = 371
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATIDENTIFIER(self):
            return self.getToken(CSlangParser.ATIDENTIFIER, 0)

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def array(self):
            return self.getTypedRuleContext(CSlangParser.ArrayContext,0)


        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(CSlangParser.ExprlistContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def expr10(self):
            return self.getTypedRuleContext(CSlangParser.Expr10Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = CSlangParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr9)
        self._la = 0 # Token type
        try:
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.IDENTIFIER:
                    self.state = 372
                    self.match(CSlangParser.IDENTIFIER)
                    self.state = 373
                    self.match(CSlangParser.DOT)


                self.state = 376
                self.match(CSlangParser.ATIDENTIFIER)
                self.state = 378
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 377
                    self.array()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.IDENTIFIER:
                    self.state = 380
                    self.match(CSlangParser.IDENTIFIER)
                    self.state = 381
                    self.match(CSlangParser.DOT)


                self.state = 384
                self.match(CSlangParser.ATIDENTIFIER)
                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.SLB:
                    self.state = 385
                    self.array()


                self.state = 388
                self.match(CSlangParser.LB)
                self.state = 389
                self.exprlist()
                self.state = 390
                self.match(CSlangParser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 392
                self.expr10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def new(self):
            return self.getTypedRuleContext(CSlangParser.NewContext,0)


        def expr11(self):
            return self.getTypedRuleContext(CSlangParser.Expr11Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = CSlangParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr10)
        try:
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.new()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.LB, CSlangParser.SLB, CSlangParser.ATIDENTIFIER, CSlangParser.IDENTIFIER, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                self.expr11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def expr12(self):
            return self.getTypedRuleContext(CSlangParser.Expr12Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = CSlangParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr11)
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.match(CSlangParser.LB)
                self.state = 400
                self.expr()
                self.state = 401
                self.match(CSlangParser.RB)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.SLB, CSlangParser.ATIDENTIFIER, CSlangParser.IDENTIFIER, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
                self.expr12()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr12Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lits(self):
            return self.getTypedRuleContext(CSlangParser.LitsContext,0)


        def iden(self):
            return self.getTypedRuleContext(CSlangParser.IdenContext,0)


        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr12

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr12" ):
                return visitor.visitExpr12(self)
            else:
                return visitor.visitChildren(self)




    def expr12(self):

        localctx = CSlangParser.Expr12Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr12)
        try:
            self.state = 409
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SLB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.lits()
                pass
            elif token in [CSlangParser.ATIDENTIFIER, CSlangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.iden()
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 408
                self.match(CSlangParser.SELF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def iden(self):
            return self.getTypedRuleContext(CSlangParser.IdenContext,0)


        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(CSlangParser.ExprlistContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_new

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNew" ):
                return visitor.visitNew(self)
            else:
                return visitor.visitChildren(self)




    def new(self):

        localctx = CSlangParser.NewContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_new)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(CSlangParser.NEW)
            self.state = 412
            self.iden()
            self.state = 413
            self.match(CSlangParser.LB)
            self.state = 414
            self.exprlist()
            self.state = 415
            self.match(CSlangParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprlst(self):
            return self.getTypedRuleContext(CSlangParser.ExprlstContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = CSlangParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_exprlist)
        try:
            self.state = 419
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.DIFF, CSlangParser.LB, CSlangParser.SLB, CSlangParser.ATIDENTIFIER, CSlangParser.IDENTIFIER, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.exprlst()
                pass
            elif token in [CSlangParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def exprlst(self):
            return self.getTypedRuleContext(CSlangParser.ExprlstContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlst" ):
                return visitor.visitExprlst(self)
            else:
                return visitor.visitChildren(self)




    def exprlst(self):

        localctx = CSlangParser.ExprlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_exprlst)
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.expr()
                self.state = 422
                self.match(CSlangParser.CM)
                self.state = 423
                self.exprlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlkstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(CSlangParser.LCB, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(CSlangParser.StmtlistContext,0)


        def RCB(self):
            return self.getToken(CSlangParser.RCB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_blkstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlkstate" ):
                return visitor.visitBlkstate(self)
            else:
                return visitor.visitChildren(self)




    def blkstate(self):

        localctx = CSlangParser.BlkstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_blkstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(CSlangParser.LCB)
            self.state = 429
            self.stmtlist()
            self.state = 430
            self.match(CSlangParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(CSlangParser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(CSlangParser.StmtlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = CSlangParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_stmtlist)
        try:
            self.state = 436
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.RETURN, CSlangParser.VAR, CSlangParser.CONST, CSlangParser.LCB, CSlangParser.ATIDENTIFIER, CSlangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.stmt()
                self.state = 433
                self.stmtlist()
                pass
            elif token in [CSlangParser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declstmt(self):
            return self.getTypedRuleContext(CSlangParser.DeclstmtContext,0)


        def assstmt(self):
            return self.getTypedRuleContext(CSlangParser.AssstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(CSlangParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(CSlangParser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(CSlangParser.BreakstmtContext,0)


        def contstmt(self):
            return self.getTypedRuleContext(CSlangParser.ContstmtContext,0)


        def retstmt(self):
            return self.getTypedRuleContext(CSlangParser.RetstmtContext,0)


        def metdinvoke(self):
            return self.getTypedRuleContext(CSlangParser.MetdinvokeContext,0)


        def blkstate(self):
            return self.getTypedRuleContext(CSlangParser.BlkstateContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_stmt)
        try:
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.declstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self.assstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 440
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 441
                self.forstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 442
                self.breakstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 443
                self.contstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 444
                self.retstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 445
                self.metdinvoke()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 446
                self.blkstate()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def attrlist(self):
            return self.getTypedRuleContext(CSlangParser.AttrlistContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def SC(self):
            return self.getToken(CSlangParser.SC, 0)

        def attlist(self):
            return self.getTypedRuleContext(CSlangParser.AttlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_declstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclstmt" ):
                return visitor.visitDeclstmt(self)
            else:
                return visitor.visitChildren(self)




    def declstmt(self):

        localctx = CSlangParser.DeclstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_declstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 450
                self.attrlist()
                self.state = 451
                self.match(CSlangParser.COLON)
                self.state = 452
                self.typ()
                self.state = 453
                self.match(CSlangParser.SC)
                pass

            elif la_ == 2:
                self.state = 455
                self.attlist()
                self.state = 456
                self.match(CSlangParser.SC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def SC(self):
            return self.getToken(CSlangParser.SC, 0)

        def iden(self):
            return self.getTypedRuleContext(CSlangParser.IdenContext,0)


        def metdinvoke(self):
            return self.getTypedRuleContext(CSlangParser.MetdinvokeContext,0)


        def array(self):
            return self.getTypedRuleContext(CSlangParser.ArrayContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_assstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssstmt" ):
                return visitor.visitAssstmt(self)
            else:
                return visitor.visitChildren(self)




    def assstmt(self):

        localctx = CSlangParser.AssstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_assstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 460
                self.iden()
                self.state = 462
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.SLB:
                    self.state = 461
                    self.array()


                pass

            elif la_ == 2:
                self.state = 464
                self.metdinvoke()
                pass


            self.state = 467
            self.match(CSlangParser.ASSIGN)
            self.state = 468
            self.expr()
            self.state = 469
            self.match(CSlangParser.SC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSlangParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def blkstate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.BlkstateContext)
            else:
                return self.getTypedRuleContext(CSlangParser.BlkstateContext,i)


        def ELSE(self):
            return self.getToken(CSlangParser.ELSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = CSlangParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(CSlangParser.IF)
            self.state = 473
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LCB:
                self.state = 472
                self.blkstate()


            self.state = 475
            self.expr()
            self.state = 476
            self.blkstate()
            self.state = 479
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 477
                self.match(CSlangParser.ELSE)
                self.state = 478
                self.blkstate()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def array(self):
            return self.getTypedRuleContext(CSlangParser.ArrayContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_initstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitstmt" ):
                return visitor.visitInitstmt(self)
            else:
                return visitor.visitChildren(self)




    def initstmt(self):

        localctx = CSlangParser.InitstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_initstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.match(CSlangParser.IDENTIFIER)
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.SLB:
                self.state = 482
                self.array()


            self.state = 485
            self.match(CSlangParser.ASSIGN)
            self.state = 486
            self.match(CSlangParser.INTLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.IDENTIFIER)
            else:
                return self.getToken(CSlangParser.IDENTIFIER, i)

        def operators(self):
            return self.getTypedRuleContext(CSlangParser.OperatorsContext,0)


        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ArrayContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ArrayContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_condstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondstmt" ):
                return visitor.visitCondstmt(self)
            else:
                return visitor.visitChildren(self)




    def condstmt(self):

        localctx = CSlangParser.CondstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_condstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(CSlangParser.IDENTIFIER)
            self.state = 490
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.SLB:
                self.state = 489
                self.array()


            self.state = 492
            self.operators()
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTLIT]:
                self.state = 493
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.IDENTIFIER]:
                self.state = 494
                self.match(CSlangParser.IDENTIFIER)
                self.state = 496
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.SLB:
                    self.state = 495
                    self.array()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PoststmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.IDENTIFIER)
            else:
                return self.getToken(CSlangParser.IDENTIFIER, i)

        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def adding(self):
            return self.getTypedRuleContext(CSlangParser.AddingContext,0)


        def multiplying(self):
            return self.getTypedRuleContext(CSlangParser.MultiplyingContext,0)


        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ArrayContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ArrayContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_poststmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPoststmt" ):
                return visitor.visitPoststmt(self)
            else:
                return visitor.visitChildren(self)




    def poststmt(self):

        localctx = CSlangParser.PoststmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_poststmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(CSlangParser.IDENTIFIER)
            self.state = 502
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.SLB:
                self.state = 501
                self.array()


            self.state = 504
            self.match(CSlangParser.ASSIGN)
            self.state = 505
            self.match(CSlangParser.IDENTIFIER)
            self.state = 507
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.SLB:
                self.state = 506
                self.array()


            self.state = 511
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.PLUS, CSlangParser.MINUS]:
                self.state = 509
                self.adding()
                pass
            elif token in [CSlangParser.MULTI, CSlangParser.DIVFLO, CSlangParser.DIVINT, CSlangParser.MODU]:
                self.state = 510
                self.multiplying()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 518
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTLIT]:
                self.state = 513
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.IDENTIFIER]:
                self.state = 514
                self.match(CSlangParser.IDENTIFIER)
                self.state = 516
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.SLB:
                    self.state = 515
                    self.array()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSlangParser.FOR, 0)

        def initstmt(self):
            return self.getTypedRuleContext(CSlangParser.InitstmtContext,0)


        def SC(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.SC)
            else:
                return self.getToken(CSlangParser.SC, i)

        def condstmt(self):
            return self.getTypedRuleContext(CSlangParser.CondstmtContext,0)


        def poststmt(self):
            return self.getTypedRuleContext(CSlangParser.PoststmtContext,0)


        def blkstate(self):
            return self.getTypedRuleContext(CSlangParser.BlkstateContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = CSlangParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(CSlangParser.FOR)
            self.state = 521
            self.initstmt()
            self.state = 522
            self.match(CSlangParser.SC)
            self.state = 523
            self.condstmt()
            self.state = 524
            self.match(CSlangParser.SC)
            self.state = 525
            self.poststmt()
            self.state = 526
            self.blkstate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CSlangParser.BREAK, 0)

        def SC(self):
            return self.getToken(CSlangParser.SC, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = CSlangParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.match(CSlangParser.BREAK)
            self.state = 529
            self.match(CSlangParser.SC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(CSlangParser.CONTINUE, 0)

        def SC(self):
            return self.getToken(CSlangParser.SC, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_contstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContstmt" ):
                return visitor.visitContstmt(self)
            else:
                return visitor.visitChildren(self)




    def contstmt(self):

        localctx = CSlangParser.ContstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_contstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self.match(CSlangParser.CONTINUE)
            self.state = 532
            self.match(CSlangParser.SC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CSlangParser.RETURN, 0)

        def SC(self):
            return self.getToken(CSlangParser.SC, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def iden(self):
            return self.getTypedRuleContext(CSlangParser.IdenContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_retstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetstmt" ):
                return visitor.visitRetstmt(self)
            else:
                return visitor.visitChildren(self)




    def retstmt(self):

        localctx = CSlangParser.RetstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_retstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.match(CSlangParser.RETURN)
            self.state = 537
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.state = 535
                self.expr()

            elif la_ == 2:
                self.state = 536
                self.iden()


            self.state = 539
            self.match(CSlangParser.SC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetdinvokeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATIDENTIFIER(self):
            return self.getToken(CSlangParser.ATIDENTIFIER, 0)

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(CSlangParser.ExprlistContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def SC(self):
            return self.getToken(CSlangParser.SC, 0)

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_metdinvoke

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMetdinvoke" ):
                return visitor.visitMetdinvoke(self)
            else:
                return visitor.visitChildren(self)




    def metdinvoke(self):

        localctx = CSlangParser.MetdinvokeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_metdinvoke)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.IDENTIFIER:
                self.state = 541
                self.match(CSlangParser.IDENTIFIER)
                self.state = 542
                self.match(CSlangParser.DOT)


            self.state = 545
            self.match(CSlangParser.ATIDENTIFIER)
            self.state = 546
            self.match(CSlangParser.LB)
            self.state = 547
            self.exprlist()
            self.state = 548
            self.match(CSlangParser.RB)
            self.state = 549
            self.match(CSlangParser.SC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperpartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_superpart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuperpart" ):
                return visitor.visitSuperpart(self)
            else:
                return visitor.visitChildren(self)




    def superpart(self):

        localctx = CSlangParser.SuperpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_superpart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.match(CSlangParser.IDENTIFIER)
            self.state = 552
            self.match(CSlangParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[31] = self.expr2_sempred
        self._predicates[32] = self.expr3_sempred
        self._predicates[33] = self.expr4_sempred
        self._predicates[37] = self.expr8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




