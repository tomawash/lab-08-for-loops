average = 0
sum = 0

for i in range(4):
	userinput = int(input("Number please... "))
	sum = sum + userinput

average = sum/4

print("The average is " + str(average))