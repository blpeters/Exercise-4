"""
tempfunctions.py

A library of simple temperature conversion tools.

Created by: Brett Peters
Date Created: 8/18/2024

"""

def fahr_to_celsius(temp_fahrenheit):
    """Returns degree celsius based on single argument of degrees fahrenheit"""
    
    # Returns the converted temperature, in degrees celsius
    return (temp_fahrenheit - 32) * (5/9)

def temp_classifier(temp_celsius):
    """"Returns an integer describing the tempeature class of an argument given in degrees celsius"""

    # Provides an integer return value 0-3 for the function for 4 different possible temperature classes
    if temp_celsius < -2:
        return 0
    elif temp_celsius >= -2 and temp_celsius < 2:
        return 1
    elif temp_celsius >= 2 and temp_celsius < 15:
        return 2
    else:
        return 3