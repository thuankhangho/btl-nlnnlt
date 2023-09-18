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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\34")
        buf.write("\u00c1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\3\2\6\29\n\2\r\2\16\2:")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\6\30\u00b5\n\30\r\30\16\30\u00b6\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\2\2\34\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\3")
        buf.write("\2\4\3\2c|\5\2\13\f\17\17\"\"\2\u00c2\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\38\3\2\2\2\5<\3\2\2")
        buf.write("\2\7B\3\2\2\2\tK\3\2\2\2\13N\3\2\2\2\rS\3\2\2\2\17W\3")
        buf.write("\2\2\2\21\\\3\2\2\2\23b\3\2\2\2\25f\3\2\2\2\27l\3\2\2")
        buf.write("\2\31q\3\2\2\2\33x\3\2\2\2\35\177\3\2\2\2\37\u0084\3\2")
        buf.write("\2\2!\u008a\3\2\2\2#\u0096\3\2\2\2%\u009a\3\2\2\2\'\u009f")
        buf.write("\3\2\2\2)\u00a3\3\2\2\2+\u00a8\3\2\2\2-\u00ae\3\2\2\2")
        buf.write("/\u00b4\3\2\2\2\61\u00ba\3\2\2\2\63\u00bd\3\2\2\2\65\u00bf")
        buf.write("\3\2\2\2\679\t\2\2\28\67\3\2\2\29:\3\2\2\2:8\3\2\2\2:")
        buf.write(";\3\2\2\2;\4\3\2\2\2<=\7d\2\2=>\7t\2\2>?\7g\2\2?@\7c\2")
        buf.write("\2@A\7m\2\2A\6\3\2\2\2BC\7e\2\2CD\7q\2\2DE\7p\2\2EF\7")
        buf.write("v\2\2FG\7k\2\2GH\7p\2\2HI\7w\2\2IJ\7g\2\2J\b\3\2\2\2K")
        buf.write("L\7k\2\2LM\7h\2\2M\n\3\2\2\2NO\7g\2\2OP\7n\2\2PQ\7u\2")
        buf.write("\2QR\7g\2\2R\f\3\2\2\2ST\7h\2\2TU\7q\2\2UV\7t\2\2V\16")
        buf.write("\3\2\2\2WX\7v\2\2XY\7t\2\2YZ\7w\2\2Z[\7g\2\2[\20\3\2\2")
        buf.write("\2\\]\7h\2\2]^\7c\2\2^_\7n\2\2_`\7u\2\2`a\7g\2\2a\22\3")
        buf.write("\2\2\2bc\7k\2\2cd\7p\2\2de\7v\2\2e\24\3\2\2\2fg\7h\2\2")
        buf.write("gh\7n\2\2hi\7q\2\2ij\7c\2\2jk\7v\2\2k\26\3\2\2\2lm\7d")
        buf.write("\2\2mn\7q\2\2no\7q\2\2op\7n\2\2p\30\3\2\2\2qr\7u\2\2r")
        buf.write("s\7v\2\2st\7t\2\2tu\7k\2\2uv\7p\2\2vw\7i\2\2w\32\3\2\2")
        buf.write("\2xy\7t\2\2yz\7g\2\2z{\7v\2\2{|\7w\2\2|}\7t\2\2}~\7p\2")
        buf.write("\2~\34\3\2\2\2\177\u0080\7p\2\2\u0080\u0081\7w\2\2\u0081")
        buf.write("\u0082\7n\2\2\u0082\u0083\7n\2\2\u0083\36\3\2\2\2\u0084")
        buf.write("\u0085\7e\2\2\u0085\u0086\7n\2\2\u0086\u0087\7c\2\2\u0087")
        buf.write("\u0088\7u\2\2\u0088\u0089\7u\2\2\u0089 \3\2\2\2\u008a")
        buf.write("\u008b\7e\2\2\u008b\u008c\7q\2\2\u008c\u008d\7p\2\2\u008d")
        buf.write("\u008e\7u\2\2\u008e\u008f\7v\2\2\u008f\u0090\7t\2\2\u0090")
        buf.write("\u0091\7w\2\2\u0091\u0092\7e\2\2\u0092\u0093\7v\2\2\u0093")
        buf.write("\u0094\7q\2\2\u0094\u0095\7t\2\2\u0095\"\3\2\2\2\u0096")
        buf.write("\u0097\7x\2\2\u0097\u0098\7c\2\2\u0098\u0099\7t\2\2\u0099")
        buf.write("$\3\2\2\2\u009a\u009b\7u\2\2\u009b\u009c\7g\2\2\u009c")
        buf.write("\u009d\7n\2\2\u009d\u009e\7h\2\2\u009e&\3\2\2\2\u009f")
        buf.write("\u00a0\7p\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7y\2\2\u00a2")
        buf.write("(\3\2\2\2\u00a3\u00a4\7x\2\2\u00a4\u00a5\7q\2\2\u00a5")
        buf.write("\u00a6\7k\2\2\u00a6\u00a7\7f\2\2\u00a7*\3\2\2\2\u00a8")
        buf.write("\u00a9\7e\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab\7p\2\2\u00ab")
        buf.write("\u00ac\7u\2\2\u00ac\u00ad\7v\2\2\u00ad,\3\2\2\2\u00ae")
        buf.write("\u00af\7h\2\2\u00af\u00b0\7w\2\2\u00b0\u00b1\7p\2\2\u00b1")
        buf.write("\u00b2\7e\2\2\u00b2.\3\2\2\2\u00b3\u00b5\t\3\2\2\u00b4")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b7\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\b")
        buf.write("\30\2\2\u00b9\60\3\2\2\2\u00ba\u00bb\13\2\2\2\u00bb\u00bc")
        buf.write("\b\31\3\2\u00bc\62\3\2\2\2\u00bd\u00be\13\2\2\2\u00be")
        buf.write("\64\3\2\2\2\u00bf\u00c0\13\2\2\2\u00c0\66\3\2\2\2\5\2")
        buf.write(":\u00b6\4\b\2\2\3\31\2")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    BREAK = 2
    CONTINUE = 3
    IF = 4
    ELSE = 5
    FOR = 6
    TRUE = 7
    FALSE = 8
    INT = 9
    FLOAT = 10
    BOOL = 11
    STRING = 12
    RETURN = 13
    NULL = 14
    CLASS = 15
    CONSTRUCTOR = 16
    VAR = 17
    SELF = 18
    NEW = 19
    VOID = 20
    CONST = 21
    FUNC = 22
    WS = 23
    ERROR_CHAR = 24
    UNCLOSE_STRING = 25
    ILLEGAL_ESCAPE = 26

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'break'", "'continue'", "'if'", "'else'", "'for'", "'true'", 
            "'false'", "'int'", "'float'", "'bool'", "'string'", "'return'", 
            "'null'", "'class'", "'constructor'", "'var'", "'self'", "'new'", 
            "'void'", "'const'", "'func'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", 
            "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", "CLASS", 
            "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", "CONST", "FUNC", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "ID", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", 
                  "FALSE", "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", 
                  "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", 
                  "CONST", "FUNC", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
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
            actions[23] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


