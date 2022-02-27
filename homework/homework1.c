#include <stdio.h>
#include <stdlib.h>

int main() {
  float a=1.11111;
  float b=2.22222;
  float c=3.33333;
  printf( "(a + b) + c = %0.16f\n", (a + b) + c );
  printf( "a + (b + c) = %0.16f\n", a + (b + c) );
}