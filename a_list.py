def mixed_list(list_of_ele_1, list_of_ele_2):
  print("For the elements in the first list: {}".format(list_of_ele_1))
  print("For the elements in the second list: {} ".format(list_of_ele_2))

  for element in list_of_ele_2:
    list_of_ele_1.append(element)
  return list_of_ele_1
  
#def search_list(string_srch):
    #user_list = []
    #print("List entered {}".format(user_list))

    #return user_list

def main():
    # declare lists
    list_1 = []
    list_2 = []
    string_srch = []

    # intro
    print("This program will do two problems.")
    print("Option 1: Merge two lists together.")
    print("Option 2: Find the index of the speficied string.")
    print("Please choose!")
    print("")

    # gets input
    choice = input("Which option would you like to choose (1/2): ")

    # checks to see the choice user has enters
    if choice == "1":
      # get user input
      print("Please enter a list of different elements for each list.")
      print("")

      # gets user input
      user_list_1 = input("Enter the first list of elements: ")
      list_1 = user_list_1.split(",")

      # gets more user input
      user_list_2 = input("Enter the second list of elements: ")
      list_2 = user_list_2.split(",")

      # calls function & displays to user
      final_list = mixed_list(list_1, list_2)
      print("")
      print("The two lists joined together is: {}".format(final_list))

     # does option 2
    elif choice == "2":

      user_strg = input("Enter a list of strings: ")
      list_strings = user_strg.split(",")
      print(list_strings)
      print("")
      
      user_srch = input("Enter a string to find for:")
      print(user_srch)
     
      for user_srch in list_strings :
        string_srch = list_strings.index(user_srch)  
      #result_search = search_list(string_srch)
      print("{} occurs in at indexs {} and.".format(user_srch,string_srch))
    else:
      print("Please enter a valid entry.")

if __name__ == "__main__":
  main()
