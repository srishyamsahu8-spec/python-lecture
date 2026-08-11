import os # this imports os means our code can can change the acctual data of the PC

os.mkdir("data.py") # this will just make the file fresh in the PC
if (os.path.exists("data") ) : 
    os.rename("data")

 # In this .path() will scan the folder for the file name("Data")
 # If the file found then  .rename() will remane it

folder=os.listdir("PYTHON")
print(folder)


print(os.cwd()) # in which directory the file i am using 
 
 # os.chdir() can change the directory 