# creating a list 
courses = [
    "JavaScript" , 
    "Python" ,
    "HTML" ,
    "CSS"
]

# print(courses)

# accessing an element 
# print(courses[0])
# print(courses[1])

# accessing all elements 
# for course in courses:
#     print("I love to write" + " " + course)

# updating an element 
# courses[0] = "React"
# print(courses)

# adding an element 
courses.append("React")


# deleting an element
courses.remove("CSS")
print(courses)

# Getting the length
print("Length:" , len(courses))