/**
 * Given an array of random integers, sort it in such a way that the even 
 * numbers appear first and the odd numbers appear later. The even numbers 
 * should be sorted in descending order and the odd numbers should be sorted 
 * in ascending order.
 *
 * Ying Li
 * 08/02/2016
 */

#include <stdio.h>
#include <stdlib.h>

/*
  Comparator implemented by
  Parth Parth
  03/03/2022
*/

/* the comparator function used in qsort */
int comparator (const void *p, const void *q) {
	int x = *(int *)p;
	int y = *(int *)q;

	// if both are odd, sort in ascending order
	if ((x % 2) && (y % 2)) {
		return x - y;
	}
	// if both are even, sort in descending order
	else if (!(x % 2) && !(y % 2)) {
		return y - x;
	}
	// if the first is odd and the second is even, return -1
	else if ((x % 2) && !(y % 2)) {
		return 1;
	}
	// if the first is even and the second is odd, return 1
	else {
		return -1;
	}
}

int main (int argc, char **argv) {
	int ary[] = {10, 11, 1, 8, 9, 0, 13, 4, 2, 7, 6, 3, 5, 12};
	
	int size = sizeof(ary) / sizeof(int);
	
	qsort((void *) ary, size, sizeof(int), comparator);
	
	printf("The sorted array is: ");
	for (int i = 0; i < size; i++) {
		printf("%d ", ary[i]);
	}
	printf("\n");
	
	return 0;
}