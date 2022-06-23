#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

#2, 3, 5, 7, 11, 13, 17, 19

import time

#Checks if value is a prime and returns a boolean
def is_prime(x):

    i = 2
    #only looks if number is divisible by the root of it self
    while i <= int(x**0.5):
        if x%i  == 0:
            return(False)
        i += i

    return(True)

#takes the current prime or number and calculates the next prime returns int
def next_prime(x):
    i = 0
    x = x + 1
    while i == 0:
        if is_prime(x):
            return(x)
        x = x + 1

#checks the supplied value for prime factors and returns these as a list
def list_prime_factors(x):
    prime_factors = []
    i = 1
    list_index = 0
    while i < x:
        prime = next_prime(i)
        if x%prime == 0:
            prime_factors.append(prime)
            x = x/prime
            list_index = list_index + 1
        i = i + 1
    return(prime_factors)


start_time = time.time()
print(list_prime_factors(600851475143))
print("--- %s seconds ---" % (time.time() - start_time))
