# For Loop Number Analyzer

A simple Python project that uses `for` loops to analyze a list of numbers.

## Concepts Practiced

* `for` loops
* Lists
* `if` statements
* Modulo operator `%`
* Counters
* Accumulator variables
* List indexing
* `len()`
* Finding the largest and smallest values
* Calculating an average

## What the Program Does

Given a list of numbers, the program:

1. Prints all the numbers.
2. Counts the even numbers.
3. Counts the odd numbers.
4. Calculates the total.
5. Calculates the average.
6. Finds the largest number.
7. Finds the smallest number.

## Example

Input:

```python
numbers = [-12, -7, -25, -8, -14]
```

Output:

```text
-12
-7
-25
-8
-14
3
2
-66
-13.2
-7
-25
```

## Key Learning

This project helped me understand how `for` loops can be used to process each element of a list and perform calculations or comparisons.

For example:

```python
for number in numbers:
    if number % 2 == 0:
        count_even += 1
```

This checks each number and counts how many are even.

The project also demonstrates how initializing `largest` and `smallest` with the first element of the list makes the logic work correctly with negative numbers.
