# Creating a dictionary 
user = {
    "email" : "johndeo@gmail.com" ,
    "age" : 21 ,
    "username" : "John Deo"
}



# Getting and attribute 
email = user["email"]
age = user["age"]
username = user["username"]

print("Email:" , email)
print("Age:" , age)
print("Name:" , username)

# adding new attribute 
user["biography"] = "I love to write python codes"
# print(user)


# Updating and attribute 
user.update(
{"age" : user["age"] + 1 , "biography" : "This is my new bio"} 
)
# print(user)

# removing and attribute 
del user["email"]
# print(user)

# Nesting 
user = {
    "email" : "johndeo@gmail.com" ,
    "age" : 21 ,
    "username" : "John Deo" ,
    "payment":{
        "address" : "Street 243",
        "country" : "USA",
        "zip_code" : "00393838"
    }
}

payment_details = user["payment"]
print("payment Details:" ,payment_details)

zip_code = payment_details["zip_code"]
country = payment_details["country"]
print("Zip code:" , zip_code)
print("Country:", country)