#Create tuples to store student information(name, age, grade)
student1 = ("shiva", 26, "A")
student2 = ("Unique", 26, "B")
student3 = ("Rohit", 32, "C")

#create a tuple of all student record
students = (student1,student2,student3)

#lenght of students tuple 
print(len(students))

#Check index of student2
print(f"Index of student2 :: {students.index(student2)}")

#print index 0 of student1 from students tuple
print(students[0][0])

#create set of student id and courses
student_ids = {101,102,103,104,105}
courses = {"Math", "Science", "English", "History", 'Hindi'}

#Performing set operations
print(f"Stidents Ids: {student_ids}")
print(f"Courses : {courses}")

student_ids2 = {106,103,104,109}

# union in set
print(f"Union :: {student_ids.union(student_ids2)}")
# Intersection in set
print(f"Intersection :: {student_ids.intersection(student_ids2)}")
# difference in set
print(f"Difference :: {student_ids.difference(student_ids2)}")

frozen_set = frozenset(["pepaPig", "tom", "jerry", "Goku", "Osworld"])
print(f"frozen set :: {frozen_set}")

