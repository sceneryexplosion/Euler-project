#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

#2, 3, 5, 7, 11, 13, 17, 19

import time
#Checks if the supplied value is divisible by any of its roots
#and if it is then the value is not prime
def is_prime(tal):

    root = int(tal**0.5)
    i = 2
    while i <= root:
        if tal%i  == 0:
            return(False)
        i = i + 1

    return(True)

#supply how many primes you want
def list_primes(antal):
    i = 2
    list = []
    while len(list) < antal:
        if is_prime(i):
            list.append(i)
        i = i + 1
    return(list)

#listar alla primtal upp till antal
def list_primes_to(antal):
    #print("Creating a list of all the primes upp to: " + str(antal))
    i = 2
    list = []
    while i < antal:
        if is_prime(i):
            list.append(i)
        i = i + 1
    #print("Done!")
    return(list)


def list_prime_factors(stort):
    root = int(stort**0.5)
    prime_list = list_primes_to(root)
    list = []
    i = 0
    #print(len(prime_list))
    while i < len(prime_list):

        if stort%prime_list[i] == 0:
            #print(prime_list[i])
            list.append(prime_list[i])
            stort = stort/prime_list[i]
        i = i + 1

    return(list)
start_time = time.time()
list = list_prime_factors(600851475143)
print(list)
#print(71*839*1471*6857)
print("--- %s seconds ---" % (time.time() - start_time))
#6857
