"""
Write a one-liner to count the number of lower-case t characters in each of the
following strings:

statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."
"""

statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."
statements = [statement1, statement2]

for statement in statements:
    print(statement.count('t'))

# ==========
# LS Solution
# ==========

statement1.count('t')
statement2.count('t')

