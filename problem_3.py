# Problem 2 of Project Euler
# Python 3.9.5
# Largest prime factor

# Find the largest prime factor of the number 600861475143
# Prime number is a number > 1, cannot be made by multiplying other whole #'s


# Find the factors of the large_number


large_number = 600851475143

def factors(nr):
    i = 2
    factors = []
    while i <= nr:
        if (nr % i) == 0:
            factors.append(i)
            nr = nr / i
        else:
            i = i + 1
    return factors

print(factors(8))
print(factors(9))
print(factors(10))
print(factors(84))
print(factors(large_number))
