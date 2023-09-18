# Generated from d:\btl1-nlnnlt\cslang-initial\src\main\CSlang\parser\CSlang.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("\u00cd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\6\6\63\n\6\r\6")
        buf.write("\16\6\64\3\6\7\68\n\6\f\6\16\6;\13\6\3\6\3\6\6\6?\n\6")
        buf.write("\r\6\16\6@\5\6C\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00a7\n\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\5\b\u00bc\n\b\3\t\3\t\3\n\6\n\u00c1\n")
        buf.write("\n\r\n\16\n\u00c2\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3")
        buf.write("\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\3\2\b\5\2C\\aac|\6\2\62;C\\aac|\7\2##,-")
        buf.write("//\61\61^^\4\2\'\'``\n\2*+..\60\60<=]]__}}\177\177\5\2")
        buf.write("\n\f\16\17\"\"\2\u00f0\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\3\33\3\2\2\2\5\37\3\2\2\2\7%\3\2\2\2\t*\3")
        buf.write("\2\2\2\13B\3\2\2\2\r\u00a6\3\2\2\2\17\u00bb\3\2\2\2\21")
        buf.write("\u00bd\3\2\2\2\23\u00c0\3\2\2\2\25\u00c6\3\2\2\2\27\u00c9")
        buf.write("\3\2\2\2\31\u00cb\3\2\2\2\33\34\7k\2\2\34\35\7p\2\2\35")
        buf.write("\36\7v\2\2\36\4\3\2\2\2\37 \7h\2\2 !\7n\2\2!\"\7q\2\2")
        buf.write("\"#\7c\2\2#$\7v\2\2$\6\3\2\2\2%&\7d\2\2&\'\7q\2\2\'(\7")
        buf.write("q\2\2()\7n\2\2)\b\3\2\2\2*+\7u\2\2+,\7v\2\2,-\7t\2\2-")
        buf.write(".\7k\2\2./\7p\2\2/\60\7i\2\2\60\n\3\2\2\2\61\63\t\2\2")
        buf.write("\2\62\61\3\2\2\2\63\64\3\2\2\2\64\62\3\2\2\2\64\65\3\2")
        buf.write("\2\2\659\3\2\2\2\668\t\3\2\2\67\66\3\2\2\28;\3\2\2\29")
        buf.write("\67\3\2\2\29:\3\2\2\2:C\3\2\2\2;9\3\2\2\2<>\7B\2\2=?\t")
        buf.write("\3\2\2>=\3\2\2\2?@\3\2\2\2@>\3\2\2\2@A\3\2\2\2AC\3\2\2")
        buf.write("\2B\62\3\2\2\2B<\3\2\2\2C\f\3\2\2\2DE\7d\2\2EF\7t\2\2")
        buf.write("FG\7g\2\2GH\7c\2\2H\u00a7\7m\2\2IJ\7e\2\2JK\7q\2\2KL\7")
        buf.write("p\2\2LM\7v\2\2MN\7k\2\2NO\7p\2\2OP\7w\2\2P\u00a7\7g\2")
        buf.write("\2QR\7k\2\2R\u00a7\7h\2\2ST\7g\2\2TU\7n\2\2UV\7u\2\2V")
        buf.write("\u00a7\7g\2\2WX\7h\2\2XY\7q\2\2Y\u00a7\7t\2\2Z[\7v\2\2")
        buf.write("[\\\7t\2\2\\]\7w\2\2]\u00a7\7g\2\2^_\7h\2\2_`\7c\2\2`")
        buf.write("a\7n\2\2ab\7u\2\2b\u00a7\7g\2\2cd\7k\2\2de\7p\2\2e\u00a7")
        buf.write("\7v\2\2fg\7h\2\2gh\7n\2\2hi\7q\2\2ij\7c\2\2j\u00a7\7v")
        buf.write("\2\2kl\7d\2\2lm\7q\2\2mn\7q\2\2n\u00a7\7n\2\2op\7u\2\2")
        buf.write("pq\7v\2\2qr\7t\2\2rs\7k\2\2st\7p\2\2t\u00a7\7i\2\2uv\7")
        buf.write("t\2\2vw\7g\2\2wx\7v\2\2xy\7w\2\2yz\7t\2\2z\u00a7\7p\2")
        buf.write("\2{|\7p\2\2|}\7w\2\2}~\7n\2\2~\u00a7\7n\2\2\177\u0080")
        buf.write("\7e\2\2\u0080\u0081\7n\2\2\u0081\u0082\7c\2\2\u0082\u0083")
        buf.write("\7u\2\2\u0083\u00a7\7u\2\2\u0084\u0085\7e\2\2\u0085\u0086")
        buf.write("\7q\2\2\u0086\u0087\7p\2\2\u0087\u0088\7u\2\2\u0088\u0089")
        buf.write("\7v\2\2\u0089\u008a\7t\2\2\u008a\u008b\7w\2\2\u008b\u008c")
        buf.write("\7e\2\2\u008c\u008d\7v\2\2\u008d\u008e\7q\2\2\u008e\u00a7")
        buf.write("\7t\2\2\u008f\u0090\7x\2\2\u0090\u0091\7c\2\2\u0091\u00a7")
        buf.write("\7t\2\2\u0092\u0093\7u\2\2\u0093\u0094\7g\2\2\u0094\u0095")
        buf.write("\7n\2\2\u0095\u00a7\7h\2\2\u0096\u0097\7p\2\2\u0097\u0098")
        buf.write("\7g\2\2\u0098\u00a7\7y\2\2\u0099\u009a\7x\2\2\u009a\u009b")
        buf.write("\7q\2\2\u009b\u009c\7k\2\2\u009c\u00a7\7f\2\2\u009d\u009e")
        buf.write("\7e\2\2\u009e\u009f\7q\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1")
        buf.write("\7u\2\2\u00a1\u00a7\7v\2\2\u00a2\u00a3\7h\2\2\u00a3\u00a4")
        buf.write("\7w\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a7\7e\2\2\u00a6D\3")
        buf.write("\2\2\2\u00a6I\3\2\2\2\u00a6Q\3\2\2\2\u00a6S\3\2\2\2\u00a6")
        buf.write("W\3\2\2\2\u00a6Z\3\2\2\2\u00a6^\3\2\2\2\u00a6c\3\2\2\2")
        buf.write("\u00a6f\3\2\2\2\u00a6k\3\2\2\2\u00a6o\3\2\2\2\u00a6u\3")
        buf.write("\2\2\2\u00a6{\3\2\2\2\u00a6\177\3\2\2\2\u00a6\u0084\3")
        buf.write("\2\2\2\u00a6\u008f\3\2\2\2\u00a6\u0092\3\2\2\2\u00a6\u0096")
        buf.write("\3\2\2\2\u00a6\u0099\3\2\2\2\u00a6\u009d\3\2\2\2\u00a6")
        buf.write("\u00a2\3\2\2\2\u00a7\16\3\2\2\2\u00a8\u00bc\t\4\2\2\u00a9")
        buf.write("\u00aa\7(\2\2\u00aa\u00bc\7(\2\2\u00ab\u00ac\7~\2\2\u00ac")
        buf.write("\u00bc\7~\2\2\u00ad\u00ae\7?\2\2\u00ae\u00bc\7?\2\2\u00af")
        buf.write("\u00bc\7?\2\2\u00b0\u00b1\7#\2\2\u00b1\u00bc\7?\2\2\u00b2")
        buf.write("\u00bc\7>\2\2\u00b3\u00b4\7>\2\2\u00b4\u00bc\7?\2\2\u00b5")
        buf.write("\u00bc\7@\2\2\u00b6\u00b7\7@\2\2\u00b7\u00bc\7?\2\2\u00b8")
        buf.write("\u00b9\7<\2\2\u00b9\u00bc\7?\2\2\u00ba\u00bc\t\5\2\2\u00bb")
        buf.write("\u00a8\3\2\2\2\u00bb\u00a9\3\2\2\2\u00bb\u00ab\3\2\2\2")
        buf.write("\u00bb\u00ad\3\2\2\2\u00bb\u00af\3\2\2\2\u00bb\u00b0\3")
        buf.write("\2\2\2\u00bb\u00b2\3\2\2\2\u00bb\u00b3\3\2\2\2\u00bb\u00b5")
        buf.write("\3\2\2\2\u00bb\u00b6\3\2\2\2\u00bb\u00b8\3\2\2\2\u00bb")
        buf.write("\u00ba\3\2\2\2\u00bc\20\3\2\2\2\u00bd\u00be\t\6\2\2\u00be")
        buf.write("\22\3\2\2\2\u00bf\u00c1\t\7\2\2\u00c0\u00bf\3\2\2\2\u00c1")
        buf.write("\u00c2\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2")
        buf.write("\u00c3\u00c4\3\2\2\2\u00c4\u00c5\b\n\2\2\u00c5\24\3\2")
        buf.write("\2\2\u00c6\u00c7\13\2\2\2\u00c7\u00c8\b\13\3\2\u00c8\26")
        buf.write("\3\2\2\2\u00c9\u00ca\13\2\2\2\u00ca\30\3\2\2\2\u00cb\u00cc")
        buf.write("\13\2\2\2\u00cc\32\3\2\2\2\n\2\649@B\u00a6\u00bb\u00c2")
        buf.write("\4\b\2\2\3\13\2")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    IDENTIFIER = 5
    KEYWORDS = 6
    OPERATORS = 7
    SEPARATORS = 8
    WS = 9
    ERROR_CHAR = 10
    UNCLOSE_STRING = 11
    ILLEGAL_ESCAPE = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'bool'", "'string'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "KEYWORDS", "OPERATORS", "SEPARATORS", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "IDENTIFIER", "KEYWORDS", 
                  "OPERATORS", "SEPARATORS", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[9] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


