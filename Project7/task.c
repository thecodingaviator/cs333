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
  // start time
  clock_t start = clock();
  for(int i=0; i<100000; i++) {
    int *array = (int*) malloc(100000 * sizeof(int));
  }
  // end time
  clock_t end = clock();
  // time taken
  double time_taken = ((double) (end - start)) / CLOCKS_PER_SEC;
  printf("Time taken for call: %f\n", time_taken);
}

// for task b
void func2() {
  for(int i=0; i<100000; i++) {
    int *array = (int*) malloc(100000 * sizeof(int));
    free(array);
  }
}

void main() {
  // func1();
  for(int i=0; i< 10; i++) {
    // start time
    clock_t start = clock();
    func2();
    // end time
    clock_t end = clock();
    // time taken
    double time_taken = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Time taken for call %d: %f\n", i+1, time_taken);
  }
}