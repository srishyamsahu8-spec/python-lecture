def geomatricmean(a,b):
   b=(a*b)/(a+b)
   print(b)

a=int(input("input a number "))
b=int(input("input another number "))
geomatricmean(a,b)

while True:
   if(a==0 or b==0):
      break
   else:
      a=int(input("input a number "))
      b=int(input("input another number "))
      geomatricmean(a,b)

print("Code over")

# Here we can see that we are giving input to code and the code is give the value to the method 
#   and computing the value and printing it 
 
def less():
   pass # pass is used for leave the code for later to be written



#Types of function arguments--------------------------------------------->

#           DEFAULT ARGUMENT
   
def main(a=2,b=4):
   print("the avarage will be=",(a+b)/2)

def man(a=1,b=1):
   print("the avarage will be=",(a+b)/2)

man(2,2)   #here this 2,2  will be executed now
man(5)    #here only value of a will change to 5 , b  will have default value given in function (1)

#Where we have intially given the values to the argument

#            KEYWORD ARGUMENT

def num(a=1,n=3):
   print("the avarage will be=",(a+b)/2)

num(b=2,a=6) # in this way also the code understands and provide the answer and will take the new value not the function given value

def numb(a=1,n=3):
   return (a+b)/2  #Return function returns the value after computing

c=numb(a=1,b=13)  #Here C got the value of the returned compute 
print(c)
   

