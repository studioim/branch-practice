for i in range(1, 101):
	if i % 15 == 0:
		print("fizzbuzz", "\t")
	elif i % 3 == 0:
		print("fizz", "\t")
	elif i % 5 == 0:
		print("buzz", "\t")
	else: 
		print(i, "\t")

