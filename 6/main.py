# comparing numbers
num1 = 29 

if num1 <= 31 :
   print("the statement is true")
else:
   print("the statement is false")


# comparing a string 
username = "john deo"

if username == "john deo" :
    print("Welcome john deo")
else:
    print("user is not john deo")


# using the elif statement 
username = "scott"

if username == "john deo" :
    print("Welcome john deo")
elif username == "john mary":
    print("Welcome john mary")
elif username == "micheal":
    print("Welcome Micheal")
else:
    print("User do not exist")


# using the or and and comparison
# check if num is 30 or 40 
num  = 50
if num == 30 or num == 40:
    print("The statement is True")
else :
    print("The statement is False")

# check if user is admin and username is john deo
user = {
    "username" : "john deo" ,
    "role" :"admin" 
}

if user["username"] == "john deo" and user["role"] == "admin":
    print("Admin")
else:
    print("user not admin")

# short hand for if and else

username = "john"

print("user is John doe") if username == "john deo" else print("User is not John deo")

num = 20 

print("Number is 20") if num == 20 else print("Number is not 20")