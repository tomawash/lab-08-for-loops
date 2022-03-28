howlong = int(input("How long 'til the party? "))

if howlong >= 1:
	for i in range(howlong, 0, -1):
		print(i)
	print("PARTY TIME!!!")
else:
	print("PARTY NOW!!!")