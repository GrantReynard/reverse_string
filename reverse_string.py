


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

# 2. Write a python program to reverse the order of words in a string.
def reverseWords (str):
    a = str.split() # Split the string
    a.reverse() # reverse the list
    result = " ".join(a) #join the list together
    print(result) #reverse order of words


if __name__ == "__main__":
    reverse("Authentise")
    reverseWords("Authentise seems like an interesting company to work for")