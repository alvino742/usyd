#include <stdio.h>

int main() {
	printf("Enter any year: ");
	int input;
	scanf("%d", &input);

	if (input % 4 == 0) {
		printf("LEAP YEAR\n");
	}
	else {
		printf("COMMON YEAR\n");
	}
}
