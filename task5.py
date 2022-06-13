"""
5.	Find all perfect numbers up to 10000. A perfect number is a number that is equal to the sum of all its
divisors, except for itself. For example, the number 6 is perfect because itself is divisible by the numbers 1, 2,
and 3, which add up to 6.

"""


# Returns true if n is perfect

def numPerfect(n):
    sum = 1

    # Find all divisors and add them
    i = 2
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                sum = sum + i
            else:
                sum = sum + i + n / i
        i += 1

    return True if sum == n and n != 1 else False


n = 2
for n in range(10000):
    if numPerfect(n):
        print(n, " is a perfect number")

