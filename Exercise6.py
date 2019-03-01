# Seamus Leonard G00376550 24/02/2019 Programming & Scripting Problem Set
# Q6

# Write a program that takes a user input string and outputs every second word
# one solution would be to step through each character, noting the space characters
# as markers for words and then just print out the words from there
# However, a search of the Internet showed up https://stackoverflow.com/a/6181784
# so I'm going to see if I can implement this.
import re
sResponse = input("Please enter a sentence:")
wList=re.sub("[^\w]", " ",  sResponse).split()
x=1
for sWord in wList:
    if x==1 :
        print(sWord)
        x=0
    else:
        x=x+1