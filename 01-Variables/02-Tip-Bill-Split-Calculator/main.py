print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill? $"))
tip_percentage=float(input("How much tip would you like to give? 10, 12 or 15? "))
number_of_people=int(input("How many people to split the bill? "))
tip_amount = total_bill * tip_percentage / 100
total_amount=total_bill+tip_amount
each_person_amount=round(total_amount/number_of_people, 2)
print(f"Each person should pay: ${each_person_amount}")

