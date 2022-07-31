""""
Title of Program                            : “Looking for Fermat’s Last Theorem Near Misses”
Name of file that holds program             : Source_Code.py
External files necessary to run program     : N/A
External files program creates              : Output.json (This file contains complete output of the Source Code)
Names of programmers working on the program : Sandeep Perikala & Rashmitha Dayathri
Course number & Section Number              : Sections SU22-CPSC-60500-001 & 002
Finised program date and submitted date     : 31 July 2022
Program Explanation                         : When the program starts, it asks for 'n' and 'k' value form user. It then 
                                              calculate and return the combinations of x, y and z values who has low 
                                              relative near misses and the actual miss value.
Resources used to complete the Program      : N/A
"""


# Libraries importing that are used in this program
import math
import json
import time

# If the user enter wrong value for 'n' then this while loop will run. And if user enters correct value for 'n'. Then this loop will break.
while True:
    # Taking input from user for 'n'
    n = int(input("Please enter value for 'n'. It should be greater than 2 and less than 12: "))
    if n > 2 and n < 12:
        print()
        break
    else:
        print()
        print("Please enter value for 'n' greater than 2 and less than 12")
        print()

# If user enters wrong value for 'k' then this while loop will run. And if user enters correct value for 'k',
# Then this loop will break.
while True:
    size = int(input("Please enter value for 'k'. It should be greater than or equal to 10: "))
    if size >= 10:
        print()
        break
    else:
        print()
        print("Please enter value for 'k' greater than or equal to 10")
        print()

# This dictionary will store the information of x,y and z values. It will also store value of actual miss and relative miss.
Miss_Info = {
        'x': 0,
        'y': 0,
        'z': 0,
        'n': 0,
        'Actual Miss' : 0,
        'Relative Miss': 0
    }

# For keeping the record of low relative miss. Every time We find low relative miss I am storing that miss because 
# next time I will find that x,y and z combination that have low relative miss from previous.
Min_Relative_Miss = 1

# This dictionary will be used to store and update data in json file that created when program stops.
Output = {}

# This variable is used as key of above Output named dictionary. 
counter = 1

# These two for loops will be used to check evry combunation of given range for x and y.
for a in range(1, size+1):
    for b in range(a,  size+1):

# Calculating Xn + Yn 
        XnplusYn = math.pow(a, n) + math.pow(b, n)
# Calculating value for z.
        Z = int(math.pow(XnplusYn, 1 / n))
# Calculating (xn + yn) - zn
        Miss_zToxy = XnplusYn - math.pow(Z, n)
# Calculating (z+1)n - (xn + yn)
        Miss_zOneToxy = math.pow(Z+1, n) - XnplusYn

# Checking either (xn + yn) - zn is smaller or (z+1)n - (xn + yn) is smaller
        if Miss_zToxy < Miss_zOneToxy:
            relative = Miss_zToxy / XnplusYn
            Flag = 0
            actualMiss = Miss_zToxy
        else:
            relative = Miss_zOneToxy / XnplusYn
            Flag = 1
            actualMiss = Miss_zOneToxy

# Checking smallest relative miss.
        if relative < Min_Relative_Miss:
            if Flag == 0:
                print("(Xn + Yn) is more closer to (Z)n")
            else:
                print("(Xn + Yn) is more closer to (Z+1)n")

            c = int(math.floor(Z))
# Storing results to Miss_Info dictionary.
            Miss_Info = {
                'x': a,
                'y': b,
                'z': c,
                'n': n,
                'Actual Miss': actualMiss,
                'Relative Miss': relative
            }
# Updating Min_Relative_Miss by current relative miss
            Min_Relative_Miss = relative

# Printing results     
            print("Nearest solution for the bases between " + str(0) + " and " +
            str(size) + " and the exponent " + str(n) + " => " +
            str(Miss_Info))
            print()

# Storing results for Json file.
            Output[counter] = str(Miss_Info)

            counter += 1
        
# Making Json file.
with open('Output.json', 'w') as f:
    json.dump(Output, f)
time.sleep(60)