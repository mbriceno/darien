import sys
import os
from functools import reduce

def bubblesort(elements):
    swapped = False
    # Looping from size of array from last index[-1] to index [0]
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                swapped = True
                # swapping data if the element is less than next element in the array
                elements[i], elements[i + 1] = elements[i + 1], elements[i]       
        if not swapped:
            # exiting the function if we didn't make a single swap
            # meaning that the array is already sorted.
            return


def prime_generator():
    for j in range(1,1001):
        number = j #1
        i = 2
        factor = 0
        while i < number: 
            if number%i== 0:
                factor +=1
            i+=1
        if factor == 0 and number > 1:
            yield number


def fibo():
    i = 1
    n1 = 0
    n2 = 1
    while i <= 10:
        fab_no = n1+n2
        print("Fib de {} = {}".format(i, fab_no))
        n1,n2 = n2,fab_no
        i+=1


def palindrome():
    num=int(input("Enter a number = "))
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10

    if(temp==rev):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")


import time
import math
 
# decorator to calculate duration
# taken by any function.
def calculate_time(func):
     
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
 
        # storing time before function execution
        begin = time.time()
         
        func(*args, **kwargs)
 
        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
 
    return inner1
 

# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
 
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))


if __name__ == '__main__':
    elements = [39, 12, 18, 85, 72, 10, 2, 18]
    bubblesort(elements)
    print(elements)

    prime_no = prime_generator()
    print("1st 20 prime no = ")
    for j in range(1,5):
        print(next(prime_no))
    
    fibo()

    palindrome()

    factorial(10)

# print(sys.argv)

# name = input("Your name: ")

# print("This is your name: {}".format(name))