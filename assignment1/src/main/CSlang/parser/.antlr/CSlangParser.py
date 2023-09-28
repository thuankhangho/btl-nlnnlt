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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u0223\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\5\3\u0086\n\3\3\4\3\4\3\5\3\5\3\6\3\6\5\6\u008e\n\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u0099\n\7\3\b\3")
        buf.write("\b\5\b\u009d\n\b\3\t\3\t\5\t\u00a1\n\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00bb\n\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\5\16\u00c2\n\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\5\17\u00cc\n\17\3\17\3\17\3\20\3\20")
        buf.write("\5\20\u00d2\n\20\3\21\3\21\5\21\u00d6\n\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00e2\n\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\5\23\u00ef\n\23\3\24\3\24\5\24\u00f3\n\24\3\25\3\25\3")
        buf.write("\25\3\25\5\25\u00f9\n\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\5\30\u010a")
        buf.write("\n\30\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u0116\n\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u011e")
        buf.write("\n\33\5\33\u0120\n\33\3\34\3\34\3\34\3\34\3\34\3\35\3")
        buf.write("\35\3\35\3\35\3\36\3\36\5\36\u012d\n\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \5 \u013a\n \3 \3")
        buf.write(" \3 \3 \3 \3!\3!\3!\3!\3!\5!\u0146\n!\3\"\3\"\5\"\u014a")
        buf.write("\n\"\3#\3#\3#\3#\3#\5#\u0151\n#\3$\3$\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3(\3(\3(\5(\u0160\n(\3)\3)\3)\3)\3)\5)\u0167")
        buf.write("\n)\3*\3*\3*\3*\3*\3*\3*\7*\u0170\n*\f*\16*\u0173\13*")
        buf.write("\3+\3+\3+\3+\3+\3+\3+\7+\u017c\n+\f+\16+\u017f\13+\3,")
        buf.write("\3,\3,\3,\3,\3,\3,\7,\u0188\n,\f,\16,\u018b\13,\3-\3-")
        buf.write("\3-\5-\u0190\n-\3.\3.\3.\5.\u0195\n.\3/\3/\3/\3/\3/\3")
        buf.write("/\5/\u019d\n/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\7\60\u01ac\n\60\f\60\16\60\u01af")
        buf.write("\13\60\3\61\3\61\5\61\u01b3\n\61\3\61\3\61\3\61\5\61\u01b8")
        buf.write("\n\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u01c0\n\61\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u01c9\n\62\3\63")
        buf.write("\3\63\3\63\5\63\u01ce\n\63\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\64\3\64\3\64\3\64\5\64\u01d9\n\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\5\65\u01e4\n\65\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\67\3\67\5\67\u01ed\n\67\3\67\3\67\3\67")
        buf.write("\3\67\5\67\u01f3\n\67\38\38\38\38\38\38\39\39\39\3:\3")
        buf.write(":\3:\3;\3;\3;\5;\u0204\n;\3;\3;\3<\3<\5<\u020a\n<\3<\3")
        buf.write("<\3=\3=\3=\3=\3>\3>\3>\3>\5>\u0216\n>\3?\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\3?\5?\u0221\n?\3?\2\6RTV^@\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnprtvxz|\2\13\3\2:;\4\2\23\23\27\27\3\2")
        buf.write("\13\16\3\2\t\n\5\2  \"$\'(\3\2\36\37\3\2\31\32\4\2\33")
        buf.write("\35**\4\2\24\24::\2\u0223\2~\3\2\2\2\4\u0085\3\2\2\2\6")
        buf.write("\u0087\3\2\2\2\b\u0089\3\2\2\2\n\u008b\3\2\2\2\f\u0098")
        buf.write("\3\2\2\2\16\u009c\3\2\2\2\20\u00a0\3\2\2\2\22\u00a2\3")
        buf.write("\2\2\2\24\u00a8\3\2\2\2\26\u00ac\3\2\2\2\30\u00ba\3\2")
        buf.write("\2\2\32\u00c1\3\2\2\2\34\u00c3\3\2\2\2\36\u00d1\3\2\2")
        buf.write("\2 \u00d5\3\2\2\2\"\u00e1\3\2\2\2$\u00ee\3\2\2\2&\u00f2")
        buf.write("\3\2\2\2(\u00f8\3\2\2\2*\u00fa\3\2\2\2,\u0101\3\2\2\2")
        buf.write(".\u0109\3\2\2\2\60\u010b\3\2\2\2\62\u010d\3\2\2\2\64\u011f")
        buf.write("\3\2\2\2\66\u0121\3\2\2\28\u0126\3\2\2\2:\u012c\3\2\2")
        buf.write("\2<\u0130\3\2\2\2>\u0139\3\2\2\2@\u0145\3\2\2\2B\u0149")
        buf.write("\3\2\2\2D\u0150\3\2\2\2F\u0152\3\2\2\2H\u0154\3\2\2\2")
        buf.write("J\u0156\3\2\2\2L\u0158\3\2\2\2N\u015f\3\2\2\2P\u0166\3")
        buf.write("\2\2\2R\u0168\3\2\2\2T\u0174\3\2\2\2V\u0180\3\2\2\2X\u018f")
        buf.write("\3\2\2\2Z\u0194\3\2\2\2\\\u019c\3\2\2\2^\u019e\3\2\2\2")
        buf.write("`\u01bf\3\2\2\2b\u01c8\3\2\2\2d\u01cd\3\2\2\2f\u01cf\3")
        buf.write("\2\2\2h\u01da\3\2\2\2j\u01e5\3\2\2\2l\u01ea\3\2\2\2n\u01f4")
        buf.write("\3\2\2\2p\u01fa\3\2\2\2r\u01fd\3\2\2\2t\u0200\3\2\2\2")
        buf.write("v\u0209\3\2\2\2x\u020d\3\2\2\2z\u0215\3\2\2\2|\u0220\3")
        buf.write("\2\2\2~\177\5\4\3\2\177\u0080\7\2\2\3\u0080\3\3\2\2\2")
        buf.write("\u0081\u0082\5\6\4\2\u0082\u0083\5\4\3\2\u0083\u0086\3")
        buf.write("\2\2\2\u0084\u0086\3\2\2\2\u0085\u0081\3\2\2\2\u0085\u0084")
        buf.write("\3\2\2\2\u0086\5\3\2\2\2\u0087\u0088\5\n\6\2\u0088\7\3")
        buf.write("\2\2\2\u0089\u008a\t\2\2\2\u008a\t\3\2\2\2\u008b\u008d")
        buf.write("\7\21\2\2\u008c\u008e\5,\27\2\u008d\u008c\3\2\2\2\u008d")
        buf.write("\u008e\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0090\7:\2\2")
        buf.write("\u0090\u0091\7\63\2\2\u0091\u0092\5\f\7\2\u0092\u0093")
        buf.write("\7\64\2\2\u0093\13\3\2\2\2\u0094\u0095\5\16\b\2\u0095")
        buf.write("\u0096\5\f\7\2\u0096\u0099\3\2\2\2\u0097\u0099\3\2\2\2")
        buf.write("\u0098\u0094\3\2\2\2\u0098\u0097\3\2\2\2\u0099\r\3\2\2")
        buf.write("\2\u009a\u009d\5\20\t\2\u009b\u009d\5\34\17\2\u009c\u009a")
        buf.write("\3\2\2\2\u009c\u009b\3\2\2\2\u009d\17\3\2\2\2\u009e\u00a1")
        buf.write("\5\24\13\2\u009f\u00a1\5\22\n\2\u00a0\u009e\3\2\2\2\u00a0")
        buf.write("\u009f\3\2\2\2\u00a1\21\3\2\2\2\u00a2\u00a3\t\3\2\2\u00a3")
        buf.write("\u00a4\5\32\16\2\u00a4\u00a5\7\62\2\2\u00a5\u00a6\5\26")
        buf.write("\f\2\u00a6\u00a7\7\61\2\2\u00a7\23\3\2\2\2\u00a8\u00a9")
        buf.write("\t\3\2\2\u00a9\u00aa\5\30\r\2\u00aa\u00ab\7\61\2\2\u00ab")
        buf.write("\25\3\2\2\2\u00ac\u00ad\t\4\2\2\u00ad\27\3\2\2\2\u00ae")
        buf.write("\u00af\5\b\5\2\u00af\u00b0\7\60\2\2\u00b0\u00b1\5\30\r")
        buf.write("\2\u00b1\u00b2\7\60\2\2\u00b2\u00b3\5N(\2\u00b3\u00bb")
        buf.write("\3\2\2\2\u00b4\u00b5\5\b\5\2\u00b5\u00b6\7\62\2\2\u00b6")
        buf.write("\u00b7\5\26\f\2\u00b7\u00b8\7&\2\2\u00b8\u00b9\5N(\2\u00b9")
        buf.write("\u00bb\3\2\2\2\u00ba\u00ae\3\2\2\2\u00ba\u00b4\3\2\2\2")
        buf.write("\u00bb\31\3\2\2\2\u00bc\u00bd\5\b\5\2\u00bd\u00be\7\60")
        buf.write("\2\2\u00be\u00bf\5\32\16\2\u00bf\u00c2\3\2\2\2\u00c0\u00c2")
        buf.write("\5\b\5\2\u00c1\u00bc\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2")
        buf.write("\33\3\2\2\2\u00c3\u00c4\7\30\2\2\u00c4\u00c5\t\2\2\2\u00c5")
        buf.write("\u00c6\7+\2\2\u00c6\u00c7\5\36\20\2\u00c7\u00c8\7,\2\2")
        buf.write("\u00c8\u00cb\7\62\2\2\u00c9\u00cc\5\26\f\2\u00ca\u00cc")
        buf.write("\7\26\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc")
        buf.write("\u00cd\3\2\2\2\u00cd\u00ce\5x=\2\u00ce\35\3\2\2\2\u00cf")
        buf.write("\u00d2\5 \21\2\u00d0\u00d2\3\2\2\2\u00d1\u00cf\3\2\2\2")
        buf.write("\u00d1\u00d0\3\2\2\2\u00d2\37\3\2\2\2\u00d3\u00d6\5\"")
        buf.write("\22\2\u00d4\u00d6\5$\23\2\u00d5\u00d3\3\2\2\2\u00d5\u00d4")
        buf.write("\3\2\2\2\u00d6!\3\2\2\2\u00d7\u00d8\7:\2\2\u00d8\u00d9")
        buf.write("\7\62\2\2\u00d9\u00da\5\26\f\2\u00da\u00db\3\2\2\2\u00db")
        buf.write("\u00dc\7\60\2\2\u00dc\u00dd\5\"\22\2\u00dd\u00e2\3\2\2")
        buf.write("\2\u00de\u00df\7:\2\2\u00df\u00e0\7\62\2\2\u00e0\u00e2")
        buf.write("\5\26\f\2\u00e1\u00d7\3\2\2\2\u00e1\u00de\3\2\2\2\u00e2")
        buf.write("#\3\2\2\2\u00e3\u00e4\5&\24\2\u00e4\u00e5\7\62\2\2\u00e5")
        buf.write("\u00e6\5\26\f\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\7\60\2")
        buf.write("\2\u00e8\u00e9\5$\23\2\u00e9\u00ef\3\2\2\2\u00ea\u00eb")
        buf.write("\5&\24\2\u00eb\u00ec\7\62\2\2\u00ec\u00ed\5\26\f\2\u00ed")
        buf.write("\u00ef\3\2\2\2\u00ee\u00e3\3\2\2\2\u00ee\u00ea\3\2\2\2")
        buf.write("\u00ef%\3\2\2\2\u00f0\u00f3\5(\25\2\u00f1\u00f3\3\2\2")
        buf.write("\2\u00f2\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3\'\3\2")
        buf.write("\2\2\u00f4\u00f5\7:\2\2\u00f5\u00f6\7\60\2\2\u00f6\u00f9")
        buf.write("\5(\25\2\u00f7\u00f9\7:\2\2\u00f8\u00f4\3\2\2\2\u00f8")
        buf.write("\u00f7\3\2\2\2\u00f9)\3\2\2\2\u00fa\u00fb\7\30\2\2\u00fb")
        buf.write("\u00fc\7\22\2\2\u00fc\u00fd\7+\2\2\u00fd\u00fe\5\36\20")
        buf.write("\2\u00fe\u00ff\7,\2\2\u00ff\u0100\5x=\2\u0100+\3\2\2\2")
        buf.write("\u0101\u0102\7:\2\2\u0102\u0103\7\3\2\2\u0103-\3\2\2\2")
        buf.write("\u0104\u010a\7\65\2\2\u0105\u010a\7\66\2\2\u0106\u010a")
        buf.write("\5\60\31\2\u0107\u010a\7\67\2\2\u0108\u010a\5\62\32\2")
        buf.write("\u0109\u0104\3\2\2\2\u0109\u0105\3\2\2\2\u0109\u0106\3")
        buf.write("\2\2\2\u0109\u0107\3\2\2\2\u0109\u0108\3\2\2\2\u010a/")
        buf.write("\3\2\2\2\u010b\u010c\t\5\2\2\u010c\61\3\2\2\2\u010d\u010e")
        buf.write("\7-\2\2\u010e\u010f\5\64\33\2\u010f\u0110\7.\2\2\u0110")
        buf.write("\63\3\2\2\2\u0111\u0116\7\65\2\2\u0112\u0116\7\66\2\2")
        buf.write("\u0113\u0116\5\60\31\2\u0114\u0116\7\67\2\2\u0115\u0111")
        buf.write("\3\2\2\2\u0115\u0112\3\2\2\2\u0115\u0113\3\2\2\2\u0115")
        buf.write("\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\7\60\2")
        buf.write("\2\u0118\u0120\5\64\33\2\u0119\u011e\7\65\2\2\u011a\u011e")
        buf.write("\7\66\2\2\u011b\u011e\5\60\31\2\u011c\u011e\7\67\2\2\u011d")
        buf.write("\u0119\3\2\2\2\u011d\u011a\3\2\2\2\u011d\u011b\3\2\2\2")
        buf.write("\u011d\u011c\3\2\2\2\u011e\u0120\3\2\2\2\u011f\u0115\3")
        buf.write("\2\2\2\u011f\u011d\3\2\2\2\u0120\65\3\2\2\2\u0121\u0122")
        buf.write("\7-\2\2\u0122\u0123\7<\2\2\u0123\u0124\7.\2\2\u0124\u0125")
        buf.write("\5\26\f\2\u0125\67\3\2\2\2\u0126\u0127\5N(\2\u0127\u0128")
        buf.write("\7/\2\2\u0128\u0129\5\b\5\2\u01299\3\2\2\2\u012a\u012b")
        buf.write("\7:\2\2\u012b\u012d\7/\2\2\u012c\u012a\3\2\2\2\u012c\u012d")
        buf.write("\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u012f\7;\2\2\u012f")
        buf.write(";\3\2\2\2\u0130\u0131\5N(\2\u0131\u0132\7/\2\2\u0132\u0133")
        buf.write("\5\b\5\2\u0133\u0134\7+\2\2\u0134\u0135\5B\"\2\u0135\u0136")
        buf.write("\7,\2\2\u0136=\3\2\2\2\u0137\u0138\7:\2\2\u0138\u013a")
        buf.write("\7/\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write("\u013b\3\2\2\2\u013b\u013c\7;\2\2\u013c\u013d\7+\2\2\u013d")
        buf.write("\u013e\5B\"\2\u013e\u013f\7,\2\2\u013f?\3\2\2\2\u0140")
        buf.write("\u0141\5N(\2\u0141\u0142\7\60\2\2\u0142\u0143\5@!\2\u0143")
        buf.write("\u0146\3\2\2\2\u0144\u0146\5N(\2\u0145\u0140\3\2\2\2\u0145")
        buf.write("\u0144\3\2\2\2\u0146A\3\2\2\2\u0147\u014a\5D#\2\u0148")
        buf.write("\u014a\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u0148\3\2\2\2")
        buf.write("\u014aC\3\2\2\2\u014b\u014c\5N(\2\u014c\u014d\7\60\2\2")
        buf.write("\u014d\u014e\5D#\2\u014e\u0151\3\2\2\2\u014f\u0151\5N")
        buf.write("(\2\u0150\u014b\3\2\2\2\u0150\u014f\3\2\2\2\u0151E\3\2")
        buf.write("\2\2\u0152\u0153\t\6\2\2\u0153G\3\2\2\2\u0154\u0155\t")
        buf.write("\7\2\2\u0155I\3\2\2\2\u0156\u0157\t\b\2\2\u0157K\3\2\2")
        buf.write("\2\u0158\u0159\t\t\2\2\u0159M\3\2\2\2\u015a\u015b\5P)")
        buf.write("\2\u015b\u015c\7)\2\2\u015c\u015d\5P)\2\u015d\u0160\3")
        buf.write("\2\2\2\u015e\u0160\5P)\2\u015f\u015a\3\2\2\2\u015f\u015e")
        buf.write("\3\2\2\2\u0160O\3\2\2\2\u0161\u0162\5R*\2\u0162\u0163")
        buf.write("\5F$\2\u0163\u0164\5R*\2\u0164\u0167\3\2\2\2\u0165\u0167")
        buf.write("\5R*\2\u0166\u0161\3\2\2\2\u0166\u0165\3\2\2\2\u0167Q")
        buf.write("\3\2\2\2\u0168\u0169\b*\1\2\u0169\u016a\5T+\2\u016a\u0171")
        buf.write("\3\2\2\2\u016b\u016c\f\4\2\2\u016c\u016d\5H%\2\u016d\u016e")
        buf.write("\5T+\2\u016e\u0170\3\2\2\2\u016f\u016b\3\2\2\2\u0170\u0173")
        buf.write("\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172")
        buf.write("S\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u0175\b+\1\2\u0175")
        buf.write("\u0176\5V,\2\u0176\u017d\3\2\2\2\u0177\u0178\f\4\2\2\u0178")
        buf.write("\u0179\5J&\2\u0179\u017a\5V,\2\u017a\u017c\3\2\2\2\u017b")
        buf.write("\u0177\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2")
        buf.write("\u017d\u017e\3\2\2\2\u017eU\3\2\2\2\u017f\u017d\3\2\2")
        buf.write("\2\u0180\u0181\b,\1\2\u0181\u0182\5X-\2\u0182\u0189\3")
        buf.write("\2\2\2\u0183\u0184\f\4\2\2\u0184\u0185\5L\'\2\u0185\u0186")
        buf.write("\5X-\2\u0186\u0188\3\2\2\2\u0187\u0183\3\2\2\2\u0188\u018b")
        buf.write("\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a")
        buf.write("W\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u018d\7%\2\2\u018d")
        buf.write("\u0190\5X-\2\u018e\u0190\5Z.\2\u018f\u018c\3\2\2\2\u018f")
        buf.write("\u018e\3\2\2\2\u0190Y\3\2\2\2\u0191\u0192\7\32\2\2\u0192")
        buf.write("\u0195\5Z.\2\u0193\u0195\5\\/\2\u0194\u0191\3\2\2\2\u0194")
        buf.write("\u0193\3\2\2\2\u0195[\3\2\2\2\u0196\u0197\5^\60\2\u0197")
        buf.write("\u0198\7-\2\2\u0198\u0199\5N(\2\u0199\u019a\7.\2\2\u019a")
        buf.write("\u019d\3\2\2\2\u019b\u019d\5^\60\2\u019c\u0196\3\2\2\2")
        buf.write("\u019c\u019b\3\2\2\2\u019d]\3\2\2\2\u019e\u019f\b\60\1")
        buf.write("\2\u019f\u01a0\5`\61\2\u01a0\u01ad\3\2\2\2\u01a1\u01a2")
        buf.write("\f\5\2\2\u01a2\u01a3\7/\2\2\u01a3\u01ac\7:\2\2\u01a4\u01a5")
        buf.write("\f\4\2\2\u01a5\u01a6\7/\2\2\u01a6\u01a7\7:\2\2\u01a7\u01a8")
        buf.write("\7+\2\2\u01a8\u01a9\5@!\2\u01a9\u01aa\7,\2\2\u01aa\u01ac")
        buf.write("\3\2\2\2\u01ab\u01a1\3\2\2\2\u01ab\u01a4\3\2\2\2\u01ac")
        buf.write("\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2")
        buf.write("\u01ae_\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b1\t\n\2")
        buf.write("\2\u01b1\u01b3\7/\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3")
        buf.write("\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01c0\7;\2\2\u01b5")
        buf.write("\u01b6\t\n\2\2\u01b6\u01b8\7/\2\2\u01b7\u01b5\3\2\2\2")
        buf.write("\u01b7\u01b8\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01ba\7")
        buf.write(";\2\2\u01ba\u01bb\7+\2\2\u01bb\u01bc\5@!\2\u01bc\u01bd")
        buf.write("\7,\2\2\u01bd\u01c0\3\2\2\2\u01be\u01c0\5b\62\2\u01bf")
        buf.write("\u01b2\3\2\2\2\u01bf\u01b7\3\2\2\2\u01bf\u01be\3\2\2\2")
        buf.write("\u01c0a\3\2\2\2\u01c1\u01c2\7\25\2\2\u01c2\u01c3\5\b\5")
        buf.write("\2\u01c3\u01c4\7+\2\2\u01c4\u01c5\5@!\2\u01c5\u01c6\7")
        buf.write(",\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c9\5d\63\2\u01c8\u01c1")
        buf.write("\3\2\2\2\u01c8\u01c7\3\2\2\2\u01c9c\3\2\2\2\u01ca\u01ce")
        buf.write("\5.\30\2\u01cb\u01ce\5\b\5\2\u01cc\u01ce\7\24\2\2\u01cd")
        buf.write("\u01ca\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01cc\3\2\2\2")
        buf.write("\u01cee\3\2\2\2\u01cf\u01d8\7\23\2\2\u01d0\u01d1\5\32")
        buf.write("\16\2\u01d1\u01d2\7\62\2\2\u01d2\u01d3\5\26\f\2\u01d3")
        buf.write("\u01d4\7\61\2\2\u01d4\u01d9\3\2\2\2\u01d5\u01d6\5\30\r")
        buf.write("\2\u01d6\u01d7\7\61\2\2\u01d7\u01d9\3\2\2\2\u01d8\u01d0")
        buf.write("\3\2\2\2\u01d8\u01d5\3\2\2\2\u01d9g\3\2\2\2\u01da\u01e3")
        buf.write("\7\27\2\2\u01db\u01dc\5\32\16\2\u01dc\u01dd\7\62\2\2\u01dd")
        buf.write("\u01de\5\26\f\2\u01de\u01df\7\61\2\2\u01df\u01e4\3\2\2")
        buf.write("\2\u01e0\u01e1\5\30\r\2\u01e1\u01e2\7\61\2\2\u01e2\u01e4")
        buf.write("\3\2\2\2\u01e3\u01db\3\2\2\2\u01e3\u01e0\3\2\2\2\u01e4")
        buf.write("i\3\2\2\2\u01e5\u01e6\5N(\2\u01e6\u01e7\7!\2\2\u01e7\u01e8")
        buf.write("\5N(\2\u01e8\u01e9\7\61\2\2\u01e9k\3\2\2\2\u01ea\u01ec")
        buf.write("\7\6\2\2\u01eb\u01ed\5x=\2\u01ec\u01eb\3\2\2\2\u01ec\u01ed")
        buf.write("\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01ef\5N(\2\u01ef\u01f2")
        buf.write("\5x=\2\u01f0\u01f1\7\7\2\2\u01f1\u01f3\5x=\2\u01f2\u01f0")
        buf.write("\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3m\3\2\2\2\u01f4\u01f5")
        buf.write("\7\b\2\2\u01f5\u01f6\5j\66\2\u01f6\u01f7\5N(\2\u01f7\u01f8")
        buf.write("\7\61\2\2\u01f8\u01f9\5x=\2\u01f9o\3\2\2\2\u01fa\u01fb")
        buf.write("\7\4\2\2\u01fb\u01fc\7\61\2\2\u01fcq\3\2\2\2\u01fd\u01fe")
        buf.write("\7\5\2\2\u01fe\u01ff\7\61\2\2\u01ffs\3\2\2\2\u0200\u0203")
        buf.write("\7\17\2\2\u0201\u0204\5N(\2\u0202\u0204\5\b\5\2\u0203")
        buf.write("\u0201\3\2\2\2\u0203\u0202\3\2\2\2\u0203\u0204\3\2\2\2")
        buf.write("\u0204\u0205\3\2\2\2\u0205\u0206\7\61\2\2\u0206u\3\2\2")
        buf.write("\2\u0207\u020a\5<\37\2\u0208\u020a\5> \2\u0209\u0207\3")
        buf.write("\2\2\2\u0209\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u020c")
        buf.write("\7\61\2\2\u020cw\3\2\2\2\u020d\u020e\7\63\2\2\u020e\u020f")
        buf.write("\5z>\2\u020f\u0210\7\64\2\2\u0210y\3\2\2\2\u0211\u0212")
        buf.write("\5|?\2\u0212\u0213\5z>\2\u0213\u0216\3\2\2\2\u0214\u0216")
        buf.write("\3\2\2\2\u0215\u0211\3\2\2\2\u0215\u0214\3\2\2\2\u0216")
        buf.write("{\3\2\2\2\u0217\u0221\5f\64\2\u0218\u0221\5h\65\2\u0219")
        buf.write("\u0221\5j\66\2\u021a\u0221\5l\67\2\u021b\u0221\5n8\2\u021c")
        buf.write("\u0221\5p9\2\u021d\u0221\5r:\2\u021e\u0221\5t;\2\u021f")
        buf.write("\u0221\5v<\2\u0220\u0217\3\2\2\2\u0220\u0218\3\2\2\2\u0220")
        buf.write("\u0219\3\2\2\2\u0220\u021a\3\2\2\2\u0220\u021b\3\2\2\2")
        buf.write("\u0220\u021c\3\2\2\2\u0220\u021d\3\2\2\2\u0220\u021e\3")
        buf.write("\2\2\2\u0220\u021f\3\2\2\2\u0221}\3\2\2\2\60\u0085\u008d")
        buf.write("\u0098\u009c\u00a0\u00ba\u00c1\u00cb\u00d1\u00d5\u00e1")
        buf.write("\u00ee\u00f2\u00f8\u0109\u0115\u011d\u011f\u012c\u0139")
        buf.write("\u0145\u0149\u0150\u015f\u0166\u0171\u017d\u0189\u018f")
        buf.write("\u0194\u019c\u01ab\u01ad\u01b2\u01b7\u01bf\u01c8\u01cd")
        buf.write("\u01d8\u01e3\u01ec\u01f2\u0203\u0209\u0215\u0220")
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
    RULE_instanceattributestate = 27
    RULE_staticattributestate = 28
    RULE_instancemethodstate = 29
    RULE_staticmethodstate = 30
    RULE_explist = 31
    RULE_nullableexplist = 32
    RULE_expprime = 33
    RULE_relational = 34
    RULE_logical = 35
    RULE_adding = 36
    RULE_multiplying = 37
    RULE_exp = 38
    RULE_exp1 = 39
    RULE_exp2 = 40
    RULE_exp3 = 41
    RULE_exp4 = 42
    RULE_exp5 = 43
    RULE_exp6 = 44
    RULE_exp7 = 45
    RULE_exp8 = 46
    RULE_exp9 = 47
    RULE_exp10 = 48
    RULE_exp11 = 49
    RULE_varstate = 50
    RULE_constate = 51
    RULE_assignstate = 52
    RULE_ifstate = 53
    RULE_forstate = 54
    RULE_breakstate = 55
    RULE_continuestate = 56
    RULE_returnstate = 57
    RULE_methodinvoke = 58
    RULE_blockstate = 59
    RULE_stmtlist = 60
    RULE_stmt = 61

    ruleNames =  [ "program", "decllist", "decl", "identifier", "classdecl", 
                   "memberlist", "member", "attributedecl", "attributenodeclare", 
                   "attributewithdeclare", "typ", "attlist", "attributelist", 
                   "methoddecl", "parameterlist", "parameterprime", "parameterpart1", 
                   "parameterpart2", "identifierlist", "identifierprime", 
                   "constructor", "superpart", "literal", "boolit", "arraylit", 
                   "literallist", "arraydecl", "instanceattributestate", 
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




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.decllist()
            self.state = 125
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
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.decl()
                self.state = 128
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
            self.state = 133
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
            self.state = 135
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
            self.state = 137
            self.match(CSlangParser.CLASS)
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 138
                self.superpart()


            self.state = 141
            self.match(CSlangParser.ID)
            self.state = 142
            self.match(CSlangParser.LCB)
            self.state = 143
            self.memberlist()
            self.state = 144
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
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.member()
                self.state = 147
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
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.attributedecl()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
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
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.attributewithdeclare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
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




    def attributenodeclare(self):

        localctx = CSlangParser.AttributenodeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attributenodeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 161
            self.attributelist()
            self.state = 162
            self.match(CSlangParser.COLON)
            self.state = 163
            self.typ()
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




    def typ(self):

        localctx = CSlangParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
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




    def attlist(self):

        localctx = CSlangParser.AttlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_attlist)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.identifier()
                self.state = 173
                self.match(CSlangParser.CM)
                self.state = 174
                self.attlist()
                self.state = 175
                self.match(CSlangParser.CM)
                self.state = 176
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.identifier()
                self.state = 179
                self.match(CSlangParser.COLON)
                self.state = 180
                self.typ()
                self.state = 181
                self.match(CSlangParser.DECLARE)
                self.state = 182
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
        self.enterRule(localctx, 24, self.RULE_attributelist)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.identifier()
                self.state = 187
                self.match(CSlangParser.CM)
                self.state = 188
                self.attributelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
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




    def methoddecl(self):

        localctx = CSlangParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_methoddecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(CSlangParser.FUNC)
            self.state = 194
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.ATIDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 195
            self.match(CSlangParser.LRB)
            self.state = 196
            self.parameterlist()
            self.state = 197
            self.match(CSlangParser.RRB)
            self.state = 198
            self.match(CSlangParser.COLON)
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING]:
                self.state = 199
                self.typ()
                pass
            elif token in [CSlangParser.VOID]:
                self.state = 200
                self.match(CSlangParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 203
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
        self.enterRule(localctx, 28, self.RULE_parameterlist)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.COLON, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
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
        self.enterRule(localctx, 30, self.RULE_parameterprime)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.parameterpart1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
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
        self.enterRule(localctx, 32, self.RULE_parameterpart1)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(CSlangParser.ID)
                self.state = 214
                self.match(CSlangParser.COLON)
                self.state = 215
                self.typ()
                self.state = 217
                self.match(CSlangParser.CM)
                self.state = 218
                self.parameterpart1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(CSlangParser.ID)
                self.state = 221
                self.match(CSlangParser.COLON)
                self.state = 222
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
        self.enterRule(localctx, 34, self.RULE_parameterpart2)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.identifierlist()
                self.state = 226
                self.match(CSlangParser.COLON)
                self.state = 227
                self.typ()
                self.state = 229
                self.match(CSlangParser.CM)
                self.state = 230
                self.parameterpart2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.identifierlist()
                self.state = 233
                self.match(CSlangParser.COLON)
                self.state = 234
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
        self.enterRule(localctx, 36, self.RULE_identifierlist)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
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
        self.enterRule(localctx, 38, self.RULE_identifierprime)
        try:
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.match(CSlangParser.ID)
                self.state = 243
                self.match(CSlangParser.CM)
                self.state = 244
                self.identifierprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
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
        self.enterRule(localctx, 40, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(CSlangParser.FUNC)
            self.state = 249
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 250
            self.match(CSlangParser.LRB)
            self.state = 251
            self.parameterlist()
            self.state = 252
            self.match(CSlangParser.RRB)
            self.state = 253
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
        self.enterRule(localctx, 42, self.RULE_superpart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(CSlangParser.ID)
            self.state = 256
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
        self.enterRule(localctx, 44, self.RULE_literal)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 260
                self.boolit()
                pass
            elif token in [CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 261
                self.match(CSlangParser.STRINGLIT)
                pass
            elif token in [CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 262
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
        self.enterRule(localctx, 46, self.RULE_boolit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
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




    def arraylit(self):

        localctx = CSlangParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(CSlangParser.LSB)
            self.state = 268
            self.literallist()
            self.state = 269
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




    def literallist(self):

        localctx = CSlangParser.LiterallistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_literallist)
        try:
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
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
                else:
                    raise NoViableAltException(self)

                self.state = 277
                self.match(CSlangParser.CM)
                self.state = 278
                self.literallist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.INTLIT]:
                    self.state = 279
                    self.match(CSlangParser.INTLIT)
                    pass
                elif token in [CSlangParser.FLOATLIT]:
                    self.state = 280
                    self.match(CSlangParser.FLOATLIT)
                    pass
                elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                    self.state = 281
                    self.boolit()
                    pass
                elif token in [CSlangParser.STRINGLIT]:
                    self.state = 282
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




    def arraydecl(self):

        localctx = CSlangParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_arraydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(CSlangParser.LSB)
            self.state = 288
            self.match(CSlangParser.ARRAYSIZE)
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




    def instanceattributestate(self):

        localctx = CSlangParser.InstanceattributestateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_instanceattributestate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.exp()
            self.state = 293
            self.match(CSlangParser.DOT)
            self.state = 294
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




    def staticattributestate(self):

        localctx = CSlangParser.StaticattributestateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_staticattributestate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 296
                self.match(CSlangParser.ID)
                self.state = 297
                self.match(CSlangParser.DOT)


            self.state = 300
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




    def instancemethodstate(self):

        localctx = CSlangParser.InstancemethodstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_instancemethodstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.exp()
            self.state = 303
            self.match(CSlangParser.DOT)
            self.state = 304
            self.identifier()
            self.state = 305
            self.match(CSlangParser.LRB)
            self.state = 306
            self.nullableexplist()
            self.state = 307
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
        self.enterRule(localctx, 60, self.RULE_staticmethodstate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 309
                self.match(CSlangParser.ID)
                self.state = 310
                self.match(CSlangParser.DOT)


            self.state = 313
            self.match(CSlangParser.ATIDENTIFIER)
            self.state = 314
            self.match(CSlangParser.LRB)
            self.state = 315
            self.nullableexplist()
            self.state = 316
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
        self.enterRule(localctx, 62, self.RULE_explist)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.exp()
                self.state = 319
                self.match(CSlangParser.CM)
                self.state = 320
                self.explist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
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
        self.enterRule(localctx, 64, self.RULE_nullableexplist)
        try:
            self.state = 327
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.DIFF, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
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
        self.enterRule(localctx, 66, self.RULE_expprime)
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.exp()
                self.state = 330
                self.match(CSlangParser.CM)
                self.state = 331
                self.expprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
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
        self.enterRule(localctx, 68, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
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
        self.enterRule(localctx, 70, self.RULE_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
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
        self.enterRule(localctx, 72, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
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
        self.enterRule(localctx, 74, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
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
        self.enterRule(localctx, 76, self.RULE_exp)
        try:
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.exp1()
                self.state = 345
                self.match(CSlangParser.CONCAT)
                self.state = 346
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
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
        self.enterRule(localctx, 78, self.RULE_exp1)
        try:
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.exp2(0)
                self.state = 352
                self.relational()
                self.state = 353
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 367
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 361
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 362
                    self.logical()
                    self.state = 363
                    self.exp3(0) 
                self.state = 369
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



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 373
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 374
                    self.adding()
                    self.state = 375
                    self.exp4(0) 
                self.state = 381
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



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 391
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 385
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 386
                    self.multiplying()
                    self.state = 387
                    self.exp5() 
                self.state = 393
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




    def exp5(self):

        localctx = CSlangParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_exp5)
        try:
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.DIFF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.match(CSlangParser.DIFF)
                self.state = 395
                self.exp5()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
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
        self.enterRule(localctx, 88, self.RULE_exp6)
        try:
            self.state = 402
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.match(CSlangParser.MINUS)
                self.state = 400
                self.exp6()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
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
        self.enterRule(localctx, 90, self.RULE_exp7)
        try:
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.exp8(0)
                self.state = 405
                self.match(CSlangParser.LSB)
                self.state = 406
                self.exp()
                self.state = 407
                self.match(CSlangParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
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
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 425
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 415
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 416
                        self.match(CSlangParser.DOT)
                        self.state = 417
                        self.match(CSlangParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 418
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 419
                        self.match(CSlangParser.DOT)
                        self.state = 420
                        self.match(CSlangParser.ID)
                        self.state = 421
                        self.match(CSlangParser.LRB)
                        self.state = 422
                        self.explist()
                        self.state = 423
                        self.match(CSlangParser.RRB)
                        pass

             
                self.state = 429
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




    def exp9(self):

        localctx = CSlangParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_exp9)
        self._la = 0 # Token type
        try:
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.SELF or _la==CSlangParser.ID:
                    self.state = 430
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.SELF or _la==CSlangParser.ID):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 431
                    self.match(CSlangParser.DOT)


                self.state = 434
                self.match(CSlangParser.ATIDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.SELF or _la==CSlangParser.ID:
                    self.state = 435
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.SELF or _la==CSlangParser.ID):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 436
                    self.match(CSlangParser.DOT)


                self.state = 439
                self.match(CSlangParser.ATIDENTIFIER)
                self.state = 440
                self.match(CSlangParser.LRB)
                self.state = 441
                self.explist()
                self.state = 442
                self.match(CSlangParser.RRB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 444
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
        self.enterRule(localctx, 96, self.RULE_exp10)
        try:
            self.state = 454
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.match(CSlangParser.NEW)
                self.state = 448
                self.identifier()
                self.state = 449
                self.match(CSlangParser.LRB)
                self.state = 450
                self.explist()
                self.state = 451
                self.match(CSlangParser.RRB)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.SELF, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
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




    def exp11(self):

        localctx = CSlangParser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_exp11)
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




    def varstate(self):

        localctx = CSlangParser.VarstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_varstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.match(CSlangParser.VAR)
            self.state = 470
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 462
                self.attributelist()
                self.state = 463
                self.match(CSlangParser.COLON)
                self.state = 464
                self.typ()
                self.state = 465
                self.match(CSlangParser.SM)
                pass

            elif la_ == 2:
                self.state = 467
                self.attlist()
                self.state = 468
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




    def constate(self):

        localctx = CSlangParser.ConstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_constate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(CSlangParser.CONST)
            self.state = 481
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 473
                self.attributelist()
                self.state = 474
                self.match(CSlangParser.COLON)
                self.state = 475
                self.typ()
                self.state = 476
                self.match(CSlangParser.SM)
                pass

            elif la_ == 2:
                self.state = 478
                self.attlist()
                self.state = 479
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




    def assignstate(self):

        localctx = CSlangParser.AssignstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_assignstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.exp()
            self.state = 484
            self.match(CSlangParser.ASSIGN)
            self.state = 485
            self.exp()
            self.state = 486
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
        self.enterRule(localctx, 106, self.RULE_ifstate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(CSlangParser.IF)
            self.state = 490
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LCB:
                self.state = 489
                self.blockstate()


            self.state = 492
            self.exp()
            self.state = 493
            self.blockstate()
            self.state = 496
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 494
                self.match(CSlangParser.ELSE)
                self.state = 495
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


        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def blockstate(self):
            return self.getTypedRuleContext(CSlangParser.BlockstateContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_forstate




    def forstate(self):

        localctx = CSlangParser.ForstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_forstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(CSlangParser.FOR)
            self.state = 499
            self.assignstate()
            self.state = 500
            self.exp()
            self.state = 501
            self.match(CSlangParser.SM)
            self.state = 502
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
        self.enterRule(localctx, 110, self.RULE_breakstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(CSlangParser.BREAK)
            self.state = 505
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
        self.enterRule(localctx, 112, self.RULE_continuestate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(CSlangParser.CONTINUE)
            self.state = 508
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




    def returnstate(self):

        localctx = CSlangParser.ReturnstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_returnstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(CSlangParser.RETURN)
            self.state = 513
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 511
                self.exp()

            elif la_ == 2:
                self.state = 512
                self.identifier()


            self.state = 515
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
        self.enterRule(localctx, 116, self.RULE_methodinvoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 517
                self.instancemethodstate()
                pass

            elif la_ == 2:
                self.state = 518
                self.staticmethodstate()
                pass


            self.state = 521
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




    def blockstate(self):

        localctx = CSlangParser.BlockstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_blockstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(CSlangParser.LCB)
            self.state = 524
            self.stmtlist()
            self.state = 525
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
        self.enterRule(localctx, 120, self.RULE_stmtlist)
        try:
            self.state = 531
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BREAK, CSlangParser.CONTINUE, CSlangParser.IF, CSlangParser.FOR, CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.RETURN, CSlangParser.VAR, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.CONST, CSlangParser.MINUS, CSlangParser.DIFF, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT, CSlangParser.ID, CSlangParser.ATIDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 527
                self.stmt()
                self.state = 528
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




    def stmt(self):

        localctx = CSlangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_stmt)
        try:
            self.state = 542
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 533
                self.varstate()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 534
                self.constate()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 535
                self.assignstate()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 536
                self.ifstate()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 537
                self.forstate()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 538
                self.breakstate()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 539
                self.continuestate()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 540
                self.returnstate()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 541
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
        self._predicates[40] = self.exp2_sempred
        self._predicates[41] = self.exp3_sempred
        self._predicates[42] = self.exp4_sempred
        self._predicates[46] = self.exp8_sempred
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
         




