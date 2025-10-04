#include <stdio.h>

int main() {
	printf("Enter a positive integer: ");
	int input;
	scanf("%d", &input);

	printf("Factors of %d are", input);

	for (int i = 1; i < input+1; i++) {
		if (input % i == 0) {
			printf(" %d", i);
		}
	}
	printf("\n");
}

