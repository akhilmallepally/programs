a = int(input("enter age"))
s1 = ["F"]
s2 = ["M"]
e = input("enter gender")
if e in s1:
	print("Urban")
elif(e in s2 and a>=40 and a<=60):
	print("uban")
elif(e in s2 and a>=20 and a<=40):
	print("Anywhere")
else:
	print("error")