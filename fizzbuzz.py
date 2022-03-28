for i in range(101):
	num = int(i);
	if int(i)%3 == 0:
		num = str("Fizz")
	if int(i)%5 == 0:
		num = str("Buzz")
	if int(i)%3 == 0 and int(i)%5 == 0:
		num = str("FizzBuzz")
	print(num)