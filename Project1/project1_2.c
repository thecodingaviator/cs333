/**
 * Test how much memory can I access
 *
 * Parth Parth
 * 2/10/2022
 */

#include <stdio.h>
#include <stdlib.h>

/* Create some data and try to look for it
 */
int main(int arg, char *argv[])
{

  int i=133;
  int i1=133;
  int i2=133;
  unsigned char *ptr=(unsigned char *)&ptr;

  // access memory in sequence using ptr
  for (int k = 0; k < 10000000000000000; k++)
  {
    printf("%d: %02X\n", k, ptr[k]);
  }
  

  return 0;
}