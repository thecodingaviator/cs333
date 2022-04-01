/**
 * Defining the list structure
 *
 * Parth Parth
 * 3/11/2022
 */

typedef struct LinkedList {
  // arbitrary pointer
  void *data;
  // next pointer
  struct LinkedList *next;
} LinkedList;

LinkedList *ll_create();

void ll_push(LinkedList *l, void *data);

void *ll_pop(LinkedList *l);

void ll_append(LinkedList *l, void *data);

void *ll_remove(LinkedList *l, void *target, int (*compfunc)(void *, void *));

int ll_size(LinkedList *l);

void ll_clear(LinkedList *l, void (*freefunc)(void *));

void ll_map(LinkedList *l, void (*mapfunc)(void *));

// extension 1
void *ll_delete(LinkedList *l, int index, void (*freefunc)(void *));
