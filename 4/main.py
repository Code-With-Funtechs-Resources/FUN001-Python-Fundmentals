sentence = "This is my string"

# length 
sentence_length = len(sentence)
print("Length:" , sentence_length)


# upper case 
upper_sentence = sentence.upper()
print("Upper:", upper_sentence)

# lowercase 
lower_sentence = sentence.lower()
print("Lower:", lower_sentence)


# title and capitalize 

title_sen = sentence.title()
print("Title:" , title_sen) 

capitalize_sen = sentence.capitalize()
print("Capitalized:" , capitalize_sen)


# trimming
sentence = " This is my string "
print("Length before trimming:" , len(sentence))

sentence = sentence.strip() 
print("Length after trimming:" , len(sentence))


# starts with and ends with 
sentence = "This is my string"

check_start = sentence.startswith("T")
print("Starts with:" , check_start) 

check_end = sentence.endswith("t") 
print("Ends with:" , check_end)

# replace 
sentence = "This is my string" 

replaced_text = sentence.replace("my" , "a")
replaced_text = replaced_text.replace("string" , "text")
print(replaced_text)


# spliting 
users = "John,mary,deo,micheal"
users = users.split(",") 

print("Users:" , users)