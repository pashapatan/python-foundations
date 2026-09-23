# 🏝️ Treasure Island

A simple text-based adventure game built with Python using **conditional statements**.

##  About the Project

The player must make a series of choices to find the hidden treasure.

At each stage, the player's choice determines what happens next. Choosing the correct options leads to the treasure, while incorrect choices result in **Game Over**.

## Concepts Practiced

* `if`, `elif`, and `else`
* Nested conditional statements
* Comparison operators
* User input with `input()`
* String methods such as `.lower()`
* Program flow and decision-making
* Basic error handling for invalid choices

##  How It Works

The game has three main stages:

1. **Choose a direction**

   * `left` → continue
   * `right` → Game Over

2. **Choose what to do at the lake**

   * `wait` → continue
   * `swim` → Game Over

3. **Choose a door**

   * `red` → Game Over
   * `yellow` → You find the treasure
   * `blue` → Game Over

##  What I Learned

This project helped me understand how conditional statements control the flow of a program based on user input.

It also helped me practice breaking a problem into multiple decisions and using **nested `if` statements** to handle different possible paths.

## How to Run

Run `main.py` using Python:

```bash
python main.py
```

Then follow the instructions displayed in the terminal.
