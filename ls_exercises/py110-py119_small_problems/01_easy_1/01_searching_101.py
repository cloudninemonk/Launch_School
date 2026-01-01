'''
Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.

Example 1:

Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.

Example 2:

Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.

=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- string

Output:
- string

Rules (Explicit):
-

Rules (Implicit/Inferred):
- Numbers to be integers.

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
Example 1:
- Input:
25
15
20
17
23

- Output:
17 is in 25,15,20,17,23.

Example 2:
- Input:
25
15
20
17
23
18

- Output:
18 isn't in 25,15,20,17,23.

Edge Cases:
-

D: Data Structures
-------------------------
- list/tuple to contain the numbers entered
-

Notes
-------------------------
- loops (for), range

A: Algorithm (Step-by-step)
-------------------------
1. Ask user to enter a number and append it to a list, my_numbers.
2. Repeat step 1 four times so that the user has entered five numbers that are appended to first_five_numbers.
3. Ask user to enter a sixth number and assign it to a variable, sixth_number.
4. Check if the sixth_number is in the my_numbers.
5. If the sixth_number is in the my_numbers, output it is in the my_numbers, else output it is not in the my_numbers.

C: Code With Intent
-------------------------
'''
# ==========
# My Solution
# ==========

my_numbers = []
for _ in range(6):
    my_numbers.append(input("Enter a number: "))
sixth_number = my_numbers.pop()
if sixth_number in my_numbers:
    print(f'{sixth_number} is in {','.join(my_numbers)}')
else:
    print(f'{sixth_number} is not in {','.join(my_numbers)}')

# ==========
# LS Solution
# ==========

numbers = []

numbers.append(input("Enter the 1st number: "))
numbers.append(input("Enter the 2nd number: "))
numbers.append(input("Enter the 3rd number: "))
numbers.append(input("Enter the 4th number: "))
numbers.append(input("Enter the 5th number: "))
last_number = input("Enter the last number: ")

numbers_list = ','.join(numbers)

if last_number in numbers:
    print(f"{last_number} is in {numbers_list}.")
else:
    print(f"{last_number} isn't in {numbers_list}.")



