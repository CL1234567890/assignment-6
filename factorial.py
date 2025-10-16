'''
def factorial(n: int) -> int:
    # BUG: off-by-one (range should go to n + 1)
    if n == 0:
        return 1
    result = 1
    for i in range(1, n):  # <-- deliberate bug
        result *= i
    return result

if __name__ == "__main__":
    print("factorial(5) =", factorial(5))  # will print 24 (wrong)
'''



def factorial(n: int) -> int:
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):  # Fixed range to include n
        result *= i
    return result

if __name__ == "__main__":
    print("factorial(5) =", factorial(5))  # will now print 120 (correct)

