a="Hey my name is {} and i am from {}"
name="Ronak"
country="India"
print(a.format(name,country))
# Here the {} made spacing in the string to be inputted and .format function helps to insert the string in the {}

print(f"my name is {name} and i am from {country}")
#The starting of string is f this is called as f string

#         DOC-Strings
def main(a):
    ''' here we can see that the number given is returning the squre value'''
    b=a**2
    return b
l=main(2)
print(l,main.__doc__)

# keep in mind that fstring prints the first thing that comes in after the defining def(((methode)))

#                   RECURSION
def fibbo(b):
    if b<=1:
        return b
    else:
        return(fibbo(b-1)+fibbo(b-2))
    
nth=10

for i in range(nth):
    print(fibbo(i))