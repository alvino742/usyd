#include <stdio.h>

int main(void) {
	printf("Enter the value of a float to print: ");
	float f;
	scanf("%f", &f);

	printf("Enter an integer to represent the number of padded spaces: ");
	int a;
	scanf("%d", &a);
	
	printf("Enter an integer to represent the number of characters after the decimal point: ");
	int b;
	scanf("%d", &b);

	printf("The number is: %*.*f\n", a, b, f);

}
