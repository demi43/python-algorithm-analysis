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

# trying to figure out the best brute force way to solve the question 
<<<<<<< HEAD
sum=0
result[][]=[]
for i in range(0, len(digits)):
  sum+=digits[i]
if sum % 2==0:
  
else:
  print("No disjoint subsets with the smae sum of their elements found")
=======
def main():
    while True:
        print("""-----------------MAIN MENU-------------- 
1.  Read input string 
2.  Run algorithm and display outputs 
3.  Exit program 
 
       Enter option number:
        """)
         # error handling so it doesnt crash on invalid inputs like alphabets 
        try:
            option=int(input("Enter your option: "))
        except ValueError:
            print("\nInvalid Input! Please enter a number.....")
            continue
        match option:
            case 1:
            case 2:
            case 3:
            case 4:
            case _:
                 # if input is invalid we return an error message which only affects numbers exceeding 3 or below 1
                print("\ninvalid input try again....") 
def algorithm():
    sum=0
    result[][]=[]
    for i in range(0, len(digits)):
        sum+=digits[i]
    if sum % 2==0:
    
    else:
        print("No disjoint subsets with the smae sum of their elements found")
>>>>>>> 667f444 (Added Substrings.py comments and updated Partition.py)
