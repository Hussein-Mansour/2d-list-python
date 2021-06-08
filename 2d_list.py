#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Sun/Jun6/2021
# this program generates a 2D Array the size the user asks for
# randomly generate numbers between 1 and 50
# finds the average of all the numbers


import random


def average_number(average):
    # this function get the average of numbers in list

    avg = average[0]

    # adder
    for counter in average:
        avg = avg + counter
    # sum
    total = 0
    for counter_loop in range(0, len(avg)):
        total = total + avg[counter_loop]
    # process
    process = total / len(avg)
    # return
    return process


def main():
    # this function uses a 2D list
    a_2d_list = []

    # start
    print("Starting ...")
    print("\n")
    # input
    rows = int(input("How many row would you like: "))
    columns = int(input("How many columns would you like:"))
    print("\n")
    # random
    for loop_counter_rows in range(0, rows):
        temp_column = []
        for loop_counter_columns in range(0, columns):
            a_random_number = random.randint(0, 50)
            temp_column.append(a_random_number)
            print("{0} ".format(a_random_number), end="")
        a_2d_list.append(temp_column)
        print("")
    # output
    print(
        "\n\nThe average of all the numbers is: {0}"
        .format(average_number(a_2d_list)))
    print("\nDone.")


if __name__ == "__main__":
    main()
