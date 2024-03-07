#  simple hello world function 
# def sayHello():
#     print("Hello world")

# sayHello()


# Return an object 

# def getUser():
#     user = {
#         "username" : "John deo" ,
#         "country" : "USA" ,
#         "gender" : "Male"
#     }

#     return user



# user = getUser()
# print(user["username"])


# function with one argurement
# def gretting(user_name):
#     print("Hello" + " " + user_name)

# gretting("Mary")


# function with two or more argurements
# def calculate(x, y , z , q):
#     print("Sum", x + y + z + q)
# calculate(20 , 30 , 40 , 50)


# hello world lambda function 
# # lambda arguments : expression

# grettings = lambda user_name : "Welcome" + " " + user_name 

# greet = grettings("John Deo")
# print(greet)



# Lambda function with two or more argurements
calculate = lambda x , y ,z : "sum:" + " " +  str(x + y + z )

result = calculate(20, 30, 10)
print(result)