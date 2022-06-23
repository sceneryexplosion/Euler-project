#If we list all the natural numbers below 10 that are multiples of 3 or 5,
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

i=1  #Start at 1 to leave out the initial 0
sum = 0

while i < 1000:

    j = i%5
    k = i%3

    if j == 0 or k == 0:
        print(i)
        sum += i

    i += 1

print(sum)


#Result 233168
