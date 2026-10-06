students = ["Pasha", "Ravi", "Kiran", "Vikas", "Jaleel"]
marks = [85, 72, 91, 64, 78]

# 1. Print all students and their marks
counter = 0
for mark in marks:
    print(f"{students[counter]}: {mark}")
    counter += 1

# 2. Highest mark
print("Highest mark:", max(marks))

# 3. Lowest mark
print("Lowest mark:", min(marks))

# 4. Average mark
average_marks = sum(marks) / len(marks)
print("Average mark:", average_marks)

# 5. Count students scoring 80+
counter = 0
for mark in marks:
    if mark >= 80:
        counter += 1

print("Students scoring 80+:", counter)

# 6. Student with highest mark
max_marks = max(marks)
index_max = marks.index(max_marks)
print("Highest scorer:", students[index_max])

# 7. Student with lowest mark
min_marks = min(marks)
index_min = marks.index(min_marks)
print("Lowest scorer:", students[index_min])

# 8. Search for a student
search_name = input("Enter student name: ")

if search_name in students:
    student_index = students.index(search_name)
    print(f"{search_name} scored {marks[student_index]}")
else:
    print("Student not found")

# 9. Add a new student
students.append("Pavan")
marks.append(85)

print("After adding Pavan:")
print(students)
print(marks)

# 10. Remove a student
student_index = students.index("Pasha")
students.pop(student_index)
marks.pop(student_index)

print("After removing Pasha:")
print(students)
print(marks)

# 11. Sort marks
sorted_marks = sorted(marks)
print("Sorted marks:", sorted_marks)

# 12. Display passed students
print("Passed students:")

counter = 0
for mark in marks:
    if mark >= 60:
        print(f"{students[counter]}: {mark}")
    counter += 1

# 13. Display failed students
print("Failed students:")

counter = 0
for mark in marks:
    if mark < 60:
        print(f"{students[counter]}: {mark}")
    counter += 1
