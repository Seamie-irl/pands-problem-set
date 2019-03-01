# Seamus Leonard G00376550 24/02/2019 Programming & Scripting Problem Set
# Q5
# Write a program that asks a user to input a positive integer 
# and tells the user whether or not the number is prime

# Solution:
# 1. A prime number is a number greater than one which is only divisible
#    by the number itself and 1. '7' would be an example of a prime number
# 2. Any number, other than 2 which is divisible by 2 (i.e. even number)
#    is not a prime number
# 3. the divisor max is a quarter of the number, thereafter the divisors invert
#    for example, the divisors for 12 are 1x12, 2x6, 3x4 .. thereafter it's just
#    an inversion of the ones already mentioned ... 4x3, 6x2, 12x1
#
# input a number, check it's a positive whole number.
# I'm going to copy some code from previous exercises

bLoop = True
while bLoop== True :
    sResponse = input("Please enter a positive integer")
    #test that it's a positive integer
    if sResponse.isdigit() :
        print ("It's a number")
        # OK, at least it's a number but is it positive?
        lResponse=float(sResponse)
        if lResponse>0 : # Right, well, it's a positive number but is it an integer
            print("It's positive")
            if lResponse==float(int(lResponse)) : #bingo, we have a positivie integer
                print ("It's an integer")
                #set the loop not to repeat
                bLoop=False
                iQtr = int(lResponse/4)
                bIsPrime = True #set a flag for the Prime number and raise it
                #if a divisor divides in evenly then the flag will get dropped
                bFinished=False
                x=1
                while not bFinished :
                    x=x+1
                    #print (str(lResponse % x))
                    if lResponse % x ==0 :
                        # not a prime number
                        bIsPrime=False
                        bFinished=True #no point dividing any further
                    else :
                        if x+1>iQtr :
                            bFinished=True
if bIsPrime :
    print (sResponse + " is a prime number")
else :
    print(sResponse + " is not a prime number")

