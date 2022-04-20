fibo_cache = {}

def fibonacci(n):

    if n in fibo_cache:
        return fibo_cache[n]

    else:
        fibo_cache[n] = n if n < 2 else (fibonacci(n - 1) + fibonacci(n - 2)) % 10009
        return fibo_cache[n]

print(fibonacci(int(input())))

