
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
# Algorithm CountABSubstrings(S)
# Input: String S of length n
# Output: List of substrings that start with A and end with B,
#         and total number of comparisons
# result ← empty list
# comparisons ← 0
# n ← length(S)
# for i ← 0 to n − 1 do
#     comparisons ← comparisons + 1
#     if uppercase(S[i]) = 'A' then
#         for j ← i + 1 to n − 1 do
#             comparisons ← comparisons + 1
#             if uppercase(S[j]) = 'B' then
#                 append substring S[i..j] to result
# return result, comparisons


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

