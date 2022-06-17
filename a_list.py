#!/usr/bin/env python3

# Created by: Hertz
# Created on: June 10, 2022.
# This program has two types of question
# 1st:user enters two different list then the program join them and display it
# 2nd:user enters a list of strings and then ask the index of one string in the
# list to find .


# The function of the 1st question that Takes the two list the user entered.
def mixed_list(list_of_ele_1, list_of_ele_2):
    print("For the elements in the first list: {}".format(list_of_ele_1))
    print("For the elements in the second list: {} ".format(list_of_ele_2))

    # Joining the two list entered
    for element in list_of_ele_2:
        list_of_ele_1.append(element)
    return list_of_ele_1


# The function of the 2nd question that ask for a list
def search_list(string_srch):
    search_list = string_srch

    # finding the index of one element
    for string_srch in search_list:
        search_list.index(string_srch)
    return search_list


def main():
    # declare lists
    list_1 = []
    list_2 = []
    string_srch = []
    list_strings = []

    # Explanetion given to the user
    print("This program will do two problems.")
    print("")
    print("Option 1: Merge two lists together.")
    print("Option 2: Find the index of the specified string.")
    print("Please choose only one.")
    print("")

    # asking the user to choose between the two options.
    print("Please enter 1 or 2 for your choice.")
    choice = input("Which option would you like to choose (1/2): ")
    print("")
    # checks to see the usern choice
    if choice == "1":

        print("Please enter 2 list of different elements .")
        print("")

        # get the first list from the user.
        user_list_1 = input("Enter the first list of elements: ")
        list_1 = user_list_1.split(",")

        # get the second list from the user.
        user_list_2 = input("Enter the second list of elements: ")
        list_2 = user_list_2.split(",")

        # calls function & displays to user.
        final_list = mixed_list(list_1, list_2)
        print("")
        print("The two lists joined together are : {}".format(final_list))

    # if the user chooses option 2
    elif choice == "2":

        # asking the user to enter a list
        user_strg = input("Enter a list of strings: ")
        list_strings = user_strg.split(",")
        print(list_strings)
        print("")

        # asking for an elements to find
        user_srch = input("Enter a string to find for: ")
        print(user_srch)

        # finding the index of the element they user entered.
        for counter in range(len(list_strings) + 1):
            if list_strings[counter] == user_srch:
                string_srch = counter
                break

        # display the element and it's index
        print("{} occurs in at indexes {} ".format(user_srch, string_srch))
    else:
        print("Please enter a valid entry.")


if __name__ == "__main__":
    main()
