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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u0237\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\5\3\u008a\n\3\3\4\3\4\3\4\5\4\u008f\n\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\u009a\n\5\3\6\3")
        buf.write("\6\5\6\u009e\n\6\3\7\3\7\5\7\u00a2\n\7\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\5\n\u00ae\n\n\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\5\f\u00b9\n\f\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00c9\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u00dc\n\20\3\21\3\21\5\21\u00e0\n\21\3\22\3\22\5\22\u00e4")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\5\23\u00f0\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\5\24\u00fc\n\24\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u0102\n\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\5\27\u010e\n\27\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u0117\n\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\5\31\u0120\n\31\5\31\u0122\n\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u012f\n\33\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\5\36\u013e\n\36\3\37\3\37\3\37\3\37\3\37\5")
        buf.write("\37\u0145\n\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3$\3")
        buf.write("$\5$\u0154\n$\3%\3%\3%\3%\3%\5%\u015b\n%\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\7&\u0164\n&\f&\16&\u0167\13&\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\7\'\u0170\n\'\f\'\16\'\u0173\13\'\3(\3(\3(")
        buf.write("\3(\3(\3(\3(\7(\u017c\n(\f(\16(\u017f\13(\3)\3)\3)\5)")
        buf.write("\u0184\n)\3*\3*\3*\5*\u0189\n*\3+\3+\3+\3+\3+\3+\5+\u0191")
        buf.write("\n+\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u019c\n,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\5,\u01a5\n,\7,\u01a7\n,\f,\16,\u01aa\13,\3")
        buf.write("-\3-\3-\5-\u01af\n-\3-\3-\3-\3-\3-\3-\5-\u01b7\n-\3-\5")
        buf.write("-\u01ba\n-\3.\3.\3.\3.\3.\3.\3.\5.\u01c3\n.\3/\3/\3/\3")
        buf.write("/\3/\5/\u01ca\n/\3\60\3\60\3\60\3\60\3\60\5\60\u01d1\n")
        buf.write("\60\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\5\63\u01dd\n\63\3\63\3\63\3\63\3\63\3\63\5\63\u01e4\n")
        buf.write("\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\5\67\u01f8\n")
        buf.write("\67\3\67\3\67\38\38\58\u01fe\n8\38\38\39\39\39\39\39\3")
        buf.write("9\39\3:\3:\3:\5:\u020c\n:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3")
        buf.write("<\3<\3<\3<\5<\u021b\n<\3=\3=\3=\3=\3=\3=\3=\3=\3=\5=\u0226")
        buf.write("\n=\3>\3>\3>\3>\3?\3?\3@\3@\5@\u0230\n@\3A\3A\3A\5A\u0235")
        buf.write("\nA\3A\2\6JLNVB\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprt")
        buf.write("vxz|~\u0080\2\b\3\2\t\n\5\2  \"$\'(\3\2\36\37\3\2\31\32")
        buf.write("\4\2\33\35**\3\2:;\2\u023f\2\u0082\3\2\2\2\4\u0089\3\2")
        buf.write("\2\2\6\u008b\3\2\2\2\b\u0099\3\2\2\2\n\u009d\3\2\2\2\f")
        buf.write("\u00a1\3\2\2\2\16\u00a3\3\2\2\2\20\u00a7\3\2\2\2\22\u00ad")
        buf.write("\3\2\2\2\24\u00af\3\2\2\2\26\u00b8\3\2\2\2\30\u00ba\3")
        buf.write("\2\2\2\32\u00c8\3\2\2\2\34\u00ca\3\2\2\2\36\u00db\3\2")
        buf.write("\2\2 \u00df\3\2\2\2\"\u00e3\3\2\2\2$\u00ef\3\2\2\2&\u00fb")
        buf.write("\3\2\2\2(\u0101\3\2\2\2*\u0103\3\2\2\2,\u010d\3\2\2\2")
        buf.write(".\u010f\3\2\2\2\60\u0121\3\2\2\2\62\u0123\3\2\2\2\64\u012e")
        buf.write("\3\2\2\2\66\u0130\3\2\2\28\u0135\3\2\2\2:\u013d\3\2\2")
        buf.write("\2<\u0144\3\2\2\2>\u0146\3\2\2\2@\u0148\3\2\2\2B\u014a")
        buf.write("\3\2\2\2D\u014c\3\2\2\2F\u0153\3\2\2\2H\u015a\3\2\2\2")
        buf.write("J\u015c\3\2\2\2L\u0168\3\2\2\2N\u0174\3\2\2\2P\u0183\3")
        buf.write("\2\2\2R\u0188\3\2\2\2T\u0190\3\2\2\2V\u0192\3\2\2\2X\u01b9")
        buf.write("\3\2\2\2Z\u01c2\3\2\2\2\\\u01c9\3\2\2\2^\u01d0\3\2\2\2")
        buf.write("`\u01d2\3\2\2\2b\u01d4\3\2\2\2d\u01d9\3\2\2\2f\u01e5\3")
        buf.write("\2\2\2h\u01ee\3\2\2\2j\u01f1\3\2\2\2l\u01f4\3\2\2\2n\u01fd")
        buf.write("\3\2\2\2p\u0201\3\2\2\2r\u020b\3\2\2\2t\u0212\3\2\2\2")
        buf.write("v\u021a\3\2\2\2x\u0225\3\2\2\2z\u0227\3\2\2\2|\u022b\3")
        buf.write("\2\2\2~\u022f\3\2\2\2\u0080\u0234\3\2\2\2\u0082\u0083")
        buf.write("\5\4\3\2\u0083\u0084\7\2\2\3\u0084\3\3\2\2\2\u0085\u0086")
        buf.write("\5\6\4\2\u0086\u0087\5\4\3\2\u0087\u008a\3\2\2\2\u0088")
        buf.write("\u008a\3\2\2\2\u0089\u0085\3\2\2\2\u0089\u0088\3\2\2\2")
        buf.write("\u008a\5\3\2\2\2\u008b\u008e\7\21\2\2\u008c\u008f\5*\26")
        buf.write("\2\u008d\u008f\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008d")
        buf.write("\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0091\7:\2\2\u0091")
        buf.write("\u0092\7\63\2\2\u0092\u0093\5\b\5\2\u0093\u0094\7\64\2")
        buf.write("\2\u0094\7\3\2\2\2\u0095\u0096\5\n\6\2\u0096\u0097\5\b")
        buf.write("\5\2\u0097\u009a\3\2\2\2\u0098\u009a\3\2\2\2\u0099\u0095")
        buf.write("\3\2\2\2\u0099\u0098\3\2\2\2\u009a\t\3\2\2\2\u009b\u009e")
        buf.write("\5\f\7\2\u009c\u009e\5\36\20\2\u009d\u009b\3\2\2\2\u009d")
        buf.write("\u009c\3\2\2\2\u009e\13\3\2\2\2\u009f\u00a2\5\16\b\2\u00a0")
        buf.write("\u00a2\5\20\t\2\u00a1\u009f\3\2\2\2\u00a1\u00a0\3\2\2")
        buf.write("\2\u00a2\r\3\2\2\2\u00a3\u00a4\7\23\2\2\u00a4\u00a5\5")
        buf.write("\22\n\2\u00a5\u00a6\7\61\2\2\u00a6\17\3\2\2\2\u00a7\u00a8")
        buf.write("\7\27\2\2\u00a8\u00a9\5\22\n\2\u00a9\u00aa\7\61\2\2\u00aa")
        buf.write("\21\3\2\2\2\u00ab\u00ae\5\30\r\2\u00ac\u00ae\5\24\13\2")
        buf.write("\u00ad\u00ab\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae\23\3\2")
        buf.write("\2\2\u00af\u00b0\5\26\f\2\u00b0\u00b1\7\62\2\2\u00b1\u00b2")
        buf.write("\5~@\2\u00b2\25\3\2\2\2\u00b3\u00b4\5|?\2\u00b4\u00b5")
        buf.write("\7\60\2\2\u00b5\u00b6\5\26\f\2\u00b6\u00b9\3\2\2\2\u00b7")
        buf.write("\u00b9\5|?\2\u00b8\u00b3\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9")
        buf.write("\27\3\2\2\2\u00ba\u00bb\5\32\16\2\u00bb\31\3\2\2\2\u00bc")
        buf.write("\u00bd\5|?\2\u00bd\u00be\7\60\2\2\u00be\u00bf\5\32\16")
        buf.write("\2\u00bf\u00c0\7\60\2\2\u00c0\u00c1\5F$\2\u00c1\u00c9")
        buf.write("\3\2\2\2\u00c2\u00c3\5|?\2\u00c3\u00c4\7\62\2\2\u00c4")
        buf.write("\u00c5\5~@\2\u00c5\u00c6\7&\2\2\u00c6\u00c7\5F$\2\u00c7")
        buf.write("\u00c9\3\2\2\2\u00c8\u00bc\3\2\2\2\u00c8\u00c2\3\2\2\2")
        buf.write("\u00c9\33\3\2\2\2\u00ca\u00cb\7\30\2\2\u00cb\u00cc\7\22")
        buf.write("\2\2\u00cc\u00cd\7+\2\2\u00cd\u00ce\5 \21\2\u00ce\u00cf")
        buf.write("\7,\2\2\u00cf\u00d0\5t;\2\u00d0\35\3\2\2\2\u00d1\u00dc")
        buf.write("\5\34\17\2\u00d2\u00d3\7\30\2\2\u00d3\u00d4\5|?\2\u00d4")
        buf.write("\u00d5\7+\2\2\u00d5\u00d6\5 \21\2\u00d6\u00d7\7,\2\2\u00d7")
        buf.write("\u00d8\7\62\2\2\u00d8\u00d9\5\u0080A\2\u00d9\u00da\5t")
        buf.write(";\2\u00da\u00dc\3\2\2\2\u00db\u00d1\3\2\2\2\u00db\u00d2")
        buf.write("\3\2\2\2\u00dc\37\3\2\2\2\u00dd\u00e0\5\"\22\2\u00de\u00e0")
        buf.write("\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00de\3\2\2\2\u00e0")
        buf.write("!\3\2\2\2\u00e1\u00e4\5$\23\2\u00e2\u00e4\5&\24\2\u00e3")
        buf.write("\u00e1\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4#\3\2\2\2\u00e5")
        buf.write("\u00e6\7:\2\2\u00e6\u00e7\7\62\2\2\u00e7\u00e8\5\64\33")
        buf.write("\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\7\60\2\2\u00ea\u00eb")
        buf.write("\5$\23\2\u00eb\u00f0\3\2\2\2\u00ec\u00ed\7:\2\2\u00ed")
        buf.write("\u00ee\7\62\2\2\u00ee\u00f0\5\64\33\2\u00ef\u00e5\3\2")
        buf.write("\2\2\u00ef\u00ec\3\2\2\2\u00f0%\3\2\2\2\u00f1\u00f2\5")
        buf.write("(\25\2\u00f2\u00f3\7\62\2\2\u00f3\u00f4\5\64\33\2\u00f4")
        buf.write("\u00f5\7\60\2\2\u00f5\u00f6\5&\24\2\u00f6\u00fc\3\2\2")
        buf.write("\2\u00f7\u00f8\5(\25\2\u00f8\u00f9\7\62\2\2\u00f9\u00fa")
        buf.write("\5\64\33\2\u00fa\u00fc\3\2\2\2\u00fb\u00f1\3\2\2\2\u00fb")
        buf.write("\u00f7\3\2\2\2\u00fc\'\3\2\2\2\u00fd\u00fe\7:\2\2\u00fe")
        buf.write("\u00ff\7\60\2\2\u00ff\u0102\5(\25\2\u0100\u0102\7:\2\2")
        buf.write("\u0101\u00fd\3\2\2\2\u0101\u0100\3\2\2\2\u0102)\3\2\2")
        buf.write("\2\u0103\u0104\7:\2\2\u0104\u0105\7\3\2\2\u0105+\3\2\2")
        buf.write("\2\u0106\u010e\7\65\2\2\u0107\u010e\7\66\2\2\u0108\u010e")
        buf.write("\5.\30\2\u0109\u010e\7\67\2\2\u010a\u010e\5z>\2\u010b")
        buf.write("\u010e\7\24\2\2\u010c\u010e\7\20\2\2\u010d\u0106\3\2\2")
        buf.write("\2\u010d\u0107\3\2\2\2\u010d\u0108\3\2\2\2\u010d\u0109")
        buf.write("\3\2\2\2\u010d\u010a\3\2\2\2\u010d\u010b\3\2\2\2\u010d")
        buf.write("\u010c\3\2\2\2\u010e-\3\2\2\2\u010f\u0110\t\2\2\2\u0110")
        buf.write("/\3\2\2\2\u0111\u0117\7\65\2\2\u0112\u0117\7\66\2\2\u0113")
        buf.write("\u0117\5.\30\2\u0114\u0117\7\67\2\2\u0115\u0117\7\20\2")
        buf.write("\2\u0116\u0111\3\2\2\2\u0116\u0112\3\2\2\2\u0116\u0113")
        buf.write("\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0115\3\2\2\2\u0117")
        buf.write("\u0118\3\2\2\2\u0118\u0119\7\60\2\2\u0119\u0122\5\60\31")
        buf.write("\2\u011a\u0120\7\65\2\2\u011b\u0120\7\66\2\2\u011c\u0120")
        buf.write("\5.\30\2\u011d\u0120\7\67\2\2\u011e\u0120\7\20\2\2\u011f")
        buf.write("\u011a\3\2\2\2\u011f\u011b\3\2\2\2\u011f\u011c\3\2\2\2")
        buf.write("\u011f\u011d\3\2\2\2\u011f\u011e\3\2\2\2\u0120\u0122\3")
        buf.write("\2\2\2\u0121\u0116\3\2\2\2\u0121\u011f\3\2\2\2\u0122\61")
        buf.write("\3\2\2\2\u0123\u0124\7-\2\2\u0124\u0125\7\65\2\2\u0125")
        buf.write("\u0126\7.\2\2\u0126\u0127\5\64\33\2\u0127\63\3\2\2\2\u0128")
        buf.write("\u012f\7\r\2\2\u0129\u012f\7\13\2\2\u012a\u012f\7\f\2")
        buf.write("\2\u012b\u012f\7\16\2\2\u012c\u012f\7:\2\2\u012d\u012f")
        buf.write("\5\62\32\2\u012e\u0128\3\2\2\2\u012e\u0129\3\2\2\2\u012e")
        buf.write("\u012a\3\2\2\2\u012e\u012b\3\2\2\2\u012e\u012c\3\2\2\2")
        buf.write("\u012e\u012d\3\2\2\2\u012f\65\3\2\2\2\u0130\u0131\7\25")
        buf.write("\2\2\u0131\u0132\7:\2\2\u0132\u0133\7+\2\2\u0133\u0134")
        buf.write("\7,\2\2\u0134\67\3\2\2\2\u0135\u0136\7\25\2\2\u0136\u0137")
        buf.write("\7:\2\2\u0137\u0138\7+\2\2\u0138\u0139\5:\36\2\u0139\u013a")
        buf.write("\7,\2\2\u013a9\3\2\2\2\u013b\u013e\5<\37\2\u013c\u013e")
        buf.write("\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013c\3\2\2\2\u013e")
        buf.write(";\3\2\2\2\u013f\u0140\5F$\2\u0140\u0141\7\60\2\2\u0141")
        buf.write("\u0142\5<\37\2\u0142\u0145\3\2\2\2\u0143\u0145\5F$\2\u0144")
        buf.write("\u013f\3\2\2\2\u0144\u0143\3\2\2\2\u0145=\3\2\2\2\u0146")
        buf.write("\u0147\t\3\2\2\u0147?\3\2\2\2\u0148\u0149\t\4\2\2\u0149")
        buf.write("A\3\2\2\2\u014a\u014b\t\5\2\2\u014bC\3\2\2\2\u014c\u014d")
        buf.write("\t\6\2\2\u014dE\3\2\2\2\u014e\u014f\5H%\2\u014f\u0150")
        buf.write("\7)\2\2\u0150\u0151\5H%\2\u0151\u0154\3\2\2\2\u0152\u0154")
        buf.write("\5H%\2\u0153\u014e\3\2\2\2\u0153\u0152\3\2\2\2\u0154G")
        buf.write("\3\2\2\2\u0155\u0156\5J&\2\u0156\u0157\5> \2\u0157\u0158")
        buf.write("\5J&\2\u0158\u015b\3\2\2\2\u0159\u015b\5J&\2\u015a\u0155")
        buf.write("\3\2\2\2\u015a\u0159\3\2\2\2\u015bI\3\2\2\2\u015c\u015d")
        buf.write("\b&\1\2\u015d\u015e\5L\'\2\u015e\u0165\3\2\2\2\u015f\u0160")
        buf.write("\f\4\2\2\u0160\u0161\5@!\2\u0161\u0162\5L\'\2\u0162\u0164")
        buf.write("\3\2\2\2\u0163\u015f\3\2\2\2\u0164\u0167\3\2\2\2\u0165")
        buf.write("\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166K\3\2\2\2\u0167")
        buf.write("\u0165\3\2\2\2\u0168\u0169\b\'\1\2\u0169\u016a\5N(\2\u016a")
        buf.write("\u0171\3\2\2\2\u016b\u016c\f\4\2\2\u016c\u016d\5B\"\2")
        buf.write("\u016d\u016e\5N(\2\u016e\u0170\3\2\2\2\u016f\u016b\3\2")
        buf.write("\2\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172")
        buf.write("\3\2\2\2\u0172M\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u0175")
        buf.write("\b(\1\2\u0175\u0176\5P)\2\u0176\u017d\3\2\2\2\u0177\u0178")
        buf.write("\f\4\2\2\u0178\u0179\5D#\2\u0179\u017a\5P)\2\u017a\u017c")
        buf.write("\3\2\2\2\u017b\u0177\3\2\2\2\u017c\u017f\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017eO\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u0180\u0181\7%\2\2\u0181\u0184\5P)\2\u0182")
        buf.write("\u0184\5R*\2\u0183\u0180\3\2\2\2\u0183\u0182\3\2\2\2\u0184")
        buf.write("Q\3\2\2\2\u0185\u0186\7\32\2\2\u0186\u0189\5R*\2\u0187")
        buf.write("\u0189\5T+\2\u0188\u0185\3\2\2\2\u0188\u0187\3\2\2\2\u0189")
        buf.write("S\3\2\2\2\u018a\u018b\5V,\2\u018b\u018c\7-\2\2\u018c\u018d")
        buf.write("\5F$\2\u018d\u018e\7.\2\2\u018e\u0191\3\2\2\2\u018f\u0191")
        buf.write("\5V,\2\u0190\u018a\3\2\2\2\u0190\u018f\3\2\2\2\u0191U")
        buf.write("\3\2\2\2\u0192\u0193\b,\1\2\u0193\u0194\5X-\2\u0194\u01a8")
        buf.write("\3\2\2\2\u0195\u019b\f\4\2\2\u0196\u0197\7-\2\2\u0197")
        buf.write("\u0198\5F$\2\u0198\u0199\7.\2\2\u0199\u019c\3\2\2\2\u019a")
        buf.write("\u019c\3\2\2\2\u019b\u0196\3\2\2\2\u019b\u019a\3\2\2\2")
        buf.write("\u019c\u019d\3\2\2\2\u019d\u019e\7/\2\2\u019e\u01a4\7")
        buf.write(":\2\2\u019f\u01a0\7+\2\2\u01a0\u01a1\5:\36\2\u01a1\u01a2")
        buf.write("\7,\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a5\3\2\2\2\u01a4")
        buf.write("\u019f\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5\u01a7\3\2\2\2")
        buf.write("\u01a6\u0195\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6\3")
        buf.write("\2\2\2\u01a8\u01a9\3\2\2\2\u01a9W\3\2\2\2\u01aa\u01a8")
        buf.write("\3\2\2\2\u01ab\u01ac\7:\2\2\u01ac\u01af\7/\2\2\u01ad\u01af")
        buf.write("\3\2\2\2\u01ae\u01ab\3\2\2\2\u01ae\u01ad\3\2\2\2\u01af")
        buf.write("\u01b0\3\2\2\2\u01b0\u01b6\7;\2\2\u01b1\u01b2\7+\2\2\u01b2")
        buf.write("\u01b3\5:\36\2\u01b3\u01b4\7,\2\2\u01b4\u01b7\3\2\2\2")
        buf.write("\u01b5\u01b7\3\2\2\2\u01b6\u01b1\3\2\2\2\u01b6\u01b5\3")
        buf.write("\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01ba\5Z.\2\u01b9\u01ae")
        buf.write("\3\2\2\2\u01b9\u01b8\3\2\2\2\u01baY\3\2\2\2\u01bb\u01bc")
        buf.write("\7\25\2\2\u01bc\u01bd\7:\2\2\u01bd\u01be\7+\2\2\u01be")
        buf.write("\u01bf\5:\36\2\u01bf\u01c0\7,\2\2\u01c0\u01c3\3\2\2\2")
        buf.write("\u01c1\u01c3\5\\/\2\u01c2\u01bb\3\2\2\2\u01c2\u01c1\3")
        buf.write("\2\2\2\u01c3[\3\2\2\2\u01c4\u01c5\7+\2\2\u01c5\u01c6\5")
        buf.write("F$\2\u01c6\u01c7\7,\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01ca")
        buf.write("\5^\60\2\u01c9\u01c4\3\2\2\2\u01c9\u01c8\3\2\2\2\u01ca")
        buf.write("]\3\2\2\2\u01cb\u01d1\5,\27\2\u01cc\u01d1\5|?\2\u01cd")
        buf.write("\u01d1\7\24\2\2\u01ce\u01d1\7\20\2\2\u01cf\u01d1\58\35")
        buf.write("\2\u01d0\u01cb\3\2\2\2\u01d0\u01cc\3\2\2\2\u01d0\u01cd")
        buf.write("\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01cf\3\2\2\2\u01d1")
        buf.write("_\3\2\2\2\u01d2\u01d3\5\f\7\2\u01d3a\3\2\2\2\u01d4\u01d5")
        buf.write("\5F$\2\u01d5\u01d6\7!\2\2\u01d6\u01d7\5F$\2\u01d7\u01d8")
        buf.write("\7\61\2\2\u01d8c\3\2\2\2\u01d9\u01dc\7\6\2\2\u01da\u01dd")
        buf.write("\5t;\2\u01db\u01dd\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01db")
        buf.write("\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01df\5F$\2\u01df\u01e3")
        buf.write("\5t;\2\u01e0\u01e1\7\7\2\2\u01e1\u01e4\5t;\2\u01e2\u01e4")
        buf.write("\3\2\2\2\u01e3\u01e0\3\2\2\2\u01e3\u01e2\3\2\2\2\u01e4")
        buf.write("e\3\2\2\2\u01e5\u01e6\7\b\2\2\u01e6\u01e7\5b\62\2\u01e7")
        buf.write("\u01e8\5F$\2\u01e8\u01e9\7\61\2\2\u01e9\u01ea\5F$\2\u01ea")
        buf.write("\u01eb\7!\2\2\u01eb\u01ec\5F$\2\u01ec\u01ed\5t;\2\u01ed")
        buf.write("g\3\2\2\2\u01ee\u01ef\7\4\2\2\u01ef\u01f0\7\61\2\2\u01f0")
        buf.write("i\3\2\2\2\u01f1\u01f2\7\5\2\2\u01f2\u01f3\7\61\2\2\u01f3")
        buf.write("k\3\2\2\2\u01f4\u01f7\7\17\2\2\u01f5\u01f8\5F$\2\u01f6")
        buf.write("\u01f8\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f6\3\2\2\2")
        buf.write("\u01f8\u01f9\3\2\2\2\u01f9\u01fa\7\61\2\2\u01fam\3\2\2")
        buf.write("\2\u01fb\u01fe\5p9\2\u01fc\u01fe\5r:\2\u01fd\u01fb\3\2")
        buf.write("\2\2\u01fd\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0200")
        buf.write("\7\61\2\2\u0200o\3\2\2\2\u0201\u0202\5F$\2\u0202\u0203")
        buf.write("\7/\2\2\u0203\u0204\7:\2\2\u0204\u0205\7+\2\2\u0205\u0206")
        buf.write("\5:\36\2\u0206\u0207\7,\2\2\u0207q\3\2\2\2\u0208\u0209")
        buf.write("\7:\2\2\u0209\u020c\7/\2\2\u020a\u020c\3\2\2\2\u020b\u0208")
        buf.write("\3\2\2\2\u020b\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d")
        buf.write("\u020e\7;\2\2\u020e\u020f\7+\2\2\u020f\u0210\5:\36\2\u0210")
        buf.write("\u0211\7,\2\2\u0211s\3\2\2\2\u0212\u0213\7\63\2\2\u0213")
        buf.write("\u0214\5v<\2\u0214\u0215\7\64\2\2\u0215u\3\2\2\2\u0216")
        buf.write("\u0217\5x=\2\u0217\u0218\5v<\2\u0218\u021b\3\2\2\2\u0219")
        buf.write("\u021b\3\2\2\2\u021a\u0216\3\2\2\2\u021a\u0219\3\2\2\2")
        buf.write("\u021bw\3\2\2\2\u021c\u0226\5\f\7\2\u021d\u0226\5b\62")
        buf.write("\2\u021e\u0226\5d\63\2\u021f\u0226\5f\64\2\u0220\u0226")
        buf.write("\5h\65\2\u0221\u0226\5j\66\2\u0222\u0226\5l\67\2\u0223")
        buf.write("\u0226\5n8\2\u0224\u0226\5t;\2\u0225\u021c\3\2\2\2\u0225")
        buf.write("\u021d\3\2\2\2\u0225\u021e\3\2\2\2\u0225\u021f\3\2\2\2")
        buf.write("\u0225\u0220\3\2\2\2\u0225\u0221\3\2\2\2\u0225\u0222\3")
        buf.write("\2\2\2\u0225\u0223\3\2\2\2\u0225\u0224\3\2\2\2\u0226y")
        buf.write("\3\2\2\2\u0227\u0228\7-\2\2\u0228\u0229\5\60\31\2\u0229")
        buf.write("\u022a\7.\2\2\u022a{\3\2\2\2\u022b\u022c\t\7\2\2\u022c")
        buf.write("}\3\2\2\2\u022d\u0230\5\64\33\2\u022e\u0230\5\62\32\2")
        buf.write("\u022f\u022d\3\2\2\2\u022f\u022e\3\2\2\2\u0230\177\3\2")
        buf.write("\2\2\u0231\u0235\5\64\33\2\u0232\u0235\5\62\32\2\u0233")
        buf.write("\u0235\7\26\2\2\u0234\u0231\3\2\2\2\u0234\u0232\3\2\2")
        buf.write("\2\u0234\u0233\3\2\2\2\u0235\u0081\3\2\2\2\61\u0089\u008e")
        buf.write("\u0099\u009d\u00a1\u00ad\u00b8\u00c8\u00db\u00df\u00e3")
        buf.write("\u00ef\u00fb\u0101\u010d\u0116\u011f\u0121\u012e\u013d")
        buf.write("\u0144\u0153\u015a\u0165\u0171\u017d\u0183\u0188\u0190")
        buf.write("\u019b\u01a4\u01a8\u01ae\u01b6\u01b9\u01c2\u01c9\u01d0")
        buf.write("\u01dc\u01e3\u01f7\u01fd\u020b\u021a\u0225\u022f\u0234")
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
                      "LINECMT", "ID", "ATIDENTIFIER", "WS", "UNCLOSED_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_classdecl = 2
    RULE_memberlist = 3
    RULE_member = 4
    RULE_attributedecl = 5
    RULE_vardecl = 6
    RULE_constdecl = 7
    RULE_attributecheck = 8
    RULE_attributenodeclare = 9
    RULE_attributelist = 10
    RULE_attributewithdeclare = 11
    RULE_attlist = 12
    RULE_constructor = 13
    RULE_methoddecl = 14
    RULE_parameterlist = 15
    RULE_parameterprime = 16
    RULE_parameterpart1 = 17
    RULE_parameterpart2 = 18
    RULE_identifierlist = 19
    RULE_superpart = 20
    RULE_literal = 21
    RULE_boolit = 22
    RULE_literallist = 23
    RULE_arraydecl = 24
    RULE_typ = 25
    RULE_objdecl = 26
    RULE_createobjectexpr = 27
    RULE_nullableexplist = 28
    RULE_expprime = 29
    RULE_relational = 30
    RULE_logical = 31
    RULE_adding = 32
    RULE_multiplying = 33
    RULE_exp = 34
    RULE_exp1 = 35
    RULE_exp2 = 36
    RULE_exp3 = 37
    RULE_exp4 = 38
    RULE_exp5 = 39
    RULE_exp6 = 40
    RULE_exp7 = 41
    RULE_exp8 = 42
    RULE_exp9 = 43
    RULE_exp10 = 44
    RULE_exp11 = 45
    RULE_exp12 = 46
    RULE_declrstate = 47
    RULE_assignstate = 48
    RULE_ifstate = 49
    RULE_forstate = 50
    RULE_breakstate = 51
    RULE_continuestate = 52
    RULE_returnstate = 53
    RULE_methodinvoke = 54
    RULE_instancemethodstate = 55
    RULE_staticmethodstate = 56
    RULE_blockstate = 57
    RULE_stmtlist = 58
    RULE_stmt = 59
    RULE_arraylit = 60
    RULE_identifier = 61
    RULE_typedecl = 62
    RULE_typedeclwithvoid = 63

    ruleNames =  [ "program", "decllist", "classdecl", "memberlist", "member", 
                   "attributedecl", "vardecl", "constdecl", "attributecheck", 
                   "attributenodeclare", "attributelist", "attributewithdeclare", 
                   "attlist", "constructor", "methoddecl", "parameterlist", 
                   "parameterprime", "parameterpart1", "parameterpart2", 
                   "identifierlist", "superpart", "literal", "boolit", "literallist", 
                   "arraydecl", "typ", "objdecl", "createobjectexpr", "nullableexplist", 
                   "expprime", "relational", "logical", "adding", "multiplying", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "exp7", "exp8", "exp9", "exp10", "exp11", "exp12", "declrstate", 
                   "assignstate", "ifstate", "forstate", "breakstate", "continuestate", 
                   "returnstate", "methodinvoke", "instancemethodstate", 
                   "staticmethodstate", "blockstate", "stmtlist", "stmt", 
                   "arraylit", "identifier", "typedecl", "typedeclwithvoid" ]

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
    WS=58
    UNCLOSED_STRING=59
    ILLEGAL_ESCAPE=60
    ERROR_CHAR=61

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
            self.state = 128
            self.decllist()
            self.state = 129
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

        def classdecl(self):
            return self.getTypedRuleContext(CSlangParser.ClassdeclContext,0)


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
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.classdecl()
                self.state = 132
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
        self.enterRule(localctx, 4, self.RULE_classdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(CSlangParser.CLASS)
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 138
                self.superpart()
                pass

            elif la_ == 2:
                pass


            self.state = 142
            self.match(CSlangParser.ID)
            self.state = 143
            self.match(CSlangParser.LCB)
            self.state = 144
            self.memberlist()
            self.state = 145
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
        self.enterRule(localctx, 6, self.RULE_memberlist)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.member()
                self.state = 148
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
        self.enterRule(localctx, 8, self.RULE_member)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.attributedecl()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
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

        def vardecl(self):
            return self.getTypedRuleContext(CSlangParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(CSlangParser.ConstdeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attributedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributedecl" ):
                return visitor.visitAttributedecl(self)
            else:
                return visitor.visitChildren(self)




    def attributedecl(self):

        localctx = CSlangParser.AttributedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attributedecl)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.vardecl()
                pass
            elif token in [CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.constdecl()
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


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def attributecheck(self):
            return self.getTypedRuleContext(CSlangParser.AttributecheckContext,0)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = CSlangParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(CSlangParser.VAR)
            self.state = 162
            self.attributecheck()
            self.state = 163
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def attributecheck(self):
            return self.getTypedRuleContext(CSlangParser.AttributecheckContext,0)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = CSlangParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(CSlangParser.CONST)
            self.state = 166
            self.attributecheck()
            self.state = 167
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributecheckContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributewithdeclare(self):
            return self.getTypedRuleContext(CSlangParser.AttributewithdeclareContext,0)


        def attributenodeclare(self):
            return self.getTypedRuleContext(CSlangParser.AttributenodeclareContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attributecheck

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributecheck" ):
                return visitor.visitAttributecheck(self)
            else:
                return visitor.visitChildren(self)




    def attributecheck(self):

        localctx = CSlangParser.AttributecheckContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attributecheck)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.attributewithdeclare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
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

        def typedecl(self):
            return self.getTypedRuleContext(CSlangParser.TypedeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attributenodeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributenodeclare" ):
                return visitor.visitAttributenodeclare(self)
            else:
                return visitor.visitChildren(self)




    def attributenodeclare(self):

        localctx = CSlangParser.AttributenodeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attributenodeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.attributelist()
            self.state = 174
            self.match(CSlangParser.COLON)
            self.state = 175
            self.typedecl()
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
        self.enterRule(localctx, 20, self.RULE_attributelist)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.identifier()
                self.state = 178
                self.match(CSlangParser.CM)
                self.state = 179
                self.attributelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.identifier()
                pass


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


        def getRuleIndex(self):
            return CSlangParser.RULE_attributewithdeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributewithdeclare" ):
                return visitor.visitAttributewithdeclare(self)
            else:
                return visitor.visitChildren(self)




    def attributewithdeclare(self):

        localctx = CSlangParser.AttributewithdeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_attributewithdeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.attlist()
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

        def typedecl(self):
            return self.getTypedRuleContext(CSlangParser.TypedeclContext,0)


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
        self.enterRule(localctx, 24, self.RULE_attlist)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.identifier()
                self.state = 187
                self.match(CSlangParser.CM)
                self.state = 188
                self.attlist()
                self.state = 189
                self.match(CSlangParser.CM)
                self.state = 190
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.identifier()
                self.state = 193
                self.match(CSlangParser.COLON)
                self.state = 194
                self.typedecl()
                self.state = 195
                self.match(CSlangParser.DECLARE)
                self.state = 196
                self.exp()
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
        self.enterRule(localctx, 26, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(CSlangParser.FUNC)
            self.state = 201
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 202
            self.match(CSlangParser.LRB)
            self.state = 203
            self.parameterlist()
            self.state = 204
            self.match(CSlangParser.RRB)
            self.state = 205
            self.blockstate()
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

        def constructor(self):
            return self.getTypedRuleContext(CSlangParser.ConstructorContext,0)


        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def identifier(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierContext,0)


        def LRB(self):
            return self.getToken(CSlangParser.LRB, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(CSlangParser.ParameterlistContext,0)


        def RRB(self):
            return self.getToken(CSlangParser.RRB, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typedeclwithvoid(self):
            return self.getTypedRuleContext(CSlangParser.TypedeclwithvoidContext,0)


        def blockstate(self):
            return self.getTypedRuleContext(CSlangParser.BlockstateContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_methoddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethoddecl" ):
                return visitor.visitMethoddecl(self)
            else:
                return visitor.visitChildren(self)




    def methoddecl(self):

        localctx = CSlangParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_methoddecl)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.constructor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.match(CSlangParser.FUNC)
                self.state = 209
                self.identifier()
                self.state = 210
                self.match(CSlangParser.LRB)
                self.state = 211
                self.parameterlist()
                self.state = 212
                self.match(CSlangParser.RRB)
                self.state = 213
                self.match(CSlangParser.COLON)
                self.state = 214
                self.typedeclwithvoid()
                self.state = 215
                self.blockstate()
                pass


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
        self.enterRule(localctx, 30, self.RULE_parameterlist)
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
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
        self.enterRule(localctx, 32, self.RULE_parameterprime)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.parameterpart1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
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
        self.enterRule(localctx, 34, self.RULE_parameterpart1)
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(CSlangParser.ID)
                self.state = 228
                self.match(CSlangParser.COLON)
                self.state = 229
                self.typ()
                self.state = 231
                self.match(CSlangParser.CM)
                self.state = 232
                self.parameterpart1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(CSlangParser.ID)
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


    class Parameterpart2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierlist(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierlistContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def parameterpart2(self):
            return self.getTypedRuleContext(CSlangParser.Parameterpart2Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_parameterpart2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterpart2" ):
                return visitor.visitParameterpart2(self)
            else:
                return visitor.visitChildren(self)




    def parameterpart2(self):

        localctx = CSlangParser.Parameterpart2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_parameterpart2)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.identifierlist()
                self.state = 240
                self.match(CSlangParser.COLON)
                self.state = 241
                self.typ()
                self.state = 242
                self.match(CSlangParser.CM)
                self.state = 243
                self.parameterpart2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.identifierlist()
                self.state = 246
                self.match(CSlangParser.COLON)
                self.state = 247
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

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def identifierlist(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_identifierlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierlist" ):
                return visitor.visitIdentifierlist(self)
            else:
                return visitor.visitChildren(self)




    def identifierlist(self):

        localctx = CSlangParser.IdentifierlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_identifierlist)
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.match(CSlangParser.ID)
                self.state = 252
                self.match(CSlangParser.CM)
                self.state = 253
                self.identifierlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.match(CSlangParser.ID)
                pass


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
        self.enterRule(localctx, 40, self.RULE_superpart)
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


        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def NULL(self):
            return self.getToken(CSlangParser.NULL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CSlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_literal)
        try:
            self.state = 267
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
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 6)
                self.state = 265
                self.match(CSlangParser.SELF)
                pass
            elif token in [CSlangParser.NULL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 266
                self.match(CSlangParser.NULL)
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
        self.enterRule(localctx, 44, self.RULE_boolit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
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

        def NULL(self):
            return self.getToken(CSlangParser.NULL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_literallist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterallist" ):
                return visitor.visitLiterallist(self)
            else:
                return visitor.visitChildren(self)




    def literallist(self):

        localctx = CSlangParser.LiterallistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_literallist)
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.INTLIT]:
                    self.state = 271
                    self.match(CSlangParser.INTLIT)
                    pass
                elif token in [CSlangParser.FLOATLIT]:
                    self.state = 272
                    self.match(CSlangParser.FLOATLIT)
                    pass
                elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                    self.state = 273
                    self.boolit()
                    pass
                elif token in [CSlangParser.STRINGLIT]:
                    self.state = 274
                    self.match(CSlangParser.STRINGLIT)
                    pass
                elif token in [CSlangParser.NULL]:
                    self.state = 275
                    self.match(CSlangParser.NULL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 278
                self.match(CSlangParser.CM)
                self.state = 279
                self.literallist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.INTLIT]:
                    self.state = 280
                    self.match(CSlangParser.INTLIT)
                    pass
                elif token in [CSlangParser.FLOATLIT]:
                    self.state = 281
                    self.match(CSlangParser.FLOATLIT)
                    pass
                elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                    self.state = 282
                    self.boolit()
                    pass
                elif token in [CSlangParser.STRINGLIT]:
                    self.state = 283
                    self.match(CSlangParser.STRINGLIT)
                    pass
                elif token in [CSlangParser.NULL]:
                    self.state = 284
                    self.match(CSlangParser.NULL)
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

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

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
        self.enterRule(localctx, 48, self.RULE_arraydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(CSlangParser.LSB)
            self.state = 290
            self.match(CSlangParser.INTLIT)
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

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def arraydecl(self):
            return self.getTypedRuleContext(CSlangParser.ArraydeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = CSlangParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_typ)
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BOOL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(CSlangParser.BOOL)
                pass
            elif token in [CSlangParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(CSlangParser.INT)
                pass
            elif token in [CSlangParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
                self.match(CSlangParser.FLOAT)
                pass
            elif token in [CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 297
                self.match(CSlangParser.STRING)
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 298
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 299
                self.arraydecl()
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
        self.enterRule(localctx, 52, self.RULE_objdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(CSlangParser.NEW)
            self.state = 303
            self.match(CSlangParser.ID)
            self.state = 304
            self.match(CSlangParser.LRB)
            self.state = 305
            self.match(CSlangParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateobjectexprContext(ParserRuleContext):
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

        def nullableexplist(self):
            return self.getTypedRuleContext(CSlangParser.NullableexplistContext,0)


        def RRB(self):
            return self.getToken(CSlangParser.RRB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_createobjectexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateobjectexpr" ):
                return visitor.visitCreateobjectexpr(self)
            else:
                return visitor.visitChildren(self)




    def createobjectexpr(self):

        localctx = CSlangParser.CreateobjectexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_createobjectexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(CSlangParser.NEW)
            self.state = 308
            self.match(CSlangParser.ID)
            self.state = 309
            self.match(CSlangParser.LRB)
            self.state = 310
            self.nullableexplist()
            self.state = 311
            self.match(CSlangParser.RRB)
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
        self.enterRule(localctx, 56, self.RULE_nullableexplist)
        try:
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.DIFF, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
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
        self.enterRule(localctx, 58, self.RULE_expprime)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.exp()
                self.state = 318
                self.match(CSlangParser.CM)
                self.state = 319
                self.expprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
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
        self.enterRule(localctx, 60, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
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
        self.enterRule(localctx, 62, self.RULE_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
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
        self.enterRule(localctx, 64, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
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
        self.enterRule(localctx, 66, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
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
        self.enterRule(localctx, 68, self.RULE_exp)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.exp1()
                self.state = 333
                self.match(CSlangParser.CONCAT)
                self.state = 334
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
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
        self.enterRule(localctx, 70, self.RULE_exp1)
        try:
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.exp2(0)
                self.state = 340
                self.relational()
                self.state = 341
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 355
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 349
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 350
                    self.logical()
                    self.state = 351
                    self.exp3(0) 
                self.state = 357
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 367
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 361
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 362
                    self.adding()
                    self.state = 363
                    self.exp4(0) 
                self.state = 369
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 373
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 374
                    self.multiplying()
                    self.state = 375
                    self.exp5() 
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        self.enterRule(localctx, 78, self.RULE_exp5)
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.DIFF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.match(CSlangParser.DIFF)
                self.state = 383
                self.exp5()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
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
        self.enterRule(localctx, 80, self.RULE_exp6)
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.match(CSlangParser.MINUS)
                self.state = 388
                self.exp6()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
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
        self.enterRule(localctx, 82, self.RULE_exp7)
        try:
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.exp8(0)
                self.state = 393
                self.match(CSlangParser.LSB)
                self.state = 394
                self.exp()
                self.state = 395
                self.match(CSlangParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
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

        def LSB(self):
            return self.getToken(CSlangParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def RSB(self):
            return self.getToken(CSlangParser.RSB, 0)

        def LRB(self):
            return self.getToken(CSlangParser.LRB, 0)

        def nullableexplist(self):
            return self.getTypedRuleContext(CSlangParser.NullableexplistContext,0)


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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 422
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 403
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 409
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [CSlangParser.LSB]:
                        self.state = 404
                        self.match(CSlangParser.LSB)
                        self.state = 405
                        self.exp()
                        self.state = 406
                        self.match(CSlangParser.RSB)
                        pass
                    elif token in [CSlangParser.DOT]:
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 411
                    self.match(CSlangParser.DOT)
                    self.state = 412
                    self.match(CSlangParser.ID)
                    self.state = 418
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                    if la_ == 1:
                        self.state = 413
                        self.match(CSlangParser.LRB)
                        self.state = 414
                        self.nullableexplist()
                        self.state = 415
                        self.match(CSlangParser.RRB)
                        pass

                    elif la_ == 2:
                        pass

             
                self.state = 424
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def LRB(self):
            return self.getToken(CSlangParser.LRB, 0)

        def nullableexplist(self):
            return self.getTypedRuleContext(CSlangParser.NullableexplistContext,0)


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
        self.enterRule(localctx, 86, self.RULE_exp9)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.ID]:
                    self.state = 425
                    self.match(CSlangParser.ID)
                    self.state = 426
                    self.match(CSlangParser.DOT)
                    pass
                elif token in [CSlangParser.ATIDENTIFIER]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 430
                self.match(CSlangParser.ATIDENTIFIER)
                self.state = 436
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 431
                    self.match(CSlangParser.LRB)
                    self.state = 432
                    self.nullableexplist()
                    self.state = 433
                    self.match(CSlangParser.RRB)
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
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

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LRB(self):
            return self.getToken(CSlangParser.LRB, 0)

        def nullableexplist(self):
            return self.getTypedRuleContext(CSlangParser.NullableexplistContext,0)


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
        self.enterRule(localctx, 88, self.RULE_exp10)
        try:
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.match(CSlangParser.NEW)
                self.state = 442
                self.match(CSlangParser.ID)
                self.state = 443
                self.match(CSlangParser.LRB)
                self.state = 444
                self.nullableexplist()
                self.state = 445
                self.match(CSlangParser.RRB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.exp11()
                pass


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

        def LRB(self):
            return self.getToken(CSlangParser.LRB, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def RRB(self):
            return self.getToken(CSlangParser.RRB, 0)

        def exp12(self):
            return self.getTypedRuleContext(CSlangParser.Exp12Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp11" ):
                return visitor.visitExp11(self)
            else:
                return visitor.visitChildren(self)




    def exp11(self):

        localctx = CSlangParser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_exp11)
        try:
            self.state = 455
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LRB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.match(CSlangParser.LRB)
                self.state = 451
                self.exp()
                self.state = 452
                self.match(CSlangParser.RRB)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.exp12()
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


    class Exp12Context(ParserRuleContext):
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

        def NULL(self):
            return self.getToken(CSlangParser.NULL, 0)

        def createobjectexpr(self):
            return self.getTypedRuleContext(CSlangParser.CreateobjectexprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp12

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp12" ):
                return visitor.visitExp12(self)
            else:
                return visitor.visitChildren(self)




    def exp12(self):

        localctx = CSlangParser.Exp12Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_exp12)
        try:
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 458
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 459
                self.match(CSlangParser.SELF)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 460
                self.match(CSlangParser.NULL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 461
                self.createobjectexpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclrstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributedecl(self):
            return self.getTypedRuleContext(CSlangParser.AttributedeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_declrstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclrstate" ):
                return visitor.visitDeclrstate(self)
            else:
                return visitor.visitChildren(self)




    def declrstate(self):

        localctx = CSlangParser.DeclrstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_declrstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.attributedecl()
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
        self.enterRule(localctx, 96, self.RULE_assignstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.exp()
            self.state = 467
            self.match(CSlangParser.ASSIGN)
            self.state = 468
            self.exp()
            self.state = 469
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
        self.enterRule(localctx, 98, self.RULE_ifstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(CSlangParser.IF)
            self.state = 474
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LCB]:
                self.state = 472
                self.blockstate()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.DIFF, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 476
            self.exp()
            self.state = 477
            self.blockstate()
            self.state = 481
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ELSE]:
                self.state = 478
                self.match(CSlangParser.ELSE)
                self.state = 479
                self.blockstate()
                pass
            elif token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.RETURN, CSlangParser.NULL, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.CONST, CSlangParser.MINUS, CSlangParser.DIFF, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.LCB, CSlangParser.RCB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
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


    class ForstateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSlangParser.FOR, 0)

        def assignstate(self):
            return self.getTypedRuleContext(CSlangParser.AssignstateContext,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExpContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExpContext,i)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

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
        self.enterRule(localctx, 100, self.RULE_forstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(CSlangParser.FOR)
            self.state = 484
            self.assignstate()
            self.state = 485
            self.exp()
            self.state = 486
            self.match(CSlangParser.SM)
            self.state = 487
            self.exp()
            self.state = 488
            self.match(CSlangParser.ASSIGN)
            self.state = 489
            self.exp()
            self.state = 490
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
        self.enterRule(localctx, 102, self.RULE_breakstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(CSlangParser.BREAK)
            self.state = 493
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
        self.enterRule(localctx, 104, self.RULE_continuestate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(CSlangParser.CONTINUE)
            self.state = 496
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


        def getRuleIndex(self):
            return CSlangParser.RULE_returnstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstate" ):
                return visitor.visitReturnstate(self)
            else:
                return visitor.visitChildren(self)




    def returnstate(self):

        localctx = CSlangParser.ReturnstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_returnstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(CSlangParser.RETURN)
            self.state = 501
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.DIFF, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.state = 499
                self.exp()
                pass
            elif token in [CSlangParser.SM]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 503
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
        self.enterRule(localctx, 108, self.RULE_methodinvoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 505
                self.instancemethodstate()
                pass

            elif la_ == 2:
                self.state = 506
                self.staticmethodstate()
                pass


            self.state = 509
            self.match(CSlangParser.SM)
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

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

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
        self.enterRule(localctx, 110, self.RULE_instancemethodstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.exp()
            self.state = 512
            self.match(CSlangParser.DOT)
            self.state = 513
            self.match(CSlangParser.ID)
            self.state = 514
            self.match(CSlangParser.LRB)
            self.state = 515
            self.nullableexplist()
            self.state = 516
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
        self.enterRule(localctx, 112, self.RULE_staticmethodstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ID]:
                self.state = 518
                self.match(CSlangParser.ID)
                self.state = 519
                self.match(CSlangParser.DOT)
                pass
            elif token in [CSlangParser.ATIDENTIFIER]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 523
            self.match(CSlangParser.ATIDENTIFIER)
            self.state = 524
            self.match(CSlangParser.LRB)
            self.state = 525
            self.nullableexplist()
            self.state = 526
            self.match(CSlangParser.RRB)
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
        self.enterRule(localctx, 114, self.RULE_blockstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.match(CSlangParser.LCB)
            self.state = 529
            self.stmtlist()
            self.state = 530
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
        self.enterRule(localctx, 116, self.RULE_stmtlist)
        try:
            self.state = 536
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.RETURN, CSlangParser.NULL, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.CONST, CSlangParser.MINUS, CSlangParser.DIFF, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.LCB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 532
                self.stmt()
                self.state = 533
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

        def attributedecl(self):
            return self.getTypedRuleContext(CSlangParser.AttributedeclContext,0)


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


        def blockstate(self):
            return self.getTypedRuleContext(CSlangParser.BlockstateContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_stmt)
        try:
            self.state = 547
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 538
                self.attributedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 539
                self.assignstate()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 540
                self.ifstate()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 541
                self.forstate()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 542
                self.breakstate()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 543
                self.continuestate()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 544
                self.returnstate()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 545
                self.methodinvoke()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 546
                self.blockstate()
                pass


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
        self.enterRule(localctx, 120, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(CSlangParser.LSB)
            self.state = 550
            self.literallist()
            self.state = 551
            self.match(CSlangParser.RSB)
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
        self.enterRule(localctx, 122, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
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


    class TypedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(CSlangParser.ArraydeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_typedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedecl" ):
                return visitor.visitTypedecl(self)
            else:
                return visitor.visitChildren(self)




    def typedecl(self):

        localctx = CSlangParser.TypedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_typedecl)
        try:
            self.state = 557
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 555
                self.typ()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 556
                self.arraydecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedeclwithvoidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(CSlangParser.ArraydeclContext,0)


        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_typedeclwithvoid

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedeclwithvoid" ):
                return visitor.visitTypedeclwithvoid(self)
            else:
                return visitor.visitChildren(self)




    def typedeclwithvoid(self):

        localctx = CSlangParser.TypedeclwithvoidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_typedeclwithvoid)
        try:
            self.state = 562
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 559
                self.typ()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 560
                self.arraydecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 561
                self.match(CSlangParser.VOID)
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
        self._predicates[36] = self.exp2_sempred
        self._predicates[37] = self.exp3_sempred
        self._predicates[38] = self.exp4_sempred
        self._predicates[42] = self.exp8_sempred
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
                return self.precpred(self._ctx, 2)
         




