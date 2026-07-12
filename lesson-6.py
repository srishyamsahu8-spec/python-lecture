a=[1,2,True,"hello world"]  #this is called as list it is content friendly mean it can have any datatype

print(a)
print(len(a))
print(type(a))


print(a[1:3])  #Here also we can see that range is given 1 ---> 3
# here the code will work for 1 upto 2 (it will show)

print(a[1:3:2])
#The 3rd one will actually mean skip 




#   LIST COMPRIHENTION

lst=[i for i in range(10)]  # Output---->[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lst)


lst=[i*i for i in range(20) if i%2==0]
print(lst)



""""""
lst1=[1,2,3,4,]

lst1.append(5)  #append adds the following element in the last of the list  
#note we can apply append like that only noe like (5,6) this is wrong   X

print(lst1)


""""""
lst1.sort() #Here sort function is used to sort a list in a accending order
print(lst1)

lst1.sort(reverse=True) #Here sort Function is reversed then it makes Decending order
print(lst1)


lst.reverse() #This function only reverse the original list

lstrev=[1,1,1,2,3,4] 

print(lstrev.count(1)) #Count function only counts the number if the given is there in the list 
#ex=1 is 3 times

m=lst
m[0]=1212
print(lst) #Rather being changing in M the lst also changes because m becomes the reffrance of lst only

m=lst.copy()
m[0]=1212
print(lst) #Now the problem solved because of "copy" fucntion m is no longer is reffrance of lst

lst.insert(1,423) # now insert function helps like first the insert number then the number to be inserted


m=[23,23,23]
lst.extend(m)
#It will expand M and then insert it to the end of L 

k=lst+m
# yes we can concat 2 list with this but there in .extend function we see l=l+m
#               TUPLE


tup=(1,2,3)
print(type(tup),tup)
#the round bracket one is Tuple 
#we can't chance the date in Tuple but we can in list
#tup2=tup(1,2)  # tuf 2 will be not be corresponding tuple of tup and the range will be [x ---> y  (y-1)]

#to do any changes in Tuple we have to conveert the tuple first into list then the changes(list) into Tuple

#yet we can concat 2 tupels

tup2=(12,32,12)
print((tup+tup2))