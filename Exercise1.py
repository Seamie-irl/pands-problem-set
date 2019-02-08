# started 31/01/19
bValid = False
sResponse=""
while not bValid:
    sResponse=input("Please enter a positive integer")
    if sResponse.isdigit():
        iResponse=int(sResponse)
        #print(iResponse)
        if iResponse > 0:
            bValid=True
            print(bValid) 
    else:
        print(sResponse, " is not a positive integer, try again")   

print("You entered",iResponse)
iResult=0
for i in range(iResponse+1):
    iResult = iResult + i
    #print(i,"  ", iResult)

print("The sum of all numbers between 1 and ",sResponse," is ", iResult)
