"""
Write a Python decorator that, when applied to a function,
logs the arguments the function was called with.

"""
from functools import wraps

def mydecorator(f):
                      def wrapper(*args,**kwargs):
                             print ("first")
                             f(*args,**kwargs)
                             print (" second")
                      return wrapper
    
                      
           

@mydecorator
def printName(name):
           print(name)

printName("RHT")
