print("******** String Class ********")
string1 = "  Welcome    "
string2 = " to "
string3 = "  the first    "
string4 = "Lab activity "
string5 = " in the   "
string6 = " OOP Course "
string = string1 + string2 + string3 + string4 + string5 + string6
print(string)

print("The length of the concatenated string is: ", len(string))

new_string = string1.strip() + " "+ string2.strip() + " "+string3.strip()+" "+string4.strip()+" "+string5.strip()+" "+string6.strip()+"!"

print(new_string)
print("The length of the above string is : ", len(new_string))
sub_string = new_string[new_string.index("La"):new_string.index("in")]
print("Retrieved: ",sub_string)

print("Index of first I in 'LAB ACTIVITY' is at: ",sub_string.upper().index("I"))

lab_activities = "lab interesting activities are activities lab Interesting Lab Activities Are Interesting Lab activities Lab Interesting"

print("First occurrence of Interesting is at: ",lab_activities.index("Interesting"))

oops = "Object-Oriented-Programming 44542"
print(oops)
print(oops.replace("-", "_").replace(" ","-"))
String1 = "Computer"
String2 = "Science"

print("The ID is: "+String1[0:4]+String2[0:3].upper()+str(len(String1))+str(len(String2)))

