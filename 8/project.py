#  list of shopping courses 
courses = [
    "JavaScript" ,
    "Python" ,
    "Machine Learning" ,
    "HTML" ,
    "CSS"
]

# get all the courses 
def get_courses():
    if len(courses) > 0:
        return {
            "status" : "ok" ,
            "data" : courses ,
            "total": len(courses) 
        } 
    else:
        return {
            "status" : "error" ,
            "message" : "No courses available"
        }


if get_courses()["status"] == "ok":
   print(get_courses()["data"])
else:
    print(get_courses()["message"])


# add a course 
def new_course(course):
    courses.append(course)
    return get_courses()["data"]

docs = new_course("React")
# print(docs)


# update a course 
def  update_course(id , new_value):
    courses[id] = new_value 
    return get_courses()["data"]

docs = update_course(1 , "Next JS")
print(docs)

# Removing a course 
def delete_course(value):
    courses.remove(value)
    return get_courses()["data"]

docs = delete_course("HTML")
print(docs)