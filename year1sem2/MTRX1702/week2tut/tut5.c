#include <stdio.h>

int main(void) {
	float inputC, inputF, outputF, outputC;
	printf("Enter the temperature in Celsius: ");
	scanf("%f", &inputC);

	outputF = (9.00/5.00) * inputC + 32.00;
	

	printf("%.2f degree C is %.2f degree F\n", inputC, outputF);

	printf("Enter the temperature in Fahrenheit: ");
	scanf("%f", &inputF);

	outputC = (5.00/9.00) * (inputF - 32.00);
	

	printf("%.2f degree Fahrenheit is %.2f degree C\n", inputF, outputC);

}
