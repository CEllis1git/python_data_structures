"""
Function to print the first and last days of the week and to verify that Wednesday is in the tuple.
"""

days = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")

def print_and_check(days):

    print("First day is " + days[0] + " and last day is " + days[6])
    if "Wednesday" in days:
        print("Wednesday is in the list")
    else:
        print("Wednesday is not in the list")

print_and_check(days)


