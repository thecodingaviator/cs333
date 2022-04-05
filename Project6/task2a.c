/**
 * Program that can respond to a cntl-C interrupt
 *
 * Parth Parth
 * 4/4/2022
 */

#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

void handler(int sig) {
  printf("Signal called with code: %d\n", sig);

  // explicitly check for interrupt signal
  if (sig == SIGINT) {
    printf("Interrupt signal. Exiting.\n");
  }

  exit(0);
}

void main() {
  signal(SIGINT, handler);
  
  // loop until signal recieved
  while (1) {
    printf("I'm waiting for you to cntl-C me\n");
  }
}