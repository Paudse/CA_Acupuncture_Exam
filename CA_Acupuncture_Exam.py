
folder = "./CA_Acupuncture_Exam_Sheet/"
file = "模擬試題 加州600 题"

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
		if i%6 == 0:
			q.append(data[i].replace('\n', ''))
		if i%6 == 1:
			s1.append(data[i].replace('\n', ''))
		if i%6 == 2:
			s2.append(data[i].replace('\n', ''))
		if i%6 == 3:
			s3.append(data[i].replace('\n', ''))
		if i%6 == 4:
			s4.append(data[i].replace('\n', ''))
		if i%6 == 5:
			a.append(data[i].replace('\n', ''))

	# for j in range (0,len(de)):
		# print(de[j], ' : ',ch[j])

	not_finished = 1
	k = 0
	score = 0

	while not_finished:
		print('<', k+1 , '/', len(q) , '>')
		ans_num = ['1', '2']

		# ans = ['', '']
		# for m in range(0,2):
		# 	r = list(range(0,k)) + list(range(k+1, 2))
		# 	# print(r)
		# 	ans[m] = ch[random.choice(r)]

		print(colored(q[k], 'yellow', attrs=['bold']))
		print('(1)', s1[k])
		print('(2)', s2[k])
		print('(3)', s3[k])
		print('(4)', s4[k])

		input_ans = input('Your answer: ')

		if input_ans == str(a[k]):
			print(colored('Correct!', 'green'))
			score = score + 1
			k = k + 1
		else:
			print(colored('Wrong. Try again.', 'red'))
			score = score - 1
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
			if score == len(q):
				print(colored('Your score: '+ str(score)+ '/'+ str(len(q)) + '   GREAT!!!', 'green'))
			else:
				print(colored('Your score: '+ str(score)+ '/'+ str(len(q)), 'red'))
			print(colored("test finished", 'cyan'))
			time_end = time.time()
			print('time cost: ', round(time_end-time_start, 3), 's')
			if not os.path.exists('./score_record'):
				os.makedirs('./score_record')
			with open('./score_record/score_' + file + ".txt", "a", encoding='utf-8') as f:
				now = datetime.now()
				dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
				score_message = file+'   '+dt_string+'   '+str(score)+'/'+str(len(q))+'   '+str(round(time_end-time_start, 3))+'\n'
				f.write(score_message)


if __name__ == '__main__':
	test(foler_file_name)




