//Student ID: 2052496
//Name: Nguyễn Khánh Huy
grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: class_declarelist EOF ;

class_declarelist: class_declare class_declarelist | ;
class_declare: CLASS superX IDENTIFIER LC list_of_member RC;
list_of_member: member list_of_member | ;
member: attribute | method;
attribute: attributeconst | attributevar;

attributeconst: CONST attributedecl SM;
attributevar: VAR attributedecl SM;
attributedecl: attribute1 | attribute2;

attribute1: list_of_attribute CL typeorarrtype;
list_of_attribute: xdd CM list_of_attribute | xdd;

attribute2: list_of_a;
list_of_a: xdd CM list_of_a CM exp | xdd CL typeorarrtype DECLARE exp ;

method: FUNC xdd LB list_of_param RB CL typev block_statement | constructor;
list_of_param: list_of_param1 | list_of_param2;
list_of_param1: primee | ;
primee: param_declare CM primee | param_declare ;
param_declare: IDENTIFIER CL typee ;
list_of_param2: primeme | ;
primeme: list_of_identifier CM primeme | list_of_identifier ;
list_of_identifier: (primy | ) CL typee;
primy: IDENTIFIER CM primy | IDENTIFIER ;
constructor: FUNC CONSTRUCTOR LB list_of_param RB block_statement ;
typee: BOOL | INT | FLOAT | STRING | IDENTIFIER;
typev: BOOL | INT | FLOAT | STRING | VOID | IDENTIFIER;
arr_type: LS INTLIT RS typee ;
class_type: NEW IDENTIFIER LS RS;
typeorarrtype: typee|arr_type;

list_of_exp: primu | ;
primu: exp CM primu | exp;
exp: exp1 CONCAT exp1 | exp1;
exp1: exp2 (EQUAL | DIFFER | SMOL | BIG | SMOL_EQUAL | BIG_EQUAL) exp2| exp2;
exp2: exp2 (AND | OR) exp3| exp3 ;
exp3: exp3 (PLUS | MINUS) exp4 | exp4 ;
exp4: exp4 (MULTIPLE | DIVIDE_FLOAT | DIVIDE_INT | MOD) exp5 | exp5 ;
exp5: CHAMTHAN exp5 | exp6 ;
exp6: MINUS exp6 | exp7 ;
exp7: exp8 LS exp RS | exp8 ;
exp8: exp8 DOT IDENTIFIER( LB list_of_exp RB | ) | exp9 ;
exp9: (IDENTIFIER DOT | ) AT_ID | (IDENTIFIER DOT | ) AT_ID LB list_of_exp RB | exp10;
exp10: NEW IDENTIFIER LB list_of_exp RB | exp11 ;
exp11: LB exp RB | exp12;
exp12: literal | arrlit | xdd | SELF ;
literal: INTLIT | FLOATLIT | BOOLLIT | STRLIT | SELF | NULL | arrlit | xdd;
var_const_statement: attribute ;
ass_statement: assex_statement SM ;
assex_statement: lhs ASSIGN exp;
lhs: IDENTIFIER | exp8 |  IDENTIFIER LS exp RS ;
if_statement: IF (block_statement |) exp block_statement (ELSE block_statement |) ;
for_statement: FOR ass_statement exp SM assex_statement block_statement ;
break_statement:BREAK SM;
continue_statement:CONTINUE SM ;
return_statement: RETURN (exp | ) SM ;
method_invocation_statement: instance_method_invocation|static_method_invocation SM ;
instance_method_invocation:exp DOT IDENTIFIER LB list_of_exp RB ;
static_method_invocation: (IDENTIFIER DOT |) AT_ID LB list_of_exp RB  ;
block_statement: LC list_of_statement RC ;
list_of_statement: statement list_of_statement | ;
statement:var_const_statement | ass_statement | if_statement | for_statement | break_statement | continue_statement | 
return_statement | method_invocation_statement | block_statement;
xdd:IDENTIFIER | AT_ID;
superX: IDENTIFIER '<-' | ;
arrlit: LS arr RS ;
arr:literal CM arr|literal;


BREAK:'break';
TRUE:'true';
STRING:'string';
VAR:'var';
FUNC:'func';
CONTINUE:'continue';
FALSE:'false';
RETURN:'return';
SELF:'self';
IF:'if';
INT:'int';
NULL:'null';
NEW:'new';
ELSE:'else';
FLOAT:'float';
CLASS:'class';
VOID:'void';
FOR:'for';
BOOL:'bool';
CONSTRUCTOR:'constructor';
CONST:'const';

PLUS:'+';
MINUS:'-';
MULTIPLE:'*';
DIVIDE_FLOAT:'/';
DIVIDE_INT:'\\';
CHAMTHAN:'!';
AND:'&&';
OR:'||';
EQUAL:'==';
DECLARE:'=';
DIFFER:'!=';
SMOL:'<';
SMOL_EQUAL:'<=';
BIG:'>';
BIG_EQUAL:'>=';
ASSIGN:':=';
CONCAT:'^';
MOD:'%';

LB:'(';
RB:')';
LS:'[';
RS:']';
DOT:'.';
CM:',';
SM:';';
CL:':';
LC:'{';
RC:'}';
BLOCK_COMMENT: '/*' .*? '*/' -> skip ;
LINE_COMMENT: '//'.*? ( '\n' | EOF ) -> skip ;

IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]* ;
AT_ID: '@'[a-zA-Z_0-9]+;
INTLIT:[0-9]+;
FLOATLIT:INTPART DEC | INTPART DEC? EXP;
fragment INTPART: [0-9]+;
fragment DEC: '.' [0-9]*;
fragment EXP: [eE] [+-]? [0-9]+;
BOOLLIT: TRUE | FALSE ;
STRLIT: '"' CHARS* '"' {self.text = self.text[1:-1]};
fragment CHARS: ~['"\\\r\nEOF] | ESC_SEQ | '\\"';
fragment ESC_SEQ: '\\b'|'\\f'|'\\r'|'\\n'|'\\t'|'\\"'|'\\\\' ;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


UNCLOSE_STRING: '"' CHARS* {self.text=self.text[1:]; raise UncloseString(self.text)};
ILLEGAL_ESCAPE: ( '"' ('\\'[bfrnt\\'] | ~[\n\r\\"])* ('\\'(~[bfrnt'\\]))) {self.text = self.text[1:]; raise IllegalEscape(self.text)};
ERROR_CHAR: .{raise ErrorToken(self.text)};