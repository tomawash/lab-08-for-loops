largest = 0

for i in range(4):
	userinput = int(input("Number please... "))
	if userinput > largest:
		largest = userinput

print("The largest number is " + str(largest))