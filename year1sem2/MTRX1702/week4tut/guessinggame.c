#include <stdio.h>


int check_input(int *input) {
	if (*input > 10 || *input < 1) {
		return 0;
	}
	else return 1;
}


int main() {
	int running1 = 1;
	int running2 = 1;
	int input1, input2;

	while (running1) {
		printf("Enter player 1 number (1-10): ");
		scanf("%d", &input1);

		if (check_input(&input1) == 0) {
			printf("must be a number between 1-10!\n");
			continue;
		}

		printf("Enter player 2 number (1-10): ");
		scanf("%d", &input2);

		if (check_input(&input2) == 0) {
			printf("must be a number between 1-10!\n");
			continue;
		}
		running1 = 0; break;
	}

	while (running2) {
		int move1;
		printf("Player 1 turn: ");
		scanf("%d", &move1);

		

		if (move1 == input2){
			printf("Yes! Player 1 Wins!\n");
			running2 = 0;
			break;
		} else printf("Nope!\n");
		
		int move2;
		printf("Player 2 turn: ");
		scanf("%d", &move2);

		if (move2 == input1){
			printf("Yes! Player 2 Wins!\n");
			running2 = 0;
			break;
		} else printf("Nope!\n");
	}
}
