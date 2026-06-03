score = int(0)
for i in range (5):
# the user chooses a number
	number1 = int (input("\33[31m" + "Please choose a number\n"))
# now the user needs to do a math calculation
	number2 = int (input("\33[34m" + f"What is {number1} times 3\n"))
# calculating the correct answer as it is
	correct = int(number1*3)
# if the answer of the user is right the game adds 1 to the user score and gives a feedback
	if correct == number2:
	   score = score+1
	   print("\33[33m" + "Nice answer")
# if the answer of the user is not right he also gets a feedback
	else:
	   print("\33[35m" + "wrong answer")
# prints to the user his final score
print ("\33[32m" + "Your score is " + str(score) + "\nGood work")
# end of the game
input("\nPress Enter to exit...")
