# 2. Weather Forecast

"""
Our predict_weather function should output a message indicating whether a sunny 
or cloudy day lies ahead. However, the output is the same every time the 
function is invoked. Why? Fix the code so that it behaves as expected.

import random

def predict_weather():
    sunshine = random.choice(['True', 'False'])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

"""

# My response:

"""
The function invokement has not been implemented outside of the function.
The function arguments are both strings. Considering non-empty strings 
are truthy, sunshine will always be True.
"""
import random

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()



