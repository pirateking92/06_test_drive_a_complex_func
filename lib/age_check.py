import re
from dateutil.relativedelta import relativedelta
from datetime import datetime

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