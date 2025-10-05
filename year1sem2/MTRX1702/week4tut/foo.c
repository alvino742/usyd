#include <math.h>
#include <stdio.h>
#include <limits.h>

void chop(double d, long *whole_part, double *fraction_part);

int main(void)
{
	double d, fraction_part;
	long whole_part;

	printf("enter a double ");
	scanf("%lf", &d);

	chop(d, &whole_part, &fraction_part);
	
	printf("%.10lg chopped is %ld and %.10lg\n", d, whole_part, fraction_part);

	return 0;
}


void chop(double d, long *whole_part, double *fraction_part)
{
	double w = floor(d);
	if (w < LONG_MIN || w > LONG_MAX) {
		printf("Error, out of bounds");
		return;
	}
	*whole_part = (long)w;
	*fraction_part = d - (double)w;
}
