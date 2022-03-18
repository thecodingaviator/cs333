

#include <stdio.h>
#include <stdlib.h>

#include "linkedlist.h"

LinkedList *ll_create() {
  // allocate space for the linked list
  LinkedList *ll = malloc(sizeof(LinkedList));
  // set the next pointer to NULL
  ll->next = NULL;
  // return the linked list
  return ll;
}

void ll_push(LinkedList *l, void *data) {
  // allocate space for a new node
  LinkedList *new = malloc(sizeof(LinkedList));
  // fill in the data
  new->data = data;
  // set the next pointer to the current head
  new->next = l->next;
  // set the head to the new node
  l->next = new;
}

void *ll_pop(LinkedList *l) {
  // if the list is empty, return NULL
  if (l->next == NULL) {
    return NULL;
  }
  // otherwise, save the data and the next pointer
  void *data = l->next->data;
  LinkedList *next = l->next->next;
  // free the old head
  free(l->next);
  // set the head to the next pointer
  l->next = next;
  // return the data
  return data;
}

void ll_append(LinkedList *l, void *data) {
  // if the list is empty, push the data
  if (l->next == NULL) {
    ll_push(l, data);
    return;
  }
  // otherwise, find the end of the list
  LinkedList *curr = l->next;
  while (curr->next != NULL) {
    curr = curr->next;
  }
  // allocate space for a new node
  LinkedList *new = malloc(sizeof(LinkedList));
  // fill in the data
  new->data = data;
  // set the next pointer to NULL
  new->next = NULL;
  // set the next pointer of the current end to the new node
  curr->next = new;
}

void *ll_remove(LinkedList *l, void *target, int (*compfunc)(void *, void *)) {
  // if the list is empty, return NULL
  if (l->next == NULL) {
    return NULL;
  }
  // otherwise, save the head
  LinkedList *curr = l->next;
  // if the head is the target, pop the head
  if (compfunc(curr->data, target) == 0) {
    return ll_pop(l);
  }
  // otherwise, loop through the list
  while (curr->next != NULL) {
    // if the next node is the target, remove it
    if (compfunc(curr->next->data, target) == 0) {
      // save the data and the next pointer
      void *data = curr->next->data;
      LinkedList *next = curr->next->next;
      // free the old node
      free(curr->next);
      // set the next pointer of the current node to the next pointer
      curr->next = next;
      // return the data
      return data;
    }
    // otherwise, move to the next node
    curr = curr->next;
  }
  // if the target was not found, return NULL
  return NULL;
}

int ll_size(LinkedList *l) {
  // if the list is empty, return 0
  if (l->next == NULL) {
    return 0;
  }
  // otherwise, count the number of nodes
  int count = 1;
  LinkedList *curr = l->next;
  while (curr->next != NULL) {
    count++;
    curr = curr->next;
  }
  // return the number of nodes
  return count;
}

void ll_clear(LinkedList *l, void (*freefunc)(void *)) {
  // if the list is empty, return
  if (l->next == NULL) {
    return;
  }
  // otherwise, loop through the list
  LinkedList *curr = l->next;
  while (curr->next != NULL) {
    // free the data
    freefunc(curr->data);
    // move to the next node
    curr = curr->next;
  }
  // free the last node
  freefunc(curr->data);
  // free the list
  free(l);
}

void ll_map(LinkedList *l, void (*mapfunc)(void *)) {
  // if the list is empty, return
  if (l->next == NULL) {
    return;
  }
  // otherwise, loop through the list
  LinkedList *curr = l->next;
  while (curr->next != NULL) {
    // call the map function on the data
    mapfunc(curr->data);
    // move to the next node
    curr = curr->next;
  }
  // call the map function on the last node
  mapfunc(curr->data);
}
