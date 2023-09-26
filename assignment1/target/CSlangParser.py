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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u0218\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\6\2\u0082\n\2\r\2")
        buf.write("\16\2\u0083\3\2\3\2\3\3\3\3\5\3\u008a\n\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\5\4\u0095\n\4\3\5\3\5\5\5\u0099")
        buf.write("\n\5\3\6\3\6\5\6\u009d\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\5\n\u00b7\n\n\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u00bd\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\5\r\u00ca\n\r\3\16\3\16\5\16\u00ce\n\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00da\n\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\5\20\u00e7\n\20\3\21\3\21\5\21\u00eb\n\21\3\22\3\22\3")
        buf.write("\22\3\22\5\22\u00f1\n\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25\u0102")
        buf.write("\n\25\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u010e\n\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0116")
        buf.write("\n\30\5\30\u0118\n\30\3\31\3\31\3\31\3\31\3\31\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\5\33\u0129")
        buf.write("\n\33\3\34\3\34\5\34\u012d\n\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\5\35\u0134\n\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\3\"\5\"\u0143\n\"\3#\3#\3#\3#\3#\5#\u014a")
        buf.write("\n#\3$\3$\3$\3$\3$\3$\3$\7$\u0153\n$\f$\16$\u0156\13$")
        buf.write("\3%\3%\3%\3%\3%\3%\3%\7%\u015f\n%\f%\16%\u0162\13%\3&")
        buf.write("\3&\3&\3&\3&\3&\3&\7&\u016b\n&\f&\16&\u016e\13&\3\'\3")
        buf.write("\'\3\'\5\'\u0173\n\'\3(\3(\3(\5(\u0178\n(\3)\3)\3)\3)")
        buf.write("\3)\3)\5)\u0180\n)\3*\3*\3*\3*\3*\3*\7*\u0188\n*\f*\16")
        buf.write("*\u018b\13*\3+\3+\3+\3+\3+\5+\u0192\n+\3,\3,\3,\3,\3,")
        buf.write("\3,\3,\5,\u019b\n,\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\5")
        buf.write(".\u01a8\n.\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u01b3\n/\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\61\3\61\5\61\u01bc\n\61\3\61\3")
        buf.write("\61\3\61\3\61\5\61\u01c2\n\61\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\67\3\67\5\67\u01db\n\67\3")
        buf.write("\67\3\67\3\67\38\38\38\38\38\39\39\59\u01e7\n9\39\39\3")
        buf.write("9\3:\3:\3:\3:\3;\3;\3;\3;\5;\u01f4\n;\3<\3<\5<\u01f8\n")
        buf.write("<\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\3?\3?\5?\u0210\n?\3@\3@\3@\3@\5@\u0216\n@\3@\2")
        buf.write("\6FHJRA\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(",.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\2")
        buf.write("\n\4\2\23\23\27\27\3\2\13\16\3\2;<\3\2\t\n\5\2  \"$\'")
        buf.write("(\3\2\36\37\3\2\31\32\4\2\33\35**\2\u0208\2\u0081\3\2")
        buf.write("\2\2\4\u0087\3\2\2\2\6\u0094\3\2\2\2\b\u0098\3\2\2\2\n")
        buf.write("\u009c\3\2\2\2\f\u009e\3\2\2\2\16\u00a4\3\2\2\2\20\u00a8")
        buf.write("\3\2\2\2\22\u00b6\3\2\2\2\24\u00bc\3\2\2\2\26\u00be\3")
        buf.write("\2\2\2\30\u00c9\3\2\2\2\32\u00cd\3\2\2\2\34\u00d9\3\2")
        buf.write("\2\2\36\u00e6\3\2\2\2 \u00ea\3\2\2\2\"\u00f0\3\2\2\2$")
        buf.write("\u00f2\3\2\2\2&\u00f9\3\2\2\2(\u0101\3\2\2\2*\u0103\3")
        buf.write("\2\2\2,\u0105\3\2\2\2.\u0117\3\2\2\2\60\u0119\3\2\2\2")
        buf.write("\62\u011e\3\2\2\2\64\u0128\3\2\2\2\66\u012c\3\2\2\28\u0133")
        buf.write("\3\2\2\2:\u0135\3\2\2\2<\u0137\3\2\2\2>\u0139\3\2\2\2")
        buf.write("@\u013b\3\2\2\2B\u0142\3\2\2\2D\u0149\3\2\2\2F\u014b\3")
        buf.write("\2\2\2H\u0157\3\2\2\2J\u0163\3\2\2\2L\u0172\3\2\2\2N\u0177")
        buf.write("\3\2\2\2P\u017f\3\2\2\2R\u0181\3\2\2\2T\u0191\3\2\2\2")
        buf.write("V\u019a\3\2\2\2X\u019c\3\2\2\2Z\u019e\3\2\2\2\\\u01a9")
        buf.write("\3\2\2\2^\u01b4\3\2\2\2`\u01b9\3\2\2\2b\u01c3\3\2\2\2")
        buf.write("d\u01c9\3\2\2\2f\u01cc\3\2\2\2h\u01cf\3\2\2\2j\u01d3\3")
        buf.write("\2\2\2l\u01da\3\2\2\2n\u01df\3\2\2\2p\u01e6\3\2\2\2r\u01eb")
        buf.write("\3\2\2\2t\u01f3\3\2\2\2v\u01f7\3\2\2\2x\u01f9\3\2\2\2")
        buf.write("z\u01ff\3\2\2\2|\u020f\3\2\2\2~\u0215\3\2\2\2\u0080\u0082")
        buf.write("\5\4\3\2\u0081\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083")
        buf.write("\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0085\3\2\2\2")
        buf.write("\u0085\u0086\7\2\2\3\u0086\3\3\2\2\2\u0087\u0089\7\21")
        buf.write("\2\2\u0088\u008a\5&\24\2\u0089\u0088\3\2\2\2\u0089\u008a")
        buf.write("\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\7;\2\2\u008c")
        buf.write("\u008d\7\63\2\2\u008d\u008e\5\6\4\2\u008e\u008f\7\64\2")
        buf.write("\2\u008f\5\3\2\2\2\u0090\u0091\5\b\5\2\u0091\u0092\5\6")
        buf.write("\4\2\u0092\u0095\3\2\2\2\u0093\u0095\3\2\2\2\u0094\u0090")
        buf.write("\3\2\2\2\u0094\u0093\3\2\2\2\u0095\7\3\2\2\2\u0096\u0099")
        buf.write("\5\n\6\2\u0097\u0099\5\26\f\2\u0098\u0096\3\2\2\2\u0098")
        buf.write("\u0097\3\2\2\2\u0099\t\3\2\2\2\u009a\u009d\5\16\b\2\u009b")
        buf.write("\u009d\5\f\7\2\u009c\u009a\3\2\2\2\u009c\u009b\3\2\2\2")
        buf.write("\u009d\13\3\2\2\2\u009e\u009f\t\2\2\2\u009f\u00a0\5\24")
        buf.write("\13\2\u00a0\u00a1\7\62\2\2\u00a1\u00a2\5\20\t\2\u00a2")
        buf.write("\u00a3\7\61\2\2\u00a3\r\3\2\2\2\u00a4\u00a5\t\2\2\2\u00a5")
        buf.write("\u00a6\5\22\n\2\u00a6\u00a7\7\61\2\2\u00a7\17\3\2\2\2")
        buf.write("\u00a8\u00a9\t\3\2\2\u00a9\21\3\2\2\2\u00aa\u00ab\7:\2")
        buf.write("\2\u00ab\u00ac\7\60\2\2\u00ac\u00ad\5\22\n\2\u00ad\u00ae")
        buf.write("\7\60\2\2\u00ae\u00af\5B\"\2\u00af\u00b7\3\2\2\2\u00b0")
        buf.write("\u00b1\7:\2\2\u00b1\u00b2\7\62\2\2\u00b2\u00b3\5\20\t")
        buf.write("\2\u00b3\u00b4\7&\2\2\u00b4\u00b5\5B\"\2\u00b5\u00b7\3")
        buf.write("\2\2\2\u00b6\u00aa\3\2\2\2\u00b6\u00b0\3\2\2\2\u00b7\23")
        buf.write("\3\2\2\2\u00b8\u00b9\7:\2\2\u00b9\u00ba\7\60\2\2\u00ba")
        buf.write("\u00bd\5\24\13\2\u00bb\u00bd\7:\2\2\u00bc\u00b8\3\2\2")
        buf.write("\2\u00bc\u00bb\3\2\2\2\u00bd\25\3\2\2\2\u00be\u00bf\7")
        buf.write("\30\2\2\u00bf\u00c0\t\4\2\2\u00c0\u00c1\7+\2\2\u00c1\u00c2")
        buf.write("\5\30\r\2\u00c2\u00c3\7,\2\2\u00c3\u00c4\7\62\2\2\u00c4")
        buf.write("\u00c5\5\20\t\2\u00c5\u00c6\5r:\2\u00c6\27\3\2\2\2\u00c7")
        buf.write("\u00ca\5\32\16\2\u00c8\u00ca\3\2\2\2\u00c9\u00c7\3\2\2")
        buf.write("\2\u00c9\u00c8\3\2\2\2\u00ca\31\3\2\2\2\u00cb\u00ce\5")
        buf.write("\34\17\2\u00cc\u00ce\5\36\20\2\u00cd\u00cb\3\2\2\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00ce\33\3\2\2\2\u00cf\u00d0\7:\2\2\u00d0")
        buf.write("\u00d1\7\62\2\2\u00d1\u00d2\5\20\t\2\u00d2\u00d3\3\2\2")
        buf.write("\2\u00d3\u00d4\7\60\2\2\u00d4\u00d5\5\34\17\2\u00d5\u00da")
        buf.write("\3\2\2\2\u00d6\u00d7\7:\2\2\u00d7\u00d8\7\62\2\2\u00d8")
        buf.write("\u00da\5\20\t\2\u00d9\u00cf\3\2\2\2\u00d9\u00d6\3\2\2")
        buf.write("\2\u00da\35\3\2\2\2\u00db\u00dc\5 \21\2\u00dc\u00dd\7")
        buf.write("\62\2\2\u00dd\u00de\5\20\t\2\u00de\u00df\3\2\2\2\u00df")
        buf.write("\u00e0\7\60\2\2\u00e0\u00e1\5\36\20\2\u00e1\u00e7\3\2")
        buf.write("\2\2\u00e2\u00e3\5 \21\2\u00e3\u00e4\7\62\2\2\u00e4\u00e5")
        buf.write("\5\20\t\2\u00e5\u00e7\3\2\2\2\u00e6\u00db\3\2\2\2\u00e6")
        buf.write("\u00e2\3\2\2\2\u00e7\37\3\2\2\2\u00e8\u00eb\5\"\22\2\u00e9")
        buf.write("\u00eb\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00e9\3\2\2\2")
        buf.write("\u00eb!\3\2\2\2\u00ec\u00ed\7:\2\2\u00ed\u00ee\7\60\2")
        buf.write("\2\u00ee\u00f1\5\"\22\2\u00ef\u00f1\7:\2\2\u00f0\u00ec")
        buf.write("\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1#\3\2\2\2\u00f2\u00f3")
        buf.write("\7\30\2\2\u00f3\u00f4\7\22\2\2\u00f4\u00f5\7+\2\2\u00f5")
        buf.write("\u00f6\5\30\r\2\u00f6\u00f7\7,\2\2\u00f7\u00f8\5r:\2\u00f8")
        buf.write("%\3\2\2\2\u00f9\u00fa\7:\2\2\u00fa\u00fb\7\3\2\2\u00fb")
        buf.write("\'\3\2\2\2\u00fc\u0102\7\65\2\2\u00fd\u0102\7\66\2\2\u00fe")
        buf.write("\u0102\5*\26\2\u00ff\u0102\7\67\2\2\u0100\u0102\5,\27")
        buf.write("\2\u0101\u00fc\3\2\2\2\u0101\u00fd\3\2\2\2\u0101\u00fe")
        buf.write("\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0100\3\2\2\2\u0102")
        buf.write(")\3\2\2\2\u0103\u0104\t\5\2\2\u0104+\3\2\2\2\u0105\u0106")
        buf.write("\7-\2\2\u0106\u0107\5.\30\2\u0107\u0108\7.\2\2\u0108-")
        buf.write("\3\2\2\2\u0109\u010e\7\65\2\2\u010a\u010e\7\66\2\2\u010b")
        buf.write("\u010e\5*\26\2\u010c\u010e\7\67\2\2\u010d\u0109\3\2\2")
        buf.write("\2\u010d\u010a\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010c")
        buf.write("\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0110\7\60\2\2\u0110")
        buf.write("\u0118\5.\30\2\u0111\u0116\7\65\2\2\u0112\u0116\7\66\2")
        buf.write("\2\u0113\u0116\5*\26\2\u0114\u0116\7\67\2\2\u0115\u0111")
        buf.write("\3\2\2\2\u0115\u0112\3\2\2\2\u0115\u0113\3\2\2\2\u0115")
        buf.write("\u0114\3\2\2\2\u0116\u0118\3\2\2\2\u0117\u010d\3\2\2\2")
        buf.write("\u0117\u0115\3\2\2\2\u0118/\3\2\2\2\u0119\u011a\7-\2\2")
        buf.write("\u011a\u011b\7=\2\2\u011b\u011c\7.\2\2\u011c\u011d\5\20")
        buf.write("\t\2\u011d\61\3\2\2\2\u011e\u011f\7\25\2\2\u011f\u0120")
        buf.write("\7:\2\2\u0120\u0121\7+\2\2\u0121\u0122\7,\2\2\u0122\63")
        buf.write("\3\2\2\2\u0123\u0124\5B\"\2\u0124\u0125\7\60\2\2\u0125")
        buf.write("\u0126\5\64\33\2\u0126\u0129\3\2\2\2\u0127\u0129\5B\"")
        buf.write("\2\u0128\u0123\3\2\2\2\u0128\u0127\3\2\2\2\u0129\65\3")
        buf.write("\2\2\2\u012a\u012d\58\35\2\u012b\u012d\3\2\2\2\u012c\u012a")
        buf.write("\3\2\2\2\u012c\u012b\3\2\2\2\u012d\67\3\2\2\2\u012e\u012f")
        buf.write("\5B\"\2\u012f\u0130\7\60\2\2\u0130\u0131\58\35\2\u0131")
        buf.write("\u0134\3\2\2\2\u0132\u0134\5B\"\2\u0133\u012e\3\2\2\2")
        buf.write("\u0133\u0132\3\2\2\2\u01349\3\2\2\2\u0135\u0136\t\6\2")
        buf.write("\2\u0136;\3\2\2\2\u0137\u0138\t\7\2\2\u0138=\3\2\2\2\u0139")
        buf.write("\u013a\t\b\2\2\u013a?\3\2\2\2\u013b\u013c\t\t\2\2\u013c")
        buf.write("A\3\2\2\2\u013d\u013e\5D#\2\u013e\u013f\7)\2\2\u013f\u0140")
        buf.write("\5D#\2\u0140\u0143\3\2\2\2\u0141\u0143\5D#\2\u0142\u013d")
        buf.write("\3\2\2\2\u0142\u0141\3\2\2\2\u0143C\3\2\2\2\u0144\u0145")
        buf.write("\5F$\2\u0145\u0146\5:\36\2\u0146\u0147\5F$\2\u0147\u014a")
        buf.write("\3\2\2\2\u0148\u014a\5F$\2\u0149\u0144\3\2\2\2\u0149\u0148")
        buf.write("\3\2\2\2\u014aE\3\2\2\2\u014b\u014c\b$\1\2\u014c\u014d")
        buf.write("\5H%\2\u014d\u0154\3\2\2\2\u014e\u014f\f\4\2\2\u014f\u0150")
        buf.write("\5<\37\2\u0150\u0151\5H%\2\u0151\u0153\3\2\2\2\u0152\u014e")
        buf.write("\3\2\2\2\u0153\u0156\3\2\2\2\u0154\u0152\3\2\2\2\u0154")
        buf.write("\u0155\3\2\2\2\u0155G\3\2\2\2\u0156\u0154\3\2\2\2\u0157")
        buf.write("\u0158\b%\1\2\u0158\u0159\5J&\2\u0159\u0160\3\2\2\2\u015a")
        buf.write("\u015b\f\4\2\2\u015b\u015c\5> \2\u015c\u015d\5J&\2\u015d")
        buf.write("\u015f\3\2\2\2\u015e\u015a\3\2\2\2\u015f\u0162\3\2\2\2")
        buf.write("\u0160\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161I\3\2\2")
        buf.write("\2\u0162\u0160\3\2\2\2\u0163\u0164\b&\1\2\u0164\u0165")
        buf.write("\5L\'\2\u0165\u016c\3\2\2\2\u0166\u0167\f\4\2\2\u0167")
        buf.write("\u0168\5@!\2\u0168\u0169\5L\'\2\u0169\u016b\3\2\2\2\u016a")
        buf.write("\u0166\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2")
        buf.write("\u016c\u016d\3\2\2\2\u016dK\3\2\2\2\u016e\u016c\3\2\2")
        buf.write("\2\u016f\u0170\7%\2\2\u0170\u0173\5L\'\2\u0171\u0173\5")
        buf.write("N(\2\u0172\u016f\3\2\2\2\u0172\u0171\3\2\2\2\u0173M\3")
        buf.write("\2\2\2\u0174\u0175\7\32\2\2\u0175\u0178\5N(\2\u0176\u0178")
        buf.write("\5P)\2\u0177\u0174\3\2\2\2\u0177\u0176\3\2\2\2\u0178O")
        buf.write("\3\2\2\2\u0179\u017a\5R*\2\u017a\u017b\7-\2\2\u017b\u017c")
        buf.write("\5B\"\2\u017c\u017d\7.\2\2\u017d\u0180\3\2\2\2\u017e\u0180")
        buf.write("\5R*\2\u017f\u0179\3\2\2\2\u017f\u017e\3\2\2\2\u0180Q")
        buf.write("\3\2\2\2\u0181\u0182\b*\1\2\u0182\u0183\5T+\2\u0183\u0189")
        buf.write("\3\2\2\2\u0184\u0185\f\4\2\2\u0185\u0186\7/\2\2\u0186")
        buf.write("\u0188\5T+\2\u0187\u0184\3\2\2\2\u0188\u018b\3\2\2\2\u0189")
        buf.write("\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018aS\3\2\2\2\u018b")
        buf.write("\u0189\3\2\2\2\u018c\u018d\5V,\2\u018d\u018e\7/\2\2\u018e")
        buf.write("\u018f\5V,\2\u018f\u0192\3\2\2\2\u0190\u0192\5V,\2\u0191")
        buf.write("\u018c\3\2\2\2\u0191\u0190\3\2\2\2\u0192U\3\2\2\2\u0193")
        buf.write("\u0194\7\25\2\2\u0194\u0195\5V,\2\u0195\u0196\7+\2\2\u0196")
        buf.write("\u0197\5\64\33\2\u0197\u0198\7,\2\2\u0198\u019b\3\2\2")
        buf.write("\2\u0199\u019b\5X-\2\u019a\u0193\3\2\2\2\u019a\u0199\3")
        buf.write("\2\2\2\u019bW\3\2\2\2\u019c\u019d\5(\25\2\u019dY\3\2\2")
        buf.write("\2\u019e\u01a7\7\23\2\2\u019f\u01a0\5\24\13\2\u01a0\u01a1")
        buf.write("\7\62\2\2\u01a1\u01a2\5\20\t\2\u01a2\u01a3\7\61\2\2\u01a3")
        buf.write("\u01a8\3\2\2\2\u01a4\u01a5\5\22\n\2\u01a5\u01a6\7\61\2")
        buf.write("\2\u01a6\u01a8\3\2\2\2\u01a7\u019f\3\2\2\2\u01a7\u01a4")
        buf.write("\3\2\2\2\u01a8[\3\2\2\2\u01a9\u01b2\7\27\2\2\u01aa\u01ab")
        buf.write("\5\24\13\2\u01ab\u01ac\7\62\2\2\u01ac\u01ad\5\20\t\2\u01ad")
        buf.write("\u01ae\7\61\2\2\u01ae\u01b3\3\2\2\2\u01af\u01b0\5\22\n")
        buf.write("\2\u01b0\u01b1\7\61\2\2\u01b1\u01b3\3\2\2\2\u01b2\u01aa")
        buf.write("\3\2\2\2\u01b2\u01af\3\2\2\2\u01b3]\3\2\2\2\u01b4\u01b5")
        buf.write("\5B\"\2\u01b5\u01b6\7!\2\2\u01b6\u01b7\5B\"\2\u01b7\u01b8")
        buf.write("\7\61\2\2\u01b8_\3\2\2\2\u01b9\u01bb\7\6\2\2\u01ba\u01bc")
        buf.write("\5r:\2\u01bb\u01ba\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bd")
        buf.write("\3\2\2\2\u01bd\u01be\5B\"\2\u01be\u01c1\5r:\2\u01bf\u01c0")
        buf.write("\7\7\2\2\u01c0\u01c2\5r:\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2")
        buf.write("\3\2\2\2\u01c2a\3\2\2\2\u01c3\u01c4\7\b\2\2\u01c4\u01c5")
        buf.write("\5^\60\2\u01c5\u01c6\5B\"\2\u01c6\u01c7\7\61\2\2\u01c7")
        buf.write("\u01c8\5r:\2\u01c8c\3\2\2\2\u01c9\u01ca\7\4\2\2\u01ca")
        buf.write("\u01cb\7\61\2\2\u01cbe\3\2\2\2\u01cc\u01cd\7\5\2\2\u01cd")
        buf.write("\u01ce\7\61\2\2\u01ceg\3\2\2\2\u01cf\u01d0\7\17\2\2\u01d0")
        buf.write("\u01d1\5B\"\2\u01d1\u01d2\7\61\2\2\u01d2i\3\2\2\2\u01d3")
        buf.write("\u01d4\5B\"\2\u01d4\u01d5\7/\2\2\u01d5\u01d6\7:\2\2\u01d6")
        buf.write("\u01d7\7\61\2\2\u01d7k\3\2\2\2\u01d8\u01d9\7:\2\2\u01d9")
        buf.write("\u01db\7/\2\2\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2\2")
        buf.write("\u01db\u01dc\3\2\2\2\u01dc\u01dd\7<\2\2\u01dd\u01de\7")
        buf.write("\61\2\2\u01dem\3\2\2\2\u01df\u01e0\5B\"\2\u01e0\u01e1")
        buf.write("\7/\2\2\u01e1\u01e2\7:\2\2\u01e2\u01e3\5\66\34\2\u01e3")
        buf.write("o\3\2\2\2\u01e4\u01e5\7:\2\2\u01e5\u01e7\7/\2\2\u01e6")
        buf.write("\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e8\3\2\2\2")
        buf.write("\u01e8\u01e9\7<\2\2\u01e9\u01ea\5\66\34\2\u01eaq\3\2\2")
        buf.write("\2\u01eb\u01ec\7\63\2\2\u01ec\u01ed\5t;\2\u01ed\u01ee")
        buf.write("\7\64\2\2\u01ees\3\2\2\2\u01ef\u01f0\5v<\2\u01f0\u01f1")
        buf.write("\5t;\2\u01f1\u01f4\3\2\2\2\u01f2\u01f4\3\2\2\2\u01f3\u01ef")
        buf.write("\3\2\2\2\u01f3\u01f2\3\2\2\2\u01f4u\3\2\2\2\u01f5\u01f8")
        buf.write("\5x=\2\u01f6\u01f8\5z>\2\u01f7\u01f5\3\2\2\2\u01f7\u01f6")
        buf.write("\3\2\2\2\u01f8w\3\2\2\2\u01f9\u01fa\t\2\2\2\u01fa\u01fb")
        buf.write("\5~@\2\u01fb\u01fc\7\62\2\2\u01fc\u01fd\5\20\t\2\u01fd")
        buf.write("\u01fe\7\61\2\2\u01fey\3\2\2\2\u01ff\u0200\t\2\2\2\u0200")
        buf.write("\u0201\5|?\2\u0201\u0202\7\61\2\2\u0202{\3\2\2\2\u0203")
        buf.write("\u0204\7;\2\2\u0204\u0205\7\60\2\2\u0205\u0206\5\22\n")
        buf.write("\2\u0206\u0207\7\60\2\2\u0207\u0208\5B\"\2\u0208\u0210")
        buf.write("\3\2\2\2\u0209\u020a\7;\2\2\u020a\u020b\7\62\2\2\u020b")
        buf.write("\u020c\5\20\t\2\u020c\u020d\7&\2\2\u020d\u020e\5B\"\2")
        buf.write("\u020e\u0210\3\2\2\2\u020f\u0203\3\2\2\2\u020f\u0209\3")
        buf.write("\2\2\2\u0210}\3\2\2\2\u0211\u0212\7;\2\2\u0212\u0213\7")
        buf.write("\60\2\2\u0213\u0216\5\24\13\2\u0214\u0216\7;\2\2\u0215")
        buf.write("\u0211\3\2\2\2\u0215\u0214\3\2\2\2\u0216\177\3\2\2\2+")
        buf.write("\u0083\u0089\u0094\u0098\u009c\u00b6\u00bc\u00c9\u00cd")
        buf.write("\u00d9\u00e6\u00ea\u00f0\u0101\u010d\u0115\u0117\u0128")
        buf.write("\u012c\u0133\u0142\u0149\u0154\u0160\u016c\u0172\u0177")
        buf.write("\u017f\u0189\u0191\u019a\u01a7\u01b2\u01bb\u01c1\u01da")
        buf.write("\u01e6\u01f3\u01f7\u020f\u0215")
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
                      "AND", "OR", "EQUAL", "ASSIGN", "NEQ", "LEQ", "GEQ", 
                      "DIFF", "DECLARE", "LE", "GE", "CONCAT", "MOD", "LRB", 
                      "RRB", "LSB", "RSB", "DOT", "CM", "SM", "COLON", "LCB", 
                      "RCB", "INTLIT", "FLOATLIT", "STRINGLIT", "BLOCKCMT", 
                      "LINECMT", "IDENTIFIER", "ID", "ATIDENTIFIER", "ARRAYSIZE", 
                      "WS", "UNCLOSED_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classdecl = 1
    RULE_memberlist = 2
    RULE_member = 3
    RULE_attribute = 4
    RULE_attributenodeclare = 5
    RULE_attributewithdeclare = 6
    RULE_typ = 7
    RULE_attlist = 8
    RULE_attributelist = 9
    RULE_method = 10
    RULE_parameterlist = 11
    RULE_parameterprime = 12
    RULE_parameterpart1 = 13
    RULE_parameterpart2 = 14
    RULE_identifierlist = 15
    RULE_identifierprime = 16
    RULE_constructor = 17
    RULE_superpart = 18
    RULE_literal = 19
    RULE_boolit = 20
    RULE_arraylit = 21
    RULE_literallist = 22
    RULE_arraydecl = 23
    RULE_objdecl = 24
    RULE_explist = 25
    RULE_nullableexplist = 26
    RULE_expprime = 27
    RULE_relational = 28
    RULE_logical = 29
    RULE_adding = 30
    RULE_multiplying = 31
    RULE_exp = 32
    RULE_exp1 = 33
    RULE_exp2 = 34
    RULE_exp3 = 35
    RULE_exp4 = 36
    RULE_exp5 = 37
    RULE_exp6 = 38
    RULE_exp7 = 39
    RULE_exp8 = 40
    RULE_exp9 = 41
    RULE_exp10 = 42
    RULE_exp11 = 43
    RULE_varstate = 44
    RULE_constate = 45
    RULE_assignstate = 46
    RULE_ifstate = 47
    RULE_forstate = 48
    RULE_breakstate = 49
    RULE_continuestate = 50
    RULE_returnstate = 51
    RULE_instanceattributestate = 52
    RULE_staticattributestate = 53
    RULE_instancemethodstate = 54
    RULE_staticmethodstate = 55
    RULE_blockstate = 56
    RULE_stmtlist = 57
    RULE_noatstmt = 58
    RULE_noatstmtnodeclare = 59
    RULE_noatstmtwithdeclare = 60
    RULE_attlist1 = 61
    RULE_attributelist1 = 62

    ruleNames =  [ "program", "classdecl", "memberlist", "member", "attribute", 
                   "attributenodeclare", "attributewithdeclare", "typ", 
                   "attlist", "attributelist", "method", "parameterlist", 
                   "parameterprime", "parameterpart1", "parameterpart2", 
                   "identifierlist", "identifierprime", "constructor", "superpart", 
                   "literal", "boolit", "arraylit", "literallist", "arraydecl", 
                   "objdecl", "explist", "nullableexplist", "expprime", 
                   "relational", "logical", "adding", "multiplying", "exp", 
                   "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", 
                   "exp8", "exp9", "exp10", "exp11", "varstate", "constate", 
                   "assignstate", "ifstate", "forstate", "breakstate", "continuestate", 
                   "returnstate", "instanceattributestate", "staticattributestate", 
                   "instancemethodstate", "staticmethodstate", "blockstate", 
                   "stmtlist", "noatstmt", "noatstmtnodeclare", "noatstmtwithdeclare", 
                   "attlist1", "attributelist1" ]

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
    EQUAL=30
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
    IDENTIFIER=56
    ID=57
    ATIDENTIFIER=58
    ARRAYSIZE=59
    WS=60
    UNCLOSED_STRING=61
    ILLEGAL_ESCAPE=62
    ERROR_CHAR=63

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

        def EOF(self):
            return self.getToken(CSlangParser.EOF, 0)

        def classdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ClassdeclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ClassdeclContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 126
                self.classdecl()
                self.state = 129 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSlangParser.CLASS):
                    break

            self.state = 131
            self.match(CSlangParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_classdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(CSlangParser.CLASS)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.IDENTIFIER:
                self.state = 134
                self.superpart()


            self.state = 137
            self.match(CSlangParser.ID)
            self.state = 138
            self.match(CSlangParser.LCB)
            self.state = 139
            self.memberlist()
            self.state = 140
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
        self.enterRule(localctx, 4, self.RULE_memberlist)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST, CSlangParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.member()
                self.state = 143
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
        self.enterRule(localctx, 6, self.RULE_member)
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

        def attributewithdeclare(self):
            return self.getTypedRuleContext(CSlangParser.AttributewithdeclareContext,0)


        def attributenodeclare(self):
            return self.getTypedRuleContext(CSlangParser.AttributenodeclareContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = CSlangParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.attributewithdeclare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
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
        self.enterRule(localctx, 10, self.RULE_attributenodeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 157
            self.attributelist()
            self.state = 158
            self.match(CSlangParser.COLON)
            self.state = 159
            self.typ()
            self.state = 160
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
        self.enterRule(localctx, 12, self.RULE_attributewithdeclare)
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
            self.attlist()
            self.state = 164
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
        self.enterRule(localctx, 14, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
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

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 16, self.RULE_attlist)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(CSlangParser.IDENTIFIER)
                self.state = 169
                self.match(CSlangParser.CM)
                self.state = 170
                self.attlist()
                self.state = 171
                self.match(CSlangParser.CM)
                self.state = 172
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.match(CSlangParser.IDENTIFIER)
                self.state = 175
                self.match(CSlangParser.COLON)
                self.state = 176
                self.typ()
                self.state = 177
                self.match(CSlangParser.DECLARE)
                self.state = 178
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

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 18, self.RULE_attributelist)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(CSlangParser.IDENTIFIER)
                self.state = 183
                self.match(CSlangParser.CM)
                self.state = 184
                self.attributelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(CSlangParser.IDENTIFIER)
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

        def LRB(self):
            return self.getToken(CSlangParser.LRB, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(CSlangParser.ParameterlistContext,0)


        def RRB(self):
            return self.getToken(CSlangParser.RRB, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def blockstate(self):
            return self.getTypedRuleContext(CSlangParser.BlockstateContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def ATIDENTIFIER(self):
            return self.getToken(CSlangParser.ATIDENTIFIER, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = CSlangParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(CSlangParser.FUNC)
            self.state = 189
            _la = self._input.LA(1)
            if not(_la==CSlangParser.ID or _la==CSlangParser.ATIDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 190
            self.match(CSlangParser.LRB)
            self.state = 191
            self.parameterlist()
            self.state = 192
            self.match(CSlangParser.RRB)
            self.state = 193
            self.match(CSlangParser.COLON)
            self.state = 194
            self.typ()
            self.state = 195
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
        self.enterRule(localctx, 22, self.RULE_parameterlist)
        try:
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.COLON, CSlangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
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
        self.enterRule(localctx, 24, self.RULE_parameterprime)
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.parameterpart1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
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


        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 26, self.RULE_parameterpart1)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(CSlangParser.IDENTIFIER)
                self.state = 206
                self.match(CSlangParser.COLON)
                self.state = 207
                self.typ()
                self.state = 209
                self.match(CSlangParser.CM)
                self.state = 210
                self.parameterpart1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(CSlangParser.IDENTIFIER)
                self.state = 213
                self.match(CSlangParser.COLON)
                self.state = 214
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
        self.enterRule(localctx, 28, self.RULE_parameterpart2)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.identifierlist()
                self.state = 218
                self.match(CSlangParser.COLON)
                self.state = 219
                self.typ()
                self.state = 221
                self.match(CSlangParser.CM)
                self.state = 222
                self.parameterpart2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.identifierlist()
                self.state = 225
                self.match(CSlangParser.COLON)
                self.state = 226
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
        self.enterRule(localctx, 30, self.RULE_identifierlist)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
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

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 32, self.RULE_identifierprime)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(CSlangParser.IDENTIFIER)
                self.state = 235
                self.match(CSlangParser.CM)
                self.state = 236
                self.identifierprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
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
        self.enterRule(localctx, 34, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(CSlangParser.FUNC)
            self.state = 241
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 242
            self.match(CSlangParser.LRB)
            self.state = 243
            self.parameterlist()
            self.state = 244
            self.match(CSlangParser.RRB)
            self.state = 245
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
        self.enterRule(localctx, 36, self.RULE_superpart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(CSlangParser.IDENTIFIER)
            self.state = 248
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
        self.enterRule(localctx, 38, self.RULE_literal)
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.boolit()
                pass
            elif token in [CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 253
                self.match(CSlangParser.STRINGLIT)
                pass
            elif token in [CSlangParser.LSB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 254
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
        self.enterRule(localctx, 40, self.RULE_boolit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
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
        self.enterRule(localctx, 42, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(CSlangParser.LSB)
            self.state = 260
            self.literallist()
            self.state = 261
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
        self.enterRule(localctx, 44, self.RULE_literallist)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CSlangParser.INTLIT]:
                    self.state = 263
                    self.match(CSlangParser.INTLIT)
                    pass
                elif token in [CSlangParser.FLOATLIT]:
                    self.state = 264
                    self.match(CSlangParser.FLOATLIT)
                    pass
                elif token in [CSlangParser.TRUE, CSlangParser.FALSE]:
                    self.state = 265
                    self.boolit()
                    pass
                elif token in [CSlangParser.STRINGLIT]:
                    self.state = 266
                    self.match(CSlangParser.STRINGLIT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 269
                self.match(CSlangParser.CM)
                self.state = 270
                self.literallist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
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
        self.enterRule(localctx, 46, self.RULE_arraydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(CSlangParser.LSB)
            self.state = 280
            self.match(CSlangParser.ARRAYSIZE)
            self.state = 281
            self.match(CSlangParser.RSB)
            self.state = 282
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

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 48, self.RULE_objdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(CSlangParser.NEW)
            self.state = 285
            self.match(CSlangParser.IDENTIFIER)
            self.state = 286
            self.match(CSlangParser.LRB)
            self.state = 287
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
        self.enterRule(localctx, 50, self.RULE_explist)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.exp()
                self.state = 290
                self.match(CSlangParser.CM)
                self.state = 291
                self.explist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
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
        self.enterRule(localctx, 52, self.RULE_nullableexplist)
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.DIFF, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.expprime()
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
        self.enterRule(localctx, 54, self.RULE_expprime)
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.exp()
                self.state = 301
                self.match(CSlangParser.CM)
                self.state = 302
                self.expprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
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

        def EQUAL(self):
            return self.getToken(CSlangParser.EQUAL, 0)

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
        self.enterRule(localctx, 56, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQUAL) | (1 << CSlangParser.NEQ) | (1 << CSlangParser.LEQ) | (1 << CSlangParser.GEQ) | (1 << CSlangParser.LE) | (1 << CSlangParser.GE))) != 0)):
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
        self.enterRule(localctx, 58, self.RULE_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
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
        self.enterRule(localctx, 60, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
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
        self.enterRule(localctx, 62, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
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
        self.enterRule(localctx, 64, self.RULE_exp)
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.exp1()
                self.state = 316
                self.match(CSlangParser.CONCAT)
                self.state = 317
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
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
        self.enterRule(localctx, 66, self.RULE_exp1)
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.exp2(0)
                self.state = 323
                self.relational()
                self.state = 324
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 338
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 332
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 333
                    self.logical()
                    self.state = 334
                    self.exp3(0) 
                self.state = 340
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 350
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 344
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 345
                    self.adding()
                    self.state = 346
                    self.exp4(0) 
                self.state = 352
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 362
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 356
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 357
                    self.multiplying()
                    self.state = 358
                    self.exp5() 
                self.state = 364
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        self.enterRule(localctx, 74, self.RULE_exp5)
        try:
            self.state = 368
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.DIFF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.match(CSlangParser.DIFF)
                self.state = 366
                self.exp5()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NEW, CSlangParser.MINUS, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
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
        self.enterRule(localctx, 76, self.RULE_exp6)
        try:
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.match(CSlangParser.MINUS)
                self.state = 371
                self.exp6()
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.NEW, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
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
        self.enterRule(localctx, 78, self.RULE_exp7)
        try:
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.exp8(0)
                self.state = 376
                self.match(CSlangParser.LSB)
                self.state = 377
                self.exp()
                self.state = 378
                self.match(CSlangParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 391
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 386
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 387
                    self.match(CSlangParser.DOT)
                    self.state = 388
                    self.exp9() 
                self.state = 393
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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

        def exp10(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Exp10Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Exp10Context,i)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)




    def exp9(self):

        localctx = CSlangParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_exp9)
        try:
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.exp10()
                self.state = 395
                self.match(CSlangParser.DOT)
                self.state = 396
                self.exp10()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
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

        def exp10(self):
            return self.getTypedRuleContext(CSlangParser.Exp10Context,0)


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
        self.enterRule(localctx, 84, self.RULE_exp10)
        try:
            self.state = 408
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(CSlangParser.NEW)
                self.state = 402
                self.exp10()
                self.state = 403
                self.match(CSlangParser.LRB)
                self.state = 404
                self.explist()
                self.state = 405
                self.match(CSlangParser.RRB)
                pass
            elif token in [CSlangParser.TRUE, CSlangParser.FALSE, CSlangParser.LSB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
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


        def getRuleIndex(self):
            return CSlangParser.RULE_exp11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp11" ):
                return visitor.visitExp11(self)
            else:
                return visitor.visitChildren(self)




    def exp11(self):

        localctx = CSlangParser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_exp11)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.literal()
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
        self.enterRule(localctx, 88, self.RULE_varstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(CSlangParser.VAR)
            self.state = 421
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 413
                self.attributelist()
                self.state = 414
                self.match(CSlangParser.COLON)
                self.state = 415
                self.typ()
                self.state = 416
                self.match(CSlangParser.SM)
                pass

            elif la_ == 2:
                self.state = 418
                self.attlist()
                self.state = 419
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
        self.enterRule(localctx, 90, self.RULE_constate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(CSlangParser.CONST)
            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 424
                self.attributelist()
                self.state = 425
                self.match(CSlangParser.COLON)
                self.state = 426
                self.typ()
                self.state = 427
                self.match(CSlangParser.SM)
                pass

            elif la_ == 2:
                self.state = 429
                self.attlist()
                self.state = 430
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
        self.enterRule(localctx, 92, self.RULE_assignstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.exp()
            self.state = 435
            self.match(CSlangParser.ASSIGN)
            self.state = 436
            self.exp()
            self.state = 437
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
        self.enterRule(localctx, 94, self.RULE_ifstate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(CSlangParser.IF)
            self.state = 441
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LCB:
                self.state = 440
                self.blockstate()


            self.state = 443
            self.exp()
            self.state = 444
            self.blockstate()
            self.state = 447
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 445
                self.match(CSlangParser.ELSE)
                self.state = 446
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstate" ):
                return visitor.visitForstate(self)
            else:
                return visitor.visitChildren(self)




    def forstate(self):

        localctx = CSlangParser.ForstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_forstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(CSlangParser.FOR)
            self.state = 450
            self.assignstate()
            self.state = 451
            self.exp()
            self.state = 452
            self.match(CSlangParser.SM)
            self.state = 453
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
        self.enterRule(localctx, 98, self.RULE_breakstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.match(CSlangParser.BREAK)
            self.state = 456
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
        self.enterRule(localctx, 100, self.RULE_continuestate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(CSlangParser.CONTINUE)
            self.state = 459
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
        self.enterRule(localctx, 102, self.RULE_returnstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.match(CSlangParser.RETURN)

            self.state = 462
            self.exp()
            self.state = 463
            self.match(CSlangParser.SM)
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

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_instanceattributestate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceattributestate" ):
                return visitor.visitInstanceattributestate(self)
            else:
                return visitor.visitChildren(self)




    def instanceattributestate(self):

        localctx = CSlangParser.InstanceattributestateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_instanceattributestate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.exp()
            self.state = 466
            self.match(CSlangParser.DOT)
            self.state = 467
            self.match(CSlangParser.IDENTIFIER)
            self.state = 468
            self.match(CSlangParser.SM)
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

        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 106, self.RULE_staticattributestate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.IDENTIFIER:
                self.state = 470
                self.match(CSlangParser.IDENTIFIER)
                self.state = 471
                self.match(CSlangParser.DOT)


            self.state = 474
            self.match(CSlangParser.ATIDENTIFIER)
            self.state = 475
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

        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

        def nullableexplist(self):
            return self.getTypedRuleContext(CSlangParser.NullableexplistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_instancemethodstate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstancemethodstate" ):
                return visitor.visitInstancemethodstate(self)
            else:
                return visitor.visitChildren(self)




    def instancemethodstate(self):

        localctx = CSlangParser.InstancemethodstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_instancemethodstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.exp()
            self.state = 478
            self.match(CSlangParser.DOT)
            self.state = 479
            self.match(CSlangParser.IDENTIFIER)

            self.state = 480
            self.nullableexplist()
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

        def nullableexplist(self):
            return self.getTypedRuleContext(CSlangParser.NullableexplistContext,0)


        def IDENTIFIER(self):
            return self.getToken(CSlangParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 110, self.RULE_staticmethodstate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.IDENTIFIER:
                self.state = 482
                self.match(CSlangParser.IDENTIFIER)
                self.state = 483
                self.match(CSlangParser.DOT)


            self.state = 486
            self.match(CSlangParser.ATIDENTIFIER)

            self.state = 487
            self.nullableexplist()
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
            self.state = 489
            self.match(CSlangParser.LCB)
            self.state = 490
            self.stmtlist()
            self.state = 491
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

        def noatstmt(self):
            return self.getTypedRuleContext(CSlangParser.NoatstmtContext,0)


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
            self.state = 497
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR, CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.noatstmt()
                self.state = 494
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


    class NoatstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def noatstmtnodeclare(self):
            return self.getTypedRuleContext(CSlangParser.NoatstmtnodeclareContext,0)


        def noatstmtwithdeclare(self):
            return self.getTypedRuleContext(CSlangParser.NoatstmtwithdeclareContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_noatstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoatstmt" ):
                return visitor.visitNoatstmt(self)
            else:
                return visitor.visitChildren(self)




    def noatstmt(self):

        localctx = CSlangParser.NoatstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_noatstmt)
        try:
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.noatstmtnodeclare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
                self.noatstmtwithdeclare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoatstmtnodeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributelist1(self):
            return self.getTypedRuleContext(CSlangParser.Attributelist1Context,0)


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
            return CSlangParser.RULE_noatstmtnodeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoatstmtnodeclare" ):
                return visitor.visitNoatstmtnodeclare(self)
            else:
                return visitor.visitChildren(self)




    def noatstmtnodeclare(self):

        localctx = CSlangParser.NoatstmtnodeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_noatstmtnodeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 504
            self.attributelist1()
            self.state = 505
            self.match(CSlangParser.COLON)
            self.state = 506
            self.typ()
            self.state = 507
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoatstmtwithdeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attlist1(self):
            return self.getTypedRuleContext(CSlangParser.Attlist1Context,0)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_noatstmtwithdeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoatstmtwithdeclare" ):
                return visitor.visitNoatstmtwithdeclare(self)
            else:
                return visitor.visitChildren(self)




    def noatstmtwithdeclare(self):

        localctx = CSlangParser.NoatstmtwithdeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_noatstmtwithdeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            _la = self._input.LA(1)
            if not(_la==CSlangParser.VAR or _la==CSlangParser.CONST):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 510
            self.attlist1()
            self.state = 511
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attlist1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

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
            return CSlangParser.RULE_attlist1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttlist1" ):
                return visitor.visitAttlist1(self)
            else:
                return visitor.visitChildren(self)




    def attlist1(self):

        localctx = CSlangParser.Attlist1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_attlist1)
        try:
            self.state = 525
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 513
                self.match(CSlangParser.ID)
                self.state = 514
                self.match(CSlangParser.CM)
                self.state = 515
                self.attlist()
                self.state = 516
                self.match(CSlangParser.CM)
                self.state = 517
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 519
                self.match(CSlangParser.ID)
                self.state = 520
                self.match(CSlangParser.COLON)
                self.state = 521
                self.typ()
                self.state = 522
                self.match(CSlangParser.DECLARE)
                self.state = 523
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attributelist1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def attributelist(self):
            return self.getTypedRuleContext(CSlangParser.AttributelistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attributelist1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributelist1" ):
                return visitor.visitAttributelist1(self)
            else:
                return visitor.visitChildren(self)




    def attributelist1(self):

        localctx = CSlangParser.Attributelist1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_attributelist1)
        try:
            self.state = 531
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 527
                self.match(CSlangParser.ID)
                self.state = 528
                self.match(CSlangParser.CM)
                self.state = 529
                self.attributelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 530
                self.match(CSlangParser.ID)
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
        self._predicates[34] = self.exp2_sempred
        self._predicates[35] = self.exp3_sempred
        self._predicates[36] = self.exp4_sempred
        self._predicates[40] = self.exp8_sempred
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
         




