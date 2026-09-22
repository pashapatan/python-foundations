
print("-------- STUDENT RESULT --------")
print()

student_name = input("Student: ")
print()

math_marks = int(input("Math: "))
physics_marks = int(input("Physics: "))
chemistry_marks = int(input("Chemistry: "))
english_marks = int(input("English: "))
computer_science_marks = int(input("Computer Science: "))

print()

total_marks = math_marks + physics_marks + chemistry_marks + english_marks + computer_science_marks
average = total_marks / 5
percentage = (total_marks * 100) / 500

print(f"Student: {student_name}")
print(f"Total: {total_marks}/500")
print(f"Average: {average}")
print(f"Percentage: {percentage}%")

if percentage >= 91:
    print("Grade: A+")
elif percentage >= 81:
    print("Grade: A")
elif percentage >= 71:
    print("Grade: B")
elif percentage >= 61:
    print("Grade: C")
elif percentage >= 51:
    print("Grade: D")
else:
    print("You are fail")

