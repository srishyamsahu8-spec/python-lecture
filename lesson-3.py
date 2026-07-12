a=int(input("enter your age"))
if(a>=18):
    print("you can drive")
else:
    print("you cannot drive")

# Conditional Operators-------->                     <  ,  >  ,  ==  ,  >=   ,   <=  ,  !=

# &--> means and       |----> means or  


b=10
 
if(b>10 & b < 15):
    print("hell yeah")
elif(b==10):
    print('ok')  #elif means ELSE IF (WHAT) if first condition does not satisfy

#   Good moring sir
import time # it takes time from the system
timespan=time.strftime('%H:%M:%S') #remember .strftime()
print(timespan)
 
timespam=int(time.strftime('%H'))

if (timespam >= 0 and timespam < 12):
    print("good morning sir")
elif (timespam >= 12 and timespam < 16):
    print("good afternoon sir")
else:
    print("good evening sir")


''''''




#match case--------swtich case()

num=int(input("enter a number"))
match num:
    case 0:
        print("NUMBER IS ZERO",num)
        #Here the case is given by of num 0
    case _ if num > 1 and num < 10:
        print("NUMBER IS ABOVE 1 AND BELOW 10:",num)
        #this defult case and we use if() like this 
    case _ if num!=11:
        print("the number is not 11")
    case _ if num !=12:
        print("Number is not 12")

#''''''If we input num=11 then the below case  
#    case _ if num !=12:
      #  print("Number is not 12")------> this will execute 
    