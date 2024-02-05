import pytest

from lib.age_check import *

"""
As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.
"""
# def test_seeing_if_date_is_a_string():
#     result = age_check("string")
#     assert result == True
"""
As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied, telling them their current age and the required age (16).
"""
# def test_check_for_under_sixteen():
#     result = age_check('2022-02-05')
#     assert result == "access denied!"

def test_underage_returns_current_age_and_required_age():
    result = age_check('2022-02-05')
    assert result == "access denied! you are 2 years old and need to be 16"

def test_underage_returns_access_denied_almost_sixteen():
    result = age_check('2008-02-06')
    assert result == "access denied! you are 15 years old and need to be 16"

"""
As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.
"""
def test_granted_access_to_correct_ages():
    result = age_check('1992-04-14')
    assert result == 'access granted!'

def test_granted_access_to_sixteen():
    result = age_check('2008-02-05')
    assert result == 'access granted!'
"""

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.
"""
def test_for_incorrect_type():
    with pytest.raises(Exception) as err:
        age_check(19920414)
    error_message = str(err.value)
    assert error_message == "Incorrect type"

def test_for_another_incorrect_type():
    with pytest.raises(Exception) as err:
        age_check(True)
    error_message = str(err.value)
    assert error_message == "Incorrect type"

def test_for_an_incorrect_date_format():
    with pytest.raises(Exception) as err:
        age_check("14-04-92")
    error_message = str(err.value)
    assert error_message == "Incorrect date format"

def test_for_another_incorrect_date_format():
    with pytest.raises(Exception) as err:
        age_check("04-92")
    error_message = str(err.value)
    assert error_message == "Incorrect date format"
