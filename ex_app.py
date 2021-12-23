# Exercise App
import csv
import database
from datetime import date
from datetime import datetime

prompt = "Welcome to the exercise log.\n"
print(prompt)
selection = input("What would you like to do? 1=single entry, 2=multiple entires, \
3=csv file, or '4' to exit. ")
while True:
    if selection == '4':
        print('Goodbye')
        break
    elif selection == '3':
        print("placeholder for csv file")
        break


    ### START HERE NEXT ###
    # this section sucessfully takes the input...
    # however, it does not print the output when calling the functions
    # I think I need to change the indentation or...
    # remove / alter a break from one of the if statements
    elif selection == '2' or selection == '1':
        log_lst = []
        print("-----------test for selection 1 or 2 ------------------")
        while True:
            add_entry = input("Would you like to make an entry? (Y/N): ").upper()
            if add_entry == 'N':
                print("No further entries. Exiting the program...")
                print("---------break successful----------------")
                break

            elif add_entry == 'Y':
                print("---------------add_entry 'yes' test successful------------")

                # get user input for the date
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
                            dym = tday, int(year), int(month)
                            return dym
                        elif len(date)==10 and '/' in date:
                            tday = date
                            year = tday[6:10]
                            month = tday[:2]
                            dym = tday, int(year), int(month)
                            return dym
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

                # call the functions
                # append the output of the functions into a list
                lst = []
                for item in today_date(date):
                    lst.append(item)
                lst.append(miles_walked())
                print("------------ func call successful -----------------")
                log_lst.append(lst)
                print("-------------test list input -----------------------")
                print(log_lst)
                continue
        break

    # OUTER WHILE LOOP: exit if user does not select an entry 1-4
    else:
        print("Invalid entry. Exiting the program....")
        break
    # call the database.py functions to add records to the db
    # database.add_one(log_lst)
    database.add_many(log_lst)
    print(database.show_all())
