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
        buf.write("\u021e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0082\n")
        buf.write("\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\5\6\u008b\n\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u0096\n\7\3\b\3\b\5\b\u009a")
        buf.write("\n\b\3\t\3\t\5\t\u009e\n\t\3\n\3\n\3\n\3\n\3\n\5\n\u00a5")
        buf.write("\n\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\5\f\u00b7\n\f\3\f\3\f\3\f\5\f\u00bc")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00c3\n\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00ce\n\16\3\16\3")
        buf.write("\16\3\17\3\17\5\17\u00d4\n\17\3\20\3\20\5\20\u00d8\n\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00e4\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\5\22\u00f1\n\22\3\23\3\23\5\23\u00f5\n\23")
        buf.write("\3\24\3\24\3\24\3\24\5\24\u00fb\n\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u010c\n\27\3\30\3\30\3\31\3\31\3\31\3\31\3")
        buf.write("\31\5\31\u0115\n\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u011e\n\31\5\31\u0120\n\31\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\5\36\u0138\n\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\37\3\37\5\37\u0141\n\37\3 \3")
        buf.write(" \3 \3 \3 \5 \u0148\n \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3")
        buf.write("%\3%\3%\3%\5%\u0157\n%\3&\3&\3&\3&\3&\5&\u015e\n&\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u0167\n\'\f\'\16\'\u016a")
        buf.write("\13\'\3(\3(\3(\3(\3(\3(\3(\7(\u0173\n(\f(\16(\u0176\13")
        buf.write("(\3)\3)\3)\3)\3)\3)\3)\7)\u017f\n)\f)\16)\u0182\13)\3")
        buf.write("*\3*\3*\5*\u0187\n*\3+\3+\3+\5+\u018c\n+\3,\3,\3,\3,\3")
        buf.write(",\3,\5,\u0194\n,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01a1")
        buf.write("\n-\7-\u01a3\n-\f-\16-\u01a6\13-\3.\3.\3.\5.\u01ab\n.")
        buf.write("\3.\3.\3.\3.\5.\u01b1\n.\3.\3.\3.\3.\3.\3.\5.\u01b9\n")
        buf.write(".\3/\3/\3/\3/\3/\3/\3/\5/\u01c2\n/\3\60\3\60\3\60\3\60")
        buf.write("\3\60\5\60\u01c9\n\60\3\61\3\61\3\61\5\61\u01ce\n\61\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\5\63\u01d8\n\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\5\63\u01df\n\63\3\64\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\67\3\67\3\67\5\67\u01f5\n\67\3")
        buf.write("\67\3\67\38\38\58\u01fb\n8\38\38\39\39\39\39\39\39\3:")
        buf.write("\3:\3:\3:\3;\3;\3;\3;\5;\u020d\n;\3<\3<\3<\3<\3<\3<\3")
        buf.write("<\3<\3<\5<\u0218\n<\3=\3=\3=\3=\3=\2\6LNPX>\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVXZ\\^`bdfhjlnprtvx\2\n\3\2:;\4\2\23\23\27")
        buf.write("\27\3\2\t\n\4\2\13\16::\5\2  \"$\'(\3\2\36\37\3\2\31\32")
        buf.write("\4\2\33\35**\2\u0221\2z\3\2\2\2\4\u0081\3\2\2\2\6\u0083")
        buf.write("\3\2\2\2\b\u0085\3\2\2\2\n\u0087\3\2\2\2\f\u0095\3\2\2")
        buf.write("\2\16\u0099\3\2\2\2\20\u009d\3\2\2\2\22\u009f\3\2\2\2")
        buf.write("\24\u00a8\3\2\2\2\26\u00bb\3\2\2\2\30\u00c2\3\2\2\2\32")
        buf.write("\u00c4\3\2\2\2\34\u00d3\3\2\2\2\36\u00d7\3\2\2\2 \u00e3")
        buf.write("\3\2\2\2\"\u00f0\3\2\2\2$\u00f4\3\2\2\2&\u00fa\3\2\2\2")
        buf.write("(\u00fc\3\2\2\2*\u0103\3\2\2\2,\u010b\3\2\2\2.\u010d\3")
        buf.write("\2\2\2\60\u011f\3\2\2\2\62\u0121\3\2\2\2\64\u0126\3\2")
        buf.write("\2\2\66\u0128\3\2\2\28\u012d\3\2\2\2:\u0137\3\2\2\2<\u0140")
        buf.write("\3\2\2\2>\u0147\3\2\2\2@\u0149\3\2\2\2B\u014b\3\2\2\2")
        buf.write("D\u014d\3\2\2\2F\u014f\3\2\2\2H\u0156\3\2\2\2J\u015d\3")
        buf.write("\2\2\2L\u015f\3\2\2\2N\u016b\3\2\2\2P\u0177\3\2\2\2R\u0186")
        buf.write("\3\2\2\2T\u018b\3\2\2\2V\u0193\3\2\2\2X\u0195\3\2\2\2")
        buf.write("Z\u01b8\3\2\2\2\\\u01c1\3\2\2\2^\u01c8\3\2\2\2`\u01cd")
        buf.write("\3\2\2\2b\u01cf\3\2\2\2d\u01d4\3\2\2\2f\u01e0\3\2\2\2")
        buf.write("h\u01eb\3\2\2\2j\u01ee\3\2\2\2l\u01f1\3\2\2\2n\u01fa\3")
        buf.write("\2\2\2p\u01fe\3\2\2\2r\u0204\3\2\2\2t\u020c\3\2\2\2v\u0217")
        buf.write("\3\2\2\2x\u0219\3\2\2\2z{\5\4\3\2{|\7\2\2\3|\3\3\2\2\2")
        buf.write("}~\5\6\4\2~\177\5\4\3\2\177\u0082\3\2\2\2\u0080\u0082")
        buf.write("\3\2\2\2\u0081}\3\2\2\2\u0081\u0080\3\2\2\2\u0082\5\3")
        buf.write("\2\2\2\u0083\u0084\5\n\6\2\u0084\7\3\2\2\2\u0085\u0086")
        buf.write("\t\2\2\2\u0086\t\3\2\2\2\u0087\u008a\7\21\2\2\u0088\u008b")
        buf.write("\5*\26\2\u0089\u008b\3\2\2\2\u008a\u0088\3\2\2\2\u008a")
        buf.write("\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d\7:\2\2")
        buf.write("\u008d\u008e\7\63\2\2\u008e\u008f\5\f\7\2\u008f\u0090")
        buf.write("\7\64\2\2\u0090\13\3\2\2\2\u0091\u0092\5\16\b\2\u0092")
        buf.write("\u0093\5\f\7\2\u0093\u0096\3\2\2\2\u0094\u0096\3\2\2\2")
        buf.write("\u0095\u0091\3\2\2\2\u0095\u0094\3\2\2\2\u0096\r\3\2\2")
        buf.write("\2\u0097\u009a\5\20\t\2\u0098\u009a\5\32\16\2\u0099\u0097")
        buf.write("\3\2\2\2\u0099\u0098\3\2\2\2\u009a\17\3\2\2\2\u009b\u009e")
        buf.write("\5\24\13\2\u009c\u009e\5\22\n\2\u009d\u009b\3\2\2\2\u009d")
        buf.write("\u009c\3\2\2\2\u009e\21\3\2\2\2\u009f\u00a0\t\3\2\2\u00a0")
        buf.write("\u00a1\5\30\r\2\u00a1\u00a4\7\62\2\2\u00a2\u00a5\5\64")
        buf.write("\33\2\u00a3\u00a5\5\62\32\2\u00a4\u00a2\3\2\2\2\u00a4")
        buf.write("\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\7\61\2")
        buf.write("\2\u00a7\23\3\2\2\2\u00a8\u00a9\t\3\2\2\u00a9\u00aa\5")
        buf.write("\26\f\2\u00aa\u00ab\7\61\2\2\u00ab\25\3\2\2\2\u00ac\u00ad")
        buf.write("\5\b\5\2\u00ad\u00ae\7\60\2\2\u00ae\u00af\5\26\f\2\u00af")
        buf.write("\u00b0\7\60\2\2\u00b0\u00b1\5H%\2\u00b1\u00bc\3\2\2\2")
        buf.write("\u00b2\u00b3\5\b\5\2\u00b3\u00b6\7\62\2\2\u00b4\u00b7")
        buf.write("\5\64\33\2\u00b5\u00b7\5\62\32\2\u00b6\u00b4\3\2\2\2\u00b6")
        buf.write("\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\7&\2\2")
        buf.write("\u00b9\u00ba\5H%\2\u00ba\u00bc\3\2\2\2\u00bb\u00ac\3\2")
        buf.write("\2\2\u00bb\u00b2\3\2\2\2\u00bc\27\3\2\2\2\u00bd\u00be")
        buf.write("\5\b\5\2\u00be\u00bf\7\60\2\2\u00bf\u00c0\5\30\r\2\u00c0")
        buf.write("\u00c3\3\2\2\2\u00c1\u00c3\5\b\5\2\u00c2\u00bd\3\2\2\2")
        buf.write("\u00c2\u00c1\3\2\2\2\u00c3\31\3\2\2\2\u00c4\u00c5\7\30")
        buf.write("\2\2\u00c5\u00c6\t\2\2\2\u00c6\u00c7\7+\2\2\u00c7\u00c8")
        buf.write("\5\34\17\2\u00c8\u00c9\7,\2\2\u00c9\u00cd\7\62\2\2\u00ca")
        buf.write("\u00ce\5\64\33\2\u00cb\u00ce\7\26\2\2\u00cc\u00ce\5\62")
        buf.write("\32\2\u00cd\u00ca\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc")
        buf.write("\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\5r:\2\u00d0\33")
        buf.write("\3\2\2\2\u00d1\u00d4\5\36\20\2\u00d2\u00d4\3\2\2\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4\35\3\2\2\2\u00d5")
        buf.write("\u00d8\5 \21\2\u00d6\u00d8\5\"\22\2\u00d7\u00d5\3\2\2")
        buf.write("\2\u00d7\u00d6\3\2\2\2\u00d8\37\3\2\2\2\u00d9\u00da\7")
        buf.write(":\2\2\u00da\u00db\7\62\2\2\u00db\u00dc\5\64\33\2\u00dc")
        buf.write("\u00dd\3\2\2\2\u00dd\u00de\7\60\2\2\u00de\u00df\5 \21")
        buf.write("\2\u00df\u00e4\3\2\2\2\u00e0\u00e1\7:\2\2\u00e1\u00e2")
        buf.write("\7\62\2\2\u00e2\u00e4\5\64\33\2\u00e3\u00d9\3\2\2\2\u00e3")
        buf.write("\u00e0\3\2\2\2\u00e4!\3\2\2\2\u00e5\u00e6\5$\23\2\u00e6")
        buf.write("\u00e7\7\62\2\2\u00e7\u00e8\5\64\33\2\u00e8\u00e9\3\2")
        buf.write("\2\2\u00e9\u00ea\7\60\2\2\u00ea\u00eb\5\"\22\2\u00eb\u00f1")
        buf.write("\3\2\2\2\u00ec\u00ed\5$\23\2\u00ed\u00ee\7\62\2\2\u00ee")
        buf.write("\u00ef\5\64\33\2\u00ef\u00f1\3\2\2\2\u00f0\u00e5\3\2\2")
        buf.write("\2\u00f0\u00ec\3\2\2\2\u00f1#\3\2\2\2\u00f2\u00f5\5&\24")
        buf.write("\2\u00f3\u00f5\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f3")
        buf.write("\3\2\2\2\u00f5%\3\2\2\2\u00f6\u00f7\7:\2\2\u00f7\u00f8")
        buf.write("\7\60\2\2\u00f8\u00fb\5&\24\2\u00f9\u00fb\7:\2\2\u00fa")
        buf.write("\u00f6\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\'\3\2\2\2\u00fc")
        buf.write("\u00fd\7\30\2\2\u00fd\u00fe\7\22\2\2\u00fe\u00ff\7+\2")
        buf.write("\2\u00ff\u0100\5\34\17\2\u0100\u0101\7,\2\2\u0101\u0102")
        buf.write("\5r:\2\u0102)\3\2\2\2\u0103\u0104\7:\2\2\u0104\u0105\7")
        buf.write("\3\2\2\u0105+\3\2\2\2\u0106\u010c\7\65\2\2\u0107\u010c")
        buf.write("\7\66\2\2\u0108\u010c\5.\30\2\u0109\u010c\7\67\2\2\u010a")
        buf.write("\u010c\5x=\2\u010b\u0106\3\2\2\2\u010b\u0107\3\2\2\2\u010b")
        buf.write("\u0108\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010a\3\2\2\2")
        buf.write("\u010c-\3\2\2\2\u010d\u010e\t\4\2\2\u010e/\3\2\2\2\u010f")
        buf.write("\u0115\7\65\2\2\u0110\u0115\7\66\2\2\u0111\u0115\5.\30")
        buf.write("\2\u0112\u0115\7\67\2\2\u0113\u0115\7\20\2\2\u0114\u010f")
        buf.write("\3\2\2\2\u0114\u0110\3\2\2\2\u0114\u0111\3\2\2\2\u0114")
        buf.write("\u0112\3\2\2\2\u0114\u0113\3\2\2\2\u0115\u0116\3\2\2\2")
        buf.write("\u0116\u0117\7\60\2\2\u0117\u0120\5\60\31\2\u0118\u011e")
        buf.write("\7\65\2\2\u0119\u011e\7\66\2\2\u011a\u011e\5.\30\2\u011b")
        buf.write("\u011e\7\67\2\2\u011c\u011e\7\20\2\2\u011d\u0118\3\2\2")
        buf.write("\2\u011d\u0119\3\2\2\2\u011d\u011a\3\2\2\2\u011d\u011b")
        buf.write("\3\2\2\2\u011d\u011c\3\2\2\2\u011e\u0120\3\2\2\2\u011f")
        buf.write("\u0114\3\2\2\2\u011f\u011d\3\2\2\2\u0120\61\3\2\2\2\u0121")
        buf.write("\u0122\7-\2\2\u0122\u0123\7\65\2\2\u0123\u0124\7.\2\2")
        buf.write("\u0124\u0125\5\64\33\2\u0125\63\3\2\2\2\u0126\u0127\t")
        buf.write("\5\2\2\u0127\65\3\2\2\2\u0128\u0129\7\25\2\2\u0129\u012a")
        buf.write("\7:\2\2\u012a\u012b\7+\2\2\u012b\u012c\7,\2\2\u012c\67")
        buf.write("\3\2\2\2\u012d\u012e\5H%\2\u012e\u012f\7/\2\2\u012f\u0130")
        buf.write("\7:\2\2\u0130\u0131\7+\2\2\u0131\u0132\5<\37\2\u0132\u0133")
        buf.write("\7,\2\2\u01339\3\2\2\2\u0134\u0135\7:\2\2\u0135\u0138")
        buf.write("\7/\2\2\u0136\u0138\3\2\2\2\u0137\u0134\3\2\2\2\u0137")
        buf.write("\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013a\7;\2\2")
        buf.write("\u013a\u013b\7+\2\2\u013b\u013c\5<\37\2\u013c\u013d\7")
        buf.write(",\2\2\u013d;\3\2\2\2\u013e\u0141\5> \2\u013f\u0141\3\2")
        buf.write("\2\2\u0140\u013e\3\2\2\2\u0140\u013f\3\2\2\2\u0141=\3")
        buf.write("\2\2\2\u0142\u0143\5H%\2\u0143\u0144\7\60\2\2\u0144\u0145")
        buf.write("\5> \2\u0145\u0148\3\2\2\2\u0146\u0148\5H%\2\u0147\u0142")
        buf.write("\3\2\2\2\u0147\u0146\3\2\2\2\u0148?\3\2\2\2\u0149\u014a")
        buf.write("\t\6\2\2\u014aA\3\2\2\2\u014b\u014c\t\7\2\2\u014cC\3\2")
        buf.write("\2\2\u014d\u014e\t\b\2\2\u014eE\3\2\2\2\u014f\u0150\t")
        buf.write("\t\2\2\u0150G\3\2\2\2\u0151\u0152\5J&\2\u0152\u0153\7")
        buf.write(")\2\2\u0153\u0154\5J&\2\u0154\u0157\3\2\2\2\u0155\u0157")
        buf.write("\5J&\2\u0156\u0151\3\2\2\2\u0156\u0155\3\2\2\2\u0157I")
        buf.write("\3\2\2\2\u0158\u0159\5L\'\2\u0159\u015a\5@!\2\u015a\u015b")
        buf.write("\5L\'\2\u015b\u015e\3\2\2\2\u015c\u015e\5L\'\2\u015d\u0158")
        buf.write("\3\2\2\2\u015d\u015c\3\2\2\2\u015eK\3\2\2\2\u015f\u0160")
        buf.write("\b\'\1\2\u0160\u0161\5N(\2\u0161\u0168\3\2\2\2\u0162\u0163")
        buf.write("\f\4\2\2\u0163\u0164\5B\"\2\u0164\u0165\5N(\2\u0165\u0167")
        buf.write("\3\2\2\2\u0166\u0162\3\2\2\2\u0167\u016a\3\2\2\2\u0168")
        buf.write("\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169M\3\2\2\2\u016a")
        buf.write("\u0168\3\2\2\2\u016b\u016c\b(\1\2\u016c\u016d\5P)\2\u016d")
        buf.write("\u0174\3\2\2\2\u016e\u016f\f\4\2\2\u016f\u0170\5D#\2\u0170")
        buf.write("\u0171\5P)\2\u0171\u0173\3\2\2\2\u0172\u016e\3\2\2\2\u0173")
        buf.write("\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u0175O\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u0178\b)\1\2")
        buf.write("\u0178\u0179\5R*\2\u0179\u0180\3\2\2\2\u017a\u017b\f\4")
        buf.write("\2\2\u017b\u017c\5F$\2\u017c\u017d\5R*\2\u017d\u017f\3")
        buf.write("\2\2\2\u017e\u017a\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e")
        buf.write("\3\2\2\2\u0180\u0181\3\2\2\2\u0181Q\3\2\2\2\u0182\u0180")
        buf.write("\3\2\2\2\u0183\u0184\7%\2\2\u0184\u0187\5R*\2\u0185\u0187")
        buf.write("\5T+\2\u0186\u0183\3\2\2\2\u0186\u0185\3\2\2\2\u0187S")
        buf.write("\3\2\2\2\u0188\u0189\7\32\2\2\u0189\u018c\5T+\2\u018a")
        buf.write("\u018c\5V,\2\u018b\u0188\3\2\2\2\u018b\u018a\3\2\2\2\u018c")
        buf.write("U\3\2\2\2\u018d\u018e\5X-\2\u018e\u018f\7-\2\2\u018f\u0190")
        buf.write("\5H%\2\u0190\u0191\7.\2\2\u0191\u0194\3\2\2\2\u0192\u0194")
        buf.write("\5X-\2\u0193\u018d\3\2\2\2\u0193\u0192\3\2\2\2\u0194W")
        buf.write("\3\2\2\2\u0195\u0196\b-\1\2\u0196\u0197\5Z.\2\u0197\u01a4")
        buf.write("\3\2\2\2\u0198\u0199\f\4\2\2\u0199\u019a\7/\2\2\u019a")
        buf.write("\u01a0\7:\2\2\u019b\u019c\7+\2\2\u019c\u019d\5<\37\2\u019d")
        buf.write("\u019e\7,\2\2\u019e\u01a1\3\2\2\2\u019f\u01a1\3\2\2\2")
        buf.write("\u01a0\u019b\3\2\2\2\u01a0\u019f\3\2\2\2\u01a1\u01a3\3")
        buf.write("\2\2\2\u01a2\u0198\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2")
        buf.write("\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5Y\3\2\2\2\u01a6\u01a4")
        buf.write("\3\2\2\2\u01a7\u01a8\7:\2\2\u01a8\u01ab\7/\2\2\u01a9\u01ab")
        buf.write("\3\2\2\2\u01aa\u01a7\3\2\2\2\u01aa\u01a9\3\2\2\2\u01ab")
        buf.write("\u01ac\3\2\2\2\u01ac\u01b9\7;\2\2\u01ad\u01ae\7:\2\2\u01ae")
        buf.write("\u01b1\7/\2\2\u01af\u01b1\3\2\2\2\u01b0\u01ad\3\2\2\2")
        buf.write("\u01b0\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\7")
        buf.write(";\2\2\u01b3\u01b4\7+\2\2\u01b4\u01b5\5<\37\2\u01b5\u01b6")
        buf.write("\7,\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b9\5\\/\2\u01b8\u01aa")
        buf.write("\3\2\2\2\u01b8\u01b0\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9")
        buf.write("[\3\2\2\2\u01ba\u01bb\7\25\2\2\u01bb\u01bc\5\b\5\2\u01bc")
        buf.write("\u01bd\7+\2\2\u01bd\u01be\5<\37\2\u01be\u01bf\7,\2\2\u01bf")
        buf.write("\u01c2\3\2\2\2\u01c0\u01c2\5^\60\2\u01c1\u01ba\3\2\2\2")
        buf.write("\u01c1\u01c0\3\2\2\2\u01c2]\3\2\2\2\u01c3\u01c4\7+\2\2")
        buf.write("\u01c4\u01c5\5H%\2\u01c5\u01c6\7,\2\2\u01c6\u01c9\3\2")
        buf.write("\2\2\u01c7\u01c9\5`\61\2\u01c8\u01c3\3\2\2\2\u01c8\u01c7")
        buf.write("\3\2\2\2\u01c9_\3\2\2\2\u01ca\u01ce\5,\27\2\u01cb\u01ce")
        buf.write("\5\b\5\2\u01cc\u01ce\7\24\2\2\u01cd\u01ca\3\2\2\2\u01cd")
        buf.write("\u01cb\3\2\2\2\u01cd\u01cc\3\2\2\2\u01cea\3\2\2\2\u01cf")
        buf.write("\u01d0\5H%\2\u01d0\u01d1\7!\2\2\u01d1\u01d2\5H%\2\u01d2")
        buf.write("\u01d3\7\61\2\2\u01d3c\3\2\2\2\u01d4\u01d7\7\6\2\2\u01d5")
        buf.write("\u01d8\5r:\2\u01d6\u01d8\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7")
        buf.write("\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da\5H%\2\u01da")
        buf.write("\u01de\5r:\2\u01db\u01dc\7\7\2\2\u01dc\u01df\5r:\2\u01dd")
        buf.write("\u01df\3\2\2\2\u01de\u01db\3\2\2\2\u01de\u01dd\3\2\2\2")
        buf.write("\u01dfe\3\2\2\2\u01e0\u01e1\7\b\2\2\u01e1\u01e2\5b\62")
        buf.write("\2\u01e2\u01e3\5H%\2\u01e3\u01e4\7\61\2\2\u01e4\u01e5")
        buf.write("\3\2\2\2\u01e5\u01e6\5H%\2\u01e6\u01e7\7!\2\2\u01e7\u01e8")
        buf.write("\5H%\2\u01e8\u01e9\3\2\2\2\u01e9\u01ea\5r:\2\u01eag\3")
        buf.write("\2\2\2\u01eb\u01ec\7\4\2\2\u01ec\u01ed\7\61\2\2\u01ed")
        buf.write("i\3\2\2\2\u01ee\u01ef\7\5\2\2\u01ef\u01f0\7\61\2\2\u01f0")
        buf.write("k\3\2\2\2\u01f1\u01f4\7\17\2\2\u01f2\u01f5\5H%\2\u01f3")
        buf.write("\u01f5\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f3\3\2\2\2")
        buf.write("\u01f5\u01f6\3\2\2\2\u01f6\u01f7\7\61\2\2\u01f7m\3\2\2")
        buf.write("\2\u01f8\u01fb\58\35\2\u01f9\u01fb\5:\36\2\u01fa\u01f8")
        buf.write("\3\2\2\2\u01fa\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc")
        buf.write("\u01fd\7\61\2\2\u01fdo\3\2\2\2\u01fe\u01ff\7\25\2\2\u01ff")
        buf.write("\u0200\7:\2\2\u0200\u0201\7+\2\2\u0201\u0202\5<\37\2\u0202")
        buf.write("\u0203\7,\2\2\u0203q\3\2\2\2\u0204\u0205\7\63\2\2\u0205")
        buf.write("\u0206\5t;\2\u0206\u0207\7\64\2\2\u0207s\3\2\2\2\u0208")
        buf.write("\u0209\5v<\2\u0209\u020a\5t;\2\u020a\u020d\3\2\2\2\u020b")
        buf.write("\u020d\3\2\2\2\u020c\u0208\3\2\2\2\u020c\u020b\3\2\2\2")
        buf.write("\u020du\3\2\2\2\u020e\u0218\5\20\t\2\u020f\u0218\5b\62")
        buf.write("\2\u0210\u0218\5d\63\2\u0211\u0218\5f\64\2\u0212\u0218")
        buf.write("\5h\65\2\u0213\u0218\5j\66\2\u0214\u0218\5l\67\2\u0215")
        buf.write("\u0218\5n8\2\u0216\u0218\5r:\2\u0217\u020e\3\2\2\2\u0217")
        buf.write("\u020f\3\2\2\2\u0217\u0210\3\2\2\2\u0217\u0211\3\2\2\2")
        buf.write("\u0217\u0212\3\2\2\2\u0217\u0213\3\2\2\2\u0217\u0214\3")
        buf.write("\2\2\2\u0217\u0215\3\2\2\2\u0217\u0216\3\2\2\2\u0218w")
        buf.write("\3\2\2\2\u0219\u021a\7-\2\2\u021a\u021b\5\60\31\2\u021b")
        buf.write("\u021c\7.\2\2\u021cy\3\2\2\2/\u0081\u008a\u0095\u0099")
        buf.write("\u009d\u00a4\u00b6\u00bb\u00c2\u00cd\u00d3\u00d7\u00e3")
        buf.write("\u00f0\u00f4\u00fa\u010b\u0114\u011d\u011f\u0137\u0140")
        buf.write("\u0147\u0156\u015d\u0168\u0174\u0180\u0186\u018b\u0193")
        buf.write("\u01a0\u01a4\u01aa\u01b0\u01b8\u01c1\u01c8\u01cd\u01d7")
        buf.write("\u01de\u01f4\u01fa\u020c\u0217")
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
    RULE_decl = 2
    RULE_identifier = 3
    RULE_classdecl = 4
    RULE_memberlist = 5
    RULE_member = 6
    RULE_attributedecl = 7
    RULE_attributenodeclare = 8
    RULE_attributewithdeclare = 9
    RULE_attlist = 10
    RULE_attributelist = 11
    RULE_methoddecl = 12
    RULE_parameterlist = 13
    RULE_parameterprime = 14
    RULE_parameterpart1 = 15
    RULE_parameterpart2 = 16
    RULE_identifierlist = 17
    RULE_identifierprime = 18
    RULE_constructor = 19
    RULE_superpart = 20
    RULE_literal = 21
    RULE_boolit = 22
    RULE_literallist = 23
    RULE_arraydecl = 24
    RULE_typ = 25
    RULE_objdecl = 26
    RULE_instancemethodstate = 27
    RULE_staticmethodstate = 28
    RULE_nullableexplist = 29
    RULE_expprime = 30
    RULE_relational = 31
    RULE_logical = 32
    RULE_adding = 33
    RULE_multiplying = 34
    RULE_exp = 35
    RULE_exp1 = 36
    RULE_exp2 = 37
    RULE_exp3 = 38
    RULE_exp4 = 39
    RULE_exp5 = 40
    RULE_exp6 = 41
    RULE_exp7 = 42
    RULE_exp8 = 43
    RULE_exp9 = 44
    RULE_exp10 = 45
    RULE_exp11 = 46
    RULE_exp12 = 47
    RULE_assignstate = 48
    RULE_ifstate = 49
    RULE_forstate = 50
    RULE_breakstate = 51
    RULE_continuestate = 52
    RULE_returnstate = 53
    RULE_methodinvoke = 54
    RULE_createobjectstate = 55
    RULE_blockstate = 56
    RULE_stmtlist = 57
    RULE_stmt = 58
    RULE_arraylit = 59

    ruleNames =  [ "program", "decllist", "decl", "identifier", "classdecl", 
                   "memberlist", "member", "attributedecl", "attributenodeclare", 
                   "attributewithdeclare", "attlist", "attributelist", "methoddecl", 
                   "parameterlist", "parameterprime", "parameterpart1", 
                   "parameterpart2", "identifierlist", "identifierprime", 
                   "constructor", "superpart", "literal", "boolit", "literallist", 
                   "arraydecl", "typ", "objdecl", "instancemethodstate", 
                   "staticmethodstate", "nullableexplist", "expprime", "relational", 
                   "logical", "adding", "multiplying", "exp", "exp1", "exp2", 
                   "exp3", "exp4", "exp5", "exp6", "exp7", "exp8", "exp9", 
                   "exp10", "exp11", "exp12", "assignstate", "ifstate", 
                   "forstate", "breakstate", "continuestate", "returnstate", 
                   "methodinvoke", "createobjectstate", "blockstate", "stmtlist", 
                   "stmt", "arraylit" ]

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
            self.state = 120
            self.decllist()
            self.state = 121
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
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.decl()
                self.state = 124
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
            self.state = 129
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
            self.state = 131
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
            self.state = 133
            self.match(CSlangParser.CLASS)
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 134
                self.superpart()
                pass

            elif la_ == 2:
                pass


            self.state = 138
            self.match(CSlangParser.ID)
            self.state = 139
            self.match(CSlangParser.LCB)
            self.state = 140
            self.memberlist()
            self.state = 141
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
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.member()
                self.state = 144
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
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.attributedecl()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
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
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.attributewithdeclare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
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

        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(CSlangParser.ArraydeclContext,0)


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
            self.state = 157
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 158
            self.attributelist()
            self.state = 159
            self.match(CSlangParser.COLON)
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.ID]:
                self.state = 160
                self.typ()
                pass
            elif token in [CSlangParser.LSB]:
                self.state = 161
                self.arraydecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 164
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
            self.state = 166
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 167
            self.attlist()
            self.state = 168
            self.match(CSlangParser.SM)
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

        def DECLARE(self):
            return self.getToken(CSlangParser.DECLARE, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(CSlangParser.ArraydeclContext,0)


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
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.identifier()
                self.state = 171
                self.match(CSlangParser.CM)
                self.state = 172
                self.attlist()
                self.state = 173
                self.match(CSlangParser.CM)
                self.state = 174
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.identifier()
                self.state = 177
                self.match(CSlangParser.COLON)
                self.state = 180
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.ID]:
                    self.state = 178
                    self.typ()
                    pass
                elif token in [CSlangParser.LSB]:
                    self.state = 179
                    self.arraydecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 182
                self.match(CSlangParser.DECLARE)
                self.state = 183
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
        self.enterRule(localctx, 22, self.RULE_attributelist)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.identifier()
                self.state = 188
                self.match(CSlangParser.CM)
                self.state = 189
                self.attributelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
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

        def arraydecl(self):
            return self.getTypedRuleContext(CSlangParser.ArraydeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_methoddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethoddecl" ):
                return visitor.visitMethoddecl(self)
            else:
                return visitor.visitChildren(self)




    def methoddecl(self):

        localctx = CSlangParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_methoddecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(CSlangParser.FUNC)
            self.state = 195
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.ATIDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 196
            self.match(CSlangParser.LRB)
            self.state = 197
            self.parameterlist()
            self.state = 198
            self.match(CSlangParser.RRB)
            self.state = 199
            self.match(CSlangParser.COLON)
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.ID]:
                self.state = 200
                self.typ()
                pass
            elif token in [CSlangParser.VOID]:
                self.state = 201
                self.match(CSlangParser.VOID)
                pass
            elif token in [CSlangParser.LSB]:
                self.state = 202
                self.arraydecl()
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
        self.enterRule(localctx, 26, self.RULE_parameterlist)
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
        self.enterRule(localctx, 28, self.RULE_parameterprime)
        try:
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
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
        self.enterRule(localctx, 30, self.RULE_parameterpart1)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
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
        self.enterRule(localctx, 32, self.RULE_parameterpart2)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
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
        self.enterRule(localctx, 34, self.RULE_identifierlist)
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
        self.enterRule(localctx, 36, self.RULE_identifierprime)
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
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
        self.enterRule(localctx, 38, self.RULE_constructor)
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
        self.enterRule(localctx, 44, self.RULE_boolit)
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
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.INTLIT]:
                    self.state = 269
                    self.match(CSlangParser.INTLIT)
                    pass
                elif token in [CSlangParser.FLOATLIT]:
                    self.state = 270
                    self.match(CSlangParser.FLOATLIT)
                    pass
                elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                    self.state = 271
                    self.boolit()
                    pass
                elif token in [CSlangParser.STRINGLIT]:
                    self.state = 272
                    self.match(CSlangParser.STRINGLIT)
                    pass
                elif token in [CSlangParser.NULL]:
                    self.state = 273
                    self.match(CSlangParser.NULL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 276
                self.match(CSlangParser.CM)
                self.state = 277
                self.literallist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.INTLIT]:
                    self.state = 278
                    self.match(CSlangParser.INTLIT)
                    pass
                elif token in [CSlangParser.FLOATLIT]:
                    self.state = 279
                    self.match(CSlangParser.FLOATLIT)
                    pass
                elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                    self.state = 280
                    self.boolit()
                    pass
                elif token in [CSlangParser.STRINGLIT]:
                    self.state = 281
                    self.match(CSlangParser.STRINGLIT)
                    pass
                elif token in [CSlangParser.NULL]:
                    self.state = 282
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
            self.state = 287
            self.match(CSlangParser.LSB)
            self.state = 288
            self.match(CSlangParser.INTLIT)
            self.state = 289
            self.match(CSlangParser.RSB)
            self.state = 290
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.INT) | (1 << CSlangParser.FLOAT) | (1 << CSlangParser.BOOL) | (1 << CSlangParser.STRING) | (1 << CSlangParser.ID))) != 0)):
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
        self.enterRule(localctx, 54, self.RULE_instancemethodstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.exp()
            self.state = 300
            self.match(CSlangParser.DOT)
            self.state = 301
            self.match(CSlangParser.ID)
            self.state = 302
            self.match(CSlangParser.LRB)
            self.state = 303
            self.nullableexplist()
            self.state = 304
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
        self.enterRule(localctx, 56, self.RULE_staticmethodstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ID]:
                self.state = 306
                self.match(CSlangParser.ID)
                self.state = 307
                self.match(CSlangParser.DOT)
                pass
            elif token in [CSlangParser.ATIDENTIFIER]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 311
            self.match(CSlangParser.ATIDENTIFIER)
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
        self.enterRule(localctx, 58, self.RULE_nullableexplist)
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.DIFF, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
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
        self.enterRule(localctx, 60, self.RULE_expprime)
        try:
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.exp()
                self.state = 321
                self.match(CSlangParser.CM)
                self.state = 322
                self.expprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
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
        self.enterRule(localctx, 62, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
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
        self.enterRule(localctx, 64, self.RULE_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
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
        self.enterRule(localctx, 66, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
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
        self.enterRule(localctx, 68, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
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
        self.enterRule(localctx, 70, self.RULE_exp)
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.exp1()
                self.state = 336
                self.match(CSlangParser.CONCAT)
                self.state = 337
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
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
        self.enterRule(localctx, 72, self.RULE_exp1)
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.exp2(0)
                self.state = 343
                self.relational()
                self.state = 344
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 358
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 352
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 353
                    self.logical()
                    self.state = 354
                    self.exp3(0) 
                self.state = 360
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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 370
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 364
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 365
                    self.adding()
                    self.state = 366
                    self.exp4(0) 
                self.state = 372
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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 382
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 376
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 377
                    self.multiplying()
                    self.state = 378
                    self.exp5() 
                self.state = 384
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
        self.enterRule(localctx, 80, self.RULE_exp5)
        try:
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.DIFF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.match(CSlangParser.DIFF)
                self.state = 386
                self.exp5()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
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
        self.enterRule(localctx, 82, self.RULE_exp6)
        try:
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.match(CSlangParser.MINUS)
                self.state = 391
                self.exp6()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
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
        self.enterRule(localctx, 84, self.RULE_exp7)
        try:
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.exp8(0)
                self.state = 396
                self.match(CSlangParser.LSB)
                self.state = 397
                self.exp()
                self.state = 398
                self.match(CSlangParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 418
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 406
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 407
                    self.match(CSlangParser.DOT)
                    self.state = 408
                    self.match(CSlangParser.ID)
                    self.state = 414
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        self.state = 409
                        self.match(CSlangParser.LRB)
                        self.state = 410
                        self.nullableexplist()
                        self.state = 411
                        self.match(CSlangParser.RRB)
                        pass

                    elif la_ == 2:
                        pass

             
                self.state = 420
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
        self.enterRule(localctx, 88, self.RULE_exp9)
        try:
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.ID]:
                    self.state = 421
                    self.match(CSlangParser.ID)
                    self.state = 422
                    self.match(CSlangParser.DOT)
                    pass
                elif token in [CSlangParser.ATIDENTIFIER]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 426
                self.match(CSlangParser.ATIDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.ID]:
                    self.state = 427
                    self.match(CSlangParser.ID)
                    self.state = 428
                    self.match(CSlangParser.DOT)
                    pass
                elif token in [CSlangParser.ATIDENTIFIER]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 432
                self.match(CSlangParser.ATIDENTIFIER)
                self.state = 433
                self.match(CSlangParser.LRB)
                self.state = 434
                self.nullableexplist()
                self.state = 435
                self.match(CSlangParser.RRB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 437
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
        self.enterRule(localctx, 90, self.RULE_exp10)
        try:
            self.state = 447
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.match(CSlangParser.NEW)
                self.state = 441
                self.identifier()
                self.state = 442
                self.match(CSlangParser.LRB)
                self.state = 443
                self.nullableexplist()
                self.state = 444
                self.match(CSlangParser.RRB)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
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
        self.enterRule(localctx, 92, self.RULE_exp11)
        try:
            self.state = 454
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LRB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.match(CSlangParser.LRB)
                self.state = 450
                self.exp()
                self.state = 451
                self.match(CSlangParser.RRB)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
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

        def getRuleIndex(self):
            return CSlangParser.RULE_exp12

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp12" ):
                return visitor.visitExp12(self)
            else:
                return visitor.visitChildren(self)




    def exp12(self):

        localctx = CSlangParser.Exp12Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_exp12)
        try:
            self.state = 459
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.literal()
                pass
            elif token in [CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.identifier()
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 458
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
            self.state = 461
            self.exp()
            self.state = 462
            self.match(CSlangParser.ASSIGN)
            self.state = 463
            self.exp()
            self.state = 464
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
            self.state = 466
            self.match(CSlangParser.IF)
            self.state = 469
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LCB]:
                self.state = 467
                self.blockstate()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.DIFF, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 471
            self.exp()
            self.state = 472
            self.blockstate()
            self.state = 476
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ELSE]:
                self.state = 473
                self.match(CSlangParser.ELSE)
                self.state = 474
                self.blockstate()
                pass
            elif token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.RETURN, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.CONST, CSlangParser.MINUS, CSlangParser.DIFF, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.LCB, CSlangParser.RCB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
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


        def blockstate(self):
            return self.getTypedRuleContext(CSlangParser.BlockstateContext,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExpContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExpContext,i)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

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
            self.state = 478
            self.match(CSlangParser.FOR)
            self.state = 479
            self.assignstate()

            self.state = 480
            self.exp()
            self.state = 481
            self.match(CSlangParser.SM)

            self.state = 483
            self.exp()
            self.state = 484
            self.match(CSlangParser.ASSIGN)
            self.state = 485
            self.exp()
            self.state = 487
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
            self.state = 489
            self.match(CSlangParser.BREAK)
            self.state = 490
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
            self.state = 492
            self.match(CSlangParser.CONTINUE)
            self.state = 493
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
            self.state = 495
            self.match(CSlangParser.RETURN)
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.DIFF, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.state = 496
                self.exp()
                pass
            elif token in [CSlangParser.SM]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 500
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
            self.state = 504
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 502
                self.instancemethodstate()
                pass

            elif la_ == 2:
                self.state = 503
                self.staticmethodstate()
                pass


            self.state = 506
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateobjectstateContext(ParserRuleContext):
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
            return CSlangParser.RULE_createobjectstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateobjectstate" ):
                return visitor.visitCreateobjectstate(self)
            else:
                return visitor.visitChildren(self)




    def createobjectstate(self):

        localctx = CSlangParser.CreateobjectstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_createobjectstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(CSlangParser.NEW)
            self.state = 509
            self.match(CSlangParser.ID)
            self.state = 510
            self.match(CSlangParser.LRB)
            self.state = 511
            self.nullableexplist()
            self.state = 512
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
        self.enterRule(localctx, 112, self.RULE_blockstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(CSlangParser.LCB)
            self.state = 515
            self.stmtlist()
            self.state = 516
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
        self.enterRule(localctx, 114, self.RULE_stmtlist)
        try:
            self.state = 522
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.RETURN, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.CONST, CSlangParser.MINUS, CSlangParser.DIFF, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.LCB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.stmt()
                self.state = 519
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
        self.enterRule(localctx, 116, self.RULE_stmt)
        try:
            self.state = 533
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.attributedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 525
                self.assignstate()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 526
                self.ifstate()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 527
                self.forstate()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 528
                self.breakstate()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 529
                self.continuestate()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 530
                self.returnstate()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 531
                self.methodinvoke()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 532
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
        self.enterRule(localctx, 118, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            self.match(CSlangParser.LSB)
            self.state = 536
            self.literallist()
            self.state = 537
            self.match(CSlangParser.RSB)
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
        self._predicates[37] = self.exp2_sempred
        self._predicates[38] = self.exp3_sempred
        self._predicates[39] = self.exp4_sempred
        self._predicates[43] = self.exp8_sempred
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
         




