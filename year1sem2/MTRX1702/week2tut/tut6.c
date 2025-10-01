#include <stdio.h>

#define RATE 0.056


int main() {
	printf("Enter the values of principle and time period\n");
	float principal, time_period, si;
	scanf("%f", &principal);
	scanf("%f", &time_period);

	printf("Amount = %.2f\n", principal);
	printf("Rate = %.2f%%\n", RATE * 100);

	si = principal * time_period * RATE;
	
	printf("\nSimple interest = %.2f\n", si);
}
