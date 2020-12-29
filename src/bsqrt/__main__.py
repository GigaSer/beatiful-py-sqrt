import sys
from __init__ import *


def main():
    args_count = len(sys.argv)
    if args_count >= 2:
        try:
            if sys.argv[1] == 'convert':
                if args_count >= 4:
                    print(f'√{bad_sqrt(int(sys.argv[2]), int(sys.argv[3]))}')
                else:
                    print('You need enter two numbers: factor and square root like 4 1 -> 16')
            elif sys.argv[1] == 'parse':
                if args_count >= 3:
                    res, sqrt = better_sqrt(int(sys.argv[2]))
                    print(f'{res if res != 1 or sqrt == 1 else ""}{("√" + str(sqrt)) if sqrt > 1 else ""}')
                else:
                    print('You need enter a square root like 16 -> 4√1')
            else:
                print('The first argument is invalid, you can use:\n'
                      '\tparse - it will return a tuple, where the first number taken out, and the second number '
                      'remainder of the root\n'
                      '\tconvert - it returns a full square root and takes two argument, where first is a factor and '
                      'second is square root')
        except ValueError:
            print('Number(s) is invalid')


# print(f'√{bad_sqrt(num, num2)}')
# print(f'{res if res != 1 or sqrt == 1 else ""}{("√" + str(sqrt)) if sqrt > 1 else ""}')

if __name__ == '__main__':
    main()
