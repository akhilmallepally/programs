#Given a string of odd length greater than 7,
#return a new string made of the middle three characters of a given String

str1 = input("enter string : ")
new_str = ""
if (len(str1)>7) and (len(str1)%2 !=0):
    for i in str1:
        str1[i]