/**
 * Find the number to which i can add one and get the same number (Extension)
 *
 * Parth Parth
 * 2/10/2022
 */

#include <stdio.h>
#include <stdlib.h>

int main(int arg, char *argv[])
{
  float a=0xFFFFFFE;
  float b=a;
  a+=1;
  printf("%f\n", b-a);
  return 0;
}