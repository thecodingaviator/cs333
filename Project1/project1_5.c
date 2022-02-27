/**
 * Test strcpy
 *
 * Parth Parth
 * 2/10/2022
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Have fun with memory allocation
 */
int main(int arg, char *argv[])
{

  char str1[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  // Extension 2:
  // if there is a command line argument, copy it to str2
  if (arg > 1)
  {
    strcpy(str1, argv[1]);
  }
  
  char str2[5];
  int x=0;
  strcpy(str2, str1);

  // print str2 byte-by-byte
  for (int i = 0; i < sizeof(str1); i++)
  {
    printf("%d: %c\n", i, str2[i]);
  }

  if(x==0) {
    printf("safe\n");
  }
  else {
    printf("hacked\n");
  }

  return 0;
}