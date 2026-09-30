import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '@', '#', '$', '%', '^', '&', '*']
print("Welcome to the Password Generator!")
letters_count=int(input("How many letters would you like in your password?\n "))
numbers_count=int(input("How many numbers would you like?\n"))
symbols_count=int(input("How many symbols would you like?\n"))
password=[]
for _ in range(letters_count):
    password.append(random.choice(letters))
for _ in range(numbers_count):
    password.append(random.choice(numbers))
for _ in range(symbols_count):
    password.append(random.choice(symbols))
random.shuffle(password)
final_password = ''.join(password)
print(f"Here is your final password: {final_password}")

