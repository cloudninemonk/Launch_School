"""
Build a program that displays when the user will retire and how many years she has to work till retirement.

What is your age? 30
At what age would you like to retire? 70

It's 2024. You will retire in 2064.
You have only 40 years of work to go!
"""
# ==========
# My Solution
# ==========
from datetime import date

current_year = date.today().year
current_age = int(input("What is your age? "))
retirement_age = int(input("At what age would you like to retire? "))
remaining_years = retirement_age - current_age
retirement_year = current_year + remaining_years

current_year = date.today().year

print(f"It's {current_year}. You will retire in {retirement_year}.\n"
      f"You have only {remaining_years} years of work to go.")

# ==========
# LS Solution
# ==========
from datetime import datetime

current_age = int(input('What is your current age? '))
retirement_age = int(input('At what age would you like to retire? '))

current_year = datetime.now().year
years_to_go = retirement_age - current_age
retirement_year = current_year + years_to_go

print(f"It's {current_year}. You will retire in {retirement_year}.")
print(f"You have only {years_to_go} years of work to go!")

# Discussion

# In this solution, we use datetime.now from the datetime module to get the
# current date. This returns a datetime object. The datetime object has a year
# attribute that provides the current year. From there, we can determine the
# retirement year based on the two inputs and the current year.