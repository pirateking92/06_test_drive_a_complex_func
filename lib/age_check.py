import re
from dateutil.relativedelta import relativedelta
from datetime import datetime

# Info on importing dateutil from here:
# https://www.influxdata.com/blog/guide-dateutil-module-python/#:~:text=The%20dateutil%20module%20is%20not,normally%20use%20other%20Python%20modules.

# Info on using re.match
# https://www.guru99.com/python-regular-expressions-complete-tutorial.html

# Convert age to years using dateutil relativedelta
# https://stackoverflow.com/questions/32083726/how-do-i-convert-days-into-years-and-months-in-python



def age_check(date):
    if type(date) is not str:
        raise Exception("Incorrect type")
    format = (r'^\d{4}-\d{2}-\d{2}$')
    if bool(re.match(r'^\d{4}-\d{2}-\d{2}$', date)) == False:
        raise Exception("Incorrect date format")
    print(re.match(r'^\d{4}-\d{2}-\d{2}$', date))

    age = (relativedelta(datetime.now(), datetime.strptime(date, '%Y-%m-%d'))).years
    # age = (datetime.now() - datetime.strptime(date, '%Y-%m-%d')).days // 365
    print(age)
    if age < 16:
        return f"access denied! you are {age} years old and need to be 16"
    return "access granted!"
    # return date == str(date)
    # parameters:
    #  date in string format 'YYYY-MM-DD"
    # returns:
    #  error message or "access granted!"