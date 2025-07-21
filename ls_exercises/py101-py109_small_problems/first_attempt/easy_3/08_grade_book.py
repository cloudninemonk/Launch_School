"""
Write a function that determines the mean (average) of the three scores passed
to it, and returns the letter associated with that grade.

Numerical score letter grade list:
90 <= score <= 100: 'A'
80 <= score < 90: 'B'
70 <= score < 80: 'C'
60 <= score < 70: 'D'
0 <= score < 60: 'F'

Tested values are all between 0 and 100. There is no need to check for negative
values or values greater than 100.

Examples:
print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
"""

def get_grade(score1, score2, score3):
    avg_grade = (score1 + score2 + score3) / 3
    if 90 <= avg_grade <= 100:
        return 'A'
    if 80 <= avg_grade < 90:
        return 'B'
    if 70 <= avg_grade < 80:
        return 'C'
    if 60 <= avg_grade < 70:
        return 'D'
    return 'A'

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True