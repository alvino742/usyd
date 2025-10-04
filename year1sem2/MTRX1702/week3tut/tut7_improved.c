#include <stdio.h>

int main(void) {
    int dim;
    printf("Enter an integer: ");
    if (scanf("%d", &dim) != 1 || dim <= 0) return 0;

    int width = 2 * dim; // ensures square alignment

    for (int i = 0; i < dim; i++) {
        for (int j = 0; j < width; j++) {
            // Unindented rows (i even) start with '#'
            // Indented rows (i odd) start with ' '
            int hash_here = (i % 2 == 0) ? (j % 2 == 0) : (j % 2 == 1);
            putchar(hash_here ? '#' : ' ');
        }
        putchar('\n');
    }
    return 0;
}
