import os

#if number divisible by 3, print fizz, if divisible by 5, print buzz, if divisible by both, print fizzbuzz,else print num

for num in range(1,100):
    if (num%3==0 and num%5==0):
        print("fizzbuzz")
    elif(num%3==0):
        print("fizz")
    elif(num%5==0):
        print("buzz")
    else:
        print(num)