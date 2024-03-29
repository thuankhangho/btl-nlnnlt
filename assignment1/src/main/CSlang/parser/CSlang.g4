// Student ID: 2011357
// Name: Ho Thuan Khang
grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decllist EOF ;

//Parser

decllist: decl decllist | ;

decl: classdecl;

identifier: ID | ATIDENTIFIER;

classdecl: CLASS (superpart | ) ID LCB memberlist RCB;

memberlist: member memberlist | ;

member: attributedecl | methoddecl;

attributedecl: attributewithdeclare | attributenodeclare;

attributenodeclare: (CONST | VAR) attributelist COLON (typ | arraydecl) SM;

attributewithdeclare: (CONST | VAR) attlist SM;

attlist: identifier CM attlist CM exp | identifier COLON (typ | arraydecl) DECLARE exp;
//id comma comma expr
//id : type = expr

attributelist: identifier CM attributelist | identifier;

methoddecl: FUNC (ID | ATIDENTIFIER) LRB parameterlist RRB COLON (typ | VOID | arraydecl) blockstate;

parameterlist: parameterprime | ;

parameterprime: parameterpart1 | parameterpart2;

parameterpart1: (ID COLON typ) CM parameterpart1 | (ID COLON typ);

parameterpart2: (identifierlist COLON typ) CM parameterpart2 | (identifierlist COLON typ);

identifierlist: identifierprime | ;

identifierprime: ID CM identifierprime | ID;

constructor: FUNC CONSTRUCTOR LRB parameterlist RRB blockstate;

superpart: ID '<-';

literal: INTLIT | FLOATLIT | boolit | STRINGLIT | arraylit;

boolit: TRUE | FALSE;

literallist: (INTLIT | FLOATLIT | boolit | STRINGLIT | NULL) CM literallist | (INTLIT | FLOATLIT | boolit | STRINGLIT | NULL);

arraydecl: LSB INTLIT RSB typ;

typ: BOOL | INT | FLOAT | STRING | ID;

objdecl: NEW ID LRB RRB;

//Expressions
// instanceattributestate: exp DOT identifier;

// staticattributestate: (ID DOT)? ATIDENTIFIER;

instancemethodstate: exp DOT ID LRB nullableexplist RRB;

staticmethodstate: (ID DOT | ) ATIDENTIFIER LRB nullableexplist RRB;

nullableexplist: expprime |;

expprime: exp CM expprime | exp;

relational: EQ | NEQ | LE | GE | LEQ | GEQ;

logical: AND | OR;

adding: PLUS | MINUS;

multiplying: MULTIPLY | DIVIDE_FLOAT | DIVIDE_INT | MOD;

exp: exp1 CONCAT exp1 | exp1;

exp1: exp2 relational exp2 | exp2;

exp2: exp2 logical exp3 | exp3;

exp3: exp3 adding exp4 | exp4;

exp4: exp4 multiplying exp5 | exp5;

exp5: DIFF exp5 | exp6;

exp6: MINUS exp6 | exp7;

exp7: exp8 LSB exp RSB | exp8;

exp8: exp8 DOT ID (LRB nullableexplist RRB | ) | exp9;

exp9: (ID DOT | ) ATIDENTIFIER | (ID DOT | ) ATIDENTIFIER LRB nullableexplist RRB | exp10;

exp10: NEW ID LRB nullableexplist RRB | exp11;

exp11: LRB exp RRB | exp12;

exp12: literal | identifier | SELF;

//Statements
// varstate: VAR (attributelist COLON typ SM | attlist SM);

// constate: CONST (attributelist COLON typ SM | attlist SM);

assignstate: exp ASSIGN exp SM;

ifstate: IF (blockstate | ) exp blockstate (ELSE blockstate | );

forstate: FOR assignstate (exp SM) (exp ASSIGN exp) blockstate;

breakstate: BREAK SM;

continuestate: CONTINUE SM;

returnstate: RETURN (exp | ) SM;

methodinvoke: (instancemethodstate | staticmethodstate) SM;

blockstate: LCB stmtlist RCB;

stmtlist: stmt stmtlist | ;

stmt: attributedecl | assignstate | ifstate | forstate | breakstate | continuestate
| returnstate | methodinvoke | blockstate;

arraylit: LSB literallist RSB;

//Lexer
BREAK : 'break';

CONTINUE : 'continue';

IF : 'if';

ELSE : 'else';

FOR : 'for';

TRUE : 'true';

FALSE : 'false';

INT : 'int';

FLOAT : 'float';

BOOL : 'bool';

STRING : 'string';

RETURN : 'return';

NULL : 'null';

CLASS : 'class';

CONSTRUCTOR : 'constructor';

VAR : 'var';

SELF : 'self';

NEW : 'new';

VOID : 'void';

CONST : 'const';

FUNC : 'func';

//Operators
PLUS: '+';

MINUS: '-';

MULTIPLY: '*';

DIVIDE_FLOAT: '/';

DIVIDE_INT: '\\';

AND: '&&';

OR: '||';

EQ: '==';

ASSIGN: ':=';

NEQ: '!=';

LEQ: '<=';

GEQ: '>=';

DIFF: '!';

DECLARE: '=';

LE: '<';

GE: '>';

CONCAT: '^';

MOD: '%';

//Separators
LRB: '(';

RRB: ')';

LSB: '[';

RSB: ']';

DOT: '.';

CM: ',';

SM: ';';

COLON: ':';

LCB: '{';

RCB: '}';

//Literals
INTLIT: [0-9]+;

FLOATLIT: INTLIT DEC | INTLIT DEC? EXP;

STRINGLIT: '"' CHAR_LIT* '"' {self.text = self.text[1:-1]};

BLOCKCMT: '/*' .*? '*/' -> skip;

LINECMT: '//' .*? ('\n'|EOF) -> skip;

ID: [A-Za-z_] [A-Za-z_0-9]*;

ATIDENTIFIER: '@' [A-Za-z_0-9]+;

fragment DEC: '.'?[0-9]*;

fragment EXP: [Ee][+-]?[0-9]+;

fragment ESCAPESEQ: '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\"' | '\\\\';

fragment CHAR_LIT: ~["\\\r\n] | ESCAPESEQ | '\\"';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSED_STRING: '"' CHAR_LIT* {self.text = self.text[1:]; raise UncloseString(self.text)};
ILLEGAL_ESCAPE: '"' ('\\'[bfrnt\\'] | ~[\n\r\\"])* ('\\'(~[bfrnt'\\])) {self.text = self.text[1:]; raise IllegalEscape(self.text)};
ERROR_CHAR: . {raise ErrorToken(self.text)};