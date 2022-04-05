/**
 * Program that can handle floating point exceptions
 *
 * Parth Parth
 * 4/4/2022
 */

#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

void handler(int sig) {
  printf("Signal called with code: %d\n", sig);

  // check if the signal is SIGFPE
  if (sig == SIGFPE) {
    printf("Floating point exception. Exiting\n");
  }

  exit(0);
}

void main() {
  signal(SIGFPE, handler);
  
  // cause a floating point exception
  double a = 1.0;

  printf("%f\n", a / 0.0);
}