# Write a program that reads in a text file and outputs every second line. The program
# should take the filename from an argument on the command line.

#sFilename=input("Please enter the filename including the filetype extension (e.g. '.txt')")
# This was my original method for inputting a file given my misunderstanding of 'argument' :-)

#oFile = open(sFilename.strip(),"r") # removes any spaces before or after the user text entered

import sys 

# https://www.w3schools.com/python/python_file_open.asp use to help with File IO

if len (sys.argv)==2: #checks that an argument was passed at runtime
    # from here set a flag and raise. Read a line and print it if the flag is raised
    # otherwise move to the next line
    # when a line is printed, lower the flag
    bPrint = True
    iLine =0 # bucket for line numbers
    sFilename=sys.argv[1]
    try: # wrap the code in an error-trapping routine
        oFile=open(sFilename,"r")  # open the file to read
        for oLine in oFile: # loop through each oLine in oFile
            iLine+=1 # increment the line number
            if not oLine in ['\n','\r\n']: # found this in https://stackoverflow.com/questions/7896495/python-how-to-check-if-a-line-is-an-empty-line
                # there's text in this line
                if bPrint: # print this line
                    print(f'Line number: {iLine}') # prints the line number
                    print(oLine) # then the line
                    bPrint=False # then lowers the flag for the next line
                else: #skip this line
                    print(f'Line number: {iLine} [skipped]') # but print that it was skipped
                    bPrint=True # raises the flag for the next line

            else: # there's no text in this line. It's just CrLf. Annotate it but treat it the same
                # reset the flag
                sResponse=''
                if bPrint: # this line would have printed but is skipped as it's empty
                    print(f'          <Empty Line {iLine} not printed>')
                    bPrint=False # lowers the flag for the next line
                else: # this line would not have printed but in any case deal with the flag
                    print(f'          <Empty Line {iLine} would have been skipped>')
                    bPrint=True
    except FileNotFoundError: # found this by creating the error :-)
        print("I'm afraid the filename you gave me doesn't exist")
else:
    print('You must provide a filename')
