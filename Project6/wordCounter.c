#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "linkedlist.h"
#include "wordCount.c"

char* removePunctuation(char* str) {
  int i = 0;
  int j = 0;
  int len = strlen(str);
  char* newStr = malloc(sizeof(char) * len);
  while (str[i] != '\0') {
    if (str[i] != '.' && str[i] != ',' && str[i] != '?' && str[i] != '!' && str[i] != ';' && str[i] != ':') {
      newStr[j] = str[i];
      j++;
    }
    i++;
  }
  newStr[j] = '\0';
  return newStr;
}

void main(int argc, char* argv[]) {
  // check for correct number of arguments
  if (argc != 2) {
    printf("Usage: ./wordCounter <filename>\n");
    exit(1);
  }

  // open file
  FILE* fp = fopen(argv[1], "r");
  // check if file exists
  if (fp == NULL) {
    printf("Error: File not found\n");
    exit(1);
  }

  // create a linked list to store the words
  LinkedList* ll = ll_create();

  // go through the file
  char* line = NULL;
  size_t len = 0;
  ssize_t read;

  // while line is not null
  while ((read = getline(&line, &len, fp)) != -1) {
    // remove punctuation
    char* newLine = removePunctuation(line);

    // split the line into words
    char* word = strtok(newLine, " ");
    
    // loop through line
    while(word != NULL) {
      // search for work in the linked list
      char* wordStruct = ll_find(ll, word, wordCountComparator);
      // if the word is not in the linked list
      if (wordStruct == NULL) {
        // create a new wordCount struct
        wordCount* wc = malloc(sizeof(wordCount));
        // fill in the data
        wc->word = word;
        wc->count = 1;
        // add the wordCount struct to the linked list
        ll_push(ll, wc);
      }
      // otherwise, increment the count
      else {
        wordCount* wc = (wordCount*)wordStruct;
        wc->count++;
      }
      word = strtok(NULL, " ");
    } 
  }

  // print the linked list
  ll_map(ll, wordCountPrinter);
}