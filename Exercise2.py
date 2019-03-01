# Q2. Write a program that outputs whether or not today is a day that begins with the letter T.

# referenced https://stackoverflow.com/a/36341648 for the Weekday Name
# and
# https://stackoverflow.com/a/9847269 for the day-of-week


# bolt on both the DateTime and Calendar modules
import datetime
import calendar
#today=datetime.datetime.now() <- used for testing

# create string variable and then get the day of the week, convert it to the day name and put in variable
todayName=calendar.day_name[datetime.datetime.today().weekday()]
# raise a flag for denoting when the day has a 'T' in it
bLetterFound=False
# get the lowercase letters sequentially in the todayName variable as [T]hursday<>[t]hursday
# cycle through the the letters in turn. I didn't put an escape as 9 iterations is the max (Wednesday)
for letter in todayName.lower():
    if letter=="t":
        # 'T' found so raise the flag
        bLetterFound=True

# give user feedback
if bLetterFound:
    print("Yes, ", todayName, " has a 'T' in it!")
else:
    print("There's no T in today because it's ",todayName)