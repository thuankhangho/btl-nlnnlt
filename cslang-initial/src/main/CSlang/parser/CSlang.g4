/* Student ID: 2011357 */
grammar CSlang;

@lexer::header {
	from lexererr import *
}

options{
	language=Python3;
}

program: constant EOF ; // grammar rule

// ID: [a-z]+; // token

constant: INT | FLOAT | BOOL | STRING;

classdecl: CLASS superpart? IDENTIFIER memberlist;

memberlist: LCB memberprime RCB;

memberprime: (member memberlist | member);

superpart: IDENTIFIER '<-';

member: attribute | method;

attribute: (CONST | VAR) attributename;

attributename: ;

method: ;

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

DIFF: '!';

AND: '&&';

OR: '||';

EQUAL: '==';

DECLARE: '=';

NEQ: '!=';

LE: '<';

LEQ: '<=';

GE: '>';

GEQ: '>=';

ASSIGN: ':=';

XOR: '^';

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


// INT: [0-9]+;

// FLOAT: INT DEC | INT DEC EXP;

// fragment DEC: '.'?[0-9]+;

// fragment EXP: [Ee][+-][0-9]+;

// BOOL: 'true'|'false';

IDENTIFIER: [A-Za-z_]+ ([A-Za-z_0-9])* | '@'[A-Za-z_0-9]+;

// COMMENT: '//'.?'\n' | '/*'.?'*/' -> skip;

WS : [ \t\r\n\b\f]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;