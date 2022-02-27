/*
Parth Parth
2/24/2022
This program strips all HTML tags, going to a new line everything a <p> tag is found.
*/

%%

"<p>" printf("\n");
"<"[^>]*">" ;
[ \t\n]+ ;
"&gt;" {printf("%s", ">");} // Extension 2
"&lt;" {printf("%s", "<");} // Extension 2

%%

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