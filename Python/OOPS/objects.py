"""
•	For the String problems in this lab, use only String methods.  You do not need to use arrays, split method, or any looping or selection constructs.
•	Do not hard code any values unless specified and you must follow the given naming conventions.

"""

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


import math
print("******** Math Class ********")
value1 = 9
value2 = 13
sqrt = math.sqrt((value1**2) + (value2**2))
print("sqrt (value12 +value22): ",sqrt)

print("exp (9): ", math.exp(value1))
print("sec (9): ", 1/(math.cos(value1)))
myNumber = 27
print("Cube root of 27.00: ", math.pow(myNumber, 1/3))
print("Logarithm value is: ",math.log(myNumber))
print("tan 60° - tan 45° / (1 + tan 60° tan 45°) = ",math.tan(60-45))
tan90 = math.tan(90)
print("Theoretical value of tan (90) is: ",tan90)
print("Cubic root of modulus value of tan (90) is: ",math.pow(abs(tan90),1/3))
print("Cosecant of 30 is: ", 1/math.sin(30))
print("Secant of 30 is: ", 1/math.cos(30))
print("Minimum value in Cosec (30) and Sec (30) is: ", min(1/math.sin(30), 1/math.cos(30)))
print("Maximum value in Cosec (30) and Sec (30) is: ", max(1/math.sin(30), 1/math.cos(30)))
myNumber1 = 45
myNumber2 = 27
print("Rounded Value of cos 45: ", round(math.cos(myNumber1)))
print("Rounded Value of cos 27: ", round(math.cos(myNumber2)))
print("Rounded Value of tan 45: ", round(math.tan(myNumber1)))
print("Rounded Value of tan 27: ", round(math.tan(myNumber2)))
