# 1st March 2019
#
# Q7. Write a program that takes a positive floating point number as input and outputs
# an approximation of its square root

# referenced work: https://stackoverflow.com/a/9595150
# before starting this coding, the above was my first thought
# i.e. half the power is the square root
# however, this can not be used for floats - would that it were that simple

# bolt on the Maths module
import math as m
# lNumber=float(input("Please enter a decimal number"))
# using the above creates an error if the user enters a non-number
bDecimal=False
while not bDecimal:
    sResponse=input("Please enter a decimal number: ")
    try:
        lResponse=float(sResponse)
        if lResponse!=int(lResponse): # it's a decimal
            # raise the flag
            bDecimal=True
            print("The calculated Square Root of " + sResponse + "= " + str(m.sqrt(lResponse)))

            # this next part is subsequent to the Newton Square Root tutorial
            # I'm picking a starting point as 1/10th of the number
            sp = lResponse/10
            while abs((sp**2)-lResponse)>0.001: # increased accuracy to 3 decimal places
                sp-=((sp**2)-lResponse)/(2*sp) # formual derived from https://tour.golang.org/flowcontrol/8
            print(f"...whereas the estimated Square Root of {lResponse} is {sp}")
        else:
            print("Sorry, you didn't enter a decimal number")
    except ValueError:
        print("Sorry, what you entered wasn't a number, least of all a decimal one!")
           