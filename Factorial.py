import sys


def Fact(n):
    return 1 if n == 0 else n*Fact(n-1)


def Fib(n):
    if n > 2:
        return Fib(n-1)+Fib(n-2)
    return 1 if n > 0 else 0


if len(sys.argv) > 1:
    print(f'There are one or more arguments {sys.argv[1:]}')
else:
    print("no argument input")

print(Fact(5))
print(Fact(7))

print(Fib(1))
print(Fib(4))
print(Fib(7))