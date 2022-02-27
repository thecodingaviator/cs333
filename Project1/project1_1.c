/**
 * Memory access
 *
 * Parth Parth
 * 2/7/2022
 */

#include <stdio.h>
#include <stdlib.h>

/* To allocate memory on the heap for an int and make ptr point to it to look at the heap */
int main(int arg, char *argv[])
{

  unsigned char *ptr;

  printf("char\n");
  // assign a to the char
  char c = 'a';
  // assign the address of c to ptr
  ptr = (unsigned char *)&(c);
  // print the value of the char byte-by-byte
  for(int i=0; i<sizeof(char); i++) {
    printf("%d: %02X\n", i, ptr[i]);
  }

  // repeat for other data types
  printf("short\n");
  short s = 789;
  ptr = (unsigned char *)&(s);
  for(int i=0; i<sizeof(short); i++) {
    printf("%d: %02X\n", i, ptr[i]);
  }

  printf("int\n");
  int i = 10;
  ptr = (unsigned char *)&(i);
  for(int i=0; i<sizeof(int); i++) {
    printf("%d: %02X\n", i, ptr[i]);
  }

  printf("long\n");
  long l = 12785639;
  ptr = (unsigned char *)&(l);
  for(int i=0; i<sizeof(long); i++) {
    printf("%d: %02X\n", i, ptr[i]);
  }

  printf("float\n");
  float f = 18678.578678;
  ptr = (unsigned char *)&(f);
  for(int i=0; i<sizeof(float); i++) {
    printf("%d: %02X\n", i, ptr[i]);
  }

  printf("double\n");
  double d = 12785639.6589;
  ptr = (unsigned char *)&(d);
  for(int i=0; i<sizeof(double); i++) {
    printf("%d: %02X\n", i, ptr[i]);
  }

  return 0;
}
