#include <stdio.h>

int main() {
	int numbers[6];
	int largest;

	for (int i = 0; i < 6; i++) {
		printf("Element %d: ", i + 1);
		scanf("%d", &numbers[i]);
	}
	
	largest = numbers[0];
	for (int i = 1; i < 6; i++) {
		if (numbers[i] > largest) {
			largest = numbers[i];
		}
	}

	printf("The largest number is %d\n", largest);

	return 0;
}
	
