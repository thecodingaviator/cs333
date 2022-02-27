typedef struct stack {
    int* stack;
	int top;
} Stack;

int CSTK_MAX = 50;

Stack *stk_create(int);
void stk_destroy (Stack*);
void stk_push(Stack*, int);
int stk_pop(Stack*);
void stk_display(Stack*, int);