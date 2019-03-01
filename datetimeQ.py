# 1st March 2019
#Q8. Write a program that outputs today’s date and time in the format ”Monday, January
# 10th 2019 at 1:15pm”.

# logic: get the month and day names then just concatenate the whole lot

# referenced: 
# https://stackoverflow.com/a/20007730 for the Ordinal function **
# https://stackoverflow.com/a/13855243 
# and https://www.pythoncentral.io/how-to-display-the-date-and-time-using-python/ for the 12-hour time ***

# from previous exercises, bolt on DateTime and Calendar
import datetime as d
import calendar
import math
import time

rightNow=d.datetime.now() #get the timestamp
monthName=calendar.month_name[rightNow.month] # get the name for the current month
dayName=calendar.day_name[rightNow.day] # get the name of today
sTime=time.strftime("%I:%M %p") # ***       get the time in the 12hr clock
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4]) # **
# the above line is taken from the aforementioned reference

# now put it all together and print
sResult=dayName + ", " + monthName + " " + ordinal(13) +" " + str(rightNow.year) + " at " + sTime
print(sResult)

# note: it would be possible to put most of the calculations / conversions into the print statement
#       but it would be difficult to read