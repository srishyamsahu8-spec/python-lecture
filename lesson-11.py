f=open('file.txt', 'r')  # it will open the file name and then 'r' it means Read
text=f.read() # We are extrect the data from the file

print(text)
f.close()


f=open('file.txt','w')
f.write('Hello, world')
# it will now open the file and then it will edit the file
f.close()

#____________________________________________________________________________________

#Similarly readline()
f=open('file.txt','r')
while True:
    line=f.readline()
    if not line:
        break
f.close()
# When it will finds empty line it will break

#Similarly writeline()
f=open('file.txt','w')
while True:
    if not line:
        line=f.writelines("hello guys")
    else:
        break
f.close()
# When it will finds a empty line it will write hello guys 
