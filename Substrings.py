
# Name: Omodemi Olaoluwa Adedamola
# Class: CS 4306/03
# Term: Spring 2026
# Instructor: Dr. Abdur Rahman
# Assignment: 2
# IDE Name: Visual Studio Code

# Algorithm Design Block
# Algorithm Title: Substrings 

# Logical Steps:
# 1. Display a menu to the user.
# 2. Prompt the user to select an option.
# 3. If Option 1 is selected:
#     a. prompt user for a string   
# 4. If Option 2 is selected:
#     base cases
#           check if the string has any values if so return enter string values from A-Z  values  
#     run algorithm using two pointer algorithm 
#        we have a pointer l if the pointer value is A then we increment r which is equal to l at the point of seeing A then we increment r until we see B then store that into the list then continue incrementing to check if there is any other B then once we see there is no other B we increment l then repeat the sequence 
# 5. If Option 3 is selected:
#    a. Exit the program.
# 6. Repeat the menu until the user chooses to exit.

# trying to figure out the best brute force way to solve the question 
i=0
list=[]
for i in range(len(string))://looping through the given string to find A 
  if string[i]=="A":  //Checking if the A is in the current index
     for j=i+1 in range(len(string)):// if A is found start from the index after A 
        if string[j]=="B":// check if it is B and if it is store it into the list and continue looking for other B 
          list.add(string[i:j])

          
    
