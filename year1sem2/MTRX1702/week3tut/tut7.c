#include <stdio.h>

int main() {
	printf("Enter an integer: ");
	int dim;
	scanf("%d", &dim);
	

	for (int i = 1; i < dim+1; i++){
		if (i % 2 == 0) {
			for (int j = 1; j < dim*2+1; j++) {
				if (j % 2 == 0) printf("#");
				else printf(" ");
			}
		} 
		else {
			for (int j = 1; j < dim*2+1; j++) {
				if (j % 2 == 0) printf(" ");
				else printf("#");
			}
		}
		printf("\n");
	}
}
