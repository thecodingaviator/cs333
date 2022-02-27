#include <stdio.h>
#include <stdlib.h>

void demo1() {
  // will store a pointer to (address of) an int
  int *ptr;

  // allocate memory on the heap for an int and make ptr point to it
  ptr = (int *) malloc(sizeof(int));

  // assign a value to the int
  // dereference  the point and put the value in the int
  // dereference means to get the value of the pointer/follow the pointer
  *ptr = 10;

  // print the value of the int
  printf("ptr points to %p and had value %d\n", ptr, *ptr);

  // free the memory
  free(ptr);
}

void demo2() {
  int *ptr = (int *) malloc(sizeof(int) * 8);

  // assign values to the ints
  for(int i = 0; i < 8; i++) {
    ptr[i] = i;
  }

  // print the values of the ints
  for(int i = 0; i < 8; i++) {
    printf("ptr[%d] = %d\n", i, ptr[i]);
  }

  // make all the ints double
  for(int i = 0; i < 8; i++) {
    ptr[i] *= 2;
  }

  // print the values of the ints
  for(int i = 0; i < 8; i++) {
    printf("ptr[%d] = %d\n", i, ptr[i]);
  }

  // can loop through it with a different kind of pointer
  unsigned char *cp = (unsigned char *) ptr;
  for(int i = 0; i < 32; i++) {
    printf("cp[%d] = %d\n", i, cp[i]);
  }
}

void demo3() {
  int a = 4;
  char b = 'g';
  int *ptr;

  // ptr gets "Address of" a
  ptr  = &a;

  printf("ptr is %p and it points to %d\n", ptr, *ptr);
}

void demo4() {
  // store on the stack
  int nums[4];

  // assign values to the ints
  for(int i = 0; i < 4; i++) {
    nums[i] = i * 2;
  }

  // print the values of the ints
  for(int i = 0; i < 4; i++) {
    printf("nums[%d] = %d\n", i, nums[i]);
  }
}

typedef struct {
  int a;
  char b;
} Container;

void demo5() {

  // goes on the stack
  Container c;
  c.a = 10;
  c.b = 'a';

  // goes on the heap
  Container *cp;
  cp = (Container *) malloc(sizeof(Container));
  cp->a = 10;
  cp->b = 'a'; // sugar for (*cp).b = 'a';

  printf("c.a = %d and c.b = %c\n", c.a, c.b);
}


int main(int argn, char *argv[])
{
  demo5();
  return 0;
}