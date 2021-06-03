#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: June 3, 2021
# This program returns the middle percentage for each number
# grade, if invalid input then it will say so


# finds the result and returns it to the user
def calc_mark(grade_num):
    determiner = {
        '4+': 97.5,
        '4': 90.5,
        '4-': 83,
        '3+': 78,
        '3': 74.5,
        '3-': 71,
        '2+': 68,
        '2': 64.5,
        '2-': 61,
        '1+': 58,
        '1': 54.4,
        '1-': 51,
    }
    # this is from
    # https://www.geeksforgeeks.org/switch-case-in-python-replacement/
    # it returns the result, and if none of the conditions are met
    # it will return -1
    return determiner.get(grade_num, -1)


# main function
def main():
    # get the input from the user
    grade_num = input("What is the grade(ie: 4+): ")

    # call the function and save the result as "percentage"
    percentage = calc_mark(grade_num)

    # if the result is -1 it means that the input was invalid
    if(percentage == -1):
        print("{} is not a valid grade".format(grade_num))
        main()
    # otherwise tell the user what the percentage is
    else:
        print("{} is the middle percentage for {}\n"
              .format(percentage, grade_num))
        main()


# get the program started
if __name__ == "__main__":
    main()
