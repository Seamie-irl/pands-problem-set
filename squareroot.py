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
sResponse=input("Please enter a decimal number: ")
bDecimal=False
while not bDecimal:
    if sResponse.isdigit: # it's a number!
        lResponse=float(sResponse)
        if lResponse!=int(lResponse): # it's a decimal
            # raise the flag
            bDecimal=True
            print("The approximate Square Root of " + sResponse + "= " + str(m.sqrt(lResponse)))
        else:
            print("Sorry, you didn't enter a decimal number")

    