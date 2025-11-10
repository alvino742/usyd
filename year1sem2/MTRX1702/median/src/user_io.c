#include "user_io.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFF_SIZE 256
#define START_SIZE 10

int read_num_from_stdin(char *prompt, double **out_arr, size_t *out_len) {
	size_t len = *out_len;

	if (prompt){
		fputs(prompt, stdout);
	}


	char buff[BUFF_SIZE];
	if(!fgets(buff, BUFF_SIZE, stdin)) {
			return 1;
	}

	buff[strcspn(buff, "\n")] = '\0';

	
	//dynamic array
	size_t cap = START_SIZE;
	double *arr = (double*) malloc(cap * sizeof(double));

	char *p = buff, *end;
	
	for (;;){
			if (len == cap){
					cap *= 2;
					double *tmp = realloc(arr, cap * sizeof(double));
					if (!tmp) { free(arr); return 1; }
					arr = tmp;
			}

			double v = strtod(p, &end);
			if (end == p) break;
			
			arr[len++] = v;
			p = end;
	}
	
	*out_arr = arr;
	*out_len = len;
	
	return 0;
}
