/**
 * Local Counter Array Protected by Mutex at final
 *
 * Parth Parth
 * 4/4/2022
 */

#include <stdio.h>
#include <stdlib.h>
#include "my_timing.h"
#include <pthread.h>
#include <math.h>
#include <string.h>

// global counts array
int global_counts[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
// global mutex array
pthread_mutex_t mutex[10] = PTHREAD_MUTEX_INITIALIZER;
// global data
double *data;
// global N
int N;

typedef struct {
  int id;
  int start;
  int end;
  int local_counts[10];
} ThreadInfo;

// method to return the leading digit of a double
int leadingDigit(double n)
{
  while(floor(fabs(n)) > 10)
  {
    n /= 10;
  }
  return (int)floor(fabs(n));
}

// method to load data from a binary file
int loadData(char *filename)
{
  FILE *fp;

  if (filename != NULL && strlen(filename))
    fp = fopen(filename, "r");
  else
    return -1;

  if (!fp)
    return -1;

  fread(&N, sizeof(int), 1, fp);
  data = (double *)malloc(sizeof(double) * N);
  fread(data, sizeof(double), N, fp);
  fclose(fp);

  return 1; // success
}

// method to count the leading digits of the data
void *count(void *arg)
{
  ThreadInfo *info = (ThreadInfo *)arg;
  for(int i = info->start; i < info->end; i++)
  {
    // get the leading digit
    int digit = leadingDigit(data[i]);

    // increment the counter in local array
    info->local_counts[digit]++;
  }

  // add the local counts to the global counts
  for(int i=0; i<10; i++)
  {
    // get digit from local array
    int digit = info->local_counts[i];
    // increment the counter
    pthread_mutex_lock(&mutex[digit]);
    global_counts[digit]++;
    pthread_mutex_unlock(&mutex[digit]);
  }

  pthread_exit(NULL);
}

// main method will accept filename
int main(int argc, char *argv[])
{
  double t1, t2;

  // check if filename is passed
  if (argc != 2)
  {
    printf("Usage: %s <filename>\n", argv[0]);
    return -1;
  }

  // load data from file
  if (loadData(argv[1]) != 1)
  {
    printf("Error loading data from file.\n");
    return -1;
  }

  ThreadInfo info[4];

  // create threads
  pthread_t threads[4];

  // set thread info
  for(int i = 0; i < 4; i++)
  {
    info[i].id = i;
    info[i].start = floor(i * (N / 4.0));
    info[i].end = floor((i + 1) * (N / 4.0));
    for(int j = 0; j < 10; j++)
    {
      info[i].local_counts[j] = 0;
    }
  }

  // start time
  t1 = get_time_sec();

  // create threads
  for(int i = 0; i < 4; i++)
  {
    pthread_create(&threads[i], NULL, count, &info[i]);
  }

  // join threads
  for(int i = 0; i < 4; i++)
  {
    pthread_join(threads[i], NULL);
  }

  // end time
  t2 = get_time_sec();

  // print results
  printf("\n");
  printf("Digit\tCount\n");
  printf("-----\t-----\n");
  for (int i = 0; i < 10; i++)
  {
    printf("%d\t%d\n", i, global_counts[i]);
  }

  // print time
  printf("\nTime: %f\n", t2 - t1);

  return 0;
}