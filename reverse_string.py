#!/usr/bin/env python3
import os.path
import sys

# Written goals
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
   # reverse("Authentise")
   # reverseWords("Authentise seems like an interesting company to work for")
   #3. Write  a python program that takes a string at the command line, and a flag
   argv = sys.argv
   byletter = "-r" in argv
   if byletter: argv.remove("-r") #isolates and checks if ist a -r flag
   byword = "-w" in argv
   if byword: argv.remove("-w")#isolates and checks if its a -w flag
   value = argv[1]
   if os.path.isfile(value): #checks if the imput is a file
     f=open(value, "r") #opens file  in read mode
     if f.mode == 'r': #checks if its read mode
        value=f.read() #sets value to contents
   if byletter: #runs reverse if proper flag
       reverse(value)
   elif byword: #runs reverseWords if proper flag
       reverseWords(value)
   else:
      print("invalid flags, value: ", value) #If no flag is set returns string
