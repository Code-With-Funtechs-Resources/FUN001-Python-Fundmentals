import os
# check if file exist 
if os.path.exists("demo.txt"):
    print("File Exist")
else:
    print("File Do Not Exist")




# opening a file : r
if os.path.exists("demo.txt"):
    f = open("demo.txt" , "r")
    docs = f.readlines()
    
    for x in docs:
        print(x)
    else:
        f.close()

else:
    print("File Do Not Exist")




# Creating a file x
if os.path.exists("demo2.txt"):
    print("File Already Exist")
else:
    f = open("demo2.txt" , "x")
    print("File created")
    f.close()



# Appending: a and overwriting:w to a file 
if os.path.exists("demo2.txt"):
    f = open("demo2.txt" , "w")
    f.writelines(
        [
            "\nThis is the second line" ,
            "\nThis is the 3 line" ,
            "\nHappy Python" ,
        ]
    )

    f.close()
else:
    print("File Do not Exist")
   