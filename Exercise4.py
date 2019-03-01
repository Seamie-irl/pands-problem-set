 # 13th February 2019
 # Don't know why this one interests me.
 # I think it's because of the convoluted nature

 # Ask the user for a positive integer
 # If the number is even - divide by two
 #               if odd - multiply by 3 then add 1
 # The program ends when the result is 1

 # I'm going to copy some code from previous exercises
sResponse = input("Please enter a positive integer")
 #test that it's a positive integer
if sResponse.isdigit():
    # OK, at least it's a number but is it positive?
    lResponse=float(sResponse) #used float in case the number isn't an integer
    if lResponse>0: # Right, well, it's a positive number but is it an integer
        if lResponse==float(int(lResponse)): #bingo, we have a positivie integer
            lResult=lResponse # introduce the pointer for the Result
            while lResult!=1: # used <> initially. Then remembered Ian using !=
                if lResult%2==0:
                    print(lResult," was even, leading to: ")
                    lResult=lResult/2
                    print(lResult)
                else:
                    print(lResult, " was odd, leading to: ")
                    lResult=(lResult*3)+1
                    print(lResult)

# The output of this is cool
# It forms a rising wave pattern until it hits a value where all the divisors
# and child-divisors are divisible by 2 wherein it sinks to 2/2 = 1 and the program ends