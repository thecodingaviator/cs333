/**
 * Program that can handle segmentation faults
 *
 * Parth Parth
 * 4/4/2022
 */

#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

void handler(int sig) {
  printf("Signal called with code: %d\n", sig);

  // check if the signal is SIGSEGV
  if (sig == SIGSEGV) {
    printf("Segmentation fault signal. Exiting.\n");
  }

  exit(0);
}

void main() {
  signal(SIGSEGV, handler);
  
  // cause a segmentation fault
  char *a = NULL;
  printf("%s\n", a);
}