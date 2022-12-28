import numpy

limit = 100_000

def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(n//2, dtype=bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1

primes = primesfrom3to(limit)

print("Computed primes")

def get_a_primes(primes):
    a_working = []
    for x in range(len(primes) - 1):
        sum = 0
        for digit in str(primes[x]): 
            sum += int(digit)
        if (int(primes[x]) + sum) == primes[x + 1]:
            a_working.append(primes[x])
    return a_working

a_primes = get_a_primes(primes)
print("Solved a primes")
print(a_primes)


def get_am_primes(primes):
    am_working = []
    for x in range(len(primes) - 1):
        sum = 0
        for digit in str(primes[x]): 
            sum += int(digit)
        mul = 1
        for digit in str(primes[x]): 
            mul *= int(digit)
        if (int(primes[x]) + sum + mul) == primes[x + 1]:
            am_working.append(primes[x])
    return am_working

am_primes = get_am_primes(primes)
print(am_primes)

solution = []
for x in range(len(am_primes)):
    if am_primes[x] not in a_primes:
        solution.append(am_primes[x])
    else:
        continue
        
print("Solved:", solution)
