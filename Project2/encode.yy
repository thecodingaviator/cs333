/*
Parth Parth
2/24/2022
An encoder that moves input ahead by 13 characters with a wrap around after z/Z
*/

alphabet  [a-zA-Z]

%%

{alphabet}  {
  int a = (int) yytext[0];
  /* will have to check separately for both a-z and A-Z because letters like V will spillover otherwise */
  if(a >= 'A' && a <= 'Z') {
    a += 13;
    if(a > 'Z') {
      a -= 26;
    }
  }
  if(a >= 'a' && a <= 'z') {
    a += 13;
    if(a > 'z') {
      a -= 26;
    }
  }
  printf("%c", a);
  }

%%

int main ( int argc, char *argv[] ) {
 
  yylex();
  
  return 0;

}
