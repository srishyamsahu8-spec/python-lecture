a=330
b=3330
print("A") if a>b else print("=") if a==b else print("B")
 
c=9 if a>b else 0
print(c)  # this called short hand if-else 
# here we can assign the value using condtion

marks=[12,32,54,65,76]

for index,mark in enumerate(marks): #it means i=0 then 12
    print(mark)
    if(index==3):
        print("NAME,AUSOME!!")

# means when the index gets 3 it prints "NAME,AUSOME!"
# Enumerate helps to increment index as marks

import math # we can wwrite also   from math import floor,sqrt
print(math.floor(13.2))
print(math.sqrt(4))

import math as m
print(m.pi)
import PYTHON as q
a=q.fun(10)
print(a)

def mai():
    print("Hello good boy! ")

print(__name__)

if __name__=="__main__": #this gives a specific or it run the function 2 times
 mai()

# -------------------------------------------------------------------------------------------------------------

x=10 # Global variable

def function():
    x=5 # Local variable
    print(x)

function()

print(x)
 
#but we can chnage the global variable also

def func():
    global x
    x=3
    print(x)
func()
print(f"Number: {x}")