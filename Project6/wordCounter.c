/**
 * Implementing the File I/O functions
 *
 * Parth Parth
 * 4/3/2022
 */

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

// sort the given linkedlist in ascending order based on count
void sortWordCount(LinkedList *l, int (*comparator)(void *, void *)) {
  // if the list is empty, return
  if (l->next == NULL)
  {
    return;
  }

  // start bubble sort
  LinkedList *curr = l->next;
  LinkedList *prev = l;
  LinkedList *temp = NULL;

  while (curr != NULL)
  {
    temp = curr->next;
    while (temp != NULL)
    {
      if (comparator(curr->data, temp->data) > 0)
      {
        void *tempData = curr->data;
        curr->data = temp->data;
        temp->data = tempData;
      }
      temp = temp->next;
    }
    curr = curr->next;
  }
}

void main(int argc, char *argv[])
{

  // Extension 1: Check for file existence and readability
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

      // check if the word is already in the list
      wordCount *found = ll_find(ll, wc, wordCountComparator);

      // print whether or not word is in the list
      if (found == NULL)
      {
        // add the wordCount struct to the linked list
        ll_push(ll, wc);
      }
      else
      {
        // increment the count
        found->count = found->count + 1;
        // free the wordCount struct
        free(wc);
      }

      word = strtok(NULL, " ");
    }
  }

  // sort the linked list
  sortWordCount(ll, wordFrequencyComparator);

  // print first 20 words
  int i = 0;
  LinkedList *curr = ll->next;
  while (curr != NULL && i < 20)
  {
    wordCountPrinter(curr->data);
    curr = curr->next;
    i++;
  }
}