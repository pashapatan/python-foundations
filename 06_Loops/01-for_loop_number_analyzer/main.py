numbers = [-12, -7, -25, -8, -14]

##To print all elements
for number in numbers:
    print(number)

##To count even numbers
count_even=0
for number in numbers:
    if number % 2 == 0:
        count_even += 1
print(count_even)


##To count odd numbers
count_odd=0
for number in numbers:
    if number % 2 != 0:
        count_odd += 1
print(count_odd)

##To print total and average
total=0
for number in numbers:
    total += number
print(total)
print(total/len(numbers))

##To print the largest number
largest=numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print(largest)

##To print the smallest number

smallest=numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
print(smallest)

