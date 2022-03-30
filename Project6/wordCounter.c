#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#include "linkedlist.h"
#include "wordCount.c"

char *removePunctuation(char *str)
{
  int i = 0;
  int j = 0;
  int len = strlen(str);
  char *newStr = malloc(sizeof(char) * len);
  while (str[i] != '\0')
  {
    if (str[i] != '.' && str[i] != ',' && str[i] != '?' && str[i] != '!' && str[i] != ';' && str[i] != ':')
    {
      newStr[j] = str[i];
      j++;
    }
    i++;
  }
  newStr[j] = '\0';
  return newStr;
}

LinkedList* sortWordCount(LinkedList *l)
{
  LinkedList *curr = l;
  LinkedList *prev = NULL;
  LinkedList *next = NULL;
  while (curr != NULL)
  {
    next = curr->next;
    while (prev != NULL && wordFrequencyComparator(prev->data, curr->data) < 0)
    {
      prev->next = next;
      curr->next = prev;
      prev = curr;
      curr = next;
      next = curr->next;
    }
    prev = curr;
    curr = next;
  }
  return l;
}

void main(int argc, char *argv[])
{
  // check for correct number of arguments
  if (argc != 2)
  {
    printf("Usage: ./wordCounter <filename>\n");
    exit(1);
  }

  // open file
  FILE *fp = fopen(argv[1], "r");
  // check if file exists
  if (fp == NULL)
  {
    printf("Error: File not found\n");
    exit(1);
  }

  // create a linked list to store the words
  LinkedList *ll = ll_create();

  // go through the file
  char *line = NULL;
  size_t len = 0;
  ssize_t read;

  // while line is not null
  while ((read = getline(&line, &len, fp)) != -1)
  {
    // remove punctuation
    char *newLine = removePunctuation(line);

    // split the line into words
    char *word = strtok(newLine, " ");

    // loop through line
    while (word != NULL)
    {

      // make word lowercase
      int i = 0;
      while (word[i] != '\0')
      {
        word[i] = tolower(word[i]);
        i++;
      }

      // create a new wordCount struct
      wordCount *wc = malloc(sizeof(wordCount));
      // fill in the data
      wc->word = word;
      wc->count = 1;

      // search for work in the linked list
      char *wordStruct = ll_find(ll, wc, wordCountComparator);
      // if the word is not in the linked list
      if (wordStruct == NULL)
      {
        // add the wordCount struct to the linked list
        ll_push(ll, wc);
      }
      // otherwise, increment the count
      else
      {
        wordCount *wc = (wordCount *)wordStruct;
        wc->count++;
      }
      word = strtok(NULL, " ");
    }
  }

  // sort the linked list
  ll = sortWordCount(ll);

  // print the linked list
  ll_map(ll, wordCountPrinter);
}