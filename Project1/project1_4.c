/**
 * Check for inconsistencies in struct
 *
 * Parth Parth
 * 2/10/2022
 */

#include <stdio.h>
#include <stdlib.h>

/* Define and use a struct
 */

struct Test
{
  short s1;
  short s2;
  char c;
};

int main(int arg, char *argv[])
{
  // allocate memory for struct
  struct Test p = {1, 1, 'a'}; //(Test *)malloc(sizeof(Test));
  // p->s1 = 1;
  // p->s2 = 2;
  // p->c = 'a';

  unsigned char *ptr;
  ptr = (unsigned char *)&(p);

  printf("sizeof(struct Test): %d\n", sizeof(struct Test));
  printf("sizeof(ptr): %d\n", sizeof(ptr));

  // print the value of the struct byte-by-byte
  for (int i = 0; i < sizeof(ptr); i++)
  {
    printf("%d: %02X\n", i, ptr[i]);
  }
}