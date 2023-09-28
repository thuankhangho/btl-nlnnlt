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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u022a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\5\3\u0088\n\3\3\4\3\4\3\5\3\5\3\6\3\6\5\6\u0090")
        buf.write("\n\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u009b\n\7")
        buf.write("\3\b\3\b\5\b\u009f\n\b\3\t\3\t\5\t\u00a3\n\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00bd\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u00c4\n\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\5\17\u00ce\n\17\3\17\3\17\3\20")
        buf.write("\3\20\5\20\u00d4\n\20\3\21\3\21\5\21\u00d8\n\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00e4")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u00f1\n\23\3\24\3\24\5\24\u00f5\n\24\3\25\3")
        buf.write("\25\3\25\3\25\5\25\u00fb\n\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u010c\n\30\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3")
        buf.write("\33\3\33\5\33\u0118\n\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u0120\n\33\5\33\u0122\n\33\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\5\37\u0134\n\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3")
        buf.write("!\3!\5!\u0141\n!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\5")
        buf.write("\"\u014d\n\"\3#\3#\5#\u0151\n#\3$\3$\3$\3$\3$\5$\u0158")
        buf.write("\n$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3)\3)\5)\u0167")
        buf.write("\n)\3*\3*\3*\3*\3*\5*\u016e\n*\3+\3+\3+\3+\3+\3+\3+\7")
        buf.write("+\u0177\n+\f+\16+\u017a\13+\3,\3,\3,\3,\3,\3,\3,\7,\u0183")
        buf.write("\n,\f,\16,\u0186\13,\3-\3-\3-\3-\3-\3-\3-\7-\u018f\n-")
        buf.write("\f-\16-\u0192\13-\3.\3.\3.\5.\u0197\n.\3/\3/\3/\5/\u019c")
        buf.write("\n/\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u01a4\n\60\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\7\61\u01b3\n\61\f\61\16\61\u01b6\13\61\3\62\3\62")
        buf.write("\5\62\u01ba\n\62\3\62\3\62\3\62\5\62\u01bf\n\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\5\62\u01c7\n\62\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\5\63\u01d0\n\63\3\64\3\64\3\64\5")
        buf.write("\64\u01d5\n\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\5\65\u01e0\n\65\3\66\3\66\3\66\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\5\66\u01eb\n\66\3\67\3\67\3\67\3\67\3\67")
        buf.write("\38\38\58\u01f4\n8\38\38\38\38\58\u01fa\n8\39\39\39\3")
        buf.write("9\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3<\5<\u020b\n<\3<\3<\3")
        buf.write("=\3=\5=\u0211\n=\3=\3=\3>\3>\3>\3>\3?\3?\3?\3?\5?\u021d")
        buf.write("\n?\3@\3@\3@\3@\3@\3@\3@\3@\3@\5@\u0228\n@\3@\2\6TVX`")
        buf.write("A\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\2\13\3\2:")
        buf.write(";\4\2\23\23\27\27\3\2\13\16\3\2\t\n\5\2  \"$\'(\3\2\36")
        buf.write("\37\3\2\31\32\4\2\33\35**\4\2\24\24::\2\u0229\2\u0080")
        buf.write("\3\2\2\2\4\u0087\3\2\2\2\6\u0089\3\2\2\2\b\u008b\3\2\2")
        buf.write("\2\n\u008d\3\2\2\2\f\u009a\3\2\2\2\16\u009e\3\2\2\2\20")
        buf.write("\u00a2\3\2\2\2\22\u00a4\3\2\2\2\24\u00aa\3\2\2\2\26\u00ae")
        buf.write("\3\2\2\2\30\u00bc\3\2\2\2\32\u00c3\3\2\2\2\34\u00c5\3")
        buf.write("\2\2\2\36\u00d3\3\2\2\2 \u00d7\3\2\2\2\"\u00e3\3\2\2\2")
        buf.write("$\u00f0\3\2\2\2&\u00f4\3\2\2\2(\u00fa\3\2\2\2*\u00fc\3")
        buf.write("\2\2\2,\u0103\3\2\2\2.\u010b\3\2\2\2\60\u010d\3\2\2\2")
        buf.write("\62\u010f\3\2\2\2\64\u0121\3\2\2\2\66\u0123\3\2\2\28\u0128")
        buf.write("\3\2\2\2:\u012d\3\2\2\2<\u0133\3\2\2\2>\u0137\3\2\2\2")
        buf.write("@\u0140\3\2\2\2B\u014c\3\2\2\2D\u0150\3\2\2\2F\u0157\3")
        buf.write("\2\2\2H\u0159\3\2\2\2J\u015b\3\2\2\2L\u015d\3\2\2\2N\u015f")
        buf.write("\3\2\2\2P\u0166\3\2\2\2R\u016d\3\2\2\2T\u016f\3\2\2\2")
        buf.write("V\u017b\3\2\2\2X\u0187\3\2\2\2Z\u0196\3\2\2\2\\\u019b")
        buf.write("\3\2\2\2^\u01a3\3\2\2\2`\u01a5\3\2\2\2b\u01c6\3\2\2\2")
        buf.write("d\u01cf\3\2\2\2f\u01d4\3\2\2\2h\u01d6\3\2\2\2j\u01e1\3")
        buf.write("\2\2\2l\u01ec\3\2\2\2n\u01f1\3\2\2\2p\u01fb\3\2\2\2r\u0201")
        buf.write("\3\2\2\2t\u0204\3\2\2\2v\u0207\3\2\2\2x\u0210\3\2\2\2")
        buf.write("z\u0214\3\2\2\2|\u021c\3\2\2\2~\u0227\3\2\2\2\u0080\u0081")
        buf.write("\5\4\3\2\u0081\u0082\7\2\2\3\u0082\3\3\2\2\2\u0083\u0084")
        buf.write("\5\6\4\2\u0084\u0085\5\4\3\2\u0085\u0088\3\2\2\2\u0086")
        buf.write("\u0088\3\2\2\2\u0087\u0083\3\2\2\2\u0087\u0086\3\2\2\2")
        buf.write("\u0088\5\3\2\2\2\u0089\u008a\5\n\6\2\u008a\7\3\2\2\2\u008b")
        buf.write("\u008c\t\2\2\2\u008c\t\3\2\2\2\u008d\u008f\7\21\2\2\u008e")
        buf.write("\u0090\5,\27\2\u008f\u008e\3\2\2\2\u008f\u0090\3\2\2\2")
        buf.write("\u0090\u0091\3\2\2\2\u0091\u0092\7:\2\2\u0092\u0093\7")
        buf.write("\63\2\2\u0093\u0094\5\f\7\2\u0094\u0095\7\64\2\2\u0095")
        buf.write("\13\3\2\2\2\u0096\u0097\5\16\b\2\u0097\u0098\5\f\7\2\u0098")
        buf.write("\u009b\3\2\2\2\u0099\u009b\3\2\2\2\u009a\u0096\3\2\2\2")
        buf.write("\u009a\u0099\3\2\2\2\u009b\r\3\2\2\2\u009c\u009f\5\20")
        buf.write("\t\2\u009d\u009f\5\34\17\2\u009e\u009c\3\2\2\2\u009e\u009d")
        buf.write("\3\2\2\2\u009f\17\3\2\2\2\u00a0\u00a3\5\24\13\2\u00a1")
        buf.write("\u00a3\5\22\n\2\u00a2\u00a0\3\2\2\2\u00a2\u00a1\3\2\2")
        buf.write("\2\u00a3\21\3\2\2\2\u00a4\u00a5\t\3\2\2\u00a5\u00a6\5")
        buf.write("\32\16\2\u00a6\u00a7\7\62\2\2\u00a7\u00a8\5\26\f\2\u00a8")
        buf.write("\u00a9\7\61\2\2\u00a9\23\3\2\2\2\u00aa\u00ab\t\3\2\2\u00ab")
        buf.write("\u00ac\5\30\r\2\u00ac\u00ad\7\61\2\2\u00ad\25\3\2\2\2")
        buf.write("\u00ae\u00af\t\4\2\2\u00af\27\3\2\2\2\u00b0\u00b1\5\b")
        buf.write("\5\2\u00b1\u00b2\7\60\2\2\u00b2\u00b3\5\30\r\2\u00b3\u00b4")
        buf.write("\7\60\2\2\u00b4\u00b5\5P)\2\u00b5\u00bd\3\2\2\2\u00b6")
        buf.write("\u00b7\5\b\5\2\u00b7\u00b8\7\62\2\2\u00b8\u00b9\5\26\f")
        buf.write("\2\u00b9\u00ba\7&\2\2\u00ba\u00bb\5P)\2\u00bb\u00bd\3")
        buf.write("\2\2\2\u00bc\u00b0\3\2\2\2\u00bc\u00b6\3\2\2\2\u00bd\31")
        buf.write("\3\2\2\2\u00be\u00bf\5\b\5\2\u00bf\u00c0\7\60\2\2\u00c0")
        buf.write("\u00c1\5\32\16\2\u00c1\u00c4\3\2\2\2\u00c2\u00c4\5\b\5")
        buf.write("\2\u00c3\u00be\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\33\3")
        buf.write("\2\2\2\u00c5\u00c6\7\30\2\2\u00c6\u00c7\t\2\2\2\u00c7")
        buf.write("\u00c8\7+\2\2\u00c8\u00c9\5\36\20\2\u00c9\u00ca\7,\2\2")
        buf.write("\u00ca\u00cd\7\62\2\2\u00cb\u00ce\5\26\f\2\u00cc\u00ce")
        buf.write("\7\26\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce")
        buf.write("\u00cf\3\2\2\2\u00cf\u00d0\5z>\2\u00d0\35\3\2\2\2\u00d1")
        buf.write("\u00d4\5 \21\2\u00d2\u00d4\3\2\2\2\u00d3\u00d1\3\2\2\2")
        buf.write("\u00d3\u00d2\3\2\2\2\u00d4\37\3\2\2\2\u00d5\u00d8\5\"")
        buf.write("\22\2\u00d6\u00d8\5$\23\2\u00d7\u00d5\3\2\2\2\u00d7\u00d6")
        buf.write("\3\2\2\2\u00d8!\3\2\2\2\u00d9\u00da\7:\2\2\u00da\u00db")
        buf.write("\7\62\2\2\u00db\u00dc\5\26\f\2\u00dc\u00dd\3\2\2\2\u00dd")
        buf.write("\u00de\7\60\2\2\u00de\u00df\5\"\22\2\u00df\u00e4\3\2\2")
        buf.write("\2\u00e0\u00e1\7:\2\2\u00e1\u00e2\7\62\2\2\u00e2\u00e4")
        buf.write("\5\26\f\2\u00e3\u00d9\3\2\2\2\u00e3\u00e0\3\2\2\2\u00e4")
        buf.write("#\3\2\2\2\u00e5\u00e6\5&\24\2\u00e6\u00e7\7\62\2\2\u00e7")
        buf.write("\u00e8\5\26\f\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\7\60\2")
        buf.write("\2\u00ea\u00eb\5$\23\2\u00eb\u00f1\3\2\2\2\u00ec\u00ed")
        buf.write("\5&\24\2\u00ed\u00ee\7\62\2\2\u00ee\u00ef\5\26\f\2\u00ef")
        buf.write("\u00f1\3\2\2\2\u00f0\u00e5\3\2\2\2\u00f0\u00ec\3\2\2\2")
        buf.write("\u00f1%\3\2\2\2\u00f2\u00f5\5(\25\2\u00f3\u00f5\3\2\2")
        buf.write("\2\u00f4\u00f2\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5\'\3\2")
        buf.write("\2\2\u00f6\u00f7\7:\2\2\u00f7\u00f8\7\60\2\2\u00f8\u00fb")
        buf.write("\5(\25\2\u00f9\u00fb\7:\2\2\u00fa\u00f6\3\2\2\2\u00fa")
        buf.write("\u00f9\3\2\2\2\u00fb)\3\2\2\2\u00fc\u00fd\7\30\2\2\u00fd")
        buf.write("\u00fe\7\22\2\2\u00fe\u00ff\7+\2\2\u00ff\u0100\5\36\20")
        buf.write("\2\u0100\u0101\7,\2\2\u0101\u0102\5z>\2\u0102+\3\2\2\2")
        buf.write("\u0103\u0104\7:\2\2\u0104\u0105\7\3\2\2\u0105-\3\2\2\2")
        buf.write("\u0106\u010c\7\65\2\2\u0107\u010c\7\66\2\2\u0108\u010c")
        buf.write("\5\60\31\2\u0109\u010c\7\67\2\2\u010a\u010c\5\62\32\2")
        buf.write("\u010b\u0106\3\2\2\2\u010b\u0107\3\2\2\2\u010b\u0108\3")
        buf.write("\2\2\2\u010b\u0109\3\2\2\2\u010b\u010a\3\2\2\2\u010c/")
        buf.write("\3\2\2\2\u010d\u010e\t\5\2\2\u010e\61\3\2\2\2\u010f\u0110")
        buf.write("\7-\2\2\u0110\u0111\5\64\33\2\u0111\u0112\7.\2\2\u0112")
        buf.write("\63\3\2\2\2\u0113\u0118\7\65\2\2\u0114\u0118\7\66\2\2")
        buf.write("\u0115\u0118\5\60\31\2\u0116\u0118\7\67\2\2\u0117\u0113")
        buf.write("\3\2\2\2\u0117\u0114\3\2\2\2\u0117\u0115\3\2\2\2\u0117")
        buf.write("\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011a\7\60\2")
        buf.write("\2\u011a\u0122\5\64\33\2\u011b\u0120\7\65\2\2\u011c\u0120")
        buf.write("\7\66\2\2\u011d\u0120\5\60\31\2\u011e\u0120\7\67\2\2\u011f")
        buf.write("\u011b\3\2\2\2\u011f\u011c\3\2\2\2\u011f\u011d\3\2\2\2")
        buf.write("\u011f\u011e\3\2\2\2\u0120\u0122\3\2\2\2\u0121\u0117\3")
        buf.write("\2\2\2\u0121\u011f\3\2\2\2\u0122\65\3\2\2\2\u0123\u0124")
        buf.write("\7-\2\2\u0124\u0125\7<\2\2\u0125\u0126\7.\2\2\u0126\u0127")
        buf.write("\5\26\f\2\u0127\67\3\2\2\2\u0128\u0129\7\25\2\2\u0129")
        buf.write("\u012a\7:\2\2\u012a\u012b\7+\2\2\u012b\u012c\7,\2\2\u012c")
        buf.write("9\3\2\2\2\u012d\u012e\5P)\2\u012e\u012f\7/\2\2\u012f\u0130")
        buf.write("\5\b\5\2\u0130;\3\2\2\2\u0131\u0132\7:\2\2\u0132\u0134")
        buf.write("\7/\2\2\u0133\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134")
        buf.write("\u0135\3\2\2\2\u0135\u0136\7;\2\2\u0136=\3\2\2\2\u0137")
        buf.write("\u0138\5P)\2\u0138\u0139\7/\2\2\u0139\u013a\5\b\5\2\u013a")
        buf.write("\u013b\7+\2\2\u013b\u013c\5D#\2\u013c\u013d\7,\2\2\u013d")
        buf.write("?\3\2\2\2\u013e\u013f\7:\2\2\u013f\u0141\7/\2\2\u0140")
        buf.write("\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0142\3\2\2\2")
        buf.write("\u0142\u0143\7;\2\2\u0143\u0144\7+\2\2\u0144\u0145\5D")
        buf.write("#\2\u0145\u0146\7,\2\2\u0146A\3\2\2\2\u0147\u0148\5P)")
        buf.write("\2\u0148\u0149\7\60\2\2\u0149\u014a\5B\"\2\u014a\u014d")
        buf.write("\3\2\2\2\u014b\u014d\5P)\2\u014c\u0147\3\2\2\2\u014c\u014b")
        buf.write("\3\2\2\2\u014dC\3\2\2\2\u014e\u0151\5F$\2\u014f\u0151")
        buf.write("\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u014f\3\2\2\2\u0151")
        buf.write("E\3\2\2\2\u0152\u0153\5P)\2\u0153\u0154\7\60\2\2\u0154")
        buf.write("\u0155\5F$\2\u0155\u0158\3\2\2\2\u0156\u0158\5P)\2\u0157")
        buf.write("\u0152\3\2\2\2\u0157\u0156\3\2\2\2\u0158G\3\2\2\2\u0159")
        buf.write("\u015a\t\6\2\2\u015aI\3\2\2\2\u015b\u015c\t\7\2\2\u015c")
        buf.write("K\3\2\2\2\u015d\u015e\t\b\2\2\u015eM\3\2\2\2\u015f\u0160")
        buf.write("\t\t\2\2\u0160O\3\2\2\2\u0161\u0162\5R*\2\u0162\u0163")
        buf.write("\7)\2\2\u0163\u0164\5R*\2\u0164\u0167\3\2\2\2\u0165\u0167")
        buf.write("\5R*\2\u0166\u0161\3\2\2\2\u0166\u0165\3\2\2\2\u0167Q")
        buf.write("\3\2\2\2\u0168\u0169\5T+\2\u0169\u016a\5H%\2\u016a\u016b")
        buf.write("\5T+\2\u016b\u016e\3\2\2\2\u016c\u016e\5T+\2\u016d\u0168")
        buf.write("\3\2\2\2\u016d\u016c\3\2\2\2\u016eS\3\2\2\2\u016f\u0170")
        buf.write("\b+\1\2\u0170\u0171\5V,\2\u0171\u0178\3\2\2\2\u0172\u0173")
        buf.write("\f\4\2\2\u0173\u0174\5J&\2\u0174\u0175\5V,\2\u0175\u0177")
        buf.write("\3\2\2\2\u0176\u0172\3\2\2\2\u0177\u017a\3\2\2\2\u0178")
        buf.write("\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179U\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017b\u017c\b,\1\2\u017c\u017d\5X-\2\u017d")
        buf.write("\u0184\3\2\2\2\u017e\u017f\f\4\2\2\u017f\u0180\5L\'\2")
        buf.write("\u0180\u0181\5X-\2\u0181\u0183\3\2\2\2\u0182\u017e\3\2")
        buf.write("\2\2\u0183\u0186\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185")
        buf.write("\3\2\2\2\u0185W\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u0188")
        buf.write("\b-\1\2\u0188\u0189\5Z.\2\u0189\u0190\3\2\2\2\u018a\u018b")
        buf.write("\f\4\2\2\u018b\u018c\5N(\2\u018c\u018d\5Z.\2\u018d\u018f")
        buf.write("\3\2\2\2\u018e\u018a\3\2\2\2\u018f\u0192\3\2\2\2\u0190")
        buf.write("\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191Y\3\2\2\2\u0192")
        buf.write("\u0190\3\2\2\2\u0193\u0194\7%\2\2\u0194\u0197\5Z.\2\u0195")
        buf.write("\u0197\5\\/\2\u0196\u0193\3\2\2\2\u0196\u0195\3\2\2\2")
        buf.write("\u0197[\3\2\2\2\u0198\u0199\7\32\2\2\u0199\u019c\5\\/")
        buf.write("\2\u019a\u019c\5^\60\2\u019b\u0198\3\2\2\2\u019b\u019a")
        buf.write("\3\2\2\2\u019c]\3\2\2\2\u019d\u019e\5`\61\2\u019e\u019f")
        buf.write("\7-\2\2\u019f\u01a0\5P)\2\u01a0\u01a1\7.\2\2\u01a1\u01a4")
        buf.write("\3\2\2\2\u01a2\u01a4\5`\61\2\u01a3\u019d\3\2\2\2\u01a3")
        buf.write("\u01a2\3\2\2\2\u01a4_\3\2\2\2\u01a5\u01a6\b\61\1\2\u01a6")
        buf.write("\u01a7\5b\62\2\u01a7\u01b4\3\2\2\2\u01a8\u01a9\f\5\2\2")
        buf.write("\u01a9\u01aa\7/\2\2\u01aa\u01b3\7:\2\2\u01ab\u01ac\f\4")
        buf.write("\2\2\u01ac\u01ad\7/\2\2\u01ad\u01ae\7:\2\2\u01ae\u01af")
        buf.write("\7+\2\2\u01af\u01b0\5B\"\2\u01b0\u01b1\7,\2\2\u01b1\u01b3")
        buf.write("\3\2\2\2\u01b2\u01a8\3\2\2\2\u01b2\u01ab\3\2\2\2\u01b3")
        buf.write("\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2")
        buf.write("\u01b5a\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b7\u01b8\t\n\2")
        buf.write("\2\u01b8\u01ba\7/\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba")
        buf.write("\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01c7\7;\2\2\u01bc")
        buf.write("\u01bd\t\n\2\2\u01bd\u01bf\7/\2\2\u01be\u01bc\3\2\2\2")
        buf.write("\u01be\u01bf\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1\7")
        buf.write(";\2\2\u01c1\u01c2\7+\2\2\u01c2\u01c3\5B\"\2\u01c3\u01c4")
        buf.write("\7,\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c7\5d\63\2\u01c6")
        buf.write("\u01b9\3\2\2\2\u01c6\u01be\3\2\2\2\u01c6\u01c5\3\2\2\2")
        buf.write("\u01c7c\3\2\2\2\u01c8\u01c9\7\25\2\2\u01c9\u01ca\5\b\5")
        buf.write("\2\u01ca\u01cb\7+\2\2\u01cb\u01cc\5B\"\2\u01cc\u01cd\7")
        buf.write(",\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01d0\5f\64\2\u01cf\u01c8")
        buf.write("\3\2\2\2\u01cf\u01ce\3\2\2\2\u01d0e\3\2\2\2\u01d1\u01d5")
        buf.write("\5.\30\2\u01d2\u01d5\5\b\5\2\u01d3\u01d5\7\24\2\2\u01d4")
        buf.write("\u01d1\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d3\3\2\2\2")
        buf.write("\u01d5g\3\2\2\2\u01d6\u01df\7\23\2\2\u01d7\u01d8\5\32")
        buf.write("\16\2\u01d8\u01d9\7\62\2\2\u01d9\u01da\5\26\f\2\u01da")
        buf.write("\u01db\7\61\2\2\u01db\u01e0\3\2\2\2\u01dc\u01dd\5\30\r")
        buf.write("\2\u01dd\u01de\7\61\2\2\u01de\u01e0\3\2\2\2\u01df\u01d7")
        buf.write("\3\2\2\2\u01df\u01dc\3\2\2\2\u01e0i\3\2\2\2\u01e1\u01ea")
        buf.write("\7\27\2\2\u01e2\u01e3\5\32\16\2\u01e3\u01e4\7\62\2\2\u01e4")
        buf.write("\u01e5\5\26\f\2\u01e5\u01e6\7\61\2\2\u01e6\u01eb\3\2\2")
        buf.write("\2\u01e7\u01e8\5\30\r\2\u01e8\u01e9\7\61\2\2\u01e9\u01eb")
        buf.write("\3\2\2\2\u01ea\u01e2\3\2\2\2\u01ea\u01e7\3\2\2\2\u01eb")
        buf.write("k\3\2\2\2\u01ec\u01ed\5P)\2\u01ed\u01ee\7!\2\2\u01ee\u01ef")
        buf.write("\5P)\2\u01ef\u01f0\7\61\2\2\u01f0m\3\2\2\2\u01f1\u01f3")
        buf.write("\7\6\2\2\u01f2\u01f4\5z>\2\u01f3\u01f2\3\2\2\2\u01f3\u01f4")
        buf.write("\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f6\5P)\2\u01f6\u01f9")
        buf.write("\5z>\2\u01f7\u01f8\7\7\2\2\u01f8\u01fa\5z>\2\u01f9\u01f7")
        buf.write("\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fao\3\2\2\2\u01fb\u01fc")
        buf.write("\7\b\2\2\u01fc\u01fd\5l\67\2\u01fd\u01fe\5R*\2\u01fe\u01ff")
        buf.write("\7\61\2\2\u01ff\u0200\5z>\2\u0200q\3\2\2\2\u0201\u0202")
        buf.write("\7\4\2\2\u0202\u0203\7\61\2\2\u0203s\3\2\2\2\u0204\u0205")
        buf.write("\7\5\2\2\u0205\u0206\7\61\2\2\u0206u\3\2\2\2\u0207\u020a")
        buf.write("\7\17\2\2\u0208\u020b\5P)\2\u0209\u020b\5\b\5\2\u020a")
        buf.write("\u0208\3\2\2\2\u020a\u0209\3\2\2\2\u020a\u020b\3\2\2\2")
        buf.write("\u020b\u020c\3\2\2\2\u020c\u020d\7\61\2\2\u020dw\3\2\2")
        buf.write("\2\u020e\u0211\5> \2\u020f\u0211\5@!\2\u0210\u020e\3\2")
        buf.write("\2\2\u0210\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0213")
        buf.write("\7\61\2\2\u0213y\3\2\2\2\u0214\u0215\7\63\2\2\u0215\u0216")
        buf.write("\5|?\2\u0216\u0217\7\64\2\2\u0217{\3\2\2\2\u0218\u0219")
        buf.write("\5~@\2\u0219\u021a\5|?\2\u021a\u021d\3\2\2\2\u021b\u021d")
        buf.write("\3\2\2\2\u021c\u0218\3\2\2\2\u021c\u021b\3\2\2\2\u021d")
        buf.write("}\3\2\2\2\u021e\u0228\5h\65\2\u021f\u0228\5j\66\2\u0220")
        buf.write("\u0228\5l\67\2\u0221\u0228\5n8\2\u0222\u0228\5p9\2\u0223")
        buf.write("\u0228\5r:\2\u0224\u0228\5t;\2\u0225\u0228\5v<\2\u0226")
        buf.write("\u0228\5x=\2\u0227\u021e\3\2\2\2\u0227\u021f\3\2\2\2\u0227")
        buf.write("\u0220\3\2\2\2\u0227\u0221\3\2\2\2\u0227\u0222\3\2\2\2")
        buf.write("\u0227\u0223\3\2\2\2\u0227\u0224\3\2\2\2\u0227\u0225\3")
        buf.write("\2\2\2\u0227\u0226\3\2\2\2\u0228\177\3\2\2\2\60\u0087")
        buf.write("\u008f\u009a\u009e\u00a2\u00bc\u00c3\u00cd\u00d3\u00d7")
        buf.write("\u00e3\u00f0\u00f4\u00fa\u010b\u0117\u011f\u0121\u0133")
        buf.write("\u0140\u014c\u0150\u0157\u0166\u016d\u0178\u0184\u0190")
        buf.write("\u0196\u019b\u01a3\u01b2\u01b4\u01b9\u01be\u01c6\u01cf")
        buf.write("\u01d4\u01df\u01ea\u01f3\u01f9\u020a\u0210\u021c\u0227")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<-'", "'break'", "'continue'", "'if'", 
                     "'else'", "'for'", "'true'", "'false'", "'int'", "'float'", 
                     "'bool'", "'string'", "'return'", "'null'", "'class'", 
                     "'constructor'", "'var'", "'self'", "'new'", "'void'", 
                     "'const'", "'func'", "'+'", "'-'", "'*'", "'/'", "'\\'", 
                     "'&&'", "'||'", "'=='", "':='", "'!='", "'<='", "'>='", 
                     "'!'", "'='", "'<'", "'>'", "'^'", "'%'", "'('", "')'", 
                     "'['", "']'", "'.'", "','", "';'", "':'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "BREAK", "CONTINUE", "IF", 
                      "ELSE", "FOR", "TRUE", "FALSE", "INT", "FLOAT", "BOOL", 
                      "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
                      "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", "PLUS", 
                      "MINUS", "MULTIPLY", "DIVIDE_FLOAT", "DIVIDE_INT", 
                      "AND", "OR", "EQ", "ASSIGN", "NEQ", "LEQ", "GEQ", 
                      "DIFF", "DECLARE", "LE", "GE", "CONCAT", "MOD", "LRB", 
                      "RRB", "LSB", "RSB", "DOT", "CM", "SM", "COLON", "LCB", 
                      "RCB", "INTLIT", "FLOATLIT", "STRINGLIT", "BLOCKCMT", 
                      "LINECMT", "ID", "ATIDENTIFIER", "ARRAYSIZE", "WS", 
                      "UNCLOSED_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_identifier = 3
    RULE_classdecl = 4
    RULE_memberlist = 5
    RULE_member = 6
    RULE_attributedecl = 7
    RULE_attributenodeclare = 8
    RULE_attributewithdeclare = 9
    RULE_typ = 10
    RULE_attlist = 11
    RULE_attributelist = 12
    RULE_methoddecl = 13
    RULE_parameterlist = 14
    RULE_parameterprime = 15
    RULE_parameterpart1 = 16
    RULE_parameterpart2 = 17
    RULE_identifierlist = 18
    RULE_identifierprime = 19
    RULE_constructor = 20
    RULE_superpart = 21
    RULE_literal = 22
    RULE_boolit = 23
    RULE_arraylit = 24
    RULE_literallist = 25
    RULE_arraydecl = 26
    RULE_objdecl = 27
    RULE_instanceattributestate = 28
    RULE_staticattributestate = 29
    RULE_instancemethodstate = 30
    RULE_staticmethodstate = 31
    RULE_explist = 32
    RULE_nullableexplist = 33
    RULE_expprime = 34
    RULE_relational = 35
    RULE_logical = 36
    RULE_adding = 37
    RULE_multiplying = 38
    RULE_exp = 39
    RULE_exp1 = 40
    RULE_exp2 = 41
    RULE_exp3 = 42
    RULE_exp4 = 43
    RULE_exp5 = 44
    RULE_exp6 = 45
    RULE_exp7 = 46
    RULE_exp8 = 47
    RULE_exp9 = 48
    RULE_exp10 = 49
    RULE_exp11 = 50
    RULE_varstate = 51
    RULE_constate = 52
    RULE_assignstate = 53
    RULE_ifstate = 54
    RULE_forstate = 55
    RULE_breakstate = 56
    RULE_continuestate = 57
    RULE_returnstate = 58
    RULE_methodinvoke = 59
    RULE_blockstate = 60
    RULE_stmtlist = 61
    RULE_stmt = 62

    ruleNames =  [ "program", "decllist", "decl", "identifier", "classdecl", 
                   "memberlist", "member", "attributedecl", "attributenodeclare", 
                   "attributewithdeclare", "typ", "attlist", "attributelist", 
                   "methoddecl", "parameterlist", "parameterprime", "parameterpart1", 
                   "parameterpart2", "identifierlist", "identifierprime", 
                   "constructor", "superpart", "literal", "boolit", "arraylit", 
                   "literallist", "arraydecl", "objdecl", "instanceattributestate", 
                   "staticattributestate", "instancemethodstate", "staticmethodstate", 
                   "explist", "nullableexplist", "expprime", "relational", 
                   "logical", "adding", "multiplying", "exp", "exp1", "exp2", 
                   "exp3", "exp4", "exp5", "exp6", "exp7", "exp8", "exp9", 
                   "exp10", "exp11", "varstate", "constate", "assignstate", 
                   "ifstate", "forstate", "breakstate", "continuestate", 
                   "returnstate", "methodinvoke", "blockstate", "stmtlist", 
                   "stmt" ]

    EOF = Token.EOF
    T__0=1
    BREAK=2
    CONTINUE=3
    IF=4
    ELSE=5
    FOR=6
    TRUE=7
    FALSE=8
    INT=9
    FLOAT=10
    BOOL=11
    STRING=12
    RETURN=13
    NULL=14
    CLASS=15
    CONSTRUCTOR=16
    VAR=17
    SELF=18
    NEW=19
    VOID=20
    CONST=21
    FUNC=22
    PLUS=23
    MINUS=24
    MULTIPLY=25
    DIVIDE_FLOAT=26
    DIVIDE_INT=27
    AND=28
    OR=29
    EQ=30
    ASSIGN=31
    NEQ=32
    LEQ=33
    GEQ=34
    DIFF=35
    DECLARE=36
    LE=37
    GE=38
    CONCAT=39
    MOD=40
    LRB=41
    RRB=42
    LSB=43
    RSB=44
    DOT=45
    CM=46
    SM=47
    COLON=48
    LCB=49
    RCB=50
    INTLIT=51
    FLOATLIT=52
    STRINGLIT=53
    BLOCKCMT=54
    LINECMT=55
    ID=56
    ATIDENTIFIER=57
    ARRAYSIZE=58
    WS=59
    UNCLOSED_STRING=60
    ILLEGAL_ESCAPE=61
    ERROR_CHAR=62

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

        def decllist(self):
            return self.getTypedRuleContext(CSlangParser.DecllistContext,0)


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
            self.state = 126
            self.decllist()
            self.state = 127
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(CSlangParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(CSlangParser.DecllistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = CSlangParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.decl()
                self.state = 130
                self.decllist()
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


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecl(self):
            return self.getTypedRuleContext(CSlangParser.ClassdeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = CSlangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.classdecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def ATIDENTIFIER(self):
            return self.getToken(CSlangParser.ATIDENTIFIER, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = CSlangParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.ATIDENTIFIER):
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


    class ClassdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CSlangParser.CLASS, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LCB(self):
            return self.getToken(CSlangParser.LCB, 0)

        def memberlist(self):
            return self.getTypedRuleContext(CSlangParser.MemberlistContext,0)


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
        self.enterRule(localctx, 8, self.RULE_classdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(CSlangParser.CLASS)
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 140
                self.superpart()


            self.state = 143
            self.match(CSlangParser.ID)
            self.state = 144
            self.match(CSlangParser.LCB)
            self.state = 145
            self.memberlist()
            self.state = 146
            self.match(CSlangParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(CSlangParser.MemberContext,0)


        def memberlist(self):
            return self.getTypedRuleContext(CSlangParser.MemberlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_memberlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberlist" ):
                return visitor.visitMemberlist(self)
            else:
                return visitor.visitChildren(self)




    def memberlist(self):

        localctx = CSlangParser.MemberlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_memberlist)
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.member()
                self.state = 149
                self.memberlist()
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

        def attributedecl(self):
            return self.getTypedRuleContext(CSlangParser.AttributedeclContext,0)


        def methoddecl(self):
            return self.getTypedRuleContext(CSlangParser.MethoddeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = CSlangParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_member)
        try:
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.attributedecl()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.methoddecl()
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


    class AttributedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributewithdeclare(self):
            return self.getTypedRuleContext(CSlangParser.AttributewithdeclareContext,0)


        def attributenodeclare(self):
            return self.getTypedRuleContext(CSlangParser.AttributenodeclareContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attributedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributedecl" ):
                return visitor.visitAttributedecl(self)
            else:
                return visitor.visitChildren(self)




    def attributedecl(self):

        localctx = CSlangParser.AttributedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attributedecl)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.attributewithdeclare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.attributenodeclare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributenodeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributelist(self):
            return self.getTypedRuleContext(CSlangParser.AttributelistContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attributenodeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributenodeclare" ):
                return visitor.visitAttributenodeclare(self)
            else:
                return visitor.visitChildren(self)




    def attributenodeclare(self):

        localctx = CSlangParser.AttributenodeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attributenodeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 163
            self.attributelist()
            self.state = 164
            self.match(CSlangParser.COLON)
            self.state = 165
            self.typ()
            self.state = 166
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributewithdeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attlist(self):
            return self.getTypedRuleContext(CSlangParser.AttlistContext,0)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attributewithdeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributewithdeclare" ):
                return visitor.visitAttributewithdeclare(self)
            else:
                return visitor.visitChildren(self)




    def attributewithdeclare(self):

        localctx = CSlangParser.AttributewithdeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attributewithdeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 169
            self.attlist()
            self.state = 170
            self.match(CSlangParser.SM)
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

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

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
        self.enterRule(localctx, 20, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
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


    class AttlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def attlist(self):
            return self.getTypedRuleContext(CSlangParser.AttlistContext,0)


        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def DECLARE(self):
            return self.getToken(CSlangParser.DECLARE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttlist" ):
                return visitor.visitAttlist(self)
            else:
                return visitor.visitChildren(self)




    def attlist(self):

        localctx = CSlangParser.AttlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_attlist)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.identifier()
                self.state = 175
                self.match(CSlangParser.CM)
                self.state = 176
                self.attlist()
                self.state = 177
                self.match(CSlangParser.CM)
                self.state = 178
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.identifier()
                self.state = 181
                self.match(CSlangParser.COLON)
                self.state = 182
                self.typ()
                self.state = 183
                self.match(CSlangParser.DECLARE)
                self.state = 184
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def attributelist(self):
            return self.getTypedRuleContext(CSlangParser.AttributelistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attributelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributelist" ):
                return visitor.visitAttributelist(self)
            else:
                return visitor.visitChildren(self)




    def attributelist(self):

        localctx = CSlangParser.AttributelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_attributelist)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.identifier()
                self.state = 189
                self.match(CSlangParser.CM)
                self.state = 190
                self.attributelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethoddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def LRB(self):
            return self.getToken(CSlangParser.LRB, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(CSlangParser.ParameterlistContext,0)


        def RRB(self):
            return self.getToken(CSlangParser.RRB, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def blockstate(self):
            return self.getTypedRuleContext(CSlangParser.BlockstateContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def ATIDENTIFIER(self):
            return self.getToken(CSlangParser.ATIDENTIFIER, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_methoddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethoddecl" ):
                return visitor.visitMethoddecl(self)
            else:
                return visitor.visitChildren(self)




    def methoddecl(self):

        localctx = CSlangParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_methoddecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(CSlangParser.FUNC)
            self.state = 196
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.ATIDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 197
            self.match(CSlangParser.LRB)
            self.state = 198
            self.parameterlist()
            self.state = 199
            self.match(CSlangParser.RRB)
            self.state = 200
            self.match(CSlangParser.COLON)
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING]:
                self.state = 201
                self.typ()
                pass
            elif token in [CSlangParser.VOID]:
                self.state = 202
                self.match(CSlangParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 205
            self.blockstate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterprime(self):
            return self.getTypedRuleContext(CSlangParser.ParameterprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_parameterlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterlist" ):
                return visitor.visitParameterlist(self)
            else:
                return visitor.visitChildren(self)




    def parameterlist(self):

        localctx = CSlangParser.ParameterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parameterlist)
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.COLON, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.parameterprime()
                pass
            elif token in [CSlangParser.RRB]:
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


    class ParameterprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterpart1(self):
            return self.getTypedRuleContext(CSlangParser.Parameterpart1Context,0)


        def parameterpart2(self):
            return self.getTypedRuleContext(CSlangParser.Parameterpart2Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_parameterprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterprime" ):
                return visitor.visitParameterprime(self)
            else:
                return visitor.visitChildren(self)




    def parameterprime(self):

        localctx = CSlangParser.ParameterprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_parameterprime)
        try:
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.parameterpart1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.parameterpart2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameterpart1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def parameterpart1(self):
            return self.getTypedRuleContext(CSlangParser.Parameterpart1Context,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_parameterpart1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterpart1" ):
                return visitor.visitParameterpart1(self)
            else:
                return visitor.visitChildren(self)




    def parameterpart1(self):

        localctx = CSlangParser.Parameterpart1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_parameterpart1)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.match(CSlangParser.ID)
                self.state = 216
                self.match(CSlangParser.COLON)
                self.state = 217
                self.typ()
                self.state = 219
                self.match(CSlangParser.CM)
                self.state = 220
                self.parameterpart1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.match(CSlangParser.ID)
                self.state = 223
                self.match(CSlangParser.COLON)
                self.state = 224
                self.typ()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameterpart2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def parameterpart2(self):
            return self.getTypedRuleContext(CSlangParser.Parameterpart2Context,0)


        def identifierlist(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierlistContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_parameterpart2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterpart2" ):
                return visitor.visitParameterpart2(self)
            else:
                return visitor.visitChildren(self)




    def parameterpart2(self):

        localctx = CSlangParser.Parameterpart2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameterpart2)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.identifierlist()
                self.state = 228
                self.match(CSlangParser.COLON)
                self.state = 229
                self.typ()
                self.state = 231
                self.match(CSlangParser.CM)
                self.state = 232
                self.parameterpart2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.identifierlist()
                self.state = 235
                self.match(CSlangParser.COLON)
                self.state = 236
                self.typ()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierprime(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_identifierlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierlist" ):
                return visitor.visitIdentifierlist(self)
            else:
                return visitor.visitChildren(self)




    def identifierlist(self):

        localctx = CSlangParser.IdentifierlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_identifierlist)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.identifierprime()
                pass
            elif token in [CSlangParser.COLON]:
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


    class IdentifierprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def identifierprime(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_identifierprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierprime" ):
                return visitor.visitIdentifierprime(self)
            else:
                return visitor.visitChildren(self)




    def identifierprime(self):

        localctx = CSlangParser.IdentifierprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_identifierprime)
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.match(CSlangParser.ID)
                self.state = 245
                self.match(CSlangParser.CM)
                self.state = 246
                self.identifierprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.match(CSlangParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def CONSTRUCTOR(self):
            return self.getToken(CSlangParser.CONSTRUCTOR, 0)

        def LRB(self):
            return self.getToken(CSlangParser.LRB, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(CSlangParser.ParameterlistContext,0)


        def RRB(self):
            return self.getToken(CSlangParser.RRB, 0)

        def blockstate(self):
            return self.getTypedRuleContext(CSlangParser.BlockstateContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = CSlangParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(CSlangParser.FUNC)
            self.state = 251
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 252
            self.match(CSlangParser.LRB)
            self.state = 253
            self.parameterlist()
            self.state = 254
            self.match(CSlangParser.RRB)
            self.state = 255
            self.blockstate()
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

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_superpart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuperpart" ):
                return visitor.visitSuperpart(self)
            else:
                return visitor.visitChildren(self)




    def superpart(self):

        localctx = CSlangParser.SuperpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_superpart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(CSlangParser.ID)
            self.state = 258
            self.match(CSlangParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
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

        def arraylit(self):
            return self.getTypedRuleContext(CSlangParser.ArraylitContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CSlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_literal)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 262
                self.boolit()
                pass
            elif token in [CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 263
                self.match(CSlangParser.STRINGLIT)
                pass
            elif token in [CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 264
                self.arraylit()
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
        self.enterRule(localctx, 46, self.RULE_boolit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
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


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(CSlangParser.LSB, 0)

        def literallist(self):
            return self.getTypedRuleContext(CSlangParser.LiterallistContext,0)


        def RSB(self):
            return self.getToken(CSlangParser.RSB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = CSlangParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(CSlangParser.LSB)
            self.state = 270
            self.literallist()
            self.state = 271
            self.match(CSlangParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiterallistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def literallist(self):
            return self.getTypedRuleContext(CSlangParser.LiterallistContext,0)


        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(CSlangParser.FLOATLIT, 0)

        def boolit(self):
            return self.getTypedRuleContext(CSlangParser.BoolitContext,0)


        def STRINGLIT(self):
            return self.getToken(CSlangParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_literallist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterallist" ):
                return visitor.visitLiterallist(self)
            else:
                return visitor.visitChildren(self)




    def literallist(self):

        localctx = CSlangParser.LiterallistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_literallist)
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.INTLIT]:
                    self.state = 273
                    self.match(CSlangParser.INTLIT)
                    pass
                elif token in [CSlangParser.FLOATLIT]:
                    self.state = 274
                    self.match(CSlangParser.FLOATLIT)
                    pass
                elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                    self.state = 275
                    self.boolit()
                    pass
                elif token in [CSlangParser.STRINGLIT]:
                    self.state = 276
                    self.match(CSlangParser.STRINGLIT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 279
                self.match(CSlangParser.CM)
                self.state = 280
                self.literallist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.INTLIT]:
                    self.state = 281
                    self.match(CSlangParser.INTLIT)
                    pass
                elif token in [CSlangParser.FLOATLIT]:
                    self.state = 282
                    self.match(CSlangParser.FLOATLIT)
                    pass
                elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                    self.state = 283
                    self.boolit()
                    pass
                elif token in [CSlangParser.STRINGLIT]:
                    self.state = 284
                    self.match(CSlangParser.STRINGLIT)
                    pass
                else:
                    raise NoViableAltException(self)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(CSlangParser.LSB, 0)

        def ARRAYSIZE(self):
            return self.getToken(CSlangParser.ARRAYSIZE, 0)

        def RSB(self):
            return self.getToken(CSlangParser.RSB, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_arraydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




    def arraydecl(self):

        localctx = CSlangParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_arraydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(CSlangParser.LSB)
            self.state = 290
            self.match(CSlangParser.ARRAYSIZE)
            self.state = 291
            self.match(CSlangParser.RSB)
            self.state = 292
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LRB(self):
            return self.getToken(CSlangParser.LRB, 0)

        def RRB(self):
            return self.getToken(CSlangParser.RRB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_objdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjdecl" ):
                return visitor.visitObjdecl(self)
            else:
                return visitor.visitChildren(self)




    def objdecl(self):

        localctx = CSlangParser.ObjdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_objdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(CSlangParser.NEW)
            self.state = 295
            self.match(CSlangParser.ID)
            self.state = 296
            self.match(CSlangParser.LRB)
            self.state = 297
            self.match(CSlangParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceattributestateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_instanceattributestate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceattributestate" ):
                return visitor.visitInstanceattributestate(self)
            else:
                return visitor.visitChildren(self)




    def instanceattributestate(self):

        localctx = CSlangParser.InstanceattributestateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_instanceattributestate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.exp()
            self.state = 300
            self.match(CSlangParser.DOT)
            self.state = 301
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticattributestateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATIDENTIFIER(self):
            return self.getToken(CSlangParser.ATIDENTIFIER, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_staticattributestate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaticattributestate" ):
                return visitor.visitStaticattributestate(self)
            else:
                return visitor.visitChildren(self)




    def staticattributestate(self):

        localctx = CSlangParser.StaticattributestateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_staticattributestate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 303
                self.match(CSlangParser.ID)
                self.state = 304
                self.match(CSlangParser.DOT)


            self.state = 307
            self.match(CSlangParser.ATIDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstancemethodstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def LRB(self):
            return self.getToken(CSlangParser.LRB, 0)

        def nullableexplist(self):
            return self.getTypedRuleContext(CSlangParser.NullableexplistContext,0)


        def RRB(self):
            return self.getToken(CSlangParser.RRB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_instancemethodstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstancemethodstate" ):
                return visitor.visitInstancemethodstate(self)
            else:
                return visitor.visitChildren(self)




    def instancemethodstate(self):

        localctx = CSlangParser.InstancemethodstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_instancemethodstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.exp()
            self.state = 310
            self.match(CSlangParser.DOT)
            self.state = 311
            self.identifier()
            self.state = 312
            self.match(CSlangParser.LRB)
            self.state = 313
            self.nullableexplist()
            self.state = 314
            self.match(CSlangParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticmethodstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATIDENTIFIER(self):
            return self.getToken(CSlangParser.ATIDENTIFIER, 0)

        def LRB(self):
            return self.getToken(CSlangParser.LRB, 0)

        def nullableexplist(self):
            return self.getTypedRuleContext(CSlangParser.NullableexplistContext,0)


        def RRB(self):
            return self.getToken(CSlangParser.RRB, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_staticmethodstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaticmethodstate" ):
                return visitor.visitStaticmethodstate(self)
            else:
                return visitor.visitChildren(self)




    def staticmethodstate(self):

        localctx = CSlangParser.StaticmethodstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_staticmethodstate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 316
                self.match(CSlangParser.ID)
                self.state = 317
                self.match(CSlangParser.DOT)


            self.state = 320
            self.match(CSlangParser.ATIDENTIFIER)
            self.state = 321
            self.match(CSlangParser.LRB)
            self.state = 322
            self.nullableexplist()
            self.state = 323
            self.match(CSlangParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def explist(self):
            return self.getTypedRuleContext(CSlangParser.ExplistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_explist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist" ):
                return visitor.visitExplist(self)
            else:
                return visitor.visitChildren(self)




    def explist(self):

        localctx = CSlangParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_explist)
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.exp()
                self.state = 326
                self.match(CSlangParser.CM)
                self.state = 327
                self.explist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NullableexplistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expprime(self):
            return self.getTypedRuleContext(CSlangParser.ExpprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_nullableexplist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullableexplist" ):
                return visitor.visitNullableexplist(self)
            else:
                return visitor.visitChildren(self)




    def nullableexplist(self):

        localctx = CSlangParser.NullableexplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_nullableexplist)
        try:
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.DIFF, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.expprime()
                pass
            elif token in [CSlangParser.RRB]:
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


    class ExpprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def expprime(self):
            return self.getTypedRuleContext(CSlangParser.ExpprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpprime" ):
                return visitor.visitExpprime(self)
            else:
                return visitor.visitChildren(self)




    def expprime(self):

        localctx = CSlangParser.ExpprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expprime)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.exp()
                self.state = 337
                self.match(CSlangParser.CM)
                self.state = 338
                self.expprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(CSlangParser.EQ, 0)

        def NEQ(self):
            return self.getToken(CSlangParser.NEQ, 0)

        def LE(self):
            return self.getToken(CSlangParser.LE, 0)

        def GE(self):
            return self.getToken(CSlangParser.GE, 0)

        def LEQ(self):
            return self.getToken(CSlangParser.LEQ, 0)

        def GEQ(self):
            return self.getToken(CSlangParser.GEQ, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = CSlangParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQ) | (1 << CSlangParser.NEQ) | (1 << CSlangParser.LEQ) | (1 << CSlangParser.GEQ) | (1 << CSlangParser.LE) | (1 << CSlangParser.GE))) != 0)):
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
        self.enterRule(localctx, 72, self.RULE_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
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
        self.enterRule(localctx, 74, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
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

        def MULTIPLY(self):
            return self.getToken(CSlangParser.MULTIPLY, 0)

        def DIVIDE_FLOAT(self):
            return self.getToken(CSlangParser.DIVIDE_FLOAT, 0)

        def DIVIDE_INT(self):
            return self.getToken(CSlangParser.DIVIDE_INT, 0)

        def MOD(self):
            return self.getToken(CSlangParser.MOD, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_multiplying

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying" ):
                return visitor.visitMultiplying(self)
            else:
                return visitor.visitChildren(self)




    def multiplying(self):

        localctx = CSlangParser.MultiplyingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MULTIPLY) | (1 << CSlangParser.DIVIDE_FLOAT) | (1 << CSlangParser.DIVIDE_INT) | (1 << CSlangParser.MOD))) != 0)):
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


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Exp1Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Exp1Context,i)


        def CONCAT(self):
            return self.getToken(CSlangParser.CONCAT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = CSlangParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_exp)
        try:
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.exp1()
                self.state = 352
                self.match(CSlangParser.CONCAT)
                self.state = 353
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Exp2Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Exp2Context,i)


        def relational(self):
            return self.getTypedRuleContext(CSlangParser.RelationalContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = CSlangParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exp1)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.exp2(0)
                self.state = 359
                self.relational()
                self.state = 360
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(CSlangParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(CSlangParser.Exp2Context,0)


        def logical(self):
            return self.getTypedRuleContext(CSlangParser.LogicalContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 368
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 369
                    self.logical()
                    self.state = 370
                    self.exp3(0) 
                self.state = 376
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(CSlangParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(CSlangParser.Exp3Context,0)


        def adding(self):
            return self.getTypedRuleContext(CSlangParser.AddingContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 386
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 380
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 381
                    self.adding()
                    self.state = 382
                    self.exp4(0) 
                self.state = 388
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(CSlangParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(CSlangParser.Exp4Context,0)


        def multiplying(self):
            return self.getTypedRuleContext(CSlangParser.MultiplyingContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 398
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 392
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 393
                    self.multiplying()
                    self.state = 394
                    self.exp5() 
                self.state = 400
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIFF(self):
            return self.getToken(CSlangParser.DIFF, 0)

        def exp5(self):
            return self.getTypedRuleContext(CSlangParser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(CSlangParser.Exp6Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = CSlangParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_exp5)
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.DIFF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(CSlangParser.DIFF)
                self.state = 402
                self.exp5()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
                self.exp6()
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


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(CSlangParser.MINUS, 0)

        def exp6(self):
            return self.getTypedRuleContext(CSlangParser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(CSlangParser.Exp7Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = CSlangParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_exp6)
        try:
            self.state = 409
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.match(CSlangParser.MINUS)
                self.state = 407
                self.exp6()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.exp7()
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


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(CSlangParser.Exp8Context,0)


        def LSB(self):
            return self.getToken(CSlangParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def RSB(self):
            return self.getToken(CSlangParser.RSB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = CSlangParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_exp7)
        try:
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.exp8(0)
                self.state = 412
                self.match(CSlangParser.LSB)
                self.state = 413
                self.exp()
                self.state = 414
                self.match(CSlangParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.exp8(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(CSlangParser.Exp9Context,0)


        def exp8(self):
            return self.getTypedRuleContext(CSlangParser.Exp8Context,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LRB(self):
            return self.getToken(CSlangParser.LRB, 0)

        def explist(self):
            return self.getTypedRuleContext(CSlangParser.ExplistContext,0)


        def RRB(self):
            return self.getToken(CSlangParser.RRB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 434
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 432
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 422
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 423
                        self.match(CSlangParser.DOT)
                        self.state = 424
                        self.match(CSlangParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 425
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 426
                        self.match(CSlangParser.DOT)
                        self.state = 427
                        self.match(CSlangParser.ID)
                        self.state = 428
                        self.match(CSlangParser.LRB)
                        self.state = 429
                        self.explist()
                        self.state = 430
                        self.match(CSlangParser.RRB)
                        pass

             
                self.state = 436
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATIDENTIFIER(self):
            return self.getToken(CSlangParser.ATIDENTIFIER, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def LRB(self):
            return self.getToken(CSlangParser.LRB, 0)

        def explist(self):
            return self.getTypedRuleContext(CSlangParser.ExplistContext,0)


        def RRB(self):
            return self.getToken(CSlangParser.RRB, 0)

        def exp10(self):
            return self.getTypedRuleContext(CSlangParser.Exp10Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)




    def exp9(self):

        localctx = CSlangParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_exp9)
        self._la = 0 # Token type
        try:
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.SELF or _la==CSlangParser.ID:
                    self.state = 437
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.SELF or _la==CSlangParser.ID):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 438
                    self.match(CSlangParser.DOT)


                self.state = 441
                self.match(CSlangParser.ATIDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.SELF or _la==CSlangParser.ID:
                    self.state = 442
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.SELF or _la==CSlangParser.ID):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 443
                    self.match(CSlangParser.DOT)


                self.state = 446
                self.match(CSlangParser.ATIDENTIFIER)
                self.state = 447
                self.match(CSlangParser.LRB)
                self.state = 448
                self.explist()
                self.state = 449
                self.match(CSlangParser.RRB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 451
                self.exp10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def LRB(self):
            return self.getToken(CSlangParser.LRB, 0)

        def explist(self):
            return self.getTypedRuleContext(CSlangParser.ExplistContext,0)


        def RRB(self):
            return self.getToken(CSlangParser.RRB, 0)

        def exp11(self):
            return self.getTypedRuleContext(CSlangParser.Exp11Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = CSlangParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_exp10)
        try:
            self.state = 461
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.match(CSlangParser.NEW)
                self.state = 455
                self.identifier()
                self.state = 456
                self.match(CSlangParser.LRB)
                self.state = 457
                self.explist()
                self.state = 458
                self.match(CSlangParser.RRB)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                self.exp11()
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


    class Exp11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(CSlangParser.LiteralContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp11" ):
                return visitor.visitExp11(self)
            else:
                return visitor.visitChildren(self)




    def exp11(self):

        localctx = CSlangParser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_exp11)
        try:
            self.state = 466
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.literal()
                pass
            elif token in [CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
                self.identifier()
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 465
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


    class VarstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def attributelist(self):
            return self.getTypedRuleContext(CSlangParser.AttributelistContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def attlist(self):
            return self.getTypedRuleContext(CSlangParser.AttlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_varstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarstate" ):
                return visitor.visitVarstate(self)
            else:
                return visitor.visitChildren(self)




    def varstate(self):

        localctx = CSlangParser.VarstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_varstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(CSlangParser.VAR)
            self.state = 477
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 469
                self.attributelist()
                self.state = 470
                self.match(CSlangParser.COLON)
                self.state = 471
                self.typ()
                self.state = 472
                self.match(CSlangParser.SM)
                pass

            elif la_ == 2:
                self.state = 474
                self.attlist()
                self.state = 475
                self.match(CSlangParser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def attributelist(self):
            return self.getTypedRuleContext(CSlangParser.AttributelistContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def attlist(self):
            return self.getTypedRuleContext(CSlangParser.AttlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstate" ):
                return visitor.visitConstate(self)
            else:
                return visitor.visitChildren(self)




    def constate(self):

        localctx = CSlangParser.ConstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_constate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.match(CSlangParser.CONST)
            self.state = 488
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 480
                self.attributelist()
                self.state = 481
                self.match(CSlangParser.COLON)
                self.state = 482
                self.typ()
                self.state = 483
                self.match(CSlangParser.SM)
                pass

            elif la_ == 2:
                self.state = 485
                self.attlist()
                self.state = 486
                self.match(CSlangParser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExpContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExpContext,i)


        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_assignstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstate" ):
                return visitor.visitAssignstate(self)
            else:
                return visitor.visitChildren(self)




    def assignstate(self):

        localctx = CSlangParser.AssignstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_assignstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.exp()
            self.state = 491
            self.match(CSlangParser.ASSIGN)
            self.state = 492
            self.exp()
            self.state = 493
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSlangParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def blockstate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.BlockstateContext)
            else:
                return self.getTypedRuleContext(CSlangParser.BlockstateContext,i)


        def ELSE(self):
            return self.getToken(CSlangParser.ELSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_ifstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstate" ):
                return visitor.visitIfstate(self)
            else:
                return visitor.visitChildren(self)




    def ifstate(self):

        localctx = CSlangParser.IfstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_ifstate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(CSlangParser.IF)
            self.state = 497
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LCB:
                self.state = 496
                self.blockstate()


            self.state = 499
            self.exp()
            self.state = 500
            self.blockstate()
            self.state = 503
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 501
                self.match(CSlangParser.ELSE)
                self.state = 502
                self.blockstate()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSlangParser.FOR, 0)

        def assignstate(self):
            return self.getTypedRuleContext(CSlangParser.AssignstateContext,0)


        def exp1(self):
            return self.getTypedRuleContext(CSlangParser.Exp1Context,0)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def blockstate(self):
            return self.getTypedRuleContext(CSlangParser.BlockstateContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_forstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstate" ):
                return visitor.visitForstate(self)
            else:
                return visitor.visitChildren(self)




    def forstate(self):

        localctx = CSlangParser.ForstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_forstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(CSlangParser.FOR)
            self.state = 506
            self.assignstate()
            self.state = 507
            self.exp1()
            self.state = 508
            self.match(CSlangParser.SM)
            self.state = 509
            self.blockstate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CSlangParser.BREAK, 0)

        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_breakstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstate" ):
                return visitor.visitBreakstate(self)
            else:
                return visitor.visitChildren(self)




    def breakstate(self):

        localctx = CSlangParser.BreakstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_breakstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(CSlangParser.BREAK)
            self.state = 512
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(CSlangParser.CONTINUE, 0)

        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_continuestate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestate" ):
                return visitor.visitContinuestate(self)
            else:
                return visitor.visitChildren(self)




    def continuestate(self):

        localctx = CSlangParser.ContinuestateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_continuestate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(CSlangParser.CONTINUE)
            self.state = 515
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CSlangParser.RETURN, 0)

        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_returnstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstate" ):
                return visitor.visitReturnstate(self)
            else:
                return visitor.visitChildren(self)




    def returnstate(self):

        localctx = CSlangParser.ReturnstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_returnstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(CSlangParser.RETURN)
            self.state = 520
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 518
                self.exp()

            elif la_ == 2:
                self.state = 519
                self.identifier()


            self.state = 522
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodinvokeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def instancemethodstate(self):
            return self.getTypedRuleContext(CSlangParser.InstancemethodstateContext,0)


        def staticmethodstate(self):
            return self.getTypedRuleContext(CSlangParser.StaticmethodstateContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_methodinvoke

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodinvoke" ):
                return visitor.visitMethodinvoke(self)
            else:
                return visitor.visitChildren(self)




    def methodinvoke(self):

        localctx = CSlangParser.MethodinvokeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_methodinvoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 524
                self.instancemethodstate()
                pass

            elif la_ == 2:
                self.state = 525
                self.staticmethodstate()
                pass


            self.state = 528
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstateContext(ParserRuleContext):
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
            return CSlangParser.RULE_blockstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstate" ):
                return visitor.visitBlockstate(self)
            else:
                return visitor.visitChildren(self)




    def blockstate(self):

        localctx = CSlangParser.BlockstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_blockstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.match(CSlangParser.LCB)
            self.state = 531
            self.stmtlist()
            self.state = 532
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
        self.enterRule(localctx, 122, self.RULE_stmtlist)
        try:
            self.state = 538
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.RETURN, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.CONST, CSlangParser.MINUS, CSlangParser.DIFF, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 534
                self.stmt()
                self.state = 535
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

        def varstate(self):
            return self.getTypedRuleContext(CSlangParser.VarstateContext,0)


        def constate(self):
            return self.getTypedRuleContext(CSlangParser.ConstateContext,0)


        def assignstate(self):
            return self.getTypedRuleContext(CSlangParser.AssignstateContext,0)


        def ifstate(self):
            return self.getTypedRuleContext(CSlangParser.IfstateContext,0)


        def forstate(self):
            return self.getTypedRuleContext(CSlangParser.ForstateContext,0)


        def breakstate(self):
            return self.getTypedRuleContext(CSlangParser.BreakstateContext,0)


        def continuestate(self):
            return self.getTypedRuleContext(CSlangParser.ContinuestateContext,0)


        def returnstate(self):
            return self.getTypedRuleContext(CSlangParser.ReturnstateContext,0)


        def methodinvoke(self):
            return self.getTypedRuleContext(CSlangParser.MethodinvokeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_stmt)
        try:
            self.state = 549
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 540
                self.varstate()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 541
                self.constate()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 542
                self.assignstate()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 543
                self.ifstate()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 544
                self.forstate()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 545
                self.breakstate()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 546
                self.continuestate()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 547
                self.returnstate()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 548
                self.methodinvoke()
                pass


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
        self._predicates[41] = self.exp2_sempred
        self._predicates[42] = self.exp3_sempred
        self._predicates[43] = self.exp4_sempred
        self._predicates[47] = self.exp8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




