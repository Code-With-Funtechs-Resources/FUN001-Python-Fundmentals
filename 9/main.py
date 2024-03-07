# For loop: Generate list of numbers
for x in range(0, 25 , 2):
    print(x)

# For loop loop a list 
courses = [
    "JS" ,
    "Python" ,
    "Next js" ,
    "React js"
]

for course in courses:
    print("course:" , course)

# Looping a string 
sentence = "This is the sentence I wanna loop" 

for character in sentence:
    if character == "I": 
        continue  
    print(character)

  

# Using the else 
for character in sentence:
    if character == "I": 
        continue  
    print(character) 

else:
    print("Done Looping")


# While Looping 
i = 0 

while i <= 10:
    print(i)
    i += 2

# Looping a list with while loop
courses = [
    "JS" ,
    "Python" ,
    "Next js" ,
    "React js"
]
i = 0 

while i < len(courses):
    print(courses[i])
    i += 1