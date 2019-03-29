 # 13th February 2019
 # Don't know why this one interests me.
 # I think it's because of the convoluted nature

 # Ask the user for a positive integer
 # If the number is even - divide by two
 #               if odd - multiply by 3 then add 1
 # The program ends when the result is 1

 # I'm going to copy some code from previous exercises

import tkinter as tk
from tkinter import messagebox as tkMB
import matplotlib.pyplot as plt # borrowing code from Exercise10

 # the above two imports are for the user decision at the end
 # - this creates a message box

a=[]
b=[]
# create the arrays for the number outputs 
# a will just be a sequential index
# b will be the sequential result in the calculation

x=0 #set the index
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
                    a.append(x)
                    b.append(lResult)
                    x+=1 # move the index up one
                else:
                    print(lResult, " was odd, leading to: ")
                    lResult=(lResult*3)+1
                    print(lResult)
                    a.append(x)
                    b.append(lResult)

# The output of this is cool
# It forms a rising wave pattern until it hits a value where all the divisors
# and child-divisors are divisible by 2 wherein it sinks to 2/2 = 1 and the program ends
# However, I wanted to see it plotted so I added a decision tree for a graph
# with the assistance of code from https://stackoverflow.com/q/11244753/8040537
# and https://stackoverflow.com/a/19074477/8040537 and 
# https://www.python-course.eu/tkinter_dialogs.php
# for the messagebox import

print('Click on the question button at the top left of the screen')
top = tk.Tk()
def callback():
    if tkMB.askyesno('Graph','Would you like to see this plotted?'):
        plt.plot(a,b)
        plt.xlabel('Sequence')
        plt.ylabel('Result')
        plt.title('Exercise 4')
        plt.legend(['Collatz'])    
        plt.show()
    else:
        print('The End!')
        quit()
B=tk.Button(top,text='Click for question',command=callback)
B.pack()
tk.mainloop()
# not the neatest way of handling a messagebox. It's a two-step process causing
# the user to have to scan the screen for what to do next
print('The End!!')

