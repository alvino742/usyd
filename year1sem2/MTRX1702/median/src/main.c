#include <stdio.h>
#include "median.h"
#include "user_io.h"
#include <stdlib.h>
#include <string.h>

#define BUFF_SIZE 256
#define START_SIZE 10

int main() {
	double *out_arr = NULL;
	size_t len = 0;

	int rc = read_num_from_stdin("Please enter an array of numbers separated by whitespaces: ",
		&out_arr, &len);

	if (rc != 0){
		return 1;
	}

	for (int j = 0; j < len; j++){
		printf("%f\n", out_arr[j]);
	}

	free(out_arr);
}
