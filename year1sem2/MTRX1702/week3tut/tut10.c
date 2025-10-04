#include <stdio.h>

int prime(int n) {
	if (n < 2) return 0;
	int factors = 0;
	for (int i = 1; i < n+1; i++){
		if (n % i == 0) {
			factors += 1;
		}
	}
	return (factors == 2);
}


int main() {
	printf("Enter a number n: "); 
	int input;
	scanf("%d", &input);
	
	if (prime(input)) {
		print("Yes, It is a prime number.\n.");
	} else {
		print("It is not a prime number.\n")
	}
}
