prime_numbers = [2]

for i in range(3, 100):
    for k in prime_numbers:
        if i % k == 0:
            break
        elif prime_numbers[-1] == k:
            prime_numbers.append(i)
            break


def better_sqrt(sqrt_arg: int) -> (int, int):
    result, sqrt = 1 if sqrt_arg > 0 else -1, abs(sqrt_arg)
    if 0 <= sqrt <= 1:
        return result * sqrt, sqrt
    for n in prime_numbers:
        if sqrt % (n ** 2) == 0:
            sqrt = sqrt // (n ** 2)
            result = result * n
            next_sqrt = better_sqrt(abs(sqrt))
            result, sqrt = result * next_sqrt[0], next_sqrt[1]
        elif prime_numbers[-1] == n:
            return result, sqrt


def bad_sqrt(result_arg: int, sqrt_arg: int) -> int:
    if 0 <= result_arg <= 1:
        return sqrt_arg * result_arg
    return result_arg ** 2 * sqrt_arg * (-1 if result_arg < 0 else 1)
