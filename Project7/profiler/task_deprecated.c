/**
 * Program to estimate big O and
 * time cost of C memory management
 *
 * Parth Parth
 * 4/4/2022
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// for task a
void func1() {
  // allocate memory for x
  for(int i=0; i<100000; i++) {
    int *array = (int*) malloc(1000000 * sizeof(int));
    if(&array == NULL) {
      printf("Error allocating memory\n");
    }
  }
}

// for task b
void func2() {
  short* x;
  // allocate memory and free it for x
  for(int i=0; i<1000000000; i++) {
    x = (short *) malloc(sizeof(short));
    free(x);
  }
}

void main() {
  func1();
  // for(int i=0; i< 10; i++) {
  //   // start time
  //   clock_t start = clock();
  //   func2();
  //   // end time
  //   clock_t end = clock();
  //   // time taken
  //   double time_taken = ((double) (end - start)) / CLOCKS_PER_SEC;
  //   printf("Time taken for call %d: %f\n", i+1, time_taken);
  // }
}