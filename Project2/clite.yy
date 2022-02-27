/*
Parth Parth
2/24/2022
A parser for Clite
*/

KEYWORD if|else|while|for|int|float
COMPARISON [==|<|>|<=|>=]
DIGIT [0-9]
OPERATOR [+|-|*|/]

%%

\/\*(.|\n)*\*\/ ;
" "* ;
\n ;
{KEYWORD} printf("Keyword-%s\n", yytext);
{DIGIT}+\.{DIGIT}* printf("Float-%s\n", yytext);
{DIGIT}+ printf("Integer-%s\n", yytext);
[_a-zA-Z0-9]{1,31} printf("Identifier-%s\n", yytext);
= printf("Assignment\n");
{COMPARISON} printf("Comparison-%s\n", yytext);
{OPERATOR} printf("Operator-%s\n", yytext);
\{ printf("Open-bracket\n");
\} printf("Close-bracket\n");
\( printf("Open-paren\n");
\) printf("Close-paren\n");
"\*"[^"*/"]*"*/" ; // Extension 1
; ;

%% 

int yywrap() {}
int main()
{

  FILE *fp;
  char filename[255];
  printf("Filename: ");
  scanf("%s",filename);
  fp = fopen(filename, "r");
  yyin = fp;

  yylex();
  
  return 0;

}
