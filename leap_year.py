 #Enter a month (as a number between 1 and 12). 
 #Print the number of days in that month. Assume a non-leap year.
 # Check if a year is a leap year or not. Enter a month (as a number between 1 and 12). 
 # print the number of days in that month. Assume a non-leap year.
 # Check if a year is a leap year or not.

month:int=int(input("Enter your input"))
def days_in_month():
    if month == 1:
        print("January(31 days)")
    elif month == 2:
        print("Febuary(28 days)")
    elif month == 3:
        print("March(31 days)")
    elif month == 4:
        print("april(30 days)")
    elif month == 5:
        print("May(31 days)")
    elif month == 6:
        print("june(30 days)")
    elif month == 7:
        print("July(31 days)")
    elif month == 8:
        print("August(31 days)")
    elif month == 9:
        print("September(30 days)")
    elif month == 10:
        print("October(31 days)")
    elif month == 11:
        print("November(30 days)")
    elif month == 12:
        print("December(31 days)")
    else:
        print("This year year is a leap or not")