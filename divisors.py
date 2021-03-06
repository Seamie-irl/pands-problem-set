# Write a program which prints out all the number between 1,000 and 10,000 which are divisible
# by 6 but not by 12
# The key here is MOD which gives the remainder of all division calculations
# If it's zero then the numerator is divisible by the demominator
# It only matters about 6 being the divisor and then whether 12 divides in this case
# So, start at 1,000 and move sequentially.

# looking at the results from the first run, each successive print
# is 12 units apart. Therefore, it would speed up the process
# if we just jumped 12 at each successful print

for i in range(1000,10000):
    if i%6 == 0: #couldn't figure out why this line was showing up as an error. ==!!! Not used to double equals!
        # now test for 12
        if i%12 > 0: # the same number is not divisible by 12
            print (i, "is divisible by 6 but not by 12")
            # from the results of the first run
            # now just jump 12
            i += 12 # this short-hand exists in VB and I tested it in python and it works!! :-)
print("Finished! The above list is complete") # informs the user the program has finished