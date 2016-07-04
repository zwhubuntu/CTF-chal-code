'''
Created on 2016-2-21

@author: wenhuizone
'''

from itertools import count
from math import sqrt


def first_primes(n):
    def prime_gen():
        primes = []
        for n in count(2):
            if all(n%p for p in primes if p <= sqrt(n)):
                primes.append(n)
                yield n
    primes = []
    for i, j in enumerate(prime_gen()):
        # if i < n:
        if i < (n+1):
            primes.append(j)
        else:
            break
    # return primes
    print primes
print first_primes(200)