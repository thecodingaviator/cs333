#include <stdio.h>
#include <stdlib.h>

int factorial(int n) {
    if (n == 0) {
        return 1;
    }
    else {
        return n * factorial(n - 1);
    }
}

int main(int argc, char **argv) {
    int (*calc)(const int) = factorial;
    // accept a command line argumet
    int n = atoi(argv[1]);
    printf("%d\n", calc(n));
}