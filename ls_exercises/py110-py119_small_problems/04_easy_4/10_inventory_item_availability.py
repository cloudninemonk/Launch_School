'''
Building on the previous exercise, write a function that returns True or False based on whether or not an inventory item (an ID number) is available. As before, the function takes two arguments: an item ID and a list of transactions. The function should return True only if the sum of the quantity values of the item's transactions is greater than zero. Notice that there is a movement property in each transaction object. A movement value of 'out' will decrease the item's quantity.

You may (and should) use the transactions_for function from the previous exercise.

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True
'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
-

Output:
-

Rules (Explicit):
-

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
Example 1:
- Input:
- Output:

Example 2:
- Input:
- Output:

Edge Cases:
-

D: Data Structures
-------------------------
-

Notes
-------------------------
-

A: Algorithm (Step-by-step)
-------------------------
1.
2.
3.

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def transactions_for(item_id, transactions):
    return [transaction for transaction in transactions if transaction["id"] == item_id]

def is_item_available(item_id, transactions):
    quantities = sum([t['quantity'] if t['movement'] == 'in' else -t['quantity'] for t in transactions_for(item_id, transactions)])
    return quantities > 0

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True

def transactions_for(item_id, transactions): return [t for t in transactions if t["id"] == item_id]

def is_item_available(item_id, transactions):
    total = sum(transaction["quantity"] if transaction["movement"] == "in" else -transaction["quantity"] for transaction in transactions_for(item_id, transactions))
    return total > 0

# ==========
# LS Solution
# ==========

def transactions_for(item_id, transactions):
    return [transaction for transaction in transactions if transaction["id"] == item_id]

def is_item_available(item, transactions):
    relevant_transactions = transactions_for(item, transactions)
    quantity = 0

    for transaction in relevant_transactions:
        if transaction["movement"] == 'in':
            quantity += transaction["quantity"]
        else:
            quantity -= transaction["quantity"]

    return quantity > 0