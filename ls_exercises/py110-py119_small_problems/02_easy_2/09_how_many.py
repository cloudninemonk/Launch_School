'''
Write a function that counts the number of occurrences of each element in a given list. Once counted, print each element alongside the number of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# your output sequence may appear in a different sequence
car => 4
truck => 3
SUV => 1
motorcycle => 2
'''

"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- list of values

Output:
- strings

Rules (Explicit):
- elements are case-sensitive

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# your output sequence may appear in a different sequence
car => 4
truck => 3
SUV => 1
motorcycle => 2

Edge Cases:
-

D: Data Structures
-------------------------
- set

Notes
-------------------------
- for loop

A: Algorithm (Step-by-step)
-------------------------
1. Pass the list to the function count_occurrences
2. Create a frozenset, vehicle_type, of the list vehicles
3. Iterate through vehicle_type and count number of occurrences of that vehicle type in vehicles
4. Output vehicle_type and the corresponding count

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========

def count_occurrences(vehicles):
    for vehicle in frozenset(vehicles):
        print(f'{vehicle} -> {vehicles.count(vehicle)}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# ==========
# LS Solution
# ==========

def print_occurrences(occurrences):
    for item, count in occurrences.items():
        print(f"{item} => {count}")

def count_occurrences(elements):
    occurrences = {}

    for item in elements:
        occurrences[item] = occurrences.get(item, 0) + 1

    print_occurrences(occurrences)