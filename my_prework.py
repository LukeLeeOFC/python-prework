# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    """Print a formated USERNAME as is in the question."""
    print('"hello_'+user_name.upper()+'!"')

hello_name('Lucas')
print("\nThis is filler text to keep track of my problems")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    """Write a function that prints odd numbers from 1-100 and returns nothing"""
    for odd in range(1,100):
        if odd % 2 == 1:
            print(odd)

first_odds()

print("\nThis is a filler text to keep track of my problems")
# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    """Write a function to return the max number of a given list"""
    a_list = [23, 7, 19, 1003]
    return max(a_list)

print(max_num_in_list(f"digits"))

print("\nThis is filler text to keep track of my problems")
# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# The return should be boolean Type (true/false)
def is_leap_year(a_year):
    if a_year % 4 == 0:
        return True
    elif a_year % 400 == 0:
        return True
    else:
        return False

print(is_leap_year(2020))

print("\nThis is filler text to keep track of my problems")
# Question 5
# Write a function to check to see if all numbers in a list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive
# numbers. The return should be boolean Type.
def is_consecutive(a_list):
    """Create a function to be sure numbers listed are consecutive numbers using a boolean"""
# I'm using the range function to return a list of numbers starting at the minimum number of the set list using the min function and ending at
# the maximum number of the list using the max function. I'm using the +1 interval to change the increment from the default of 0 to 1.
    consec = list(range(min(a_list),max(a_list)+1))
    if consec == a_list:
        return True

    else:
        return False

a_list = [1,2,3,4]
print(is_consecutive (a_list))
# Test code to ensure a number list not consecutive shows false.
a_list = [1,2,4,3]
print(is_consecutive(a_list))
    