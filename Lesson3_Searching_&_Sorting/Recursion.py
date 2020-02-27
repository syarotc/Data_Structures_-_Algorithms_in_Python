# Function for the Fibonacci number

def fibonacci1(n):  # Use recursion
    if n < 0:
        return "Incorrect input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci1(n - 1) + fibonacci1(n - 2)


FibArray = [0, 1]


def fibonacci2(n):  # Use Dynamic Programming
    if n < 0:
        return "Incorrect input"
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci2(n - 1) + fibonacci2(n - 2)
        FibArray.append(temp_fib)
        return temp_fib


def fibonacci3(n):  # Space Optimized
    a = 0
    b = 1
    if n < 0:
        return "Incorrect input"
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


print(fibonacci1(9))
print(fibonacci2(9))
print(fibonacci3(9))

