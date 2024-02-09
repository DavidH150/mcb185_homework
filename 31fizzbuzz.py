for i in range(1, 100):
	output = i
	if i % 3 == 0: output = 'Fizz'
	if i % 5 == 0: output = 'Buzz'
	if i % 3 == 0 and i % 5 == 0: output = 'FizzBuzz'
	print(output)