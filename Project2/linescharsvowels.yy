/*
Parth Parth
2/24/2022
Takes in the name of a file and prints the number of lines, words and vowels in the file.
*/

%{
  int lines = 0, chars = 0, vowels = 0;
%}

%%

\n    ++lines; ++chars;
[aeiou]    ++chars; ++vowels;
.     ++chars;

%%

int yywrap() {}
int main()
{

  FILE *fp;
  char filename[255];
  printf("Filename: ");
  scanf("%s",filename);
  fp = fopen(filename,"r");
  yyin = fp;

  yylex();

  /* Adding 1 to lines because the last line will have no \n chars */
  printf( "Lines = %d, Chars = %d, Vowels = %d\n", lines + 1, chars, vowels );
  
  return 0;

}
