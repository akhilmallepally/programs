a = int(input("enter year"))
if(a%4 == 0):
	if(a%100 == 0):
		if(a%400 == 0):
			print("This is a leap year")
		else:
			print("This is not a leap year")
	else:
		print("This is a leap year")
else:
	print("This is not a leap year")