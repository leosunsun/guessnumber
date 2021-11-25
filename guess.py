#猜数字游戏
import random
r = random.randint(1,100)
while True: 
	guess = input ('猜猜这是几？')
	guess = int (guess)
	if guess == r :
		print ('耶！终于猜对了！！')
		break
	elif guess > r :
		print ('比答案大')
	elif guess < r :
		print ('比答案小')