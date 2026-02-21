# Name: Omodemi Olaoluwa Adedamola
# Class: CS 4306/03
# Term: Spring 2026
# Instructor: Dr. Abdur Rahman
# Assignment: 2
# IDE Name: Visual Studio Code

# Algorithm Design Block
# Algorithm Title: Partitions

# Logical Steps:
# Main()
# 1. Initialize variables:
#        size ← 0
#        numbers ← empty list
# 2. LOOP infinitely:
#        Display Main Menu:
#            1. Read set size
#            2. Read set elements
#            3. Run algorithm and display outputs
#            4. Exit program
#        Read user option with input validation:
#            If input is not a number, display error and CONTINUE loop
#        SWITCH (option):
#            CASE 1:
#                Prompt user for set size
#                size ← user input
#                numbers ← list of zeros with length size
#            CASE 2:
#                FOR i from 0 to size-1:
#                    Prompt user for integer
#                    numbers[i] ← input value
#            CASE 3:
#                Call Partitionalgorithm(numbers) → results
#                Display:
#                    - Set size
#                    - Integer values
#                    - Disjoint subsets with same sum
#            CASE 4:
#                Print "Exiting Program"
#                BREAK loop
#            DEFAULT:
#                Print "Invalid input, try again"
# END LOOP
#  Partitionalgorithm(digits)
# INPUT: digits → list of integers
# OUTPUT: result → two disjoint subsets with equal sum or message
# 1. Sort digits using quicksort:
#        digits ← quicksort(digits)
# 2. Calculate total_sum ← sum of digits
# 3. Initialize result ← [[], []]
# 4. IF total_sum is odd:
#        RETURN "No disjoint subsets with same sum"
# 5. target ← total_sum / 2
# 6. FOR i from 0 to length of digits - 1:
#        subset_sum ← digits[i]
#        FOR j from i+1 to length of digits - 1:
#            subset_sum ← subset_sum + digits[j]
#            IF subset_sum == target:
#                result[0] ← digits[i..j]
#                result[1] ← digits[0..i-1] + digits[j+1..end]
#                RETURN result
#            ELSE IF subset_sum > target:
#                BREAK inner loop
# 7. RETURN result
# quicksort(arr)
# INPUT: arr → list of integers
# OUTPUT: sorted array
# 1. IF length(arr) ≤ 1:
#        RETURN arr
# 2. pivot ← middle element of arr
# 3. left ← elements in arr < pivot
# 4. middle ← elements in arr == pivot
# 5. right ← elements in arr > pivot
# 6. RETURN quicksort(left) + middle + quicksort(right)

# Pseudocode Syntax
# MainProgram
#     DECLARE size AS INTEGER ← 0
#     DECLARE numbers AS ARRAY OF INTEGER ← []
#     LOOP FOREVER
#         DISPLAY "----------------- MAIN MENU --------------"
#         DISPLAY "1. Read set size (number of integers)"
#         DISPLAY "2. Read set elements (integer values)"
#         DISPLAY "3. Run algorithm and display outputs"
#         DISPLAY "4. Exit program"
#         INPUT option
#         IF option IS NOT INTEGER THEN
#             DISPLAY "Invalid Input! Please enter a number."
#             CONTINUE LOOP
#         ENDIF
#         SWITCH option
#             CASE 1:
#                 INPUT size
#                 numbers ← ARRAY OF INTEGER WITH LENGTH size
#             CASE 2:
#                 FOR i FROM 0 TO size - 1 DO
#                     INPUT numbers[i]
#                 ENDFOR
#             CASE 3:
#                 results ← Partitionalgorithm(numbers)
#                 DISPLAY "Set size: ", LENGTH(numbers)
#                 DISPLAY "Integer values: ", numbers
#                 DISPLAY "Disjoint subsets with same sum: ", results
#             CASE 4:
#                 DISPLAY "Exiting Program..."
#                 EXIT LOOP
#             DEFAULT:
#                 DISPLAY "Invalid input, try again."
#         ENDSWITCH
#     ENDLOOP
# ENDPROCEDURE
# FUNCTION Partitionalgorithm(digits: ARRAY OF INTEGER) RETURNS ARRAY OF ARRAY OF INTEGER OR STRING
#     digits ← Quicksort(digits)
#     total_sum ← SUM OF digits
#     DECLARE result AS ARRAY[2] OF ARRAY OF INTEGER ← [[], []]
#     IF total_sum MOD 2 ≠ 0 THEN
#         RETURN "No disjoint subsets with same sum of elements"
#     ENDIF
#     target ← total_sum / 2
#     FOR i FROM 0 TO LENGTH(digits) - 1 DO
#         subset_sum ← digits[i]
#         FOR j FROM i + 1 TO LENGTH(digits) - 1 DO
#             subset_sum ← subset_sum + digits[j]
#             IF subset_sum = target THEN
#                 result[0] ← SUBARRAY(digits, i, j)
#                 result[1] ← CONCAT(SUBARRAY(digits, 0, i - 1), SUBARRAY(digits, j + 1, LENGTH(digits) - 1))
#                 RETURN result
#             ELSE IF subset_sum > target THEN
#                 BREAK INNER LOOP
#             ENDIF
#         ENDFOR
#     ENDFOR
#     RETURN result
# ENDFUNCTION
# FUNCTION Quicksort(arr: ARRAY OF INTEGER) RETURNS ARRAY OF INTEGER
#     IF LENGTH(arr) ≤ 1 THEN
#         RETURN arr
#     ENDIF
#     pivot ← arr[LENGTH(arr) / 2]
#     left ← [x IN arr WHERE x < pivot]
#     middle ← [x IN arr WHERE x = pivot]
#     right ← [x IN arr WHERE x > pivot]
#     RETURN CONCAT(Quicksort(left), middle, Quicksort(right))
# ENDFUNCTION

def main():
    size=0
    numbers=[]
    while True:
        print("""\n -----------------MAIN MENU-------------- 
1.  Read set size (number of integers) 
2.  Read set elements (integer values) 
3.  Run algorithm and display outputs 
4.  Exit program""")
         # error handling so it doesnt crash on invalid inputs like alphabets 
        try:
            option=int(input("Enter your option: "))
        except ValueError:
            print("\nInvalid Input! Please enter a number.....")
            continue
        match option:
            case 1:
                size=int(input("\nSet Size:   "))
                numbers=[0]*size
            case 2:
                for i in range(0,size):
                    num=int(input("\nEnter an integer:    "))
                    numbers[i]=num
            case 3:
                results=[[],[]]
                results=Partitionalgorithm(numbers)
                print(f"""\nSet size:     {len(numbers)}  integers 
Integer values:  {numbers}
Disjoint subsets with same sum: {results}\n""")
            case 4:
                print("\nExiting Program....")
                break
            case _:
                 # if input is invalid we return an error message which only affects numbers exceeding 3 or below 1
                print("\ninvalid input try again....") 
def Partitionalgorithm(digits):
    digits=quicksort(digits)
    sum=0
    subset_sum=0
    result=[[],[]]
    for i in range(0, len(digits)):
        sum+=digits[i]
    if sum % 2==0:
       average=sum//2
       for i in range(0,len(digits)):
           subset_sum=digits[i]
           for j in range(i+1,len(digits)):
               
               subset_sum+=digits[j]
               if subset_sum==average:
                   result[0]=digits[i:j+1]
                   result[1]=digits[:i]+digits[j+1:]
               elif subset_sum>average:
                   break                        
    else:
        return("No disjoint subsets with the same sum of their elements found")
    return result
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
if __name__ =="__main__":
    main()
