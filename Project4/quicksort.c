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

	// if both numbers are even, compare them in descending order
	if ((*(int *)p % 2 == 0) && (*(int *)q % 2 == 0)) {
		return *(int *)q - *(int *)p;
	}
	// if both numbers are odd, compare them in ascending order
	else if ((*(int *)p % 2 != 0) && (*(int *)q % 2 != 0)) {
		return *(int *)p - *(int *)q;
	}
	// if one of the numbers is even and the other is odd, even number comes first
	else if ((*(int *)p % 2 == 0) && (*(int *)q % 2 != 0)) {
		return 1;
	}
	// if one of the numbers is odd and the other is even, even number comes first
	else if ((*(int *)p % 2 != 0) && (*(int *)q % 2 == 0)) {
		return -1;
	}
	// if both numbers are even or odd, return 0
	else {
		return 0;
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