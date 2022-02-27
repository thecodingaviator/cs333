/**
 * Defining the stack structure
 *
 * Parth Parth
 * 2/27/2022
 */

typedef struct stack {
    int* stack;
	int top;
} Stack;

Stack *stk_create(int);
void stk_destroy (Stack*);
void stk_push(Stack*, int);
int stk_pop(Stack*);
void stk_display(Stack*, int);