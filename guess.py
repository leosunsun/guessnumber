#猜数字游戏
import random
r = random.randint(1,100)
count = 0
while True: 
	count += 1
	guess = input ('猜猜这是几？')
	guess = int (guess)
	if guess == r :
		print ('耶!经过', count , '次努力，你终于猜对了！！')
		break
	elif guess > r :
		print ('比答案大')
	elif guess < r :
		print ('比答案小')
	print ('您已经猜了', count, '次')