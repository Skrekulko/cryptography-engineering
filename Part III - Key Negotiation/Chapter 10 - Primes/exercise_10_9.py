#! /usr/bin/env python

def BinaryAlgorithm(a, s, n):
    a %= n
    for i in range(s):
        a = a ** 2 % n
    return a, i + 1

def main() -> None:
    a = 27
    s = 35
    n = 569

    result = BinaryAlgorithm(a, s, n)
    print(f"The result is {result[0]} with {result[1]} multiplications done.")


if __name__ == "__main__":
    main()
