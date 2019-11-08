a = int(input("No of classes"))
b = int(input("No of classes attended"))
c = (b/a)*100
print(c)
d = input("Is medical cause there?")
e = ["y", "yes"]
if d in e:
	print("Allowed")
elif(c>75):
	print("Allowed")
else:
	print("Not allowed")