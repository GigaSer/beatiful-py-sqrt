# Beautiful square root for Python

This module contains two functions which can convert square root.

`better_sqrt(sqrt_arg)` and `bad_sqrt(result_arg, sqrt_arg)`

`better_sqrt(sqrt_arg)` reduce some square root to readable, it will return a tuple, where the first number taken
out, and the second number remainder of the root like `better_sqrt(18)` -> `(3, 2)`

`bad_sqrt(result_arg, sqrt_arg)` is opposite of `better_sqrt(sqrt_arg)`, it returns a full square root and takes two argument, where first is a factor (it will convert to module) and second is square root
like `bad_sqrt(2, 5)` -> 20

**WARNING!** These functions want save the sign of number, that means if you put in argument negative number like `bad_sqrt(-1, 70)`, it will return -70 or `better_sqrt(-70)` -> `(-1, 70)`, you can use the `abs()` function for avoid sign this.

This package using python >= 3.9 and testing by pytest >= 6.2.1