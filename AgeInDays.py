# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    diff_years = delta_years(year1, year2)

    days_into_year1 = days_past_january(day1, month1)
    days_into_year2 = days_past_january(day2, month2)
    total = diff_years - day1 + days_into_year2

    return total


def delta_years(year1, year2):
    counter = 0
    for year in range(year1,year2):
        days = is_leap_year(year)
        counter += days
    return counter

def is_leap_year(year):
    if year % 4 != 0:
        return 365
    elif year % 100 != 0:
        return 366
    elif year % 400 != 0:
        return 365
    else:
        return 366

def days_in_months(month):
    days_of_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_of_months[month]

def days_past_january(day, month):
    m = 0
    day_counter = 0
    while m < month:
        day_counter += days_in_months(m)
        m += 1
    return (day_counter + day)

#print(daysBetweenDates(2012,1,1,2012,3,1))

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed", "The answer was supposed to be: ", answer, " Instead you got: ", result)
        else:
            print("Test case passed!")


test()
