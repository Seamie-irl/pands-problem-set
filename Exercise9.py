# Write a program that reads in a text file and outputs every second line. The program
# should take the filename from an argument on the command line.

sFilename=input("Please enter the filename including the filetype extension (e.g. '.txt')")
#oFile = open(sFilename.strip(),"r") # removes any spaces before or after the user text entered
# from here set a flag and raise. Read a line and print it if the flag is raised
# otherwise move to the next line
# when a line is printed, lower the flag
# https://www.w3schools.com/python/python_file_open.asp use to help with File IO
bPrint = True
iLine =0 # bucket for line numbers
# remove extra 'spaces' at beginning and/or end of filename

oFile=open(sFilename.strip(),"r") # looked for this in the list. Same as Trim() in vb
try:
    for oLine in oFile:
        iLine+=1 # increment the line number
        if not oLine in ['\n','\r\n']:
            try:
                if bPrint:
                    print(f'Line number: {iLine}')
                    print(oLine)
                    bPrint=False # lowers the flag for the next line
                else:
                    print(f'Line number: {iLine} [skipped]')
                    bPrint=True # raises the flag for the next line
            except:
                oFile.close
        else: # reset the flag
            sResponse=''
            if bPrint:
                print(f'          <Empty Line {iLine} not printed>')
                bPrint=False # lowers the flag for the next line
            else:
                print(f'          <Empty Line {iLine} would have been skipped>')
                bPrint=True
except FileNotFoundError:
    print("I'm afraid the filename you gave me doesn't exist")