
# Name: Omodemi Olaoluwa Adedamola
# Class: CS 4306/03
# Term: Spring 2026
# Instructor: Dr. Abdur Rahman
# Assignment: 2
# IDE Name: Visual Studio Code

# Algorithm Design Block
# Algorithm Title: Substrings 

# Display a menu to the user.
# Prompt the user to select an option.
# If Option 1 is selected:
#   Prompt the user to enter a string.
# If Option 2 is selected:
#    If the string is empty, display an error message.
#    Otherwise:
#           Initialize an empty list to store substrings.
#           Initialize comparison counter to 0.
#           For each index i from 0 to n − 1:
#               Increment comparison counter.
#                   If character at position i (ignoring case) is 'A':
#                       For each index j from i + 1 to n − 1:
#                           Increment comparison counter.
#                           If character at position j (ignoring case) is 'B':
#                               Store substring from i to j.
#            Display:
#               Input string
#                    Number of substrings
#                    List of substrings
#                    Number of comparisons
# If Option 3 is selected:
# Exit the program.
# Repeat the menu until the user chooses to exit.

# Pseudocode Syntax: 
# PROCEDURE MainProgram
#     DECLARE word AS STRING ← ""
#     LOOP FOREVER
#         DISPLAY "----------------- MAIN MENU --------------"
#         DISPLAY "1. Read input string"
#         DISPLAY "2. Run algorithm and display outputs"
#         DISPLAY "3. Exit program"
#         INPUT option
#         IF option IS NOT INTEGER THEN
#             DISPLAY "Invalid Input! Please enter a number."
#             CONTINUE LOOP
#         ENDIF
#         SWITCH option
#             CASE 1:
#                 INPUT word
#             CASE 2:
#                 CALL SubStringalgorithm(word) → result, comparisons
#                 DISPLAY "Input string: ", word
#                 DISPLAY "# of substrings: ", LENGTH(result)
#                 DISPLAY "Listing of substrings: ", result
#                 DISPLAY "# of comparisons: ", comparisons
#             CASE 3:
#                 DISPLAY "Exiting Program..."
#                 EXIT LOOP
#             DEFAULT:
#                 DISPLAY "Invalid input, try again."
#         ENDSWITCH
#     ENDLOOP
# ENDPROCEDURE
# FUNCTION SubStringalgorithm(word: STRING) RETURNS (ARRAY OF STRING, INTEGER)
#     DECLARE i, j AS INTEGER
#     DECLARE result AS ARRAY OF STRING ← []
#     DECLARE comparisons AS INTEGER ← 0
#     FOR i FROM 0 TO LENGTH(word) - 1 DO
#         comparisons ← comparisons + 1
#         IF UPPERCASE(word[i]) = "A" THEN
#             FOR j FROM i + 1 TO LENGTH(word) - 1 DO
#                 comparisons ← comparisons + 1
#                 IF UPPERCASE(word[j]) = "B" THEN
#                     APPEND SUBSTRING(word, i, j) TO result
#                 ENDIF
#             ENDFOR
#         ENDIF
#     ENDFOR
#     RETURN result, comparisons
# ENDFUNCTION

def main():
    word=""
    
    while True:
        print("""-----------------MAIN MENU-------------- 
1.  Read input string 
2.  Run algorithm and display outputs 
3.  Exit program 
        """)
         # error handling so it doesnt crash on invalid inputs like alphabets 
        try:
            option=int(input("Enter your option: "))
        except ValueError:
            print("\nInvalid Input! Please enter a number.....")
            continue
        match option:
            case 1:
                word=(input("Input String: "))
            case 2:
                result,comparisons=SubStringalgorithm(word)
                print(f"""\nInput string:  {word}
# of substrings:  {len(result)}
Listing of substrings:  {result}
# of comparisons:  {comparisons}\n""")

            case 3:
                print("\nExiting Program....")
                break
            case _:
                 # if input is invalid we return an error message which only affects numbers exceeding 3 or below 1
                print("\ninvalid input try again....") 
           
def SubStringalgorithm(word):
    i=0
    result=[]
    comparisons=0
    for i in range(len(word)):
        comparisons+=1
        if word[i].upper()=="A":  
            for j in range(i+1,len(word)):
                comparisons+=1
                if word[j].upper()=="B":
                    result.append(word[i:j+1])
    return result, comparisons

if __name__ =="__main__":
    main()

