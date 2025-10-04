#include <stdio.h>

int main() {
		printf("Enter an integer: ");
		int input;
		scanf("%d", &input);

		printf("The ASCII character for %d is '%c'\n", input, input);
		return 0;
}
