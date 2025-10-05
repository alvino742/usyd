// your code here
#include <stdio.h>


//function1 prototype
int *biggest_of_two(int*, int*);


//function2 prototype
int *biggest_of_three(int*, int*, int*);

// No need to change - inspect the two printf lines and make sure you understand them
int main(void) {
	
	int a = 100, b = -5, c = 200;
	
	printf("the biggest of %d and %d is %d\n", a, b, *biggest_of_two(&a, &b));
	printf("the biggest of %d %d and %d is %d\n", a, b, c, *biggest_of_three(&a, &b, &c));
	return 0;
}


int *biggest_of_two(int *a, int *b) {
	if (*a > *b) return a;
	else return b;
}

int *biggest_of_three(int *a, int *b, int *c) {
	int *p[] = {a, b, c};
	int *largest = p[0];
	for (int i = 0; i < sizeof(p)/sizeof(p[0]); i++) {
		if (*p[i] > *largest) {
			largest = p[i];
		}
	}
	return largest;
}
