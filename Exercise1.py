# started 31/01/19
# Question 1:
# Write a program that asks the user to input any positive integer
# and outputs the sum of all numbers between 1 and that number

# logical process:
# Take input -- check as positive integer (retry if not) -- iterate through
# numbers and sum

# no external references were used in writing this program
# however, considerable trial and error regarding syntax was used

# raise a flag which signifies that the input is a positive integer
bValid = False
# set a string variable as empty (as opposed to NULL)
sResponse=""
# loop using the earlier flag and keep doing until flag is raised
while not bValid:
    # request input from user
    sResponse=input("Please enter a positive integer")
    # proceed if it's a number, exit if not
    if sResponse.isdigit():
        # copy conversion of string to integer variable
        iResponse=int(sResponse)
        #print(iResponse) <- this was used as part of the testing
        # proceed if the number is positive, exit if not
        if iResponse > 0:
            # raise the flag
            bValid=True
            #print(bValid)  <- this was used as part of the testing
    else:
        # response back to user if conditions not met 
        print(sResponse, " is not a positive integer, try again")   
# down side of this loop is that there's no escape. You either enter a 
# positive integer or stay forever in the loop

# feedback to user
print("You entered",iResponse)
# set integer as zero (not NULL)
iResult=0
# loop from  1 to number and sum
for i in range(iResponse+1):
    iResult = iResult + i
    #print(i,"  ", iResult) <- this was used as part of the testing

# finally output the result
print("The sum of all numbers between 1 and ",sResponse," is ", iResult)
