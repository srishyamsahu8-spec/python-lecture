dic={
    "ronak": "name" ,
    "1": "number",
    1:"ronak",
    2:"sahu"

}
print(dic["1"],dic[1])
# we use the .get() to not get error
# if we use dict and the element is not there then it will through error
print(dic.keys()) # it gives the key to the dic
print(dic.values()) # it gives the values
print(dic.items()) # it gives the items in the dic list
# .info() gives the info of the set

ep1={122:20,121:40,321:50}
ep2={211:32,421:43,213:43}

ep1.update(ep2) # it means that ep1 will update and will also store ep2 value
print(ep1.popitem()) # this function will just remove last element 

#       EXCEPTION HANDLING


a=input("give a number:")
# What if input is a string then? and code breaks but want to execute full code------->
try:
    for i in range (11):
     print(f":{int(a)} X {int(i)}: {int(a)*i}")
except Exception as e:
    print("error found:  ", e)

print("program ends here")

def fun(s):
   a=[1,2,4,5,6]
   try:
      print(a[s])
      return 1
   except:
      print("found error")
      return 0
   finally:
      print("okey")
    
print(fun(int(input("give a number"))))

a=int(input("Enter a number: "))
if (a<10 or a>20):
    raise ValueError(" Nope Not OK") # this is use to stop the code 


# So here what is happening is first input is given then the input is proceed to function and function is returning a value
# but if the code breaks inside function it returns so we use finally() to execute to necceary code 