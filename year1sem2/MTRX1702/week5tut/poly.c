#include <stdio.h>
#include <string.h>


int main()
{
    char input[99];
    int index, numLetters;

    printf("Enter a word: ");
    fgets(input, sizeof(input), stdin);
		input[strcspn(input, "\n")] = '\0';


    printf("Enter starting index: ");
    scanf("%d", &index);
    size_t inputLen = strlen(input);

    printf("Enter the amount of letters printed: ");
    scanf("%d", &numLetters);

    int k = 0, i = 0;
    int q = 1;
    while(i < numLetters){
        printf("%c", input[index+k]);
		k = k + q;
		int next = index + k + q;
        if ((next < 0) || (next > (int)inputLen - 1)) q = q * (-1);
        i++;
    }
		putchar('\n');
}
