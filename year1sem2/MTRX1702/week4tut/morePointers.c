#include <stdio.h>

char* find_first(char *str, char c); 

int main() {
	int i = 4, j = 6;
	//first form -> can't change value stored in the address by accessing p. But can change the address.	
	//
	// essentially it is read-only cannot write.
	const int *p = &i;

	printf("%d\n", *p); //4
	p = &j;
	printf("%d\n", *p); //6
	
	//second form -> can change the value inside but can't change address:
	//
	//can write but cannot change address.
	
	int * const k = &i; 
	*k = 100;
	printf("%d\n", i); //100
	

	char text[] = "Hello";
	char *result = find_first(text, 'l');
	printf("%s\n", result); //prints "llo"
	//this is because %s means "start at this memory address and keep printing characters until you hit '\0'."
	//%s expects a char * 
}


char* find_first(char *str, char c) {
	while (*str != '\0') {
		if (*str == c) {
			return str;
		}
		str++;
	}
	return NULL;
}



