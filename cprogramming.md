## How to use qsort()

[sorting - C library function to perform sort - Stack Overflow](https://stackoverflow.com/questions/1787996/c-library-function-to-perform-sort)

C/C++ standard library `<stdlib.h>` contains `qsort` function.

This is not the best quick sort implementation in the world but it fast enough and VERY EASY to be used... the formal syntax of qsort is:

```c
qsort(<arrayname>,<size>,sizeof(<elementsize>),compare_function);
```

The only thing that you need to implement is the compare_function, which takes in two arguments of type "const void", which can be cast to appropriate data structure, and then return one of these three values:

- negative, if a should be before b
- 0, if a equal to b
- positive, if a should be after b

**1. Comparing a list of integers**:

simply cast a and b to integers if `x < y`,`x-y` is negative, `x == y`, `x-y = 0`, `x > y`, `x-y` is positive `x-y` is a shortcut way to do it :) reverse `*x - *y` to `*y - *x` for sorting in decreasing/reverse order

```c
int compare_function(const void *a,const void *b) {
int *x = (int *) a;
int *y = (int *) b;
return *x - *y;
}
```

**2. Comparing a list of strings**:

For comparing string, you need `strcmp` function inside `<string.h>` lib. `strcmp` will by default return -ve,0,ve appropriately... to sort in reverse order, just reverse the sign returned by strcmp

```c
#include <string.h>
int compare_function(const void *a,const void *b) {
return (strcmp((char *)a,(char *)b));
}
```

**3. Comparing floating point numbers**:

```c
int compare_function(const void *a,const void *b) {
double *x = (double *) a;
double *y = (double *) b;
// return *x - *y; // this is WRONG...
if (*x < *y) return -1;
else if (*x > *y) return 1; return 0;
}
```

**4. Comparing records based on a key**:

Sometimes you need to sort a more complex stuffs, such as record. Here is the simplest way to do it using `qsort` library.

```c
typedef struct {
int key;
double value;
} the_record;

int compare_function(const void *a,const void *b) {
the_record *x = (the_record *) a;
the_record *y = (the_record *) b;
return x->key - y->key;
}
```


