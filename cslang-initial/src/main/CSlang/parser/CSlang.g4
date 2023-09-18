/** Student ID: 2011357 */
grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: constant EOF ; // grammar rule

// ID: [a-z]+; // token

constant: 'int' | 'float' | 'bool' | 'string';

IDENTIFIER: [A-Za-z_]+ ([A-Za-z_0-9])* | '@'[A-Za-z_0-9]+;

//Keywords

KEYWORDS: 'break' | 
'continue' | 
'if' | 
'else' | 
'for' | 
'true' |
'false' | 
'int' | 
'float' | 
'bool' | 
'string' | 
'return' | 
'null' |  
'class' | 
'constructor' | 
'var' | 
'self' | 
'new' | 
'void' | 
'const' | 
'func';

// BREAK : 'break';

// CONTINUE : 'continue';

// IF : 'if';

// ELSE : 'else';

// FOR : 'for';

// TRUE : 'true';

// FALSE : 'false';

// INT : 'int';

// FLOAT : 'float';

// BOOL : 'bool';

// STRING : 'string';

// RETURN : 'return';

// NULL : 'null';

// CLASS : 'class';

// CONSTRUCTOR : 'constructor';

// VAR : 'var';

// SELF : 'self';

// NEW : 'new';

// VOID : 'void';

// CONST : 'const';

// FUNC : 'func';

//Operators
OPERATORS: '+' | 
'-' | 
'*' | 
'/' | 
'\\' | 
'!' | 
'&&' | 
'||' | 
'==' | 
'=' | 
'!=' | 
'<' | 
'<=' | 
'>' | 
'>=' | 
':=' | 
'^' | 
'%';
// PLUS: '+';

// MINUS: '-';

// MULTIPLY: '*';

// DIVIDE_FLOAT: '/';

// DIVIDE_INT: '\\';

// DIFF: '!';

// AND: '&&';

// OR: '||';

// EQUAL: '==';

// DECLARE: '=';

// NEQ: '!=';

// LE: '<';

// LEQ: '<=';

// GE: '>';

// GEQ: '>=';

// ASSIGN: ':=';

// XOR: '^';

// MOD: '%';

//Separators
SEPARATORS: '(' | ')' | '[' | ']' | '.' | ',' | ';' | ':' | '{' | '}';

WS : [ \t\r\n\b\f]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;