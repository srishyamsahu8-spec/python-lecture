
i=0
elm=[
    1   ,   2   ,   3   ,
    4   ,   5   ,   6   ,
    7   ,   8   ,   9   ,
]
Flag=1


def calc(a):
   if(elm[a-1]=="O" or elm[a-1]=="X"):
      next1()
   else:
       elm[a-1]="X"

def calcu(a):
    if(elm[a-1]=="O" or elm[a-1]=="X"):
     next2()
    else:
       elm[a-1]="O"

def display():
     print("----------------------")
     print(f":  {elm[0]}   :  {elm[1]}   :   {elm[2]}  : ")
     print("----------------------")
     print(f":  {elm[3]}   :  {elm[4]}   :   {elm[5]}  : ")
     print("----------------------")
     print(f":  {elm[6]}   :  {elm[7]}   :   {elm[8]}  : ")
     print("----------------------")
  


def accept(Flag):
    global i
    
    if Flag==1:
       print("\f PLAYER 2 WON")
    elif Flag==2:
       print("\f PLAYER 1 WON ")    
    elif Flag==3:
       print("\f DRAW")
    else:
         display()
         i=i+1
         
         next1()
         a=calculation()
         if(a is None):
         
            display()
            i=i+1

            next2()
         accept(calculation())
   

def next1():
   i=int(input("Now Select Your Number PLAYER-1:"))
   calc(i)
   

def next2():
   j=int(input("Now Select Your Number PLAYER-2:"))
   calcu(j)


def calculation():
   total=0
   if((elm[0]== "O" and elm[1]== "O" and elm[2] == "O")):
      total=1 
      total=1 
      return 1
   elif(elm[0]== "O" and elm[3] == "O"and elm[6] == "O"):
      total=1 
      total=1 
      return 1
   elif((elm[1] == "O"and elm[4]== "O" and elm[7] == "O")):
      total=1 
      total=1 
      return 1
   elif((elm[2]== "O" and elm[5]== "O" and elm[8] == "O")):
      total=1 
      total=1 
      return 1
   elif((elm[3]== "O" and elm[4]== "O" and elm[5] == "O")):
      total=1 
      total=1 
      return 1
   elif((elm[6]== "O" and elm[7]== "O" and elm[8]== "O")):
      total=1 
      total=1 
      return 1
   elif((elm[1]== "O" and elm[4]== "O" and elm[8] == "O")):
      total=1 
      return 1
   elif((elm[2]== "O" and elm[4]== "O" and elm[6] == "O")):
      total=1 
      return 1
   elif((elm[0]  == "X"and elm[1] == "X" and elm[2] == "X")):
      total=1 
      return 2
   elif((elm[0] == "X" and elm[3] == "X" and elm[6] == "X")):
      total=1 
      return 2
   elif((elm[1] == "X" and elm[4] == "X" and elm[7] == "X")):
      total=1 
      return 2
   elif((elm[2] == "X" and elm[5] == "X" and elm[8] == "X")):
      total=1 
      return 2
   elif((elm[3] == "X" and elm[4] == "X" and elm[5] == "X")):
      total=1 
      return 2
   elif((elm[6] == "X" and elm[7] == "X" and elm[8]== "X")):
      total=1 
      return 2
   elif((elm[1] == "X" and elm[4] == "X" and elm[8] == "X")):
      total=1 
      return 2
   elif((elm[2] == "X" and elm[4] == "X" and elm[6] == "X")):
      total=1 
      return 2
   
   if(i == 9 and total == 0):
      return 3

   

accept(0)
