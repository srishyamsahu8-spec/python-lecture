a="1"
b="2"
print(int(a)+int(b)) #explicit type convertor where we used int(),float(),str() etc
 
c=input("input first number")
d=input("input second number")

#-------->  if input is given 1 and 2 then 


print(c+d) #12

print(int(a)+int(d)) #3

""""""



#ok now lets see string function 

print('''  hrihfirwfoerhg
      rgengeont
      iergeii ''')  #here we can see that by using (''') we can write entire paragraph of lines

e="apple"
print(e[0]) #a
print(e[1]) #p
print(e[2]) #p
print(e[3]) #l
print(e[4]) #e

print('\n \t   loop ')




#MORE IN STRINGS

f= "my name is Srishyam sahu"
print(f[0:5])
#     when we print the starting index will print but the ending index will not print (here we can see the index number 5)
# will not be print before that mean index number 4 will print



#for length we use 'len' function
print(len('ram')) #----> output:3

#strings are immutable
name="!!ronak!!! !!! OH "
print(len(name))
print(name.upper()) #!!RONAK!!!!!!!
print(name.lower()) #!!ronak!!!!!
print(name.rstrip("!")) #!!ronak
print(name.replace("ronak","john")) #!!john!!!!!!
print(name.split(" ")) # split every words into a grp


intro="hello friend"
print(intro.capitalize()) #Hello friend



main="his name is dev he is a very good boy "
print(main.endswith("boy")) #simply checks ending word 
print(main.center(50)) #if the sentence is about 40 words then it will make it to 50(coder choice) bu adding space in front
print(main.endswith("is", 2 , 10)) #this ends with is with range like [2,10] does it ends with is or not ((true)/(false))
print(main.find("is")) #finds where the chars u asked(word)
#index is also same as find but with most precision like it does not gives true or false values it break the code instantly
print(main.isalnum()) #string with A-Z a-z 0-9
print(main.isalpha()) #string with A-z a-z
print(main.islower()) #check if all char is lower
print(main.isupper()) #check if all char is upper
print(main.isprintable()) # printable---> means no chars lke \n,\t,\b etc
str1="   "
print(str1.isspace()); # is there is space? it checks 
str2="Are O Bhai"
print(str2.istitle()) # means see the ex (A)re (O) (B)hai its a title
print(str2.swapcase()) #swaps uppercase---> lower case vice-versa
print(intro.title()) #changes it to a title if is does not also