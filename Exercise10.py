import matplotlib.pyplot as plt

a=[]
b=[]
c=[]
d=[]

for x in range(-0,4,1):
    y1=x
    y2=x**2
    y3=2**x
    a.append(x)
    b.append(y1)
    c.append(y2)
    d.append(y3)

fig= plt.figure()
axes=fig.add_subplot(111)
axes.plot(a,b)
plt.show()