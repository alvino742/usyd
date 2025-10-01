#include <stdio.h>

int main(void) {
		int a, b;
		printf("Enter first number: ");
		scanf("%d", &a);
		printf("Enter second number: ");
		scanf("%d", &b);
		
		printf("The sum of %d and %d is %d.\n", a, b, a+b);
		return 0;
}
