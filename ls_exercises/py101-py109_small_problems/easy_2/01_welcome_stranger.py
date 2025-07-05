"""
Create a function that takes 2 arguments, a list and a dictionary. The list will
contain 2 or more elements that, when joined with spaces, will produce a person's
name. The dictionary will contain two keys, "title" and "occupation", and the
appropriate values. Your function should return a greeting that uses the person's
full name, and mentions the person's title.

Example:
    greeting = greetings(
        ["John", "Q", "Doe"],
        {"title": "Master", "occupation": "Plumber"},
    )
    print(greeting)
    # Hello, John Q Doe! Nice to have a Master Plumber around.
"""

def greetings(full_name, full_occupation):
    """Return a greeting with the person's name and occupation."""
    name = ' '.join(full_name)
    occupation = ' '.join(full_occupation.values())
    return f"Hello, {name}! Nice to have a {occupation} around."

# This is an alternative method to the function
# def greetings(full_name, full_occupation):
#     """Return a greeting with the person's name and occupation."""
#     name = ' '.join(full_name)
#     role_title = full_occupation['title']
#     role_name = full_occupation['occupation']
#     return f"Hello, {name}! Nice to have a {role_title} {role_name} around."

def main():
    first_name = input("What is your first name? ")
    middle_initial = input("What is your middle initial? ")
    surname = input("What is your surname? ")
    title = input("What is your title? ")
    occupation = input("What is your occupation: ")

    full_name = [first_name, middle_initial, surname]
    full_occupation = {"title": title, "occupation": occupation}

    greeting = greetings(full_name, full_occupation)
    print(greeting)

    # greeting = greetings(
    #     ["John", "Q", "Doe"],
    #     {"title": "Master", "occupation": "Plumber"},
    # )
    # print(greeting)

main()
