//basic placeholders


// integer

printf("%d", 42);

// unsigned integer

printf("%u", 42u);


// floating point 


printf("%f", 3.114);

// floating point with n decimal places

printf("%.3f", 3.143235);


// scientific notation 

printf("%e", 123.435);

// single character


printf("%c", 'A');

// pointer address 

int x = 123;
printf("%p", &x);


// field width

printf("%5d", 42);   // "   42"

// left algin

printf("%-5d", 42);  // "42   "


// zero-padding

printf("%05d", 42);  // "00042"


//sign display 

printf("%+d", 42);   // "+42"
printf("%+d", -42);  // "-42"


// field width + precision

printf("%8.2f", 3.14159); // "    3.14"

// strings and characters

printf("%s", "Hello");     // "Hello"
printf("%10s", "Hi");      // "        Hi"
printf("%-10s", "Hi");     // "Hi        "
printf("%.3s", "Hello");   // "Hel" (limit length)

//advanced
printf("%*.*f", 8, 3, 3.14159); // width=8, precision=3 → "   3.142"

