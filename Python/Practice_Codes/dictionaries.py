courses = {

    "BS - IT": "BS - Information Technology",
    "BS - CE": "BS - Computer Engineering",
    "BS - DS": "BS - Data Science",
    "BS - CS": "BS - Computer Science",

}


course = courses["BS - DS"]

course2 = courses.get("BS - IT")

print("1st Year: " + course)
print("1st Year: " + course2)

person = {

    "George": 62,
    "Mark": 20,
    "Krishia": 19,
    "Hazel": 19

}

print(person[input("Enter name: ")])