.global _main 
.align 2

//main 

_main:
	b _printf
	b _terminate

//4	AUE_NULL	ALL	{ user_ssize_t write(int fd, user_addr_t cbuf, user_size_t nbyte); }
_printf:
	mov X0, #1 //stdout
	adr X1, hello 
	mov X2, #14
	mov X16, #4
	svc #0

_terminate:
	mov X0, #0
	mov X16, #1
	svc 0

hello: 
	.asciz "Hello, World!\n"
