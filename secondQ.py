# text file from https://www.gutenberg.org/files/2701/2701-h/2701-h.htm#link2HCH0001
#
# Q9. Write a program that reads in a text file and outputs every second line. The program
#     should take the filename from an argument on the command line.

# logic:
# ** one of the problems with this is the definition of a 'line' **
# ** generally, this is denoted by CrLf but this can be far more **
# ** than one screen-line                                        **
#
# open file (in VB this can be a line feed, I'm hoping for the same in Python)
# print every second line by using a flag (raised = print, dropped = skip)

# found line feed: https://stackoverflow.com/a/3277516

#set flag
flag=1
with open("moby-dick.txt") as o:
    for lines in o:
        if len(lines)<3: # the line just has a CrLf
            #skip empty space
            1==1 # python doesn't seem to like clauses without funtionality
        else:
            if flag==1:
                print(lines)
                flag=0
            else:
                print("< Skipped >")
                flag=1