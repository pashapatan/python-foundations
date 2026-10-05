students = ["Pasha", "Lal", "Jan", "Patan", "Jaleel"]

print(students[2])
print(students[-1])

students[1] = "Ravi"
students.append("Vikas")
students.insert(2, "Kiran")
students.remove("Patan")
students.pop(2)

print(len(students))

if "Pasha" in students:
    print("Pasha is in the list")

for student in students:
    print(student)
