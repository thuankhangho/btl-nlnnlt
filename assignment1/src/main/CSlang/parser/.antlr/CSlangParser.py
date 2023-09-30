# Generated from d:\btl1-nlnnlt\assignment1\src\main\CSlang\parser\CSlang.g4 by ANTLR 4.9.2
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
        buf.write("\u021d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0084")
        buf.write("\n\3\3\4\3\4\3\5\3\5\3\6\3\6\5\6\u008c\n\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u0097\n\7\3\b\3\b\5\b\u009b")
        buf.write("\n\b\3\t\3\t\5\t\u009f\n\t\3\n\3\n\3\n\3\n\3\n\5\n\u00a6")
        buf.write("\n\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\5\f\u00b8\n\f\3\f\3\f\3\f\5\f\u00bd")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00c4\n\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00cf\n\16\3\16\3")
        buf.write("\16\3\17\3\17\5\17\u00d5\n\17\3\20\3\20\5\20\u00d9\n\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00e5\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\5\22\u00f2\n\22\3\23\3\23\5\23\u00f6\n\23")
        buf.write("\3\24\3\24\3\24\3\24\5\24\u00fc\n\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u010d\n\27\3\30\3\30\3\31\3\31\3\31\3\31\5")
        buf.write("\31\u0115\n\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u011d")
        buf.write("\n\31\5\31\u011f\n\31\3\32\3\32\3\32\3\32\3\32\3\33\3")
        buf.write("\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\5\36\u0136\n\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\37\3\37\3\37\3\37\3\37\5\37\u0142\n\37\3 \3")
        buf.write(" \5 \u0146\n \3!\3!\3!\3!\3!\5!\u014d\n!\3\"\3\"\3#\3")
        buf.write("#\3$\3$\3%\3%\3&\3&\3&\3&\3&\5&\u015c\n&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\5\'\u0163\n\'\3(\3(\3(\3(\3(\3(\3(\7(\u016c\n(")
        buf.write("\f(\16(\u016f\13(\3)\3)\3)\3)\3)\3)\3)\7)\u0178\n)\f)")
        buf.write("\16)\u017b\13)\3*\3*\3*\3*\3*\3*\3*\7*\u0184\n*\f*\16")
        buf.write("*\u0187\13*\3+\3+\3+\5+\u018c\n+\3,\3,\3,\5,\u0191\n,")
        buf.write("\3-\3-\3-\3-\3-\3-\5-\u0199\n-\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\5.\u01a5\n.\7.\u01a7\n.\f.\16.\u01aa\13.\3/\3")
        buf.write("/\5/\u01ae\n/\3/\3/\3/\5/\u01b3\n/\3/\3/\3/\3/\3/\3/\5")
        buf.write("/\u01bb\n/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u01c4")
        buf.write("\n\60\3\61\3\61\3\61\3\61\3\61\5\61\u01cb\n\61\3\62\3")
        buf.write("\62\3\62\5\62\u01d0\n\62\3\63\3\63\3\63\3\63\3\63\3\64")
        buf.write("\3\64\5\64\u01d9\n\64\3\64\3\64\3\64\3\64\5\64\u01df\n")
        buf.write("\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\67\3\67\3\67\38\38\58\u01f4\n8")
        buf.write("\38\38\39\39\59\u01fa\n9\39\39\3:\3:\3:\3:\3:\3:\3;\3")
        buf.write(";\3;\3;\3<\3<\3<\3<\5<\u020c\n<\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write("=\3=\5=\u0217\n=\3>\3>\3>\3>\3>\2\6NPRZ?\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjlnprtvxz\2\n\3\2:;\4\2\23\23\27\27")
        buf.write("\3\2\t\n\4\2\13\16::\5\2  \"$\'(\3\2\36\37\3\2\31\32\4")
        buf.write("\2\33\35**\2\u021e\2|\3\2\2\2\4\u0083\3\2\2\2\6\u0085")
        buf.write("\3\2\2\2\b\u0087\3\2\2\2\n\u0089\3\2\2\2\f\u0096\3\2\2")
        buf.write("\2\16\u009a\3\2\2\2\20\u009e\3\2\2\2\22\u00a0\3\2\2\2")
        buf.write("\24\u00a9\3\2\2\2\26\u00bc\3\2\2\2\30\u00c3\3\2\2\2\32")
        buf.write("\u00c5\3\2\2\2\34\u00d4\3\2\2\2\36\u00d8\3\2\2\2 \u00e4")
        buf.write("\3\2\2\2\"\u00f1\3\2\2\2$\u00f5\3\2\2\2&\u00fb\3\2\2\2")
        buf.write("(\u00fd\3\2\2\2*\u0104\3\2\2\2,\u010c\3\2\2\2.\u010e\3")
        buf.write("\2\2\2\60\u011e\3\2\2\2\62\u0120\3\2\2\2\64\u0125\3\2")
        buf.write("\2\2\66\u0127\3\2\2\28\u012c\3\2\2\2:\u0135\3\2\2\2<\u0141")
        buf.write("\3\2\2\2>\u0145\3\2\2\2@\u014c\3\2\2\2B\u014e\3\2\2\2")
        buf.write("D\u0150\3\2\2\2F\u0152\3\2\2\2H\u0154\3\2\2\2J\u015b\3")
        buf.write("\2\2\2L\u0162\3\2\2\2N\u0164\3\2\2\2P\u0170\3\2\2\2R\u017c")
        buf.write("\3\2\2\2T\u018b\3\2\2\2V\u0190\3\2\2\2X\u0198\3\2\2\2")
        buf.write("Z\u019a\3\2\2\2\\\u01ba\3\2\2\2^\u01c3\3\2\2\2`\u01ca")
        buf.write("\3\2\2\2b\u01cf\3\2\2\2d\u01d1\3\2\2\2f\u01d6\3\2\2\2")
        buf.write("h\u01e0\3\2\2\2j\u01eb\3\2\2\2l\u01ee\3\2\2\2n\u01f1\3")
        buf.write("\2\2\2p\u01f9\3\2\2\2r\u01fd\3\2\2\2t\u0203\3\2\2\2v\u020b")
        buf.write("\3\2\2\2x\u0216\3\2\2\2z\u0218\3\2\2\2|}\5\4\3\2}~\7\2")
        buf.write("\2\3~\3\3\2\2\2\177\u0080\5\6\4\2\u0080\u0081\5\4\3\2")
        buf.write("\u0081\u0084\3\2\2\2\u0082\u0084\3\2\2\2\u0083\177\3\2")
        buf.write("\2\2\u0083\u0082\3\2\2\2\u0084\5\3\2\2\2\u0085\u0086\5")
        buf.write("\n\6\2\u0086\7\3\2\2\2\u0087\u0088\t\2\2\2\u0088\t\3\2")
        buf.write("\2\2\u0089\u008b\7\21\2\2\u008a\u008c\5*\26\2\u008b\u008a")
        buf.write("\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d\3\2\2\2\u008d")
        buf.write("\u008e\7:\2\2\u008e\u008f\7\63\2\2\u008f\u0090\5\f\7\2")
        buf.write("\u0090\u0091\7\64\2\2\u0091\13\3\2\2\2\u0092\u0093\5\16")
        buf.write("\b\2\u0093\u0094\5\f\7\2\u0094\u0097\3\2\2\2\u0095\u0097")
        buf.write("\3\2\2\2\u0096\u0092\3\2\2\2\u0096\u0095\3\2\2\2\u0097")
        buf.write("\r\3\2\2\2\u0098\u009b\5\20\t\2\u0099\u009b\5\32\16\2")
        buf.write("\u009a\u0098\3\2\2\2\u009a\u0099\3\2\2\2\u009b\17\3\2")
        buf.write("\2\2\u009c\u009f\5\24\13\2\u009d\u009f\5\22\n\2\u009e")
        buf.write("\u009c\3\2\2\2\u009e\u009d\3\2\2\2\u009f\21\3\2\2\2\u00a0")
        buf.write("\u00a1\t\3\2\2\u00a1\u00a2\5\30\r\2\u00a2\u00a5\7\62\2")
        buf.write("\2\u00a3\u00a6\5\64\33\2\u00a4\u00a6\5\62\32\2\u00a5\u00a3")
        buf.write("\3\2\2\2\u00a5\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7")
        buf.write("\u00a8\7\61\2\2\u00a8\23\3\2\2\2\u00a9\u00aa\t\3\2\2\u00aa")
        buf.write("\u00ab\5\26\f\2\u00ab\u00ac\7\61\2\2\u00ac\25\3\2\2\2")
        buf.write("\u00ad\u00ae\5\b\5\2\u00ae\u00af\7\60\2\2\u00af\u00b0")
        buf.write("\5\26\f\2\u00b0\u00b1\7\60\2\2\u00b1\u00b2\5J&\2\u00b2")
        buf.write("\u00bd\3\2\2\2\u00b3\u00b4\5\b\5\2\u00b4\u00b7\7\62\2")
        buf.write("\2\u00b5\u00b8\5\64\33\2\u00b6\u00b8\5\62\32\2\u00b7\u00b5")
        buf.write("\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9")
        buf.write("\u00ba\7&\2\2\u00ba\u00bb\5J&\2\u00bb\u00bd\3\2\2\2\u00bc")
        buf.write("\u00ad\3\2\2\2\u00bc\u00b3\3\2\2\2\u00bd\27\3\2\2\2\u00be")
        buf.write("\u00bf\5\b\5\2\u00bf\u00c0\7\60\2\2\u00c0\u00c1\5\30\r")
        buf.write("\2\u00c1\u00c4\3\2\2\2\u00c2\u00c4\5\b\5\2\u00c3\u00be")
        buf.write("\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\31\3\2\2\2\u00c5\u00c6")
        buf.write("\7\30\2\2\u00c6\u00c7\t\2\2\2\u00c7\u00c8\7+\2\2\u00c8")
        buf.write("\u00c9\5\34\17\2\u00c9\u00ca\7,\2\2\u00ca\u00ce\7\62\2")
        buf.write("\2\u00cb\u00cf\5\64\33\2\u00cc\u00cf\7\26\2\2\u00cd\u00cf")
        buf.write("\5\62\32\2\u00ce\u00cb\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce")
        buf.write("\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\5t;\2\u00d1")
        buf.write("\33\3\2\2\2\u00d2\u00d5\5\36\20\2\u00d3\u00d5\3\2\2\2")
        buf.write("\u00d4\u00d2\3\2\2\2\u00d4\u00d3\3\2\2\2\u00d5\35\3\2")
        buf.write("\2\2\u00d6\u00d9\5 \21\2\u00d7\u00d9\5\"\22\2\u00d8\u00d6")
        buf.write("\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9\37\3\2\2\2\u00da\u00db")
        buf.write("\7:\2\2\u00db\u00dc\7\62\2\2\u00dc\u00dd\5\64\33\2\u00dd")
        buf.write("\u00de\3\2\2\2\u00de\u00df\7\60\2\2\u00df\u00e0\5 \21")
        buf.write("\2\u00e0\u00e5\3\2\2\2\u00e1\u00e2\7:\2\2\u00e2\u00e3")
        buf.write("\7\62\2\2\u00e3\u00e5\5\64\33\2\u00e4\u00da\3\2\2\2\u00e4")
        buf.write("\u00e1\3\2\2\2\u00e5!\3\2\2\2\u00e6\u00e7\5$\23\2\u00e7")
        buf.write("\u00e8\7\62\2\2\u00e8\u00e9\5\64\33\2\u00e9\u00ea\3\2")
        buf.write("\2\2\u00ea\u00eb\7\60\2\2\u00eb\u00ec\5\"\22\2\u00ec\u00f2")
        buf.write("\3\2\2\2\u00ed\u00ee\5$\23\2\u00ee\u00ef\7\62\2\2\u00ef")
        buf.write("\u00f0\5\64\33\2\u00f0\u00f2\3\2\2\2\u00f1\u00e6\3\2\2")
        buf.write("\2\u00f1\u00ed\3\2\2\2\u00f2#\3\2\2\2\u00f3\u00f6\5&\24")
        buf.write("\2\u00f4\u00f6\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f4")
        buf.write("\3\2\2\2\u00f6%\3\2\2\2\u00f7\u00f8\7:\2\2\u00f8\u00f9")
        buf.write("\7\60\2\2\u00f9\u00fc\5&\24\2\u00fa\u00fc\7:\2\2\u00fb")
        buf.write("\u00f7\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc\'\3\2\2\2\u00fd")
        buf.write("\u00fe\7\30\2\2\u00fe\u00ff\7\22\2\2\u00ff\u0100\7+\2")
        buf.write("\2\u0100\u0101\5\34\17\2\u0101\u0102\7,\2\2\u0102\u0103")
        buf.write("\5t;\2\u0103)\3\2\2\2\u0104\u0105\7:\2\2\u0105\u0106\7")
        buf.write("\3\2\2\u0106+\3\2\2\2\u0107\u010d\7\65\2\2\u0108\u010d")
        buf.write("\7\66\2\2\u0109\u010d\5.\30\2\u010a\u010d\7\67\2\2\u010b")
        buf.write("\u010d\5z>\2\u010c\u0107\3\2\2\2\u010c\u0108\3\2\2\2\u010c")
        buf.write("\u0109\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010b\3\2\2\2")
        buf.write("\u010d-\3\2\2\2\u010e\u010f\t\4\2\2\u010f/\3\2\2\2\u0110")
        buf.write("\u0115\7\65\2\2\u0111\u0115\7\66\2\2\u0112\u0115\5.\30")
        buf.write("\2\u0113\u0115\7\67\2\2\u0114\u0110\3\2\2\2\u0114\u0111")
        buf.write("\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0113\3\2\2\2\u0115")
        buf.write("\u0116\3\2\2\2\u0116\u0117\7\60\2\2\u0117\u011f\5\60\31")
        buf.write("\2\u0118\u011d\7\65\2\2\u0119\u011d\7\66\2\2\u011a\u011d")
        buf.write("\5.\30\2\u011b\u011d\7\67\2\2\u011c\u0118\3\2\2\2\u011c")
        buf.write("\u0119\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011b\3\2\2\2")
        buf.write("\u011d\u011f\3\2\2\2\u011e\u0114\3\2\2\2\u011e\u011c\3")
        buf.write("\2\2\2\u011f\61\3\2\2\2\u0120\u0121\7-\2\2\u0121\u0122")
        buf.write("\7\65\2\2\u0122\u0123\7.\2\2\u0123\u0124\5\64\33\2\u0124")
        buf.write("\63\3\2\2\2\u0125\u0126\t\5\2\2\u0126\65\3\2\2\2\u0127")
        buf.write("\u0128\7\25\2\2\u0128\u0129\7:\2\2\u0129\u012a\7+\2\2")
        buf.write("\u012a\u012b\7,\2\2\u012b\67\3\2\2\2\u012c\u012d\5J&\2")
        buf.write("\u012d\u012e\7/\2\2\u012e\u012f\5\b\5\2\u012f\u0130\7")
        buf.write("+\2\2\u0130\u0131\5> \2\u0131\u0132\7,\2\2\u01329\3\2")
        buf.write("\2\2\u0133\u0134\7:\2\2\u0134\u0136\7/\2\2\u0135\u0133")
        buf.write("\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0137\3\2\2\2\u0137")
        buf.write("\u0138\7;\2\2\u0138\u0139\7+\2\2\u0139\u013a\5> \2\u013a")
        buf.write("\u013b\7,\2\2\u013b;\3\2\2\2\u013c\u013d\5J&\2\u013d\u013e")
        buf.write("\7\60\2\2\u013e\u013f\5<\37\2\u013f\u0142\3\2\2\2\u0140")
        buf.write("\u0142\5J&\2\u0141\u013c\3\2\2\2\u0141\u0140\3\2\2\2\u0142")
        buf.write("=\3\2\2\2\u0143\u0146\5@!\2\u0144\u0146\3\2\2\2\u0145")
        buf.write("\u0143\3\2\2\2\u0145\u0144\3\2\2\2\u0146?\3\2\2\2\u0147")
        buf.write("\u0148\5J&\2\u0148\u0149\7\60\2\2\u0149\u014a\5@!\2\u014a")
        buf.write("\u014d\3\2\2\2\u014b\u014d\5J&\2\u014c\u0147\3\2\2\2\u014c")
        buf.write("\u014b\3\2\2\2\u014dA\3\2\2\2\u014e\u014f\t\6\2\2\u014f")
        buf.write("C\3\2\2\2\u0150\u0151\t\7\2\2\u0151E\3\2\2\2\u0152\u0153")
        buf.write("\t\b\2\2\u0153G\3\2\2\2\u0154\u0155\t\t\2\2\u0155I\3\2")
        buf.write("\2\2\u0156\u0157\5L\'\2\u0157\u0158\7)\2\2\u0158\u0159")
        buf.write("\5L\'\2\u0159\u015c\3\2\2\2\u015a\u015c\5L\'\2\u015b\u0156")
        buf.write("\3\2\2\2\u015b\u015a\3\2\2\2\u015cK\3\2\2\2\u015d\u015e")
        buf.write("\5N(\2\u015e\u015f\5B\"\2\u015f\u0160\5N(\2\u0160\u0163")
        buf.write("\3\2\2\2\u0161\u0163\5N(\2\u0162\u015d\3\2\2\2\u0162\u0161")
        buf.write("\3\2\2\2\u0163M\3\2\2\2\u0164\u0165\b(\1\2\u0165\u0166")
        buf.write("\5P)\2\u0166\u016d\3\2\2\2\u0167\u0168\f\4\2\2\u0168\u0169")
        buf.write("\5D#\2\u0169\u016a\5P)\2\u016a\u016c\3\2\2\2\u016b\u0167")
        buf.write("\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2\2\u016d")
        buf.write("\u016e\3\2\2\2\u016eO\3\2\2\2\u016f\u016d\3\2\2\2\u0170")
        buf.write("\u0171\b)\1\2\u0171\u0172\5R*\2\u0172\u0179\3\2\2\2\u0173")
        buf.write("\u0174\f\4\2\2\u0174\u0175\5F$\2\u0175\u0176\5R*\2\u0176")
        buf.write("\u0178\3\2\2\2\u0177\u0173\3\2\2\2\u0178\u017b\3\2\2\2")
        buf.write("\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017aQ\3\2\2")
        buf.write("\2\u017b\u0179\3\2\2\2\u017c\u017d\b*\1\2\u017d\u017e")
        buf.write("\5T+\2\u017e\u0185\3\2\2\2\u017f\u0180\f\4\2\2\u0180\u0181")
        buf.write("\5H%\2\u0181\u0182\5T+\2\u0182\u0184\3\2\2\2\u0183\u017f")
        buf.write("\3\2\2\2\u0184\u0187\3\2\2\2\u0185\u0183\3\2\2\2\u0185")
        buf.write("\u0186\3\2\2\2\u0186S\3\2\2\2\u0187\u0185\3\2\2\2\u0188")
        buf.write("\u0189\7%\2\2\u0189\u018c\5T+\2\u018a\u018c\5V,\2\u018b")
        buf.write("\u0188\3\2\2\2\u018b\u018a\3\2\2\2\u018cU\3\2\2\2\u018d")
        buf.write("\u018e\7\32\2\2\u018e\u0191\5V,\2\u018f\u0191\5X-\2\u0190")
        buf.write("\u018d\3\2\2\2\u0190\u018f\3\2\2\2\u0191W\3\2\2\2\u0192")
        buf.write("\u0193\5Z.\2\u0193\u0194\7-\2\2\u0194\u0195\5J&\2\u0195")
        buf.write("\u0196\7.\2\2\u0196\u0199\3\2\2\2\u0197\u0199\5Z.\2\u0198")
        buf.write("\u0192\3\2\2\2\u0198\u0197\3\2\2\2\u0199Y\3\2\2\2\u019a")
        buf.write("\u019b\b.\1\2\u019b\u019c\5\\/\2\u019c\u01a8\3\2\2\2\u019d")
        buf.write("\u019e\f\4\2\2\u019e\u019f\7/\2\2\u019f\u01a4\7:\2\2\u01a0")
        buf.write("\u01a1\7+\2\2\u01a1\u01a2\5<\37\2\u01a2\u01a3\7,\2\2\u01a3")
        buf.write("\u01a5\3\2\2\2\u01a4\u01a0\3\2\2\2\u01a4\u01a5\3\2\2\2")
        buf.write("\u01a5\u01a7\3\2\2\2\u01a6\u019d\3\2\2\2\u01a7\u01aa\3")
        buf.write("\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9[")
        buf.write("\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u01ac\7:\2\2\u01ac")
        buf.write("\u01ae\7/\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2")
        buf.write("\u01ae\u01af\3\2\2\2\u01af\u01bb\7;\2\2\u01b0\u01b1\7")
        buf.write(":\2\2\u01b1\u01b3\7/\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3")
        buf.write("\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\7;\2\2\u01b5")
        buf.write("\u01b6\7+\2\2\u01b6\u01b7\5> \2\u01b7\u01b8\7,\2\2\u01b8")
        buf.write("\u01bb\3\2\2\2\u01b9\u01bb\5^\60\2\u01ba\u01ad\3\2\2\2")
        buf.write("\u01ba\u01b2\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bb]\3\2\2")
        buf.write("\2\u01bc\u01bd\7\25\2\2\u01bd\u01be\5\b\5\2\u01be\u01bf")
        buf.write("\7+\2\2\u01bf\u01c0\5<\37\2\u01c0\u01c1\7,\2\2\u01c1\u01c4")
        buf.write("\3\2\2\2\u01c2\u01c4\5`\61\2\u01c3\u01bc\3\2\2\2\u01c3")
        buf.write("\u01c2\3\2\2\2\u01c4_\3\2\2\2\u01c5\u01c6\7+\2\2\u01c6")
        buf.write("\u01c7\5J&\2\u01c7\u01c8\7,\2\2\u01c8\u01cb\3\2\2\2\u01c9")
        buf.write("\u01cb\5b\62\2\u01ca\u01c5\3\2\2\2\u01ca\u01c9\3\2\2\2")
        buf.write("\u01cba\3\2\2\2\u01cc\u01d0\5,\27\2\u01cd\u01d0\5\b\5")
        buf.write("\2\u01ce\u01d0\7\24\2\2\u01cf\u01cc\3\2\2\2\u01cf\u01cd")
        buf.write("\3\2\2\2\u01cf\u01ce\3\2\2\2\u01d0c\3\2\2\2\u01d1\u01d2")
        buf.write("\5J&\2\u01d2\u01d3\7!\2\2\u01d3\u01d4\5J&\2\u01d4\u01d5")
        buf.write("\7\61\2\2\u01d5e\3\2\2\2\u01d6\u01d8\7\6\2\2\u01d7\u01d9")
        buf.write("\5t;\2\u01d8\u01d7\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da")
        buf.write("\3\2\2\2\u01da\u01db\5J&\2\u01db\u01de\5t;\2\u01dc\u01dd")
        buf.write("\7\7\2\2\u01dd\u01df\5t;\2\u01de\u01dc\3\2\2\2\u01de\u01df")
        buf.write("\3\2\2\2\u01dfg\3\2\2\2\u01e0\u01e1\7\b\2\2\u01e1\u01e2")
        buf.write("\5d\63\2\u01e2\u01e3\5J&\2\u01e3\u01e4\7\61\2\2\u01e4")
        buf.write("\u01e5\3\2\2\2\u01e5\u01e6\5J&\2\u01e6\u01e7\7!\2\2\u01e7")
        buf.write("\u01e8\5J&\2\u01e8\u01e9\3\2\2\2\u01e9\u01ea\5t;\2\u01ea")
        buf.write("i\3\2\2\2\u01eb\u01ec\7\4\2\2\u01ec\u01ed\7\61\2\2\u01ed")
        buf.write("k\3\2\2\2\u01ee\u01ef\7\5\2\2\u01ef\u01f0\7\61\2\2\u01f0")
        buf.write("m\3\2\2\2\u01f1\u01f3\7\17\2\2\u01f2\u01f4\5J&\2\u01f3")
        buf.write("\u01f2\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f5\3\2\2\2")
        buf.write("\u01f5\u01f6\7\61\2\2\u01f6o\3\2\2\2\u01f7\u01fa\58\35")
        buf.write("\2\u01f8\u01fa\5:\36\2\u01f9\u01f7\3\2\2\2\u01f9\u01f8")
        buf.write("\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fc\7\61\2\2\u01fc")
        buf.write("q\3\2\2\2\u01fd\u01fe\7\25\2\2\u01fe\u01ff\7:\2\2\u01ff")
        buf.write("\u0200\7+\2\2\u0200\u0201\5> \2\u0201\u0202\7,\2\2\u0202")
        buf.write("s\3\2\2\2\u0203\u0204\7\63\2\2\u0204\u0205\5v<\2\u0205")
        buf.write("\u0206\7\64\2\2\u0206u\3\2\2\2\u0207\u0208\5x=\2\u0208")
        buf.write("\u0209\5v<\2\u0209\u020c\3\2\2\2\u020a\u020c\3\2\2\2\u020b")
        buf.write("\u0207\3\2\2\2\u020b\u020a\3\2\2\2\u020cw\3\2\2\2\u020d")
        buf.write("\u0217\5\20\t\2\u020e\u0217\5d\63\2\u020f\u0217\5f\64")
        buf.write("\2\u0210\u0217\5h\65\2\u0211\u0217\5j\66\2\u0212\u0217")
        buf.write("\5l\67\2\u0213\u0217\5n8\2\u0214\u0217\5p9\2\u0215\u0217")
        buf.write("\5t;\2\u0216\u020d\3\2\2\2\u0216\u020e\3\2\2\2\u0216\u020f")
        buf.write("\3\2\2\2\u0216\u0210\3\2\2\2\u0216\u0211\3\2\2\2\u0216")
        buf.write("\u0212\3\2\2\2\u0216\u0213\3\2\2\2\u0216\u0214\3\2\2\2")
        buf.write("\u0216\u0215\3\2\2\2\u0217y\3\2\2\2\u0218\u0219\7-\2\2")
        buf.write("\u0219\u021a\5\60\31\2\u021a\u021b\7.\2\2\u021b{\3\2\2")
        buf.write("\2\60\u0083\u008b\u0096\u009a\u009e\u00a5\u00b7\u00bc")
        buf.write("\u00c3\u00ce\u00d4\u00d8\u00e4\u00f1\u00f5\u00fb\u010c")
        buf.write("\u0114\u011c\u011e\u0135\u0141\u0145\u014c\u015b\u0162")
        buf.write("\u016d\u0179\u0185\u018b\u0190\u0198\u01a4\u01a8\u01ad")
        buf.write("\u01b2\u01ba\u01c3\u01ca\u01cf\u01d8\u01de\u01f3\u01f9")
        buf.write("\u020b\u0216")
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
    RULE_explist = 29
    RULE_nullableexplist = 30
    RULE_expprime = 31
    RULE_relational = 32
    RULE_logical = 33
    RULE_adding = 34
    RULE_multiplying = 35
    RULE_exp = 36
    RULE_exp1 = 37
    RULE_exp2 = 38
    RULE_exp3 = 39
    RULE_exp4 = 40
    RULE_exp5 = 41
    RULE_exp6 = 42
    RULE_exp7 = 43
    RULE_exp8 = 44
    RULE_exp9 = 45
    RULE_exp10 = 46
    RULE_exp11 = 47
    RULE_exp12 = 48
    RULE_assignstate = 49
    RULE_ifstate = 50
    RULE_forstate = 51
    RULE_breakstate = 52
    RULE_continuestate = 53
    RULE_returnstate = 54
    RULE_methodinvoke = 55
    RULE_createobjectstate = 56
    RULE_blockstate = 57
    RULE_stmtlist = 58
    RULE_stmt = 59
    RULE_arraylit = 60

    ruleNames =  [ "program", "decllist", "decl", "identifier", "classdecl", 
                   "memberlist", "member", "attributedecl", "attributenodeclare", 
                   "attributewithdeclare", "attlist", "attributelist", "methoddecl", 
                   "parameterlist", "parameterprime", "parameterpart1", 
                   "parameterpart2", "identifierlist", "identifierprime", 
                   "constructor", "superpart", "literal", "boolit", "literallist", 
                   "arraydecl", "typ", "objdecl", "instancemethodstate", 
                   "staticmethodstate", "explist", "nullableexplist", "expprime", 
                   "relational", "logical", "adding", "multiplying", "exp", 
                   "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", 
                   "exp8", "exp9", "exp10", "exp11", "exp12", "assignstate", 
                   "ifstate", "forstate", "breakstate", "continuestate", 
                   "returnstate", "methodinvoke", "createobjectstate", "blockstate", 
                   "stmtlist", "stmt", "arraylit" ]

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




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.decllist()
            self.state = 123
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




    def decllist(self):

        localctx = CSlangParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.decl()
                self.state = 126
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




    def decl(self):

        localctx = CSlangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
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




    def identifier(self):

        localctx = CSlangParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
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




    def classdecl(self):

        localctx = CSlangParser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(CSlangParser.CLASS)
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 136
                self.superpart()


            self.state = 139
            self.match(CSlangParser.ID)
            self.state = 140
            self.match(CSlangParser.LCB)
            self.state = 141
            self.memberlist()
            self.state = 142
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




    def memberlist(self):

        localctx = CSlangParser.MemberlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_memberlist)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.member()
                self.state = 145
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




    def member(self):

        localctx = CSlangParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_member)
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.attributedecl()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
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




    def attributedecl(self):

        localctx = CSlangParser.AttributedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attributedecl)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.attributewithdeclare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
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




    def attributenodeclare(self):

        localctx = CSlangParser.AttributenodeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attributenodeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 159
            self.attributelist()
            self.state = 160
            self.match(CSlangParser.COLON)
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.ID]:
                self.state = 161
                self.typ()
                pass
            elif token in [CSlangParser.LSB]:
                self.state = 162
                self.arraydecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 165
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




    def attributewithdeclare(self):

        localctx = CSlangParser.AttributewithdeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attributewithdeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 168
            self.attlist()
            self.state = 169
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




    def attlist(self):

        localctx = CSlangParser.AttlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attlist)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.identifier()
                self.state = 172
                self.match(CSlangParser.CM)
                self.state = 173
                self.attlist()
                self.state = 174
                self.match(CSlangParser.CM)
                self.state = 175
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.identifier()
                self.state = 178
                self.match(CSlangParser.COLON)
                self.state = 181
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.ID]:
                    self.state = 179
                    self.typ()
                    pass
                elif token in [CSlangParser.LSB]:
                    self.state = 180
                    self.arraydecl()
                    pass
                else:
                    raise NoViableAltException(self)

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




    def attributelist(self):

        localctx = CSlangParser.AttributelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_attributelist)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
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

        def arraydecl(self):
            return self.getTypedRuleContext(CSlangParser.ArraydeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_methoddecl




    def methoddecl(self):

        localctx = CSlangParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_methoddecl)
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
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING, CSlangParser.ID]:
                self.state = 201
                self.typ()
                pass
            elif token in [CSlangParser.VOID]:
                self.state = 202
                self.match(CSlangParser.VOID)
                pass
            elif token in [CSlangParser.LSB]:
                self.state = 203
                self.arraydecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 206
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




    def parameterlist(self):

        localctx = CSlangParser.ParameterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameterlist)
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.COLON, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
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




    def parameterprime(self):

        localctx = CSlangParser.ParameterprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parameterprime)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.parameterpart1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
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




    def parameterpart1(self):

        localctx = CSlangParser.Parameterpart1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_parameterpart1)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.match(CSlangParser.ID)
                self.state = 217
                self.match(CSlangParser.COLON)
                self.state = 218
                self.typ()
                self.state = 220
                self.match(CSlangParser.CM)
                self.state = 221
                self.parameterpart1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.match(CSlangParser.ID)
                self.state = 224
                self.match(CSlangParser.COLON)
                self.state = 225
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




    def parameterpart2(self):

        localctx = CSlangParser.Parameterpart2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_parameterpart2)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.identifierlist()
                self.state = 229
                self.match(CSlangParser.COLON)
                self.state = 230
                self.typ()
                self.state = 232
                self.match(CSlangParser.CM)
                self.state = 233
                self.parameterpart2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.identifierlist()
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


    class IdentifierlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierprime(self):
            return self.getTypedRuleContext(CSlangParser.IdentifierprimeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_identifierlist




    def identifierlist(self):

        localctx = CSlangParser.IdentifierlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_identifierlist)
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
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




    def identifierprime(self):

        localctx = CSlangParser.IdentifierprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_identifierprime)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(CSlangParser.ID)
                self.state = 246
                self.match(CSlangParser.CM)
                self.state = 247
                self.identifierprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
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




    def constructor(self):

        localctx = CSlangParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(CSlangParser.FUNC)
            self.state = 252
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 253
            self.match(CSlangParser.LRB)
            self.state = 254
            self.parameterlist()
            self.state = 255
            self.match(CSlangParser.RRB)
            self.state = 256
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




    def superpart(self):

        localctx = CSlangParser.SuperpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_superpart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(CSlangParser.ID)
            self.state = 259
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




    def literal(self):

        localctx = CSlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_literal)
        try:
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 263
                self.boolit()
                pass
            elif token in [CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 264
                self.match(CSlangParser.STRINGLIT)
                pass
            elif token in [CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 265
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




    def boolit(self):

        localctx = CSlangParser.BoolitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_boolit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
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

        def getRuleIndex(self):
            return CSlangParser.RULE_literallist




    def literallist(self):

        localctx = CSlangParser.LiterallistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_literallist)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.INTLIT]:
                    self.state = 270
                    self.match(CSlangParser.INTLIT)
                    pass
                elif token in [CSlangParser.FLOATLIT]:
                    self.state = 271
                    self.match(CSlangParser.FLOATLIT)
                    pass
                elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                    self.state = 272
                    self.boolit()
                    pass
                elif token in [CSlangParser.STRINGLIT]:
                    self.state = 273
                    self.match(CSlangParser.STRINGLIT)
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
                self.state = 282
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




    def arraydecl(self):

        localctx = CSlangParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_arraydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(CSlangParser.LSB)
            self.state = 287
            self.match(CSlangParser.INTLIT)
            self.state = 288
            self.match(CSlangParser.RSB)
            self.state = 289
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




    def typ(self):

        localctx = CSlangParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
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




    def objdecl(self):

        localctx = CSlangParser.ObjdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_objdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(CSlangParser.NEW)
            self.state = 294
            self.match(CSlangParser.ID)
            self.state = 295
            self.match(CSlangParser.LRB)
            self.state = 296
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




    def instancemethodstate(self):

        localctx = CSlangParser.InstancemethodstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_instancemethodstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.exp()
            self.state = 299
            self.match(CSlangParser.DOT)
            self.state = 300
            self.identifier()
            self.state = 301
            self.match(CSlangParser.LRB)
            self.state = 302
            self.nullableexplist()
            self.state = 303
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




    def staticmethodstate(self):

        localctx = CSlangParser.StaticmethodstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_staticmethodstate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 305
                self.match(CSlangParser.ID)
                self.state = 306
                self.match(CSlangParser.DOT)


            self.state = 309
            self.match(CSlangParser.ATIDENTIFIER)
            self.state = 310
            self.match(CSlangParser.LRB)
            self.state = 311
            self.nullableexplist()
            self.state = 312
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




    def explist(self):

        localctx = CSlangParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_explist)
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.exp()
                self.state = 315
                self.match(CSlangParser.CM)
                self.state = 316
                self.explist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
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




    def nullableexplist(self):

        localctx = CSlangParser.NullableexplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_nullableexplist)
        try:
            self.state = 323
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.DIFF, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
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




    def expprime(self):

        localctx = CSlangParser.ExpprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expprime)
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.exp()
                self.state = 326
                self.match(CSlangParser.CM)
                self.state = 327
                self.expprime()
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




    def relational(self):

        localctx = CSlangParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
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




    def logical(self):

        localctx = CSlangParser.LogicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
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




    def adding(self):

        localctx = CSlangParser.AddingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
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




    def multiplying(self):

        localctx = CSlangParser.MultiplyingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
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




    def exp(self):

        localctx = CSlangParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp)
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.exp1()
                self.state = 341
                self.match(CSlangParser.CONCAT)
                self.state = 342
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
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




    def exp1(self):

        localctx = CSlangParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp1)
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.exp2(0)
                self.state = 348
                self.relational()
                self.state = 349
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
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



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 363
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 357
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 358
                    self.logical()
                    self.state = 359
                    self.exp3(0) 
                self.state = 365
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 375
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 369
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 370
                    self.adding()
                    self.state = 371
                    self.exp4(0) 
                self.state = 377
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 387
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 381
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 382
                    self.multiplying()
                    self.state = 383
                    self.exp5() 
                self.state = 389
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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




    def exp5(self):

        localctx = CSlangParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_exp5)
        try:
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.DIFF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.match(CSlangParser.DIFF)
                self.state = 391
                self.exp5()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
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




    def exp6(self):

        localctx = CSlangParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_exp6)
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.match(CSlangParser.MINUS)
                self.state = 396
                self.exp6()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
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




    def exp7(self):

        localctx = CSlangParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_exp7)
        try:
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.exp8(0)
                self.state = 401
                self.match(CSlangParser.LSB)
                self.state = 402
                self.exp()
                self.state = 403
                self.match(CSlangParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
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



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 422
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 411
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 412
                    self.match(CSlangParser.DOT)
                    self.state = 413
                    self.match(CSlangParser.ID)
                    self.state = 418
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        self.state = 414
                        self.match(CSlangParser.LRB)
                        self.state = 415
                        self.explist()
                        self.state = 416
                        self.match(CSlangParser.RRB)

             
                self.state = 424
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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




    def exp9(self):

        localctx = CSlangParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_exp9)
        self._la = 0 # Token type
        try:
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 425
                    self.match(CSlangParser.ID)
                    self.state = 426
                    self.match(CSlangParser.DOT)


                self.state = 429
                self.match(CSlangParser.ATIDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 430
                    self.match(CSlangParser.ID)
                    self.state = 431
                    self.match(CSlangParser.DOT)


                self.state = 434
                self.match(CSlangParser.ATIDENTIFIER)
                self.state = 435
                self.match(CSlangParser.LRB)
                self.state = 436
                self.nullableexplist()
                self.state = 437
                self.match(CSlangParser.RRB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 439
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




    def exp10(self):

        localctx = CSlangParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_exp10)
        try:
            self.state = 449
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.match(CSlangParser.NEW)
                self.state = 443
                self.identifier()
                self.state = 444
                self.match(CSlangParser.LRB)
                self.state = 445
                self.explist()
                self.state = 446
                self.match(CSlangParser.RRB)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
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




    def exp11(self):

        localctx = CSlangParser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_exp11)
        try:
            self.state = 456
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LRB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 451
                self.match(CSlangParser.LRB)
                self.state = 452
                self.exp()
                self.state = 453
                self.match(CSlangParser.RRB)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 455
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




    def exp12(self):

        localctx = CSlangParser.Exp12Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_exp12)
        try:
            self.state = 461
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 458
                self.literal()
                pass
            elif token in [CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 459
                self.identifier()
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 460
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




    def assignstate(self):

        localctx = CSlangParser.AssignstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_assignstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.exp()
            self.state = 464
            self.match(CSlangParser.ASSIGN)
            self.state = 465
            self.exp()
            self.state = 466
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




    def ifstate(self):

        localctx = CSlangParser.IfstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_ifstate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(CSlangParser.IF)
            self.state = 470
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LCB:
                self.state = 469
                self.blockstate()


            self.state = 472
            self.exp()
            self.state = 473
            self.blockstate()
            self.state = 476
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 474
                self.match(CSlangParser.ELSE)
                self.state = 475
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




    def forstate(self):

        localctx = CSlangParser.ForstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_forstate)
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




    def breakstate(self):

        localctx = CSlangParser.BreakstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_breakstate)
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




    def continuestate(self):

        localctx = CSlangParser.ContinuestateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_continuestate)
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




    def returnstate(self):

        localctx = CSlangParser.ReturnstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_returnstate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(CSlangParser.RETURN)
            self.state = 497
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.TRUE) | (1 << CSlangParser.FALSE) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.MINUS) | (1 << CSlangParser.DIFF) | (1 << CSlangParser.LRB) | (1 << CSlangParser.LSB) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.STRINGLIT) | (1 << CSlangParser.ID) | (1 << CSlangParser.ATIDENTIFIER))) != 0):
                self.state = 496
                self.exp()


            self.state = 499
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




    def methodinvoke(self):

        localctx = CSlangParser.MethodinvokeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_methodinvoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 501
                self.instancemethodstate()
                pass

            elif la_ == 2:
                self.state = 502
                self.staticmethodstate()
                pass


            self.state = 505
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




    def createobjectstate(self):

        localctx = CSlangParser.CreateobjectstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_createobjectstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(CSlangParser.NEW)
            self.state = 508
            self.match(CSlangParser.ID)
            self.state = 509
            self.match(CSlangParser.LRB)
            self.state = 510
            self.nullableexplist()
            self.state = 511
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




    def blockstate(self):

        localctx = CSlangParser.BlockstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_blockstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(CSlangParser.LCB)
            self.state = 514
            self.stmtlist()
            self.state = 515
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




    def stmtlist(self):

        localctx = CSlangParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_stmtlist)
        try:
            self.state = 521
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.RETURN, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.CONST, CSlangParser.MINUS, CSlangParser.DIFF, CSlangParser.LRB, CSlangParser.LSB, CSlangParser.LCB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 517
                self.stmt()
                self.state = 518
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




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_stmt)
        try:
            self.state = 532
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 523
                self.attributedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 524
                self.assignstate()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 525
                self.ifstate()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 526
                self.forstate()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 527
                self.breakstate()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 528
                self.continuestate()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 529
                self.returnstate()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 530
                self.methodinvoke()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 531
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




    def arraylit(self):

        localctx = CSlangParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.match(CSlangParser.LSB)
            self.state = 535
            self.literallist()
            self.state = 536
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
        self._predicates[38] = self.exp2_sempred
        self._predicates[39] = self.exp3_sempred
        self._predicates[40] = self.exp4_sempred
        self._predicates[44] = self.exp8_sempred
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
         




