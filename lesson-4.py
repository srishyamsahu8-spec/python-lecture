# FOR LOOP----------------------------------->

a=["red","green","yellow"]
for i in a:
    print(i)
    # output will be ------->
                                         # red
                                         # green
                                         # yellow
#-----------------------------------------------------


for i in range (10):
    print(i)
#the loop will start from 0 to 9 // the output will be 0-9

for i in range (1,100):
    print (i)
# the loop will starts from 1 to 99


# special case increment

for i in range (0,11,2):
    print (i)                 #output will be even numbers from 0-10



#                       for i in range (x,y,z)
#   x is the starting range 
#   y is the closing range(output will be (y-1) )
#   z is the amound to increment (how much it will increment)  )


""""""

#  WHILE LOOP----------->

i=0
while(i<=3):
    print(i)
    i=i+1

print ("the looop is completed")


num=int(input("input a number"))
i=0
while(i<=num):
    print(i)
    i=i+1
else:
    print("the loop is over")  #when the loops gives false and doesnot execute then this else will work


#There is break statement use in loops and continue statement
i=0
while True:
    i=i+1
    if(i==10):
        break
    else:
        print (i)
        continue


#     FOR WITH ELSE

for i in range (10):
    print("hello:",i)
    if i==5:
        break
else:
    print("hii")
 
 #When the loop end(by the break statement the else does not execute)