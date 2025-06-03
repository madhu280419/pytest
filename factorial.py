def factorial(n):
    if n < 0:
        raise ValueError("Negative input not allowed")
    return 1 if n in (0, 1) else n * factorial(n - 1)
