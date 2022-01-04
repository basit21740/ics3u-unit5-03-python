#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Jan 2022
# This program takes the level of grade and returns the middle percentage mark


def grade_calculator(grade):
    # this function converts the levels to percentage mark

    # process
    if grade == "4+":
        grade = 97
    elif grade == "4":
        grade = 90
    elif grade == "4-":
        grade = 83
    elif grade == "3+":
        grade = 78
    elif grade == "3":
        grade = 75
    elif grade == "3-":
        grade = 71
    elif grade == "2+":
        grade = 68
    elif grade == "2":
        grade = 65
    elif grade == "2-":
        grade = 61
    elif grade == "1+":
        grade = 58
    elif grade == "1":
        grade = 55
    elif grade == "1-":
        grade = 51
    elif grade == "R":
        grade = 30
    else:
        return -1

    return grade


def main():
    # this function gets the grade

    # input
    grade_string = input("Enter the level you want converted to" " a percentage: ")
    print("\n")

    # calls function
    completed_grade_calculator = grade_calculator(grade_string)

    # output
    if completed_grade_calculator == -1:
        print("Level {} is not a valid level.".format(grade_string))
    else:
        print(
            "Level {0} has a middle percentage of {1}%.".format(
                grade_string, completed_grade_calculator
            )
        )

    print("\nDone.")


if __name__ == "__main__":
    main()
