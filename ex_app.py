# Exercise App
import database
from datetime import date
from datetime import datetime

prompt = "Welcom to the exercise log.\n"
print(prompt)

# get user input for the date
# note to self: use CAST TO re-format dates in the realtional database
def today_date(date):
    date = input("Provide the date (e.g 01/25/2022) or hit \'enter\' for today's date: ")
    while date != 'exit'.lower():
        if date == 'exit'.lower():
            break
        elif date == "":
            tday = datetime.today()
            tday = tday.strftime('%m/%d/%Y')
            year = tday[6:10]
            month = tday[:2]
            return tday, int(year), int(month)
        elif len(date)==10 and '/' in date:
            tday = date
            year = tday[6:10]
            month = tday[:2]
            return tday, int(year), int(month)
        else:
            print("DATE FORMAT ERROR! Month and day must be two digits.")

        date = input("Provide the date (e.g 01/25/2022) or hit \'enter\' for today's date: ")

# function to  get user input for miles walked
def miles_walked():
    miles = input("Enter miles walked or hit 'exit': ")
    while miles != 'exit'.lower():
        if miles == 'exit'.lower():
            break
        elif miles.isdigit() and '.' not in miles:
            print(f'You walked {miles} miles.')
            return int(miles)
        elif miles.isdigit() and '.' in miles:
            print(f'You walked {miles} miles.')
            return int(miles)
        else:
            print("ERROR! Enter a digit.")

        miles = input("Enter miles walked or hit 'exit': ")

### START HERE NEXT ###
# test the user input
# call the functions
# append the output of the functions into a list
lst = []
for item in today_date(date):
    lst.append(item)
lst.append(miles_walked())
exercise_log = lst
database.add_one(exercise_log)
print(database.show_all())
