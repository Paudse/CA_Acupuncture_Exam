
# folder = "./CA_Acupuncture_Exam_Sheet/"
# file = "模擬試題_加州600题_1-25"
# file = "模擬試題_加州600题_26-50"
# file = "模擬試題_加州600题_51-75"
# file = "模擬試題_加州600题"

folder = "./Q&A/"
file = "Q&A-1 中醫基礎 p01"
###
foler_file_name = folder + file + ".txt"

###
import random
from termcolor import colored
import time
from datetime import datetime
import os
os.system('color')
os.system('mode con: cols=100 lines=20')

def test(foler_file_name):
	print('--------------------------------------')
	print(file)
	print('--------------------------------------')
	time_start = time.time()
	with open(foler_file_name, "r", encoding='utf-8') as f: 
		data = f.readlines()

	q = []
	s1 = []
	s2 = []
	s3 = []
	s4 = []
	a = []
	for i in range (0,len(data)):
		# print(i%3)
		# print(data[i])
		if i%7 == 0:
			q.append(data[i].replace('\n', ''))
		if i%7 == 1:
			s1.append(data[i].replace('\n', ''))
		if i%7 == 2:
			s2.append(data[i].replace('\n', ''))
		if i%7 == 3:
			s3.append(data[i].replace('\n', ''))
		if i%7 == 4:
			s4.append(data[i].replace('\n', ''))
		if i%7 == 5:
			a.append(data[i].replace('\n', ''))

	# for j in range (0,len(de)):
		# print(de[j], ' : ',ch[j])


	c = list(zip(q,s1,s2,s3,s4,a))
	random.shuffle(c)
	q,s1,s2,s3,s4,a = zip(*c)

	not_finished = 1
	k = 0
	score = 0
	wrong = 0
	answer_once = 0

	while not_finished:
		print('<', k+1 , '/', len(q) , '>')
		ans_num = ['1', '2']

		# ans = ['', '']
		# for m in range(0,2):
		# 	r = list(range(0,k)) + list(range(k+1, 2))
		# 	# print(r)
		# 	ans[m] = ch[random.choice(r)]

		print(colored(q[k], 'yellow', attrs=['bold']))
		print('', s1[k])
		print('', s2[k])
		print('', s3[k])
		print('', s4[k])

		input_ans = input('Your answer: ')

		if input_ans == str(a[k]):
			print(colored('Correct!', 'green'))
			score = score + 1
			k = k + 1
			answer_once = 0
		else:
			print(colored('Wrong. Try again.', 'red'))
			score = score - 1
			if answer_once == 0:
				wrong = wrong + 1
				answer_once = 1
			if not os.path.exists('./fault_record'):
				os.makedirs('./fault_record')
			with open('./fault_record/fault_' + file + ".txt", "a", encoding='utf-8') as f:
				ans_num = a[k]
				if ans_num == str(1):
					ans = s1[k]
				if ans_num == str(2):
					ans = s2[k]
				if ans_num == str(3):
					ans = s3[k]
				if ans_num == str(4):
					ans = s4[k]
				wrong_message = q[k] + '\n' + ans + '\n'
				f.write(wrong_message)

		print('--------------------------------------')
		if k == len(q):
			not_finished = 0
			score_100 = round(((len(q)-wrong)/len(q))*100,0)
			if score_100 >= 80:
				print(colored('Your score: '+ str(score_100) + '   YOU PASS!!!', 'green'))
				print(colored('Number of questions failed: -'+ str(wrong)+'/'+ str(len(q)), 'green'))
			else:
				# print(colored('Your score: '+ str(score)+ '/'+ str(len(q)), 'red'))
				print(colored('Your score: '+ str(score_100) + '   NOT PASS...', 'red'))
				print(colored('Number of questions failed: -'+ str(wrong)+'/'+ str(len(q)), 'red'))
			print(colored("test finished", 'cyan'))
			time_end = time.time()
			print('time cost: ', round(time_end-time_start, 3), 's')
			if not os.path.exists('./score_record'):
				os.makedirs('./score_record')
			with open('./score_record/score_' + file + ".txt", "a", encoding='utf-8') as f:
				now = datetime.now()
				dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
				score_message = file+'   '+dt_string+'   '+str(score_100)+'   -'+str(wrong)+'/'+ str(len(q))+'   '+str(round(time_end-time_start, 3))+'\n'
				f.write(score_message)


if __name__ == '__main__':
	while True:
		test(foler_file_name)
		testing = input('Press any key to test again.')




