def mixed_list(list_of_def,list_of_def2):
    if len(list_of_def or list_of_def2 == 0):
       return stop
    else:
        list_of_def = sentence.split(",")
        return list_of_def
        
def main():
    
    new_list = []
    list1 = None
    list2 = None

    while list1 != "stop" or list2 != "stop":
        list1 = input("Enter any elements and to end enter stop : ")
        list2 = input("enter any elements and to end  enter stop :")

        try:
            # convert from a string to a float
            list1_string = float(list1)
            list2_string = int(list2)

            # handle invalid inputs.
            if list1_string < -1 or list2_string < -1 :
                print("Please enter a positive number.")
                continue
            new_list.append(list1_string,list2_string)

        # Error case
        except Exception:
            print(" It is taken as an invalid input.")

    # removing the last number(stop from the list and call the function
    new_list.pop()
    list = mixed_list(list_of_def)

    # displays  the two  list to the user
    print("For the lists in  first elements : {}".format(list1_string))
    print("For the lista in second elements".format(list2_string))
 
    # Adding the two list 
    for a_num in new_list :
        new_list.append(list1_string, list2_string)
        new_list= list1_string + list2_string
        print("for the mixed list = {}".format(list1_string, list2_string)

    # search
    for     


if __name__ == "__main__":
    main()

