//MSSV: 2053114
grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: classi EOF;
	/* PARSER */
classi: classdecl classi | ;
classdecl: CLASS superpart? IDENTIFIER LCB body RCB;
body: member body | ;
member: attr | methd;
hder: CONST | VAR;
attr: attrdc | attrndc;
attrdc: hder attlist SC;
attrndc: hder attrlist COLON typ SC;
attrlist: iden CM attrlist | iden;
attlist: iden CM attlist CM expr | iden COLON array? typ EQUAL expr;
//Type - Identifiers
typ: INT | FLOAT | BOOL | STRING;
idenNoAtlist: IDENTIFIER CM idenNoAtlist | IDENTIFIER;
iden: ATIDENTIFIER | IDENTIFIER;
//Attributes

//Method
methd: funct | functcons;
//Function
funct: FUNC iden LB paramlist RB COLON (typ|VOID) blkstate;
functcons: FUNC CONSTRUCTOR LB paramlist RB blkstate;
//Parameters
paramlist: paramprime | ;
paramprime: param1 | param2;
param1: (IDENTIFIER COLON typ CM param1) | (IDENTIFIER COLON typ);
param2: (idenNoAtlist COLON typ CM param2) | (idenNoAtlist COLON typ);  
//Array Literals
boolit: TRUE|FALSE;
lits: INTLIT | FLOATLIT | boolit | STRINGLIT | array;
array: SLB arraylist SRB;
arraylist: lits CM arraylist | lits;
//Expressions:
operators: COMPEQ | DIFFROM | LESS | MOR | LESSEQ | MOREEQ;
logical: AND | OR;
adding: PLUS | MINUS;
multiplying: MULTI | DIVFLO | DIVINT | MODU;
    //EXPR
expr: expr1 SPACING expr1 | expr1;
expr1: expr2 operators expr2 | expr2;
expr2: expr2 logical expr3 | expr3;
expr3: expr3 adding expr4 | expr4;
expr4: expr4 multiplying expr5 | expr5;
expr5: DIFF expr5 | expr6;
expr6: MINUS expr6 | expr7;
expr7: expr8 SLB expr SRB | expr8;
    //Member Access
expr8: expr8 DOT IDENTIFIER array? | expr8 DOT IDENTIFIER array? LB exprlist RB | expr9;
expr9: (IDENTIFIER DOT)? ATIDENTIFIER array? | (IDENTIFIER DOT)? ATIDENTIFIER array? LB exprlist RB | expr10;
expr10: new | expr11;
expr11: LB expr RB | expr12;
expr12: lits | iden | SELF;

//New Idenfier
new: NEW iden LB exprlist RB;
exprlist: exprlst | ;
exprlst: expr CM exprlst | expr;

//Blockstate
blkstate: LCB stmtlist RCB;
stmtlist: stmt stmtlist | ;
stmt: declstmt | assstmt | ifstmt | forstmt | breakstmt | contstmt | retstmt | metdinvoke | blkstate;
    //Statements
declstmt: (VAR | CONST) (attrlist COLON typ SC | attlist SC);
assstmt: (iden array? | metdinvoke) ASSIGN expr SC;
ifstmt: IF blkstate? expr blkstate (ELSE blkstate)?;
        //For Statement
initstmt: IDENTIFIER array? ASSIGN INTLIT;
condstmt: IDENTIFIER array? operators (INTLIT | IDENTIFIER array?);
poststmt: IDENTIFIER array? ASSIGN IDENTIFIER array? (adding | multiplying) (INTLIT | IDENTIFIER array?);
forstmt: FOR initstmt SC condstmt SC poststmt blkstate;
breakstmt: BREAK SC;
contstmt: CONTINUE SC;
retstmt: RETURN (expr | iden)? SC;
metdinvoke: (IDENTIFIER DOT)? ATIDENTIFIER LB exprlist RB SC;
superpart: IDENTIFIER '<-';
	/* LEXER */
//Comments:
COMMENT: (('//'.*? ('\n'|EOF)) | ('/*'.*?'*/')) -> skip; //skip comments 

//Keyword - Identifier: 
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
FOR: 'for';
TRUE: 'true';
FALSE: 'false';
INT: 'int';
FLOAT: 'float';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
NULL: 'null';
CLASS: 'class';
CONSTRUCTOR: 'constructor';
VAR: 'var';
SELF: 'self';
NEW: 'new';
VOID: 'void';
CONST: 'const';
FUNC: 'func';

//Operators - Separators:
PLUS: '+';
MINUS: '-';
MULTI: '*';
DIVFLO: '/';
DIVINT: '\\';
DIFFROM: '!=';
DIFF: '!';
AND: '&&';
OR: '||';
COMPEQ: '==';
ASSIGN: ':=';
EQUAL: '=';
LESSEQ: '<=';
LESS: '<';
MOREEQ: '>=';
MOR: '>';
SPACING: '^';
MODU: '%';

LB: '(';
RB: ')';
SLB: '[';
SRB: ']';
DOT: '.';
CM: ',';
SC: ';';
COLON: ':';
LCB: '{';
RCB: '}';


ATIDENTIFIER: '@'[A-Za-z0-9_]+;
IDENTIFIER: [A-Za-z_][A-Za-z0-9_]*;

//Literals:
fragment Int: [0-9]+;
INTLIT: Int;
fragment Decimal: '.'Int*;
fragment Exponent: [eE]([-+]?)Int+;
FLOATLIT: Int Decimal | Int Decimal? Exponent;
	//String Literal
fragment ESCSEQ: ('\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\"' | '\\\\');
fragment CHARLIT: ~["\\\r\nEOF] | ESCSEQ;
STRINGLIT: '"'CHARLIT*'"' {self.text = self.text[1:-1]};

//Original Code
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ILLEGAL_ESCAPE: ( '"' CHARLIT* ('\\'(~[bfrnt"\\])))
{
    self.text = self.text[1:]
    raise IllegalEscape(self.text)
};
UNCLOSED_STRING: ('"' CHARLIT*)
{ 
    self.text = self.text[1:]
    raise UncloseString(self.text)
};
ERROR_CHAR: .{raise ErrorToken(self.text)};
