str1 = "  Welcome    "
str2 = " to "
str3 = "  the first    "
str4 = "Lab Activity "
str5 = " in the   "
str6 = " Python Course "
str = str1 + str2 + str3 + str4 + str5 + str6
print(str)
print(len(str))
str_edit = str1[2:9]+str2+str3[2:12]+str4+str5[1:7]+str6[0:14]+"!"
print(str_edit)
print(len(str_edit))
str_lab = str_edit[21:33]
print(str_lab)
str_lab1 = str_lab.upper()
print(str_lab1)
print(str_lab1.index("I"))

#2ND QUESTION

lab_activity_string = "lab interesting activities are activities lab Interesting Lab Activities Are Interesting Lab activities Lab Interesting"
print(lab_activity_string.index("interesting"))
oops_string = "Object-Oriented-Programming 44542"
print(oops_string.replace("-","_").replace(" ","-"))

String1 = "Computer"
String2 = "Science"
a = len(String1)
b = len(String2)
final = String1[0:5]+String2[0:3].upper()+str(a)+str(b)
print(final)

print(“Why  do  you  choose  Applied Computer Science”)
print("I chose ACS because of XYZ")
