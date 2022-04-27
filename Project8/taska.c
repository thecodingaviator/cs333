/**
 * Global Counter Array Protected by Single Mutex
 *
 * Parth Parth
 * 4/4/2022
 */

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <sys/types.h>
#include <time.h>
#include <math.h>
#include "my_timing.h"

// array of 10 ints
int counter[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int N = 0;

// global mutex
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

// Return the leading Digit of n.
int leadingDigit(double n)
{
  // This is not a particularly efficient approach.
  if (fabs(n) == 1.0)
    return 1;
  else if (fabs(n) == 0.0)
    return 0;
  else if (fabs(n) < 1.0)
  {
    // multiply it by 10 until you get a number that is at least 1.
    // Then chop off the fractional part. All that remains is the first digit.
    double tmp = fabs(n);
    while (tmp < 1.0)
    {
      tmp *= 10.0;
    }
    return (int)floor(tmp);
  }
  else
  {
    // Divide it by 10 until you get a number smaller than 10.
    // That number will be the first digit of the original number.
    long long unsigned in = (long long unsigned)floor(fabs(n));
    while (in > 9)
    {
      in /= 10;
    }
    return in;
  }
} // end leadingDigit

// main function that accepts filename as argument
int main(int argc, char *argv[])
{
  double t1, t2;
  int i;
  double *data;

  // check if filename is passed
  if (argc != 2)
  {
    printf("Usage: %s <filename>\n", argv[0]);
    exit(1);
  }

  // open binary file
  FILE *fp = fopen(argv[1], "r");
  if (fp == NULL)
  {
    printf("Error opening file %s\n", argv[1]);
    exit(1);
  }

  fread(&N, sizeof(int), 1, fp);
  data = (double *)malloc(sizeof(double) * N);
  fread(data, sizeof(double), N, fp);
  fclose(fp);

  // Start the timer after we have loaded the data.
  t1 = get_time_sec();

  // Do the computation.
  for (i = 0; i < N; i++)
  {
    int d = leadingDigit(data[i]);
    counter[d]++;
  }

  // End the timer
  t2 = get_time_sec();

  // print

  printf("It took %f seconds for the whole thing to run\n", t2 - t1);

  // We are responsible for calling loadData, so we are responsible
  // for freeing the data array.
  free(data);
  return 0;
}