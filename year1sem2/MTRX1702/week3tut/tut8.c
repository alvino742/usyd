#include <stdio.h>

int main() {
	char operator;
	float input1, input2, output;

	printf("Enter an operator (+, -, *, /): ");
	scanf("%c", &operator);
	printf("Enter two operands: ");
	scanf("%f %f", &input1, &input2);

	switch (operator){
		case ('+'): output = input1 + input2; break;
		case ('-'): output = input1 - input2; break;
		case ('*'): output = input1 * input2; break; 
		case ('/'): output = input1 / input2; break;
	}


	printf("%.1f %c %.1f = %.1f\n", input1, operator, input2, output);
}
