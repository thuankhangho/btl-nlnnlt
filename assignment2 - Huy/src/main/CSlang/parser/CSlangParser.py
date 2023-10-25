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
        buf.write("\u0219\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\5\3\u0088\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\5\5\u0095\n\5\3\6\3\6\5\6\u0099\n\6\3\7\3\7")
        buf.write("\5\7\u009d\n\7\3\b\3\b\5\b\u00a1\n\b\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\5\r\u00b8\n\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00c6\n\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17")
        buf.write("\u00d2\n\17\3\20\3\20\5\20\u00d6\n\20\3\21\3\21\5\21\u00da")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u00e1\n\22\3\23\3")
        buf.write("\23\3\23\3\23\3\24\3\24\5\24\u00e9\n\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\5\25\u00f0\n\25\3\26\3\26\5\26\u00f4\n\26\3")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\3\27\5\27\u00fd\n\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\5\35\u0116\n\35\3\36\3\36\5\36\u011a\n\36\3\37\3\37\3")
        buf.write("\37\3\37\3\37\5\37\u0121\n\37\3 \3 \3 \3 \3 \5 \u0128")
        buf.write("\n \3!\3!\3!\3!\3!\5!\u012f\n!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\7\"\u0137\n\"\f\"\16\"\u013a\13\"\3#\3#\3#\3#\3#\3#\7")
        buf.write("#\u0142\n#\f#\16#\u0145\13#\3$\3$\3$\3$\3$\3$\7$\u014d")
        buf.write("\n$\f$\16$\u0150\13$\3%\3%\3%\5%\u0155\n%\3&\3&\3&\5&")
        buf.write("\u015a\n&\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0162\n\'\3(\3(")
        buf.write("\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u016f\n(\7(\u0171\n(\f")
        buf.write("(\16(\u0174\13(\3)\3)\3)\5)\u0179\n)\3)\3)\3)\3)\5)\u017f")
        buf.write("\n)\3)\3)\3)\3)\3)\3)\5)\u0187\n)\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\5*\u0190\n*\3+\3+\3+\3+\3+\5+\u0197\n+\3,\3,\3,\3,\5")
        buf.write(",\u019d\n,\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01a7\n-\3.\3.\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\5\61\u01b9\n\61\3\62\3\62\3\62\5\62\u01be\n\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\5\62\u01c5\n\62\3\63\3\63\3")
        buf.write("\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\5\66\u01d7\n\66\3\66\3\66\3\67\3\67\3")
        buf.write("\67\3\67\5\67\u01df\n\67\38\38\38\38\38\38\38\39\39\3")
        buf.write("9\59\u01eb\n9\39\39\39\39\39\3:\3:\3:\3:\3;\3;\3;\3;\5")
        buf.write(";\u01fa\n;\3<\3<\3<\3<\3<\3<\3<\3<\3<\5<\u0205\n<\3=\3")
        buf.write("=\3>\3>\3>\5>\u020c\n>\3?\3?\3?\3?\3@\3@\3@\3@\3@\5@\u0217")
        buf.write("\n@\3@\2\6BDFNA\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprt")
        buf.write("vxz|~\2\n\4\2\7\7\30\30\7\2\6\6\16\16\22\22\26\26\67\67")
        buf.write("\b\2\6\6\16\16\22\22\24\24\26\26\67\67\4\2!!#\'\3\2\37")
        buf.write(" \3\2\31\32\4\2\33\35**\3\2\678\2\u0217\2\u0080\3\2\2")
        buf.write("\2\4\u0087\3\2\2\2\6\u0089\3\2\2\2\b\u0094\3\2\2\2\n\u0098")
        buf.write("\3\2\2\2\f\u009c\3\2\2\2\16\u00a0\3\2\2\2\20\u00a2\3\2")
        buf.write("\2\2\22\u00a6\3\2\2\2\24\u00aa\3\2\2\2\26\u00ae\3\2\2")
        buf.write("\2\30\u00b7\3\2\2\2\32\u00c5\3\2\2\2\34\u00d1\3\2\2\2")
        buf.write("\36\u00d5\3\2\2\2 \u00d9\3\2\2\2\"\u00e0\3\2\2\2$\u00e2")
        buf.write("\3\2\2\2&\u00e8\3\2\2\2(\u00ef\3\2\2\2*\u00f3\3\2\2\2")
        buf.write(",\u00fc\3\2\2\2.\u00fe\3\2\2\2\60\u0105\3\2\2\2\62\u0107")
        buf.write("\3\2\2\2\64\u0109\3\2\2\2\66\u010e\3\2\2\28\u0115\3\2")
        buf.write("\2\2:\u0119\3\2\2\2<\u0120\3\2\2\2>\u0127\3\2\2\2@\u012e")
        buf.write("\3\2\2\2B\u0130\3\2\2\2D\u013b\3\2\2\2F\u0146\3\2\2\2")
        buf.write("H\u0154\3\2\2\2J\u0159\3\2\2\2L\u0161\3\2\2\2N\u0163\3")
        buf.write("\2\2\2P\u0186\3\2\2\2R\u018f\3\2\2\2T\u0196\3\2\2\2V\u019c")
        buf.write("\3\2\2\2X\u01a6\3\2\2\2Z\u01a8\3\2\2\2\\\u01aa\3\2\2\2")
        buf.write("^\u01ad\3\2\2\2`\u01b8\3\2\2\2b\u01ba\3\2\2\2d\u01c6\3")
        buf.write("\2\2\2f\u01cd\3\2\2\2h\u01d0\3\2\2\2j\u01d3\3\2\2\2l\u01de")
        buf.write("\3\2\2\2n\u01e0\3\2\2\2p\u01ea\3\2\2\2r\u01f1\3\2\2\2")
        buf.write("t\u01f9\3\2\2\2v\u0204\3\2\2\2x\u0206\3\2\2\2z\u020b\3")
        buf.write("\2\2\2|\u020d\3\2\2\2~\u0216\3\2\2\2\u0080\u0081\5\4\3")
        buf.write("\2\u0081\u0082\7\2\2\3\u0082\3\3\2\2\2\u0083\u0084\5\6")
        buf.write("\4\2\u0084\u0085\5\4\3\2\u0085\u0088\3\2\2\2\u0086\u0088")
        buf.write("\3\2\2\2\u0087\u0083\3\2\2\2\u0087\u0086\3\2\2\2\u0088")
        buf.write("\5\3\2\2\2\u0089\u008a\7\23\2\2\u008a\u008b\5z>\2\u008b")
        buf.write("\u008c\7\67\2\2\u008c\u008d\7\63\2\2\u008d\u008e\5\b\5")
        buf.write("\2\u008e\u008f\7\64\2\2\u008f\7\3\2\2\2\u0090\u0091\5")
        buf.write("\n\6\2\u0091\u0092\5\b\5\2\u0092\u0095\3\2\2\2\u0093\u0095")
        buf.write("\3\2\2\2\u0094\u0090\3\2\2\2\u0094\u0093\3\2\2\2\u0095")
        buf.write("\t\3\2\2\2\u0096\u0099\5\f\7\2\u0097\u0099\5\34\17\2\u0098")
        buf.write("\u0096\3\2\2\2\u0098\u0097\3\2\2\2\u0099\13\3\2\2\2\u009a")
        buf.write("\u009d\5\16\b\2\u009b\u009d\5\26\f\2\u009c\u009a\3\2\2")
        buf.write("\2\u009c\u009b\3\2\2\2\u009d\r\3\2\2\2\u009e\u00a1\5\20")
        buf.write("\t\2\u009f\u00a1\5\22\n\2\u00a0\u009e\3\2\2\2\u00a0\u009f")
        buf.write("\3\2\2\2\u00a1\17\3\2\2\2\u00a2\u00a3\7\30\2\2\u00a3\u00a4")
        buf.write("\5\24\13\2\u00a4\u00a5\7\61\2\2\u00a5\21\3\2\2\2\u00a6")
        buf.write("\u00a7\7\7\2\2\u00a7\u00a8\5\24\13\2\u00a8\u00a9\7\61")
        buf.write("\2\2\u00a9\23\3\2\2\2\u00aa\u00ab\5\30\r\2\u00ab\u00ac")
        buf.write("\7\62\2\2\u00ac\u00ad\58\35\2\u00ad\25\3\2\2\2\u00ae\u00af")
        buf.write("\t\2\2\2\u00af\u00b0\5\32\16\2\u00b0\u00b1\7\61\2\2\u00b1")
        buf.write("\27\3\2\2\2\u00b2\u00b3\5x=\2\u00b3\u00b4\7\60\2\2\u00b4")
        buf.write("\u00b5\5\30\r\2\u00b5\u00b8\3\2\2\2\u00b6\u00b8\5x=\2")
        buf.write("\u00b7\u00b2\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\31\3\2")
        buf.write("\2\2\u00b9\u00ba\5x=\2\u00ba\u00bb\7\60\2\2\u00bb\u00bc")
        buf.write("\5\32\16\2\u00bc\u00bd\7\60\2\2\u00bd\u00be\5> \2\u00be")
        buf.write("\u00c6\3\2\2\2\u00bf\u00c0\5x=\2\u00c0\u00c1\7\62\2\2")
        buf.write("\u00c1\u00c2\58\35\2\u00c2\u00c3\7\"\2\2\u00c3\u00c4\5")
        buf.write("> \2\u00c4\u00c6\3\2\2\2\u00c5\u00b9\3\2\2\2\u00c5\u00bf")
        buf.write("\3\2\2\2\u00c6\33\3\2\2\2\u00c7\u00c8\7\b\2\2\u00c8\u00c9")
        buf.write("\5x=\2\u00c9\u00ca\7+\2\2\u00ca\u00cb\5\36\20\2\u00cb")
        buf.write("\u00cc\7,\2\2\u00cc\u00cd\7\62\2\2\u00cd\u00ce\5\62\32")
        buf.write("\2\u00ce\u00cf\5r:\2\u00cf\u00d2\3\2\2\2\u00d0\u00d2\5")
        buf.write(".\30\2\u00d1\u00c7\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2\35")
        buf.write("\3\2\2\2\u00d3\u00d6\5 \21\2\u00d4\u00d6\5&\24\2\u00d5")
        buf.write("\u00d3\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6\37\3\2\2\2\u00d7")
        buf.write("\u00da\5\"\22\2\u00d8\u00da\3\2\2\2\u00d9\u00d7\3\2\2")
        buf.write("\2\u00d9\u00d8\3\2\2\2\u00da!\3\2\2\2\u00db\u00dc\5$\23")
        buf.write("\2\u00dc\u00dd\7\60\2\2\u00dd\u00de\5\"\22\2\u00de\u00e1")
        buf.write("\3\2\2\2\u00df\u00e1\5$\23\2\u00e0\u00db\3\2\2\2\u00e0")
        buf.write("\u00df\3\2\2\2\u00e1#\3\2\2\2\u00e2\u00e3\7\67\2\2\u00e3")
        buf.write("\u00e4\7\62\2\2\u00e4\u00e5\5\60\31\2\u00e5%\3\2\2\2\u00e6")
        buf.write("\u00e9\5(\25\2\u00e7\u00e9\3\2\2\2\u00e8\u00e6\3\2\2\2")
        buf.write("\u00e8\u00e7\3\2\2\2\u00e9\'\3\2\2\2\u00ea\u00eb\5*\26")
        buf.write("\2\u00eb\u00ec\7\60\2\2\u00ec\u00ed\5(\25\2\u00ed\u00f0")
        buf.write("\3\2\2\2\u00ee\u00f0\5*\26\2\u00ef\u00ea\3\2\2\2\u00ef")
        buf.write("\u00ee\3\2\2\2\u00f0)\3\2\2\2\u00f1\u00f4\5,\27\2\u00f2")
        buf.write("\u00f4\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2")
        buf.write("\u00f4\u00f5\3\2\2\2\u00f5\u00f6\7\62\2\2\u00f6\u00f7")
        buf.write("\5\60\31\2\u00f7+\3\2\2\2\u00f8\u00f9\7\67\2\2\u00f9\u00fa")
        buf.write("\7\60\2\2\u00fa\u00fd\5,\27\2\u00fb\u00fd\7\67\2\2\u00fc")
        buf.write("\u00f8\3\2\2\2\u00fc\u00fb\3\2\2\2\u00fd-\3\2\2\2\u00fe")
        buf.write("\u00ff\7\b\2\2\u00ff\u0100\7\27\2\2\u0100\u0101\7+\2\2")
        buf.write("\u0101\u0102\5\36\20\2\u0102\u0103\7,\2\2\u0103\u0104")
        buf.write("\5r:\2\u0104/\3\2\2\2\u0105\u0106\t\3\2\2\u0106\61\3\2")
        buf.write("\2\2\u0107\u0108\t\4\2\2\u0108\63\3\2\2\2\u0109\u010a")
        buf.write("\7-\2\2\u010a\u010b\79\2\2\u010b\u010c\7.\2\2\u010c\u010d")
        buf.write("\5\60\31\2\u010d\65\3\2\2\2\u010e\u010f\7\20\2\2\u010f")
        buf.write("\u0110\7\67\2\2\u0110\u0111\7-\2\2\u0111\u0112\7.\2\2")
        buf.write("\u0112\67\3\2\2\2\u0113\u0116\5\60\31\2\u0114\u0116\5")
        buf.write("\64\33\2\u0115\u0113\3\2\2\2\u0115\u0114\3\2\2\2\u0116")
        buf.write("9\3\2\2\2\u0117\u011a\5<\37\2\u0118\u011a\3\2\2\2\u0119")
        buf.write("\u0117\3\2\2\2\u0119\u0118\3\2\2\2\u011a;\3\2\2\2\u011b")
        buf.write("\u011c\5> \2\u011c\u011d\7\60\2\2\u011d\u011e\5<\37\2")
        buf.write("\u011e\u0121\3\2\2\2\u011f\u0121\5> \2\u0120\u011b\3\2")
        buf.write("\2\2\u0120\u011f\3\2\2\2\u0121=\3\2\2\2\u0122\u0123\5")
        buf.write("@!\2\u0123\u0124\7)\2\2\u0124\u0125\5@!\2\u0125\u0128")
        buf.write("\3\2\2\2\u0126\u0128\5@!\2\u0127\u0122\3\2\2\2\u0127\u0126")
        buf.write("\3\2\2\2\u0128?\3\2\2\2\u0129\u012a\5B\"\2\u012a\u012b")
        buf.write("\t\5\2\2\u012b\u012c\5B\"\2\u012c\u012f\3\2\2\2\u012d")
        buf.write("\u012f\5B\"\2\u012e\u0129\3\2\2\2\u012e\u012d\3\2\2\2")
        buf.write("\u012fA\3\2\2\2\u0130\u0131\b\"\1\2\u0131\u0132\5D#\2")
        buf.write("\u0132\u0138\3\2\2\2\u0133\u0134\f\4\2\2\u0134\u0135\t")
        buf.write("\6\2\2\u0135\u0137\5D#\2\u0136\u0133\3\2\2\2\u0137\u013a")
        buf.write("\3\2\2\2\u0138\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139")
        buf.write("C\3\2\2\2\u013a\u0138\3\2\2\2\u013b\u013c\b#\1\2\u013c")
        buf.write("\u013d\5F$\2\u013d\u0143\3\2\2\2\u013e\u013f\f\4\2\2\u013f")
        buf.write("\u0140\t\7\2\2\u0140\u0142\5F$\2\u0141\u013e\3\2\2\2\u0142")
        buf.write("\u0145\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2")
        buf.write("\u0144E\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u0147\b$\1\2")
        buf.write("\u0147\u0148\5H%\2\u0148\u014e\3\2\2\2\u0149\u014a\f\4")
        buf.write("\2\2\u014a\u014b\t\b\2\2\u014b\u014d\5H%\2\u014c\u0149")
        buf.write("\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014fG\3\2\2\2\u0150\u014e\3\2\2\2\u0151")
        buf.write("\u0152\7\36\2\2\u0152\u0155\5H%\2\u0153\u0155\5J&\2\u0154")
        buf.write("\u0151\3\2\2\2\u0154\u0153\3\2\2\2\u0155I\3\2\2\2\u0156")
        buf.write("\u0157\7\32\2\2\u0157\u015a\5J&\2\u0158\u015a\5L\'\2\u0159")
        buf.write("\u0156\3\2\2\2\u0159\u0158\3\2\2\2\u015aK\3\2\2\2\u015b")
        buf.write("\u015c\5N(\2\u015c\u015d\7-\2\2\u015d\u015e\5> \2\u015e")
        buf.write("\u015f\7.\2\2\u015f\u0162\3\2\2\2\u0160\u0162\5N(\2\u0161")
        buf.write("\u015b\3\2\2\2\u0161\u0160\3\2\2\2\u0162M\3\2\2\2\u0163")
        buf.write("\u0164\b(\1\2\u0164\u0165\5P)\2\u0165\u0172\3\2\2\2\u0166")
        buf.write("\u0167\f\4\2\2\u0167\u0168\7/\2\2\u0168\u016e\7\67\2\2")
        buf.write("\u0169\u016a\7+\2\2\u016a\u016b\5:\36\2\u016b\u016c\7")
        buf.write(",\2\2\u016c\u016f\3\2\2\2\u016d\u016f\3\2\2\2\u016e\u0169")
        buf.write("\3\2\2\2\u016e\u016d\3\2\2\2\u016f\u0171\3\2\2\2\u0170")
        buf.write("\u0166\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2")
        buf.write("\u0172\u0173\3\2\2\2\u0173O\3\2\2\2\u0174\u0172\3\2\2")
        buf.write("\2\u0175\u0176\7\67\2\2\u0176\u0179\7/\2\2\u0177\u0179")
        buf.write("\3\2\2\2\u0178\u0175\3\2\2\2\u0178\u0177\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017a\u0187\78\2\2\u017b\u017c\7\67\2\2")
        buf.write("\u017c\u017f\7/\2\2\u017d\u017f\3\2\2\2\u017e\u017b\3")
        buf.write("\2\2\2\u017e\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0181")
        buf.write("\78\2\2\u0181\u0182\7+\2\2\u0182\u0183\5:\36\2\u0183\u0184")
        buf.write("\7,\2\2\u0184\u0187\3\2\2\2\u0185\u0187\5R*\2\u0186\u0178")
        buf.write("\3\2\2\2\u0186\u017e\3\2\2\2\u0186\u0185\3\2\2\2\u0187")
        buf.write("Q\3\2\2\2\u0188\u0189\7\20\2\2\u0189\u018a\7\67\2\2\u018a")
        buf.write("\u018b\7+\2\2\u018b\u018c\5:\36\2\u018c\u018d\7,\2\2\u018d")
        buf.write("\u0190\3\2\2\2\u018e\u0190\5T+\2\u018f\u0188\3\2\2\2\u018f")
        buf.write("\u018e\3\2\2\2\u0190S\3\2\2\2\u0191\u0192\7+\2\2\u0192")
        buf.write("\u0193\5> \2\u0193\u0194\7,\2\2\u0194\u0197\3\2\2\2\u0195")
        buf.write("\u0197\5V,\2\u0196\u0191\3\2\2\2\u0196\u0195\3\2\2\2\u0197")
        buf.write("U\3\2\2\2\u0198\u019d\5X-\2\u0199\u019d\5|?\2\u019a\u019d")
        buf.write("\5x=\2\u019b\u019d\7\f\2\2\u019c\u0198\3\2\2\2\u019c\u0199")
        buf.write("\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019b\3\2\2\2\u019d")
        buf.write("W\3\2\2\2\u019e\u01a7\79\2\2\u019f\u01a7\7:\2\2\u01a0")
        buf.write("\u01a7\7;\2\2\u01a1\u01a7\7<\2\2\u01a2\u01a7\7\f\2\2\u01a3")
        buf.write("\u01a7\7\17\2\2\u01a4\u01a7\5|?\2\u01a5\u01a7\5x=\2\u01a6")
        buf.write("\u019e\3\2\2\2\u01a6\u019f\3\2\2\2\u01a6\u01a0\3\2\2\2")
        buf.write("\u01a6\u01a1\3\2\2\2\u01a6\u01a2\3\2\2\2\u01a6\u01a3\3")
        buf.write("\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7Y")
        buf.write("\3\2\2\2\u01a8\u01a9\5\f\7\2\u01a9[\3\2\2\2\u01aa\u01ab")
        buf.write("\5^\60\2\u01ab\u01ac\7\61\2\2\u01ac]\3\2\2\2\u01ad\u01ae")
        buf.write("\5`\61\2\u01ae\u01af\7(\2\2\u01af\u01b0\5> \2\u01b0_\3")
        buf.write("\2\2\2\u01b1\u01b9\7\67\2\2\u01b2\u01b9\5N(\2\u01b3\u01b4")
        buf.write("\7\67\2\2\u01b4\u01b5\7-\2\2\u01b5\u01b6\5> \2\u01b6\u01b7")
        buf.write("\7.\2\2\u01b7\u01b9\3\2\2\2\u01b8\u01b1\3\2\2\2\u01b8")
        buf.write("\u01b2\3\2\2\2\u01b8\u01b3\3\2\2\2\u01b9a\3\2\2\2\u01ba")
        buf.write("\u01bd\7\r\2\2\u01bb\u01be\5r:\2\u01bc\u01be\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01bd\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2")
        buf.write("\u01bf\u01c0\5> \2\u01c0\u01c4\5r:\2\u01c1\u01c2\7\21")
        buf.write("\2\2\u01c2\u01c5\5r:\2\u01c3\u01c5\3\2\2\2\u01c4\u01c1")
        buf.write("\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5c\3\2\2\2\u01c6\u01c7")
        buf.write("\7\25\2\2\u01c7\u01c8\5\\/\2\u01c8\u01c9\5> \2\u01c9\u01ca")
        buf.write("\7\61\2\2\u01ca\u01cb\5^\60\2\u01cb\u01cc\5r:\2\u01cc")
        buf.write("e\3\2\2\2\u01cd\u01ce\7\4\2\2\u01ce\u01cf\7\61\2\2\u01cf")
        buf.write("g\3\2\2\2\u01d0\u01d1\7\t\2\2\u01d1\u01d2\7\61\2\2\u01d2")
        buf.write("i\3\2\2\2\u01d3\u01d6\7\13\2\2\u01d4\u01d7\5> \2\u01d5")
        buf.write("\u01d7\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d5\3\2\2\2")
        buf.write("\u01d7\u01d8\3\2\2\2\u01d8\u01d9\7\61\2\2\u01d9k\3\2\2")
        buf.write("\2\u01da\u01df\5n8\2\u01db\u01dc\5p9\2\u01dc\u01dd\7\61")
        buf.write("\2\2\u01dd\u01df\3\2\2\2\u01de\u01da\3\2\2\2\u01de\u01db")
        buf.write("\3\2\2\2\u01dfm\3\2\2\2\u01e0\u01e1\5> \2\u01e1\u01e2")
        buf.write("\7/\2\2\u01e2\u01e3\7\67\2\2\u01e3\u01e4\7+\2\2\u01e4")
        buf.write("\u01e5\5:\36\2\u01e5\u01e6\7,\2\2\u01e6o\3\2\2\2\u01e7")
        buf.write("\u01e8\7\67\2\2\u01e8\u01eb\7/\2\2\u01e9\u01eb\3\2\2\2")
        buf.write("\u01ea\u01e7\3\2\2\2\u01ea\u01e9\3\2\2\2\u01eb\u01ec\3")
        buf.write("\2\2\2\u01ec\u01ed\78\2\2\u01ed\u01ee\7+\2\2\u01ee\u01ef")
        buf.write("\5:\36\2\u01ef\u01f0\7,\2\2\u01f0q\3\2\2\2\u01f1\u01f2")
        buf.write("\7\63\2\2\u01f2\u01f3\5t;\2\u01f3\u01f4\7\64\2\2\u01f4")
        buf.write("s\3\2\2\2\u01f5\u01f6\5v<\2\u01f6\u01f7\5t;\2\u01f7\u01fa")
        buf.write("\3\2\2\2\u01f8\u01fa\3\2\2\2\u01f9\u01f5\3\2\2\2\u01f9")
        buf.write("\u01f8\3\2\2\2\u01fau\3\2\2\2\u01fb\u0205\5Z.\2\u01fc")
        buf.write("\u0205\5\\/\2\u01fd\u0205\5b\62\2\u01fe\u0205\5d\63\2")
        buf.write("\u01ff\u0205\5f\64\2\u0200\u0205\5h\65\2\u0201\u0205\5")
        buf.write("j\66\2\u0202\u0205\5l\67\2\u0203\u0205\5r:\2\u0204\u01fb")
        buf.write("\3\2\2\2\u0204\u01fc\3\2\2\2\u0204\u01fd\3\2\2\2\u0204")
        buf.write("\u01fe\3\2\2\2\u0204\u01ff\3\2\2\2\u0204\u0200\3\2\2\2")
        buf.write("\u0204\u0201\3\2\2\2\u0204\u0202\3\2\2\2\u0204\u0203\3")
        buf.write("\2\2\2\u0205w\3\2\2\2\u0206\u0207\t\t\2\2\u0207y\3\2\2")
        buf.write("\2\u0208\u0209\7\67\2\2\u0209\u020c\7\3\2\2\u020a\u020c")
        buf.write("\3\2\2\2\u020b\u0208\3\2\2\2\u020b\u020a\3\2\2\2\u020c")
        buf.write("{\3\2\2\2\u020d\u020e\7-\2\2\u020e\u020f\5~@\2\u020f\u0210")
        buf.write("\7.\2\2\u0210}\3\2\2\2\u0211\u0212\5X-\2\u0212\u0213\7")
        buf.write("\60\2\2\u0213\u0214\5~@\2\u0214\u0217\3\2\2\2\u0215\u0217")
        buf.write("\5X-\2\u0216\u0211\3\2\2\2\u0216\u0215\3\2\2\2\u0217\177")
        buf.write("\3\2\2\2/\u0087\u0094\u0098\u009c\u00a0\u00b7\u00c5\u00d1")
        buf.write("\u00d5\u00d9\u00e0\u00e8\u00ef\u00f3\u00fc\u0115\u0119")
        buf.write("\u0120\u0127\u012e\u0138\u0143\u014e\u0154\u0159\u0161")
        buf.write("\u016e\u0172\u0178\u017e\u0186\u018f\u0196\u019c\u01a6")
        buf.write("\u01b8\u01bd\u01c4\u01d6\u01de\u01ea\u01f9\u0204\u020b")
        buf.write("\u0216")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<-'", "'break'", "'true'", "'string'", 
                     "'var'", "'func'", "'continue'", "'false'", "'return'", 
                     "'self'", "'if'", "'int'", "'null'", "'new'", "'else'", 
                     "'float'", "'class'", "'void'", "'for'", "'bool'", 
                     "'constructor'", "'const'", "'+'", "'-'", "'*'", "'/'", 
                     "'\\'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "':='", "'^'", "'%'", 
                     "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "BREAK", "TRUE", "STRING", 
                      "VAR", "FUNC", "CONTINUE", "FALSE", "RETURN", "SELF", 
                      "IF", "INT", "NULL", "NEW", "ELSE", "FLOAT", "CLASS", 
                      "VOID", "FOR", "BOOL", "CONSTRUCTOR", "CONST", "PLUS", 
                      "MINUS", "MULTIPLE", "DIVIDE_FLOAT", "DIVIDE_INT", 
                      "CHAMTHAN", "AND", "OR", "EQUAL", "DECLARE", "DIFFER", 
                      "SMOL", "SMOL_EQUAL", "BIG", "BIG_EQUAL", "ASSIGN", 
                      "CONCAT", "MOD", "LB", "RB", "LS", "RS", "DOT", "CM", 
                      "SM", "CL", "LC", "RC", "BLOCK_COMMENT", "LINE_COMMENT", 
                      "IDENTIFIER", "AT_ID", "INTLIT", "FLOATLIT", "BOOLLIT", 
                      "STRLIT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_declarelist = 1
    RULE_class_declare = 2
    RULE_list_of_member = 3
    RULE_member = 4
    RULE_attribute = 5
    RULE_attribute1 = 6
    RULE_attribute1const = 7
    RULE_attribute1var = 8
    RULE_attributedecl = 9
    RULE_attribute2 = 10
    RULE_list_of_attribute = 11
    RULE_list_of_a = 12
    RULE_method = 13
    RULE_list_of_param = 14
    RULE_list_of_param1 = 15
    RULE_primee = 16
    RULE_param_declare = 17
    RULE_list_of_param2 = 18
    RULE_primeme = 19
    RULE_list_of_identifier = 20
    RULE_primy = 21
    RULE_constructor = 22
    RULE_typee = 23
    RULE_typev = 24
    RULE_arr_type = 25
    RULE_class_type = 26
    RULE_typeorarrtype = 27
    RULE_list_of_exp = 28
    RULE_primu = 29
    RULE_exp = 30
    RULE_exp1 = 31
    RULE_exp2 = 32
    RULE_exp3 = 33
    RULE_exp4 = 34
    RULE_exp5 = 35
    RULE_exp6 = 36
    RULE_exp7 = 37
    RULE_exp8 = 38
    RULE_exp9 = 39
    RULE_exp10 = 40
    RULE_exp11 = 41
    RULE_exp12 = 42
    RULE_literal = 43
    RULE_var_const_statement = 44
    RULE_ass_statement = 45
    RULE_assex_statement = 46
    RULE_lhs = 47
    RULE_if_statement = 48
    RULE_for_statement = 49
    RULE_break_statement = 50
    RULE_continue_statement = 51
    RULE_return_statement = 52
    RULE_method_invocation_statement = 53
    RULE_instance_method_invocation = 54
    RULE_static_method_invocation = 55
    RULE_block_statement = 56
    RULE_list_of_statement = 57
    RULE_statement = 58
    RULE_xdd = 59
    RULE_superX = 60
    RULE_arrlit = 61
    RULE_arr = 62

    ruleNames =  [ "program", "class_declarelist", "class_declare", "list_of_member", 
                   "member", "attribute", "attribute1", "attribute1const", 
                   "attribute1var", "attributedecl", "attribute2", "list_of_attribute", 
                   "list_of_a", "method", "list_of_param", "list_of_param1", 
                   "primee", "param_declare", "list_of_param2", "primeme", 
                   "list_of_identifier", "primy", "constructor", "typee", 
                   "typev", "arr_type", "class_type", "typeorarrtype", "list_of_exp", 
                   "primu", "exp", "exp1", "exp2", "exp3", "exp4", "exp5", 
                   "exp6", "exp7", "exp8", "exp9", "exp10", "exp11", "exp12", 
                   "literal", "var_const_statement", "ass_statement", "assex_statement", 
                   "lhs", "if_statement", "for_statement", "break_statement", 
                   "continue_statement", "return_statement", "method_invocation_statement", 
                   "instance_method_invocation", "static_method_invocation", 
                   "block_statement", "list_of_statement", "statement", 
                   "xdd", "superX", "arrlit", "arr" ]

    EOF = Token.EOF
    T__0=1
    BREAK=2
    TRUE=3
    STRING=4
    VAR=5
    FUNC=6
    CONTINUE=7
    FALSE=8
    RETURN=9
    SELF=10
    IF=11
    INT=12
    NULL=13
    NEW=14
    ELSE=15
    FLOAT=16
    CLASS=17
    VOID=18
    FOR=19
    BOOL=20
    CONSTRUCTOR=21
    CONST=22
    PLUS=23
    MINUS=24
    MULTIPLE=25
    DIVIDE_FLOAT=26
    DIVIDE_INT=27
    CHAMTHAN=28
    AND=29
    OR=30
    EQUAL=31
    DECLARE=32
    DIFFER=33
    SMOL=34
    SMOL_EQUAL=35
    BIG=36
    BIG_EQUAL=37
    ASSIGN=38
    CONCAT=39
    MOD=40
    LB=41
    RB=42
    LS=43
    RS=44
    DOT=45
    CM=46
    SM=47
    CL=48
    LC=49
    RC=50
    BLOCK_COMMENT=51
    LINE_COMMENT=52
    IDENTIFIER=53
    AT_ID=54
    INTLIT=55
    FLOATLIT=56
    BOOLLIT=57
    STRLIT=58
    WS=59
    UNCLOSE_STRING=60
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

        def class_declarelist(self):
            return self.getTypedRuleContext(CSlangParser.Class_declarelistContext,0)


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
            self.class_declarelist()
            self.state = 127
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_declare(self):
            return self.getTypedRuleContext(CSlangParser.Class_declareContext,0)


        def class_declarelist(self):
            return self.getTypedRuleContext(CSlangParser.Class_declarelistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_declarelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declarelist" ):
                return visitor.visitClass_declarelist(self)
            else:
                return visitor.visitChildren(self)




    def class_declarelist(self):

        localctx = CSlangParser.Class_declarelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declarelist)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.class_declare()
                self.state = 130
                self.class_declarelist()
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


    class Class_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CSlangParser.CLASS, 0)

        def superX(self):
            return self.getTypedRuleContext(CSlangParser.SuperXContext,0)


        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def LC(self):
            return self.getToken(CSlangParser.LC, 0)

        def list_of_member(self):
            return self.getTypedRuleContext(CSlangParser.List_of_memberContext,0)


        def RC(self):
            return self.getToken(CSlangParser.RC, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_class_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declare" ):
                return visitor.visitClass_declare(self)
            else:
                return visitor.visitChildren(self)




    def class_declare(self):

        localctx = CSlangParser.Class_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(CSlangParser.CLASS)
            self.state = 136
            self.superX()
            self.state = 137
            self.match(CSlangParser.IDENTIFIER)
            self.state = 138
            self.match(CSlangParser.LC)
            self.state = 139
            self.list_of_member()
            self.state = 140
            self.match(CSlangParser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(CSlangParser.MemberContext,0)


        def list_of_member(self):
            return self.getTypedRuleContext(CSlangParser.List_of_memberContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_list_of_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_member" ):
                return visitor.visitList_of_member(self)
            else:
                return visitor.visitChildren(self)




    def list_of_member(self):

        localctx = CSlangParser.List_of_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_list_of_member)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.FUNC, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.member()
                self.state = 143
                self.list_of_member()
                pass
            elif token in [CSlangParser.RC]:
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

        def attribute(self):
            return self.getTypedRuleContext(CSlangParser.AttributeContext,0)


        def method(self):
            return self.getTypedRuleContext(CSlangParser.MethodContext,0)


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
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.attribute()
                pass
            elif token in [CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.method()
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


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute1(self):
            return self.getTypedRuleContext(CSlangParser.Attribute1Context,0)


        def attribute2(self):
            return self.getTypedRuleContext(CSlangParser.Attribute2Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = CSlangParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.attribute1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.attribute2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute1const(self):
            return self.getTypedRuleContext(CSlangParser.Attribute1constContext,0)


        def attribute1var(self):
            return self.getTypedRuleContext(CSlangParser.Attribute1varContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attribute1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute1" ):
                return visitor.visitAttribute1(self)
            else:
                return visitor.visitChildren(self)




    def attribute1(self):

        localctx = CSlangParser.Attribute1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute1)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.attribute1const()
                pass
            elif token in [CSlangParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.attribute1var()
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


    class Attribute1constContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def attributedecl(self):
            return self.getTypedRuleContext(CSlangParser.AttributedeclContext,0)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attribute1const

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute1const" ):
                return visitor.visitAttribute1const(self)
            else:
                return visitor.visitChildren(self)




    def attribute1const(self):

        localctx = CSlangParser.Attribute1constContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attribute1const)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(CSlangParser.CONST)
            self.state = 161
            self.attributedecl()
            self.state = 162
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute1varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def attributedecl(self):
            return self.getTypedRuleContext(CSlangParser.AttributedeclContext,0)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attribute1var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute1var" ):
                return visitor.visitAttribute1var(self)
            else:
                return visitor.visitChildren(self)




    def attribute1var(self):

        localctx = CSlangParser.Attribute1varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attribute1var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(CSlangParser.VAR)
            self.state = 165
            self.attributedecl()
            self.state = 166
            self.match(CSlangParser.SM)
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

        def list_of_attribute(self):
            return self.getTypedRuleContext(CSlangParser.List_of_attributeContext,0)


        def CL(self):
            return self.getToken(CSlangParser.CL, 0)

        def typeorarrtype(self):
            return self.getTypedRuleContext(CSlangParser.TypeorarrtypeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attributedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributedecl" ):
                return visitor.visitAttributedecl(self)
            else:
                return visitor.visitChildren(self)




    def attributedecl(self):

        localctx = CSlangParser.AttributedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attributedecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.list_of_attribute()
            self.state = 169
            self.match(CSlangParser.CL)
            self.state = 170
            self.typeorarrtype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_of_a(self):
            return self.getTypedRuleContext(CSlangParser.List_of_aContext,0)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_attribute2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute2" ):
                return visitor.visitAttribute2(self)
            else:
                return visitor.visitChildren(self)




    def attribute2(self):

        localctx = CSlangParser.Attribute2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attribute2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 173
            self.list_of_a()
            self.state = 174
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def xdd(self):
            return self.getTypedRuleContext(CSlangParser.XddContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def list_of_attribute(self):
            return self.getTypedRuleContext(CSlangParser.List_of_attributeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_list_of_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_attribute" ):
                return visitor.visitList_of_attribute(self)
            else:
                return visitor.visitChildren(self)




    def list_of_attribute(self):

        localctx = CSlangParser.List_of_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_of_attribute)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.xdd()
                self.state = 177
                self.match(CSlangParser.CM)
                self.state = 178
                self.list_of_attribute()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.xdd()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_aContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def xdd(self):
            return self.getTypedRuleContext(CSlangParser.XddContext,0)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def list_of_a(self):
            return self.getTypedRuleContext(CSlangParser.List_of_aContext,0)


        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def CL(self):
            return self.getToken(CSlangParser.CL, 0)

        def typeorarrtype(self):
            return self.getTypedRuleContext(CSlangParser.TypeorarrtypeContext,0)


        def DECLARE(self):
            return self.getToken(CSlangParser.DECLARE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_list_of_a

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_a" ):
                return visitor.visitList_of_a(self)
            else:
                return visitor.visitChildren(self)




    def list_of_a(self):

        localctx = CSlangParser.List_of_aContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_list_of_a)
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.xdd()
                self.state = 184
                self.match(CSlangParser.CM)
                self.state = 185
                self.list_of_a()
                self.state = 186
                self.match(CSlangParser.CM)
                self.state = 187
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.xdd()
                self.state = 190
                self.match(CSlangParser.CL)
                self.state = 191
                self.typeorarrtype()
                self.state = 192
                self.match(CSlangParser.DECLARE)
                self.state = 193
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def xdd(self):
            return self.getTypedRuleContext(CSlangParser.XddContext,0)


        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def list_of_param(self):
            return self.getTypedRuleContext(CSlangParser.List_of_paramContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def CL(self):
            return self.getToken(CSlangParser.CL, 0)

        def typev(self):
            return self.getTypedRuleContext(CSlangParser.TypevContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(CSlangParser.Block_statementContext,0)


        def constructor(self):
            return self.getTypedRuleContext(CSlangParser.ConstructorContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = CSlangParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_method)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(CSlangParser.FUNC)
                self.state = 198
                self.xdd()
                self.state = 199
                self.match(CSlangParser.LB)
                self.state = 200
                self.list_of_param()
                self.state = 201
                self.match(CSlangParser.RB)
                self.state = 202
                self.match(CSlangParser.CL)
                self.state = 203
                self.typev()
                self.state = 204
                self.block_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.constructor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_of_param1(self):
            return self.getTypedRuleContext(CSlangParser.List_of_param1Context,0)


        def list_of_param2(self):
            return self.getTypedRuleContext(CSlangParser.List_of_param2Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_list_of_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_param" ):
                return visitor.visitList_of_param(self)
            else:
                return visitor.visitChildren(self)




    def list_of_param(self):

        localctx = CSlangParser.List_of_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list_of_param)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.list_of_param1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.list_of_param2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_param1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primee(self):
            return self.getTypedRuleContext(CSlangParser.PrimeeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_list_of_param1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_param1" ):
                return visitor.visitList_of_param1(self)
            else:
                return visitor.visitChildren(self)




    def list_of_param1(self):

        localctx = CSlangParser.List_of_param1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_list_of_param1)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.primee()
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


    class PrimeeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_declare(self):
            return self.getTypedRuleContext(CSlangParser.Param_declareContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def primee(self):
            return self.getTypedRuleContext(CSlangParser.PrimeeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_primee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimee" ):
                return visitor.visitPrimee(self)
            else:
                return visitor.visitChildren(self)




    def primee(self):

        localctx = CSlangParser.PrimeeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_primee)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.param_declare()
                self.state = 218
                self.match(CSlangParser.CM)
                self.state = 219
                self.primee()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.param_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def CL(self):
            return self.getToken(CSlangParser.CL, 0)

        def typee(self):
            return self.getTypedRuleContext(CSlangParser.TypeeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_param_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_declare" ):
                return visitor.visitParam_declare(self)
            else:
                return visitor.visitChildren(self)




    def param_declare(self):

        localctx = CSlangParser.Param_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_param_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(CSlangParser.IDENTIFIER)
            self.state = 225
            self.match(CSlangParser.CL)
            self.state = 226
            self.typee()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_param2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primeme(self):
            return self.getTypedRuleContext(CSlangParser.PrimemeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_list_of_param2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_param2" ):
                return visitor.visitList_of_param2(self)
            else:
                return visitor.visitChildren(self)




    def list_of_param2(self):

        localctx = CSlangParser.List_of_param2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_list_of_param2)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CL, CSlangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.primeme()
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


    class PrimemeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_of_identifier(self):
            return self.getTypedRuleContext(CSlangParser.List_of_identifierContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def primeme(self):
            return self.getTypedRuleContext(CSlangParser.PrimemeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_primeme

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimeme" ):
                return visitor.visitPrimeme(self)
            else:
                return visitor.visitChildren(self)




    def primeme(self):

        localctx = CSlangParser.PrimemeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_primeme)
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.list_of_identifier()
                self.state = 233
                self.match(CSlangParser.CM)
                self.state = 234
                self.primeme()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.list_of_identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_identifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CL(self):
            return self.getToken(CSlangParser.CL, 0)

        def typee(self):
            return self.getTypedRuleContext(CSlangParser.TypeeContext,0)


        def primy(self):
            return self.getTypedRuleContext(CSlangParser.PrimyContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_list_of_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_identifier" ):
                return visitor.visitList_of_identifier(self)
            else:
                return visitor.visitChildren(self)




    def list_of_identifier(self):

        localctx = CSlangParser.List_of_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_list_of_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.IDENTIFIER]:
                self.state = 239
                self.primy()
                pass
            elif token in [CSlangParser.CL]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 243
            self.match(CSlangParser.CL)
            self.state = 244
            self.typee()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def primy(self):
            return self.getTypedRuleContext(CSlangParser.PrimyContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_primy

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimy" ):
                return visitor.visitPrimy(self)
            else:
                return visitor.visitChildren(self)




    def primy(self):

        localctx = CSlangParser.PrimyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_primy)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(CSlangParser.IDENTIFIER)
                self.state = 247
                self.match(CSlangParser.CM)
                self.state = 248
                self.primy()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.match(CSlangParser.IDENTIFIER)
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

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def list_of_param(self):
            return self.getTypedRuleContext(CSlangParser.List_of_paramContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def block_statement(self):
            return self.getTypedRuleContext(CSlangParser.Block_statementContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = CSlangParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(CSlangParser.FUNC)
            self.state = 253
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 254
            self.match(CSlangParser.LB)
            self.state = 255
            self.list_of_param()
            self.state = 256
            self.match(CSlangParser.RB)
            self.state = 257
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeeContext(ParserRuleContext):
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

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_typee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypee" ):
                return visitor.visitTypee(self)
            else:
                return visitor.visitChildren(self)




    def typee(self):

        localctx = CSlangParser.TypeeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_typee)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STRING) | (1 << CSlangParser.INT) | (1 << CSlangParser.FLOAT) | (1 << CSlangParser.BOOL) | (1 << CSlangParser.IDENTIFIER))) != 0)):
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


    class TypevContext(ParserRuleContext):
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

        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_typev

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypev" ):
                return visitor.visitTypev(self)
            else:
                return visitor.visitChildren(self)




    def typev(self):

        localctx = CSlangParser.TypevContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typev)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STRING) | (1 << CSlangParser.INT) | (1 << CSlangParser.FLOAT) | (1 << CSlangParser.VOID) | (1 << CSlangParser.BOOL) | (1 << CSlangParser.IDENTIFIER))) != 0)):
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


    class Arr_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(CSlangParser.LS, 0)

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def RS(self):
            return self.getToken(CSlangParser.RS, 0)

        def typee(self):
            return self.getTypedRuleContext(CSlangParser.TypeeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_arr_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_type" ):
                return visitor.visitArr_type(self)
            else:
                return visitor.visitChildren(self)




    def arr_type(self):

        localctx = CSlangParser.Arr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_arr_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(CSlangParser.LS)
            self.state = 264
            self.match(CSlangParser.INTLIT)
            self.state = 265
            self.match(CSlangParser.RS)
            self.state = 266
            self.typee()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def LS(self):
            return self.getToken(CSlangParser.LS, 0)

        def RS(self):
            return self.getToken(CSlangParser.RS, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = CSlangParser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(CSlangParser.NEW)
            self.state = 269
            self.match(CSlangParser.IDENTIFIER)
            self.state = 270
            self.match(CSlangParser.LS)
            self.state = 271
            self.match(CSlangParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeorarrtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typee(self):
            return self.getTypedRuleContext(CSlangParser.TypeeContext,0)


        def arr_type(self):
            return self.getTypedRuleContext(CSlangParser.Arr_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_typeorarrtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeorarrtype" ):
                return visitor.visitTypeorarrtype(self)
            else:
                return visitor.visitChildren(self)




    def typeorarrtype(self):

        localctx = CSlangParser.TypeorarrtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_typeorarrtype)
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.STRING, CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.typee()
                pass
            elif token in [CSlangParser.LS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.arr_type()
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


    class List_of_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primu(self):
            return self.getTypedRuleContext(CSlangParser.PrimuContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_list_of_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_exp" ):
                return visitor.visitList_of_exp(self)
            else:
                return visitor.visitChildren(self)




    def list_of_exp(self):

        localctx = CSlangParser.List_of_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_list_of_exp)
        try:
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SELF, CSlangParser.NULL, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.CHAMTHAN, CSlangParser.LB, CSlangParser.LS, CSlangParser.IDENTIFIER, CSlangParser.AT_ID, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.BOOLLIT, CSlangParser.STRLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.primu()
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


    class PrimuContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def primu(self):
            return self.getTypedRuleContext(CSlangParser.PrimuContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_primu

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimu" ):
                return visitor.visitPrimu(self)
            else:
                return visitor.visitChildren(self)




    def primu(self):

        localctx = CSlangParser.PrimuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_primu)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.exp()
                self.state = 282
                self.match(CSlangParser.CM)
                self.state = 283
                self.primu()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.exp()
                pass


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
        self.enterRule(localctx, 60, self.RULE_exp)
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.exp1()
                self.state = 289
                self.match(CSlangParser.CONCAT)
                self.state = 290
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
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


        def EQUAL(self):
            return self.getToken(CSlangParser.EQUAL, 0)

        def DIFFER(self):
            return self.getToken(CSlangParser.DIFFER, 0)

        def SMOL(self):
            return self.getToken(CSlangParser.SMOL, 0)

        def BIG(self):
            return self.getToken(CSlangParser.BIG, 0)

        def SMOL_EQUAL(self):
            return self.getToken(CSlangParser.SMOL_EQUAL, 0)

        def BIG_EQUAL(self):
            return self.getToken(CSlangParser.BIG_EQUAL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = CSlangParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.exp2(0)
                self.state = 296
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQUAL) | (1 << CSlangParser.DIFFER) | (1 << CSlangParser.SMOL) | (1 << CSlangParser.SMOL_EQUAL) | (1 << CSlangParser.BIG) | (1 << CSlangParser.BIG_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 297
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
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


        def AND(self):
            return self.getToken(CSlangParser.AND, 0)

        def OR(self):
            return self.getToken(CSlangParser.OR, 0)

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
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 310
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 305
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 306
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.AND or _la==CSlangParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 307
                    self.exp3(0) 
                self.state = 312
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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


        def PLUS(self):
            return self.getToken(CSlangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(CSlangParser.MINUS, 0)

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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 321
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 316
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 317
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.PLUS or _la==CSlangParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 318
                    self.exp4(0) 
                self.state = 323
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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


        def MULTIPLE(self):
            return self.getToken(CSlangParser.MULTIPLE, 0)

        def DIVIDE_FLOAT(self):
            return self.getToken(CSlangParser.DIVIDE_FLOAT, 0)

        def DIVIDE_INT(self):
            return self.getToken(CSlangParser.DIVIDE_INT, 0)

        def MOD(self):
            return self.getToken(CSlangParser.MOD, 0)

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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 332
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 327
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 328
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MULTIPLE) | (1 << CSlangParser.DIVIDE_FLOAT) | (1 << CSlangParser.DIVIDE_INT) | (1 << CSlangParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 329
                    self.exp5() 
                self.state = 334
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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

        def CHAMTHAN(self):
            return self.getToken(CSlangParser.CHAMTHAN, 0)

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
        self.enterRule(localctx, 70, self.RULE_exp5)
        try:
            self.state = 338
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CHAMTHAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.match(CSlangParser.CHAMTHAN)
                self.state = 336
                self.exp5()
                pass
            elif token in [CSlangParser.SELF, CSlangParser.NULL, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.LB, CSlangParser.LS, CSlangParser.IDENTIFIER, CSlangParser.AT_ID, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.BOOLLIT, CSlangParser.STRLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
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
        self.enterRule(localctx, 72, self.RULE_exp6)
        try:
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.match(CSlangParser.MINUS)
                self.state = 341
                self.exp6()
                pass
            elif token in [CSlangParser.SELF, CSlangParser.NULL, CSlangParser.NEW, CSlangParser.LB, CSlangParser.LS, CSlangParser.IDENTIFIER, CSlangParser.AT_ID, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.BOOLLIT, CSlangParser.STRLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
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


        def LS(self):
            return self.getToken(CSlangParser.LS, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def RS(self):
            return self.getToken(CSlangParser.RS, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = CSlangParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp7)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.exp8(0)
                self.state = 346
                self.match(CSlangParser.LS)
                self.state = 347
                self.exp()
                self.state = 348
                self.match(CSlangParser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
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

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def list_of_exp(self):
            return self.getTypedRuleContext(CSlangParser.List_of_expContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 368
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 356
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 357
                    self.match(CSlangParser.DOT)
                    self.state = 358
                    self.match(CSlangParser.IDENTIFIER)
                    self.state = 364
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        self.state = 359
                        self.match(CSlangParser.LB)
                        self.state = 360
                        self.list_of_exp()
                        self.state = 361
                        self.match(CSlangParser.RB)
                        pass

                    elif la_ == 2:
                        pass

             
                self.state = 370
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def list_of_exp(self):
            return self.getTypedRuleContext(CSlangParser.List_of_expContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

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
        self.enterRule(localctx, 78, self.RULE_exp9)
        try:
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.IDENTIFIER]:
                    self.state = 371
                    self.match(CSlangParser.IDENTIFIER)
                    self.state = 372
                    self.match(CSlangParser.DOT)
                    pass
                elif token in [CSlangParser.AT_ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 376
                self.match(CSlangParser.AT_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.IDENTIFIER]:
                    self.state = 377
                    self.match(CSlangParser.IDENTIFIER)
                    self.state = 378
                    self.match(CSlangParser.DOT)
                    pass
                elif token in [CSlangParser.AT_ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 382
                self.match(CSlangParser.AT_ID)
                self.state = 383
                self.match(CSlangParser.LB)
                self.state = 384
                self.list_of_exp()
                self.state = 385
                self.match(CSlangParser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 387
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

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def list_of_exp(self):
            return self.getTypedRuleContext(CSlangParser.List_of_expContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

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
        self.enterRule(localctx, 80, self.RULE_exp10)
        try:
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.match(CSlangParser.NEW)
                self.state = 391
                self.match(CSlangParser.IDENTIFIER)
                self.state = 392
                self.match(CSlangParser.LB)
                self.state = 393
                self.list_of_exp()
                self.state = 394
                self.match(CSlangParser.RB)
                pass
            elif token in [CSlangParser.SELF, CSlangParser.NULL, CSlangParser.LB, CSlangParser.LS, CSlangParser.IDENTIFIER, CSlangParser.AT_ID, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.BOOLLIT, CSlangParser.STRLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
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

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

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
        self.enterRule(localctx, 82, self.RULE_exp11)
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.match(CSlangParser.LB)
                self.state = 400
                self.exp()
                self.state = 401
                self.match(CSlangParser.RB)
                pass
            elif token in [CSlangParser.SELF, CSlangParser.NULL, CSlangParser.LS, CSlangParser.IDENTIFIER, CSlangParser.AT_ID, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.BOOLLIT, CSlangParser.STRLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
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


        def arrlit(self):
            return self.getTypedRuleContext(CSlangParser.ArrlitContext,0)


        def xdd(self):
            return self.getTypedRuleContext(CSlangParser.XddContext,0)


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
        self.enterRule(localctx, 84, self.RULE_exp12)
        try:
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.arrlit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 408
                self.xdd()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 409
                self.match(CSlangParser.SELF)
                pass


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

        def BOOLLIT(self):
            return self.getToken(CSlangParser.BOOLLIT, 0)

        def STRLIT(self):
            return self.getToken(CSlangParser.STRLIT, 0)

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def NULL(self):
            return self.getToken(CSlangParser.NULL, 0)

        def arrlit(self):
            return self.getTypedRuleContext(CSlangParser.ArrlitContext,0)


        def xdd(self):
            return self.getTypedRuleContext(CSlangParser.XddContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CSlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_literal)
        try:
            self.state = 420
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
                self.match(CSlangParser.BOOLLIT)
                pass
            elif token in [CSlangParser.STRLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 415
                self.match(CSlangParser.STRLIT)
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 416
                self.match(CSlangParser.SELF)
                pass
            elif token in [CSlangParser.NULL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 417
                self.match(CSlangParser.NULL)
                pass
            elif token in [CSlangParser.LS]:
                self.enterOuterAlt(localctx, 7)
                self.state = 418
                self.arrlit()
                pass
            elif token in [CSlangParser.IDENTIFIER, CSlangParser.AT_ID]:
                self.enterOuterAlt(localctx, 8)
                self.state = 419
                self.xdd()
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


    class Var_const_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(CSlangParser.AttributeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_var_const_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_const_statement" ):
                return visitor.visitVar_const_statement(self)
            else:
                return visitor.visitChildren(self)




    def var_const_statement(self):

        localctx = CSlangParser.Var_const_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_var_const_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.attribute()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ass_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assex_statement(self):
            return self.getTypedRuleContext(CSlangParser.Assex_statementContext,0)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_ass_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAss_statement" ):
                return visitor.visitAss_statement(self)
            else:
                return visitor.visitChildren(self)




    def ass_statement(self):

        localctx = CSlangParser.Ass_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_ass_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.assex_statement()
            self.state = 425
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assex_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(CSlangParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_assex_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssex_statement" ):
                return visitor.visitAssex_statement(self)
            else:
                return visitor.visitChildren(self)




    def assex_statement(self):

        localctx = CSlangParser.Assex_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_assex_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.lhs()
            self.state = 428
            self.match(CSlangParser.ASSIGN)
            self.state = 429
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def exp8(self):
            return self.getTypedRuleContext(CSlangParser.Exp8Context,0)


        def LS(self):
            return self.getToken(CSlangParser.LS, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def RS(self):
            return self.getToken(CSlangParser.RS, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = CSlangParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_lhs)
        try:
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.match(CSlangParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.exp8(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 433
                self.match(CSlangParser.IDENTIFIER)
                self.state = 434
                self.match(CSlangParser.LS)
                self.state = 435
                self.exp()
                self.state = 436
                self.match(CSlangParser.RS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSlangParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def block_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Block_statementContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Block_statementContext,i)


        def ELSE(self):
            return self.getToken(CSlangParser.ELSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = CSlangParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(CSlangParser.IF)
            self.state = 443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LC]:
                self.state = 441
                self.block_statement()
                pass
            elif token in [CSlangParser.SELF, CSlangParser.NULL, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.CHAMTHAN, CSlangParser.LB, CSlangParser.LS, CSlangParser.IDENTIFIER, CSlangParser.AT_ID, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.BOOLLIT, CSlangParser.STRLIT]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 445
            self.exp()
            self.state = 446
            self.block_statement()
            self.state = 450
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ELSE]:
                self.state = 447
                self.match(CSlangParser.ELSE)
                self.state = 448
                self.block_statement()
                pass
            elif token in [CSlangParser.BREAK, CSlangParser.VAR, CSlangParser.CONTINUE, CSlangParser.RETURN, CSlangParser.SELF, CSlangParser.IF, CSlangParser.NULL, CSlangParser.NEW, CSlangParser.FOR, CSlangParser.CONST, CSlangParser.MINUS, CSlangParser.CHAMTHAN, CSlangParser.LB, CSlangParser.LS, CSlangParser.LC, CSlangParser.RC, CSlangParser.IDENTIFIER, CSlangParser.AT_ID, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.BOOLLIT, CSlangParser.STRLIT]:
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


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSlangParser.FOR, 0)

        def ass_statement(self):
            return self.getTypedRuleContext(CSlangParser.Ass_statementContext,0)


        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def assex_statement(self):
            return self.getTypedRuleContext(CSlangParser.Assex_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(CSlangParser.Block_statementContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = CSlangParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(CSlangParser.FOR)
            self.state = 453
            self.ass_statement()
            self.state = 454
            self.exp()
            self.state = 455
            self.match(CSlangParser.SM)
            self.state = 456
            self.assex_statement()
            self.state = 457
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CSlangParser.BREAK, 0)

        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = CSlangParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(CSlangParser.BREAK)
            self.state = 460
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(CSlangParser.CONTINUE, 0)

        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = CSlangParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(CSlangParser.CONTINUE)
            self.state = 463
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
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
            return CSlangParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = CSlangParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.match(CSlangParser.RETURN)
            self.state = 468
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SELF, CSlangParser.NULL, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.CHAMTHAN, CSlangParser.LB, CSlangParser.LS, CSlangParser.IDENTIFIER, CSlangParser.AT_ID, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.BOOLLIT, CSlangParser.STRLIT]:
                self.state = 466
                self.exp()
                pass
            elif token in [CSlangParser.SM]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 470
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_method_invocation(self):
            return self.getTypedRuleContext(CSlangParser.Instance_method_invocationContext,0)


        def static_method_invocation(self):
            return self.getTypedRuleContext(CSlangParser.Static_method_invocationContext,0)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_method_invocation_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_statement" ):
                return visitor.visitMethod_invocation_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_statement(self):

        localctx = CSlangParser.Method_invocation_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_method_invocation_statement)
        try:
            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.instance_method_invocation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 473
                self.static_method_invocation()
                self.state = 474
                self.match(CSlangParser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(CSlangParser.ExpContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def list_of_exp(self):
            return self.getTypedRuleContext(CSlangParser.List_of_expContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_instance_method_invocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_invocation" ):
                return visitor.visitInstance_method_invocation(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_invocation(self):

        localctx = CSlangParser.Instance_method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_instance_method_invocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.exp()
            self.state = 479
            self.match(CSlangParser.DOT)
            self.state = 480
            self.match(CSlangParser.IDENTIFIER)
            self.state = 481
            self.match(CSlangParser.LB)
            self.state = 482
            self.list_of_exp()
            self.state = 483
            self.match(CSlangParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def list_of_exp(self):
            return self.getTypedRuleContext(CSlangParser.List_of_expContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_static_method_invocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_invocation" ):
                return visitor.visitStatic_method_invocation(self)
            else:
                return visitor.visitChildren(self)




    def static_method_invocation(self):

        localctx = CSlangParser.Static_method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_static_method_invocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.IDENTIFIER]:
                self.state = 485
                self.match(CSlangParser.IDENTIFIER)
                self.state = 486
                self.match(CSlangParser.DOT)
                pass
            elif token in [CSlangParser.AT_ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 490
            self.match(CSlangParser.AT_ID)
            self.state = 491
            self.match(CSlangParser.LB)
            self.state = 492
            self.list_of_exp()
            self.state = 493
            self.match(CSlangParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LC(self):
            return self.getToken(CSlangParser.LC, 0)

        def list_of_statement(self):
            return self.getTypedRuleContext(CSlangParser.List_of_statementContext,0)


        def RC(self):
            return self.getToken(CSlangParser.RC, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = CSlangParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(CSlangParser.LC)
            self.state = 496
            self.list_of_statement()
            self.state = 497
            self.match(CSlangParser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(CSlangParser.StatementContext,0)


        def list_of_statement(self):
            return self.getTypedRuleContext(CSlangParser.List_of_statementContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_list_of_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_statement" ):
                return visitor.visitList_of_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_of_statement(self):

        localctx = CSlangParser.List_of_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_list_of_statement)
        try:
            self.state = 503
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.BREAK, CSlangParser.VAR, CSlangParser.CONTINUE, CSlangParser.RETURN, CSlangParser.SELF, CSlangParser.IF, CSlangParser.NULL, CSlangParser.NEW, CSlangParser.FOR, CSlangParser.CONST, CSlangParser.MINUS, CSlangParser.CHAMTHAN, CSlangParser.LB, CSlangParser.LS, CSlangParser.LC, CSlangParser.IDENTIFIER, CSlangParser.AT_ID, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.BOOLLIT, CSlangParser.STRLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.statement()
                self.state = 500
                self.list_of_statement()
                pass
            elif token in [CSlangParser.RC]:
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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_const_statement(self):
            return self.getTypedRuleContext(CSlangParser.Var_const_statementContext,0)


        def ass_statement(self):
            return self.getTypedRuleContext(CSlangParser.Ass_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(CSlangParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(CSlangParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(CSlangParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(CSlangParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(CSlangParser.Return_statementContext,0)


        def method_invocation_statement(self):
            return self.getTypedRuleContext(CSlangParser.Method_invocation_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(CSlangParser.Block_statementContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CSlangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_statement)
        try:
            self.state = 514
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 505
                self.var_const_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 506
                self.ass_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 507
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 508
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 509
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 510
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 511
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 512
                self.method_invocation_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 513
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class XddContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_xdd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitXdd" ):
                return visitor.visitXdd(self)
            else:
                return visitor.visitChildren(self)




    def xdd(self):

        localctx = CSlangParser.XddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_xdd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            _la = self._input.LA(1)
            if not(_la==CSlangParser.IDENTIFIER or _la==CSlangParser.AT_ID):
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


    class SuperXContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_superX

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuperX" ):
                return visitor.visitSuperX(self)
            else:
                return visitor.visitChildren(self)




    def superX(self):

        localctx = CSlangParser.SuperXContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_superX)
        try:
            self.state = 521
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.match(CSlangParser.IDENTIFIER)
                self.state = 519
                self.match(CSlangParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(CSlangParser.LS, 0)

        def arr(self):
            return self.getTypedRuleContext(CSlangParser.ArrContext,0)


        def RS(self):
            return self.getToken(CSlangParser.RS, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_arrlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrlit" ):
                return visitor.visitArrlit(self)
            else:
                return visitor.visitChildren(self)




    def arrlit(self):

        localctx = CSlangParser.ArrlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_arrlit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(CSlangParser.LS)
            self.state = 524
            self.arr()
            self.state = 525
            self.match(CSlangParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(CSlangParser.LiteralContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def arr(self):
            return self.getTypedRuleContext(CSlangParser.ArrContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr" ):
                return visitor.visitArr(self)
            else:
                return visitor.visitChildren(self)




    def arr(self):

        localctx = CSlangParser.ArrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_arr)
        try:
            self.state = 532
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 527
                self.literal()
                self.state = 528
                self.match(CSlangParser.CM)
                self.state = 529
                self.arr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 531
                self.literal()
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
        self._predicates[32] = self.exp2_sempred
        self._predicates[33] = self.exp3_sempred
        self._predicates[34] = self.exp4_sempred
        self._predicates[38] = self.exp8_sempred
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
         




