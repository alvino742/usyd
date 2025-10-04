#include <stdio.h>
#include <string.h>

void toLowerString(char *s);
char toLowerChar(char s);

int main() {
	int numvoters;
	int running = 1;
	while (running) {
		printf("Number of Voters: ");
		scanf("%d", &numvoters);

		char name1[10], name2[10], name3[10];
		char Name1[10], Name2[10], Name3[10];

		


		printf("Name of 1st Candidate: "); 
		scanf("%s", name1);
		printf("Name of 2nd Candidate: "); 
		scanf("%s", name2);
		printf("Name of 3rd Candidate: "); 
		scanf("%s", name3);

		strcpy(Name1, name1);
		strcpy(Name2, name2);
		strcpy(Name3, name3);

		//make names lowercase
		toLowerString(name1);
		toLowerString(name2);
		toLowerString(name3);
		
		char votes[100];
		int tally1 = 0, tally2 = 0, tally3 = 0;

		for (int i = 0; i < numvoters; i++){
			scanf(" %c", &votes[i]);
			votes[i] = toLowerChar(votes[i]);
			if (votes[i] == name1[0]) tally1 += 1;
			if (votes[i] == name2[0]) tally2 += 1;
			if (votes[i] == name3[0]) tally3 += 1;
		}
		
		//results
		printf("%s: %d\n", Name1, tally1);
		printf("%s: %d\n", Name2, tally2);
		printf("%s: %d\n", Name3, tally3);

		int largest = tally1;
		if (tally2 > largest) largest = tally2;
		if (tally3 > largest) largest = tally3;

		int winners = (largest == tally1) + (largest == tally2) + (largest == tally3);

		if (winners >= 2) {
			printf("There was a tie! revote! \n");
			continue;
		} else {
			if (largest == tally1) printf("%s has won the vote! Praise %s\n", Name1, Name1);
			else if (largest == tally2) printf("%s has won the vote! Praise %s\n", Name2, Name2);
			else printf("%s has won the vote! Praise %s\n", Name3, Name3);
		}	
		running = 0;
		break;
	}
}

void toLowerString(char *s) {
	for (int i = 0; s[i] != '\0'; i++){
		if (s[i] >= 'A' && s[i] <= 'Z') {
			s[i] += 'a' - 'A'; //shift by 32
		}
	}
} 

char toLowerChar(char s) {
	if (s >= 'A' && s <= 'Z') {
		s += 'a' - 'A'; //shift by 32
	}
	return s;
}
