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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("\u00f2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u009c\n\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\5\7\u00b1\n\7\3\b\3\b\3\t\6\t\u00b6\n")
        buf.write("\t\r\t\16\t\u00b7\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00c1")
        buf.write("\n\n\3\13\5\13\u00c4\n\13\3\13\6\13\u00c7\n\13\r\13\16")
        buf.write("\13\u00c8\3\f\3\f\3\f\6\f\u00ce\n\f\r\f\16\f\u00cf\3\r")
        buf.write("\6\r\u00d3\n\r\r\r\16\r\u00d4\3\r\7\r\u00d8\n\r\f\r\16")
        buf.write("\r\u00db\13\r\3\r\3\r\6\r\u00df\n\r\r\r\16\r\u00e0\5\r")
        buf.write("\u00e3\n\r\3\16\6\16\u00e6\n\16\r\16\16\16\u00e7\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\2\2\22\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\2\27\2\31\f\33")
        buf.write("\r\35\16\37\17!\20\3\2\13\7\2##,-//\61\61^^\4\2\'\'``")
        buf.write("\n\2*+..\60\60<=]]__}}\177\177\3\2\62;\4\2GGgg\4\2--/")
        buf.write("/\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\f\16\17\"\"\2\u0118")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\3#\3\2\2\2\5\'\3\2\2\2\7-\3\2\2\2\t\62")
        buf.write("\3\2\2\2\13\u009b\3\2\2\2\r\u00b0\3\2\2\2\17\u00b2\3\2")
        buf.write("\2\2\21\u00b5\3\2\2\2\23\u00c0\3\2\2\2\25\u00c3\3\2\2")
        buf.write("\2\27\u00ca\3\2\2\2\31\u00e2\3\2\2\2\33\u00e5\3\2\2\2")
        buf.write("\35\u00eb\3\2\2\2\37\u00ee\3\2\2\2!\u00f0\3\2\2\2#$\7")
        buf.write("k\2\2$%\7p\2\2%&\7v\2\2&\4\3\2\2\2\'(\7h\2\2()\7n\2\2")
        buf.write(")*\7q\2\2*+\7c\2\2+,\7v\2\2,\6\3\2\2\2-.\7d\2\2./\7q\2")
        buf.write("\2/\60\7q\2\2\60\61\7n\2\2\61\b\3\2\2\2\62\63\7u\2\2\63")
        buf.write("\64\7v\2\2\64\65\7t\2\2\65\66\7k\2\2\66\67\7p\2\2\678")
        buf.write("\7i\2\28\n\3\2\2\29:\7d\2\2:;\7t\2\2;<\7g\2\2<=\7c\2\2")
        buf.write("=\u009c\7m\2\2>?\7e\2\2?@\7q\2\2@A\7p\2\2AB\7v\2\2BC\7")
        buf.write("k\2\2CD\7p\2\2DE\7w\2\2E\u009c\7g\2\2FG\7k\2\2G\u009c")
        buf.write("\7h\2\2HI\7g\2\2IJ\7n\2\2JK\7u\2\2K\u009c\7g\2\2LM\7h")
        buf.write("\2\2MN\7q\2\2N\u009c\7t\2\2OP\7v\2\2PQ\7t\2\2QR\7w\2\2")
        buf.write("R\u009c\7g\2\2ST\7h\2\2TU\7c\2\2UV\7n\2\2VW\7u\2\2W\u009c")
        buf.write("\7g\2\2XY\7k\2\2YZ\7p\2\2Z\u009c\7v\2\2[\\\7h\2\2\\]\7")
        buf.write("n\2\2]^\7q\2\2^_\7c\2\2_\u009c\7v\2\2`a\7d\2\2ab\7q\2")
        buf.write("\2bc\7q\2\2c\u009c\7n\2\2de\7u\2\2ef\7v\2\2fg\7t\2\2g")
        buf.write("h\7k\2\2hi\7p\2\2i\u009c\7i\2\2jk\7t\2\2kl\7g\2\2lm\7")
        buf.write("v\2\2mn\7w\2\2no\7t\2\2o\u009c\7p\2\2pq\7p\2\2qr\7w\2")
        buf.write("\2rs\7n\2\2s\u009c\7n\2\2tu\7e\2\2uv\7n\2\2vw\7c\2\2w")
        buf.write("x\7u\2\2x\u009c\7u\2\2yz\7e\2\2z{\7q\2\2{|\7p\2\2|}\7")
        buf.write("u\2\2}~\7v\2\2~\177\7t\2\2\177\u0080\7w\2\2\u0080\u0081")
        buf.write("\7e\2\2\u0081\u0082\7v\2\2\u0082\u0083\7q\2\2\u0083\u009c")
        buf.write("\7t\2\2\u0084\u0085\7x\2\2\u0085\u0086\7c\2\2\u0086\u009c")
        buf.write("\7t\2\2\u0087\u0088\7u\2\2\u0088\u0089\7g\2\2\u0089\u008a")
        buf.write("\7n\2\2\u008a\u009c\7h\2\2\u008b\u008c\7p\2\2\u008c\u008d")
        buf.write("\7g\2\2\u008d\u009c\7y\2\2\u008e\u008f\7x\2\2\u008f\u0090")
        buf.write("\7q\2\2\u0090\u0091\7k\2\2\u0091\u009c\7f\2\2\u0092\u0093")
        buf.write("\7e\2\2\u0093\u0094\7q\2\2\u0094\u0095\7p\2\2\u0095\u0096")
        buf.write("\7u\2\2\u0096\u009c\7v\2\2\u0097\u0098\7h\2\2\u0098\u0099")
        buf.write("\7w\2\2\u0099\u009a\7p\2\2\u009a\u009c\7e\2\2\u009b9\3")
        buf.write("\2\2\2\u009b>\3\2\2\2\u009bF\3\2\2\2\u009bH\3\2\2\2\u009b")
        buf.write("L\3\2\2\2\u009bO\3\2\2\2\u009bS\3\2\2\2\u009bX\3\2\2\2")
        buf.write("\u009b[\3\2\2\2\u009b`\3\2\2\2\u009bd\3\2\2\2\u009bj\3")
        buf.write("\2\2\2\u009bp\3\2\2\2\u009bt\3\2\2\2\u009by\3\2\2\2\u009b")
        buf.write("\u0084\3\2\2\2\u009b\u0087\3\2\2\2\u009b\u008b\3\2\2\2")
        buf.write("\u009b\u008e\3\2\2\2\u009b\u0092\3\2\2\2\u009b\u0097\3")
        buf.write("\2\2\2\u009c\f\3\2\2\2\u009d\u00b1\t\2\2\2\u009e\u009f")
        buf.write("\7(\2\2\u009f\u00b1\7(\2\2\u00a0\u00a1\7~\2\2\u00a1\u00b1")
        buf.write("\7~\2\2\u00a2\u00a3\7?\2\2\u00a3\u00b1\7?\2\2\u00a4\u00b1")
        buf.write("\7?\2\2\u00a5\u00a6\7#\2\2\u00a6\u00b1\7?\2\2\u00a7\u00b1")
        buf.write("\7>\2\2\u00a8\u00a9\7>\2\2\u00a9\u00b1\7?\2\2\u00aa\u00b1")
        buf.write("\7@\2\2\u00ab\u00ac\7@\2\2\u00ac\u00b1\7?\2\2\u00ad\u00ae")
        buf.write("\7<\2\2\u00ae\u00b1\7?\2\2\u00af\u00b1\t\3\2\2\u00b0\u009d")
        buf.write("\3\2\2\2\u00b0\u009e\3\2\2\2\u00b0\u00a0\3\2\2\2\u00b0")
        buf.write("\u00a2\3\2\2\2\u00b0\u00a4\3\2\2\2\u00b0\u00a5\3\2\2\2")
        buf.write("\u00b0\u00a7\3\2\2\2\u00b0\u00a8\3\2\2\2\u00b0\u00aa\3")
        buf.write("\2\2\2\u00b0\u00ab\3\2\2\2\u00b0\u00ad\3\2\2\2\u00b0\u00af")
        buf.write("\3\2\2\2\u00b1\16\3\2\2\2\u00b2\u00b3\t\4\2\2\u00b3\20")
        buf.write("\3\2\2\2\u00b4\u00b6\t\5\2\2\u00b5\u00b4\3\2\2\2\u00b6")
        buf.write("\u00b7\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2")
        buf.write("\u00b8\22\3\2\2\2\u00b9\u00ba\5\21\t\2\u00ba\u00bb\5\25")
        buf.write("\13\2\u00bb\u00c1\3\2\2\2\u00bc\u00bd\5\21\t\2\u00bd\u00be")
        buf.write("\5\25\13\2\u00be\u00bf\5\27\f\2\u00bf\u00c1\3\2\2\2\u00c0")
        buf.write("\u00b9\3\2\2\2\u00c0\u00bc\3\2\2\2\u00c1\24\3\2\2\2\u00c2")
        buf.write("\u00c4\7\60\2\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4\3\2\2")
        buf.write("\2\u00c4\u00c6\3\2\2\2\u00c5\u00c7\t\5\2\2\u00c6\u00c5")
        buf.write("\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8")
        buf.write("\u00c9\3\2\2\2\u00c9\26\3\2\2\2\u00ca\u00cb\t\6\2\2\u00cb")
        buf.write("\u00cd\t\7\2\2\u00cc\u00ce\t\5\2\2\u00cd\u00cc\3\2\2\2")
        buf.write("\u00ce\u00cf\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3")
        buf.write("\2\2\2\u00d0\30\3\2\2\2\u00d1\u00d3\t\b\2\2\u00d2\u00d1")
        buf.write("\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4")
        buf.write("\u00d5\3\2\2\2\u00d5\u00d9\3\2\2\2\u00d6\u00d8\t\t\2\2")
        buf.write("\u00d7\u00d6\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9\u00d7\3")
        buf.write("\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00e3\3\2\2\2\u00db\u00d9")
        buf.write("\3\2\2\2\u00dc\u00de\7B\2\2\u00dd\u00df\t\t\2\2\u00de")
        buf.write("\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00de\3\2\2\2")
        buf.write("\u00e0\u00e1\3\2\2\2\u00e1\u00e3\3\2\2\2\u00e2\u00d2\3")
        buf.write("\2\2\2\u00e2\u00dc\3\2\2\2\u00e3\32\3\2\2\2\u00e4\u00e6")
        buf.write("\t\n\2\2\u00e5\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7")
        buf.write("\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e9\3\2\2\2")
        buf.write("\u00e9\u00ea\b\16\2\2\u00ea\34\3\2\2\2\u00eb\u00ec\13")
        buf.write("\2\2\2\u00ec\u00ed\b\17\3\2\u00ed\36\3\2\2\2\u00ee\u00ef")
        buf.write("\13\2\2\2\u00ef \3\2\2\2\u00f0\u00f1\13\2\2\2\u00f1\"")
        buf.write("\3\2\2\2\17\2\u009b\u00b0\u00b7\u00c0\u00c3\u00c8\u00cf")
        buf.write("\u00d4\u00d9\u00e0\u00e2\u00e7\4\b\2\2\3\17\2")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    KEYWORDS = 5
    OPERATORS = 6
    SEPARATORS = 7
    INT = 8
    FLOAT = 9
    IDENTIFIER = 10
    WS = 11
    ERROR_CHAR = 12
    UNCLOSE_STRING = 13
    ILLEGAL_ESCAPE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'bool'", "'string'" ]

    symbolicNames = [ "<INVALID>",
            "KEYWORDS", "OPERATORS", "SEPARATORS", "INT", "FLOAT", "IDENTIFIER", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "KEYWORDS", "OPERATORS", 
                  "SEPARATORS", "INT", "FLOAT", "DEC", "EXP", "IDENTIFIER", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[13] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


