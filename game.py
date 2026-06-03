score = int(0)
for i in range (5):
	number1 = int (input("\33[31m" + "please choose a number\n"))
	number2 = int (input("\33[34m" + f"What is {number1} double 3\n"))
	correct = int(number1*3)
	if correct == number2:
	   score = score+1
	   print("\33[33m" + "Nice answer")
	else:
	   print("\33[35m" + "worng answer")
print ("\33[32m" + "your score is " + str(score) + "\nGood work")
input("\nPress Enter to exit...")
