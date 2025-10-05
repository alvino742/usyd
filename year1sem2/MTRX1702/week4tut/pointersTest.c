#include <stdio.h>

void someFunc(int a, int b, int *q, int *k){
		*q = a * b; // deferencing
		*k = a + b;
}


int main() {
		int a = 3, b = 4, q, k; // initialising random memory allocation for q and k
		someFunc(a, b, &q, &k);
		printf("a = %d\n", a);
		printf("b = %d\n", b);
		printf("q = %d\n", q);
		printf("k = %d\n", k);

		//arrays:
		int arr[5] = {10, 20, 30, 40, 50};
		int *p = arr; // equals to int *p = &arr[0];
		printf("%d\n", *p); // prints 10;
		printf("%d\n", *(p+1)); // prints 20;
		
		//arr[i] is just short for *(arr + i)

		//iterating with pointers
		for (int *q = arr; q < arr + 5; q++) {
				printf("%p\n", q);
				printf("%d\n", *q);
		}

		//pointer indexing
		for (int i = 0; i < 5; i++) {
				printf("%d\n", p[i]);
		}

		//p[0] is shorthand for *(p + 0)

		//length using sizeof()
		sizeof(arr); // 20 - 5 elements 4 bits each
		sizeof(arr) / sizeof(arr[0]); // 5 
		
		//note: using sizeof on pointer gives the size of the int
		//care full need to use sizeof on array not pointer
}
