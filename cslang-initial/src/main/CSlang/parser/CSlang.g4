/* Student ID: 2011357 */

//to do: method declaration & stuff
grammar CSlang;

@lexer::header {
    from lexererr import *
}

options{
    language=Python3;
}

program: classdecl+ EOF ;

classdecl: CLASS superpart? IDENTIFIER LCB memberlist RCB;

memberlist: member memberlist | ;

member: attribute | method;

attribute: attributewithdeclare | attributenodeclare;

attributenodeclare: (CONST | VAR) attributelist COLON typ SM;

attributewithdeclare: (CONST | VAR) attlist SM;

typ: BOOL | INT | FLOAT | STRING;

attlist: IDENTIFIER CM attlist CM exp | IDENTIFIER COLON typ DECLARE exp;
//id comma comma expr
//id comma id : type = expr

attributelist: IDENTIFIER CM attributelist | IDENTIFIER;

method: FUNC (ID | ATIDENTIFIER) LRB parameterlist RRB COLON typ blockstate;

parameterlist: parameterprime | ;

parameterprime: parameterpart1 | parameterpart2;

parameterpart1: (IDENTIFIER COLON typ) CM parameterprime | (IDENTIFIER COLON typ);

parameterpart2: (identifierlist COLON typ) CM identifierlist | (identifierlist COLON typ);

identifierlist: identifierprime | ;

identifierprime: IDENTIFIER CM identifierprime | IDENTIFIER;

constructor: FUNC CONSTRUCTOR LRB parameterlist RRB blockstate;

superpart: IDENTIFIER '<-';

literal: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | arraylit;

arraylit: LSB literallist RSB;

literallist: (INTLIT | FLOATLIT | BOOLLIT | STRINGLIT) CM literallist | (INTLIT | FLOATLIT | BOOLLIT | STRINGLIT);

arraydecl: LSB ARRAYSIZE RSB typ;

objdecl: NEW IDENTIFIER LRB RRB;

//Expressions
explist: exp CM explist | exp;

nullableexplist: expprime |;

expprime: exp CM expprime | exp;

relational: EQUAL | NEQ | LE | GE | LEQ | GEQ;

logical: AND | OR;

adding: PLUS | MINUS;

multiplying: MULTIPLY | DIVIDE_FLOAT | DIVIDE_INT | MOD;

exp: exp1 CONCAT exp1 | exp1;

exp1: exp2 relational exp2 | exp2;

exp2: exp2 logical exp3 | exp3;

exp3: exp3 adding exp4 | exp4;

exp4: exp4 multiplying exp5 | exp5;

exp5: DIFF exp6 | exp6;

exp6: MINUS exp7 | exp7;

exp7: exp8 LSB RSB | exp8;

exp8: exp8 DOT exp9 | exp9;

exp9: exp10 DOT exp10 | exp10;

exp10: NEW exp11 | exp11;

exp11: literal;

//Statements
varstate: VAR (attributelist COLON typ SM|attlist SM);

constate: CONST (attributelist COLON typ SM|attlist SM);

assignstate: exp ASSIGN exp SM;

ifstate: IF blockstate? exp blockstate (ELSE blockstate)?;

forstate: FOR assignstate exp SM blockstate;

breakstate: BREAK SM;

continuestate: CONTINUE SM;

returnstate: RETURN (exp) SM;

instanceattributestate: exp DOT IDENTIFIER SM;

staticattributestate: (IDENTIFIER DOT)? ATIDENTIFIER SM;

instancemethodstate: exp DOT IDENTIFIER (nullableexplist);

staticmethodstate: (IDENTIFIER DOT)? ATIDENTIFIER (nullableexplist);

// createobjectstate: NEW IDENTIFIER LRB nullableexplist RRB;

blockstate: LCB stmtlist RCB;

stmtlist: noatstmt stmtlist | ;

noatstmt: noatstmtnodeclare | noatstmtwithdeclare;

noatstmtnodeclare: (CONST | VAR) attributelist1 COLON typ SM;

noatstmtwithdeclare: (CONST | VAR) attlist1 SM;

attlist1: ID CM attlist CM exp | ID COLON typ DECLARE exp;
//id comma comma expr
//id comma id : type = expr

attributelist1: ID CM attributelist | ID;

//Keywords

// KEYWORDS: 'break' | 
// 'continue' | 
// 'if' | 
// 'else' | 
// 'for' | 
// 'true' |
// 'false' | 
// 'int' | 
// 'float' | 
// 'bool' | 
// 'string' | 
// 'return' | 
// 'null' |  
// 'class' | 
// 'constructor' | 
// 'var' | 
// 'self' | 
// 'new' | 
// 'void' | 
// 'const' | 
// 'func';

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
// OPERATORS: '+' | 
// '-' | 
// '*' | 
// '/' | 
// '\\' | 
// '!' | 
// '&&' | 
// '||' | 
// '==' | 
// '=' | 
// '!=' | 
// '<' | 
// '<=' | 
// '>' | 
// '>=' | 
// ':=' | 
// '^' | 
// '%';
PLUS: '+';

MINUS: '-';

MULTIPLY: '*';

DIVIDE_FLOAT: '/';

DIVIDE_INT: '\\';

AND: '&&';

OR: '||';

EQUAL: '==';

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
// SEPARATORS: '(' | ')' | '[' | ']' | '.' | ',' | ';' | ':' | '{' | '}';

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
INTLIT: '0' | [1-9][0-9]*;

FLOATLIT: INTLIT DEC | INTLIT DEC EXP;

fragment DEC: '.'?[0-9]+;

fragment EXP: [Ee][+-][0-9]+;

BOOLLIT: TRUE | FALSE;

fragment ESCAPESEQ: '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\"' | '\\\\';

fragment CHAR_LIT: ~["\\\r\n'] | ESCAPESEQ | '\'"';

STRINGLIT: '"' CHAR_LIT* '"' {self.text = self.text[1:-1]};

BLOCKCMT: '//*' .? '*//' -> skip;

LINECMT: '///' .*? ('\n'|EOF) -> skip;

IDENTIFIER: [A-Za-z_] ([A-Za-z_0-9])* | '@'[A-Za-z_0-9]+ | SELF;

ID: [A-Za-z_] ([A-Za-z_0-9])*;

ATIDENTIFIER: '@' [A-Za-z_0-9]+;

ARRAYSIZE: [1-9][0-9]*;

// COMMENT: '//'.?'\n' | '/*'.?'*/' -> skip;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSED_STRING: ( '"' ('\'"' | '\\' [btnfr'\\] | ~[\r\t\n\\"] )* ) {self.text = self.text[1:]; raise UncloseString(self.text)};
ILLEGAL_ESCAPE: ( '"' ('\\'[bfrnt\\'] | ~[\n\r\\"])* ('\\'(~[bfrnt'\\]))) {self.text = self.text[1:]; raise IllegalEscape(self.text)};