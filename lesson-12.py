squre= lambda x: x*x #This is lambda function use for one liner functions
print(squre(int(input())))

def cube(x):
    return x*x*x

lst=[1,2,3,4]
newlst=[]
maplst=[]
filterlst=[]

for iteams in lst:
    newlst.append(cube(iteams))

print(list(newlst))  # we can write this all or just we can use MAP function

maplst=list(map(cube,lst)) # MAP FUNCTION MAKES IT SIMPLE
print(list(maplst))


def even(x):
    if(x%2==0):
        return x

filterlst=filter(even,lst) # filter function take outs the value with the help of lambda/mathod
print(list(filterlst))
