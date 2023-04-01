def recursive_multiplication(n):
    if n == 1:
        return n
    else:
        return n * recursive_multiplication(n - 1)


print(recursive_multiplication(5))
