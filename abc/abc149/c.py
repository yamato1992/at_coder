from math import sqrt, ceil

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    for i in range(5, ceil(sqrt(n))):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    
    return True

def next_prime(N):
    if (N <= 1):
        return 2
    
    prime = N
    found = is_prime(N)

    while(not found):
        prime += 1

        if (is_prime(prime)):
            found = True
    
    return prime

X = int(input())

print(next_prime(X))
