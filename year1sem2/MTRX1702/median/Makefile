CC=gcc
CFLAGS=-g -Wall -Werror -Wpedantic -fsanitize=address -std=c11 -Iinclude
LIBS=-fsanitize=address
TARGET=main

SRC_DIR = src
OBJ_DIR = obj
INC_DIR = include
_DEPS = user_io.h
_OBJS = main.o user_io.o

DEPS = $(patsubst %,$(INC_DIR)/%,$(_DEPS))
OBJS = $(patsubst %,$(OBJ_DIR)/%,$(_OBJS))

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

$(TARGET): $(OBJS)
	$(CC) -o $@ $(OBJS) $(LIBS)

.PHONY: clean
clean:
	$(RM) $(OBJS) $(TARGET)
