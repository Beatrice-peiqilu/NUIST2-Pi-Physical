import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

GPIO.output(17,GPIO.LOW)
GPIO.output(18,GPIO.LOW)

def quiz():
	print("Welcome to the Python Quiz!")
	print("Answer the following questions:\n")

	question =[
		"1)Which the following is NOT a python data type?:a)int,b)float,c)rational,d)string,e)bool",
		"2)Which the following is NOT a built-in operation in Python?:a)+,b)%,c)abs(),d)sqrt()",
		"3)In a mixed-type expression involving ints and floats,Python will convert:a)floats to ints,b)ints to strings,c)floats and ints to strings,d)ints to floats",
		"4)The best structure for implementing a multi-way decision in Python is:a)if,b)if-else,c)if-elif-else,d)try",
		"5)What statement can be executed in the body of a loop to cause it to terminate?:a)if,b)exit,c)continue,d)break"
	]
	answers=[
		"c",
		"d",
		"d",
		"c",
		"d"
	]

	score=0

	for i in range(len(questions)):
		user_ans=input(question[i]).strip().lower()

		if user_ans ==answes[i]:
			print("Correct!\n")
			score+=1
			GPIO.output(17,GPIO.HIGH)
			time.sleep(1)
			GPIO.output(17,GPIO.LOW)
		else:
			print("Incorrect!\n")
			GPIO.output(18,GPIO.HIGH)
			time.sleep(1)
			GPIO.output(18,GPIO.LOW)

	print(f"Quiz completed!You got {score}/{len(questions)}questions correct.\n")

try:
	quiz()
finally:
	GPIO.cleanup()
