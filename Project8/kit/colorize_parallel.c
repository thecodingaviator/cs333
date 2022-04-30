/**
 * Parallel Image Colorizer
 *
 * Parth Parth
 * 4/4/2022
 */

#include <stdio.h>
#include <stdlib.h>
#include "ppmIO.h"
#include "my_timing.h"
#include <pthread.h>

typedef struct
{
  int id;
  int start;
  int end;
} ColorizeThread;

int NUMTHREADS = 4;
int cols = 0;
Pixel *src;

void *colorize(void *arg)
{
  ColorizeThread *thread = (ColorizeThread *)arg;
  int start = thread->start;
  int end = thread->end;

  // process image
  for (int i = start*cols; i < end * cols; i++)
  {
    src[i].r = src[i].r > 128 ? (220 + src[i].r) / 2 : (30 + src[i].r) / 2;
    src[i].g = src[i].g > 128 ? (220 + src[i].g) / 2 : (30 + src[i].g) / 2;
    src[i].b = src[i].b > 128 ? (220 + src[i].b) / 2 : (30 + src[i].b) / 2;
  }
}

int main(int argc, char *argv[])
{
  int rows, colors;
  int i;

  // check usage
  if (argc < 2)
  {
    printf("Usage: %s <image filename>\n", argv[0]);
    exit(-1);
  }

  // read image and check for errors
  src = ppm_read(&rows, &cols, &colors, argv[1]);
  if (!src)
  {
    printf("Unable to read file %s\n", argv[1]);
    exit(-1);
  }

  // calculate division of work
  int work_per_thread = rows / NUMTHREADS;

  // create threads
  pthread_t threads[NUMTHREADS];

  // create thread arguments
  ColorizeThread args[NUMTHREADS];

  // set thread info
  for (int i = 0; i < NUMTHREADS; i++)
  {
    args[i].id = i;
    args[i].start = i * work_per_thread;
    args[i].end = (i + 1) * work_per_thread;
  }

  // start time
  double t1 = get_time_sec();

  // create threads
  for (int i = 0; i < NUMTHREADS; i++)
  {
    pthread_create(&threads[i], NULL, colorize, &args[i]);
  }

  // join threads
  for (int i = 0; i < NUMTHREADS; i++)
  {
    pthread_join(threads[i], NULL);
  }

  // end time
  double t2 = get_time_sec();

  // print time
  printf("Time: %f\n", t2 - t1);

  // write out the image
  ppm_write(src, rows, cols, colors, "bold.ppm");

  free(src);

  return (0);
}
