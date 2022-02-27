

#include "cstk.h"

// create a stack of size size
Stack *stk_create(int size) {
    Stack *stk = malloc(sizeof(Stack));
    stk->stack = malloc(sizeof(int) * size);
    stk->top = -1;
    return stk;
}

// recycles the stack
void stk_destroy(Stack *stk) {
    free(stk->stack);
    free(stk);
}

// push an element onto the stack
void stk_push(Stack *stk, int element) {
    stk->top++;
    stk->stack[stk->top] = element;
}

// pop an element off the stack
int stk_pop(Stack *stk) {
    // if the stack is empty, return -1
    if (stk->top == -1) {
        return -1;
    }
    int element = stk->stack[stk->top];
    stk->top--;
    return element;
}

// display the stack
void stk_display(Stack *stk, int order) {
    // if order is 1, print the stack in reverse order
    if (order == 1) {
        for (int i = stk->top; i >= 0; i--) {
            printf("%d ", stk->stack[i]);
        }
    }
    // if order is 0, print the stack in normal order
    else {
        for (int i = 0; i <= stk->top; i++) {
            printf("%d ", stk->stack[i]);
        }
    }
}

extern CSTK_MAX;