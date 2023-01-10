#Decorator

"""

A decorator is something we use to add new functionality to existing code without modifying the original code and
thereby the name decorator. We just decorate the function. In Python, we work with first class functions,
which gives us the opportunity to do the implementation as shown below.

This is a basic example of a decorator.

I have the existing function siesta() and I made a decorator timer() the can measure the execution time for my function.

"""

from colorama import Fore, Style
import time
from time import sleep

#Decorators

print(Fore.GREEN + "\n1. Decorators:" + Style.RESET_ALL)

#Eksempel
def timer(func):
    def inner():
        start = time.time()
        sleep(1)
        func()
        sleep(1)
        end = time.time()
        print("Total execution time: ", func.__name__, end - start)
    return inner


@timer
def siesta():
    print("Lets do siesta")

siesta()
