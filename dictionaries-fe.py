"""
Async Content: M1_L02: Dictionaries- Skill Drills
Scripts designed for practice with designing and working with Python dictionaries.
"""
# Working with Python Dictionaries

# Following is Python Dictionary containing student loan information.
# Notice all keys are defined as strings, but the values are declared in a variety of data types.

student_loan_information_aj = {
    "student_name": "Amy Johnson",
    "university": "Yale",
    "academic_year": "2015_2016",
    "loan_amoun": 45000,
    "duration_years": 10,
    "payments_started": False,
}

# Using the student_loan_information_aj dictionary provided, complete the following instructions:

# Print the original 'student_loan_information_aj' dictionary

print("The original student loan profile:", student_loan_information_aj)


# Our student's name was spelled incorrectly.
# @TODO Update the value of the `student_name' key to `Amy Johnston`.
student_loan_information_aj["student_name"] = "Amy Johnston"
# @TODO Be sure to print the dictionary so that you know your changes are working.
print("Name updated:", student_loan_information_aj)
# HINT - Remember, bracket notation.


# Every loan should have an interest rate associated with its information.
# @TODO Add a key called 'interest_rate' and assign it a value of 3.5 percent (or 0.035).
student_loan_information_aj["interest_rate"] = "3.5%"
# @TODO Print the dictionary so that you know your changes are working.
print("Interest added:", student_loan_information_aj)

# Reviewing the information, it appears that the key for 'loan_amoun' has been spelled incorrectly.
# @TODO Delete the existing key:value pair.
del student_loan_information_aj["loan_amoun"]
# @TODO Add a new key:value pair with the correct spelling. You can use the same amount of 45000.
student_loan_information_aj["loan_amount"] = 45000
# @TODO Print the dictionary so that you know your changes are working.
print("Loan amaount removed and added again:", student_loan_information_aj)