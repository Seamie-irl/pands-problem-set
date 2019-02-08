#Write a program that outputs whether or not today is a day that begins with the letter T.

import datetime
import calendar
#today=datetime.datetime.now()
todayName=calendar.day_name[datetime.datetime.today().weekday()]
bLetterFound=False
for letter in todayName.lower():
    if letter=="t":
        bLetterFound=True
if bLetterFound:
    print("Yes, ", todayName, " has a 'T' in it!")
else:
    print("There's no T in today because it's ",todayName)