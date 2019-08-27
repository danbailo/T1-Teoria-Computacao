from os import listdir
from os.path import isfile, join
from time import time
import core

def get_instances(directory):
	return [f for f in listdir(directory) if isfile(join(directory, f))]

def get_results(directory):	
	all_results_decrescent = []
	all_results_crescent = []
	all_results_efficiency = []
	# for input_file in get_instances(directory): 
	input_file = 'input1.in'
	with open(directory+input_file) as file: instance = list(map(lambda line:line.split(),file.read().splitlines()))	
	state = 0
	weight_items = []
	values_items = []
	for inst in instance:
		if state == 0:
			number_items = int(inst[0])
			state = 1
		elif state == 1:			
			values_items.append(int(inst[1]))
			weight_items.append(int(inst[2]))
			item_id = int(inst[0])
			if item_id == number_items: state = 2
		elif state == 2:
			weight_max = int(inst[0])

	start = time()
	result_decrescent = core.decrescent(number_items, weight_max, values_items, weight_items)
	all_results_decrescent.append((input_file,result_decrescent, '{0:.5}'.format(time()-start)))
	
	start = time()
	result_crescent = core.crescent(number_items, weight_max, values_items, weight_items)
	all_results_crescent.append((input_file,result_crescent, '{0:.5}'.format(time()-start)))

	start = time()
	result_efficiency = core.efficiency(number_items, weight_max, values_items, weight_items)
	all_results_efficiency.append((input_file,result_efficiency, '{0:.5}'.format(time()-start)))
	return all_results_decrescent, all_results_crescent, all_results_efficiency

if __name__ == "__main__":
	directory = '../inputs/'

	test1 = []
	test2 = []

	for input_file in get_instances(directory): 
		start = time()
		with open(directory+input_file) as file: instance = list(map(lambda line:line.split(),file.read().splitlines()))	
		# print(instance)
		test1.append(time()-start)

		start = time()
		instance = []
		with open(directory+input_file) as file: 
			for line in file: instance.append(line.split())
		# print(instance)			
		test2.append(time()-start)

	print('USING MAP: {}'.format(sum(test1)))
	print('USING FOR: {}'.format(sum(test2)))