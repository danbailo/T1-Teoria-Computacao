from os import listdir
from os.path import isfile, join
from time import time
from knapsack import Knapsack

def get_instances(directory):
	return [f for f in listdir(directory) if isfile(join(directory, f))]

def get_results(directory):	
	all_results_decrescent = []
	all_results_crescent = []
	all_results_efficiency = []
	for input_file in get_instances(directory): 
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
		k = Knapsack(w, weigth, value, n)

		start = time()
		result_decrescent = k.fat_decrescent()
		all_results_decrescent.append((input_file,result_decrescent, '{0:.5}'.format(time()-start)))
		
		start = time()
		result_crescent = k.fat_crescent()
		all_results_crescent.append((input_file,result_crescent, '{0:.5}'.format(time()-start)))

		start = time()
		result_efficiency = k.fat_efficiency()
		all_results_efficiency.append((input_file,result_efficiency, '{0:.5}'.format(time()-start)))
	return all_results_decrescent, all_results_crescent, all_results_efficiency