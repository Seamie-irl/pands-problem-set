# Seamus Leonard G00376550 24/02/2019 Programming & Scripting Problem Set
# Q6

# Write a program that takes a user input string and outputs every second word
# one solution would be to step through each character, noting the space characters
# as markers for words and then just print out the words from there
# However, a search of the Internet showed up https://stackoverflow.com/a/6181784
# so I'm going to see if I can implement this.

# logic - take a string input, parse it into words, feed back every second word

# bolt on the 'Regular Expressions' module
import re
# take the input from the user
sResponse = input("Please enter a sentence:")
# define a string variable (array) and fill it with the parsed words

# the .split() parses the words in the string

wList=re.sub("[^\w]", " ",  sResponse).split()
# python is reporting 'Anomalous backslash in string \w
# the only part of this I don't understand is the [^\w] bit
# The caret means 'match the start of the string' but we want to match wthin in the entire string
# The \ is an escape character or a switch. In this case I'm guessing it's a switch
# The best I can come up with is \w means word and therefore ^\w means beginning of each word
x=1 #use this as a flag to print. If it's 1 then print otherwise don't, causing a skip
for sWord in wList:
    if x==1 :
        print(sWord)
        x=0
    else:
        # move next
        x=x+1