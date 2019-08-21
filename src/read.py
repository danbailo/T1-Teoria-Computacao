from os import listdir
from os.path import isfile, join
import numpy as np
from tqdm import tqdm
from time import time

def knapSack(W, wt, val, n):
	K = np.zeros((n+1, W+1), dtype=np.int32)
	for i in tqdm(range(n+1)):
		for i in range(n+1): 
			for w in range(W+1): 
				if i==0 or w==0: K[i][w] = 0 
				elif wt[i-1] <= w: 
					K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
				else: 
					K[i][w] = K[i-1][w]
	return K[n][W] 

def get_instances(directory):
	return [f for f in listdir(directory) if isfile(join(directory, f))]

def get_results(directory):
	results = []
	# print(len(get_instances(directory))) #output: 16
	for input_file in get_instances(directory): # break #caso eu queria testar so uma instancia, descomente essa linha
		with open(directory+input_file) as file: instance = list(map(lambda line:line.split(),file.read().splitlines()))	
		state = 0
		weigth = []
		value = []
		for inst in instance:
			if state == 0:
				n = int(inst[0])
				state = 1
			elif state == 1:			
				value.append(int(inst[1]))
				weigth.append(int(inst[2]))
				item_id = int(inst[0])
				if item_id == n: state = 2
			elif state == 2:
				w = int(inst[0])
		print('INSTANCE: {}\n'.format(input_file))
		print('N:',n)
		print('WEIGTH MAX:',w)
		print('VALUES: {}\n'.format(value))
		print('WEIGTHS: {}\n'.format(weigth))
		start = time()
		result_knapsack = knapSack(w, weigth, value, n)
		results.append((input_file,result_knapsack, '{0:.5}'.format(time()-start)))
		print('RESULT EXACT KNAPSACK: {}'.format(result_knapsack))
		print('='*50)		
		print()		
	return results	
	# return input_file,n,w,value,weigth				

if __name__ == "__main__":
	directory = './entradas/'
	print(get_results(directory))
	