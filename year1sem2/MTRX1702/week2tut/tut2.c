#include <stdio.h>

int main(void) {
	//1
	printf("Enter a float: ");
	float a;
	scanf("%f", &a);
	printf("Input: %f\n", a);
	printf("Output: %.2f\n", a);

	//2
	printf("Enter a second float: ");
	float b;
	scanf("%f", &b);
	printf("Input: %f\n", b);
	printf("Ouput: %10f\n", b);

	//3
	printf("Enter a third float: ");
	float c;
	scanf("%f", &c);
	printf("Input: %f\n", c);
	printf("Ouput: %6.2f\n", c);
	
	//4
	printf("Enter a string: ");
	char string1;
	scanf("%s", &string1);
	printf("Input: %s\n", string1);
	printf("Output: %10s\n", string1);


	//5
	printf("Enter a integer: ");
	int integer1;
	scanf("%d", &integer1);
	printf("Input: %d\n", integer1);
	printf("Output: %5d\n", integer1);
}
