/**
 * Implementing wordCount struct and functions
 *
 * Parth Parth
 * 4/3/2022
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
  char *word;
  int count;
} wordCount;

// comparator to check if two wordCount structs are equal
int wordCountComparator(void *a, void *b) {
  wordCount *wc1 = (wordCount*)a;
  wordCount *wc2 = (wordCount*)b;
  return strcmp(wc1->word, wc2->word);
}

// comparator to check the frequencies of two wordCount structs
int wordFrequencyComparator(void *a, void *b) {
  wordCount *wc1 = (wordCount*)a;
  wordCount *wc2 = (wordCount*)b;
  return wc2->count - wc1->count;
}

void wordCountPrinter(void *data) {
  wordCount *wc = (wordCount*)data;
  printf("%s: %d\n", wc->word, wc->count);
}