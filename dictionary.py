 myData = {"effective top tube length": 515, "seat tube length": 500, "seat tube angle": 74.4, "head tube angle": 70.5, "stack": 513, "reach": 367, "standover height": 755} 

 myKeys = [] # [] is an empty array
 myValues = []

 #parallel iteration

for k, v in myData.items():
	# k and v are two incremental variables iterating simultaneously
	# .items() is a METHOD that alows us to iterate as many times as there are "items" inside our dictionary
	print("key: " + str(k) + ", value: " + str(v)) # monitor status of each variable on each iteration
	myKeys.append(k)
	myValues.append(v)
	# .append() is another METHOD that adds items to an ARRAY for a list

print("ALL KEYS: " + str(myKeys))
print("ALL VALUES: " + str(myValues))