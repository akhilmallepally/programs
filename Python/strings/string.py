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
