


#1. Write a python program to reverse a string.

def reverse (str):
    reversedList = []
    index = len(str)  # save lenght of string in index
    while index > 0:
        reversedList += str[index - 1]  # save value of str[index-1] in reversedList
        index = index - 1  # subtract index
    str = "" # create empty string
    reversedString = str.join(reversedList) #join the list into a string
    print(reversedString)  # reversed string
