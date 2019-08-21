# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

name = input("What is your name? ")
print("Nice to meet you " + name)
age = int(input("How old are you? "))
if age >= 40:
    print(str(age) + " makes you a sage!")
elif age >= 30:
    print("People who are " + str(age) + " years old are exciting!")
elif age >= 20:
    print(str(age) + "! You are a baby!")
else:
    print(str(age) + " is such a fun age to be!")
    
name = input("What's your name again? ")   
while True:
    try:
        num = int(input("Enter a number: "))
        for i in range(num):
            print(f"{name}, it's your lucky day!")
    except ValueError:
        print("That's not a number, Smarty!")
        continue
    else:
        print("Thanks for playing!")
        break