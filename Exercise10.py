import matplotlib.pyplot as plt

# I struggled with this one as it uses MatPlotLib
# I could get it to graph one line by myself but
# didn't know how to get it to plot multiple lines
# on the one graph.
#
# I had toyed with the idea of an input from the user
# based on chosing a-c for one of three graphs and
# using the result to display the single-line graph
# relevant to the selection
# 
# Reading http://cs231n.github.io/python-numpy-tutorial/#numpy
# helped solve this.

a=[] # this will be the array of x-values
b=[] # this will be the array of y=x values
c=[] # this will be the array of y=x(Squared) values
d=[] # this will be the array of y=2 to the power of x values

for x in range(0,4,1): #loop x from 0 to 4 incl
    y=x #sets y
    ySq=x**2 #sets y=x squared
    y2x=2**x #sets y=twice x
    a.append(x) # passes x to the array by appending
    b.append(y) # passes y to the array by appending
    c.append(ySq) # passes ySq to the array by appending
    d.append(y2x) # passes y2x to the array by appending

# note: anything to the power of zero is 1 so the y2x line
#       starts at 1

plt.plot(a,b) # plot the array of x against the array of y
plt.plot(a,c) # plot the array of x against the array of ySq
plt.plot(a,d) # plot the array of x against the array of y2x
plt.xlabel('Value of x')
plt.ylabel('Value of y')
plt.title('Exercise 10')
plt.legend(['y=x','y=x Squared','y=2x'])
plt.show()