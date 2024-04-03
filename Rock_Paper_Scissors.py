#!/usr/bin/env python
# coding: utf-8

# # Title:
# Rock-Paper-Scissors Game

# # Objective:
# To create a simple interactive game where the user can play against the computer in a game of Rock-Paper-Scissors.

# # Problem Statement:
# Traditional games often require physical components and can be played only in person. This project aims to create a digital version of the popular Rock-Paper-Scissors game, providing entertainment and an opportunity for users to engage in a fun activity without the need for physical materials

# # Tools:
# 
# Programming Language: Python
# Libraries: Random (for generating computer choices)

# In[13]:


import random
user_choice=int(input("Enter Your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors."))
if user_choice >= 3 or user_choice < 0:
    print("You entered invalid number, You lose.")
else:
    computer_choice=random.randint(0,2)
    print("Computer chosen: ",computer_choice)
    if computer_choice == user_choice:
        print("It's a draw.")
    elif computer_choice > user_choice:
        print("You Lose.")
    elif user_choice > computer_choice:
        print("You win.")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif user_choice and computer_choice == 2:
        print("You win.")
    

