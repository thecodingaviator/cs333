/**
 * Test the free() function.
 *
 * Parth Parth
 * 2/10/2022
 */

#include <stdio.h>
#include <stdlib.h>

/* Have fun with memory allocation
 */
int main(int arg, char *argv[])
{
  for(int i=0; i!=-1; i++) {
    int *p = malloc(sizeof(int));
    free(p);
  }
  return 0;
}