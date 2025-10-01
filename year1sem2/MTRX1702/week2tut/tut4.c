#include <stdio.h>


int main(void) {
	printf("Number of days: ");
	int input, years, weeks, days;
	scanf("%d", &input);
	
	years = input / 365;
	weeks = input % 365 / 7;
	days = input % 365 % 7;
	

	printf("Years: %d\n", years);
	printf("Weeks: %d\n", weeks);
	printf("Days: %d\n", days);
}
