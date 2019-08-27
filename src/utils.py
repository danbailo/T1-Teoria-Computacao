import os
import time
import core

def get_instances(directory):
	return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def get_results(directory):	
	all_results_decrescent = []
	all_results_crescent = []
	all_results_efficiency = []

	instance = []
	for input_file in get_instances(directory): 
		with open(directory+input_file) as file: 
			for line in file: instance.append(line.split())
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

		start = time.time()
		result_decrescent = core.decrescent(number_items, weight_max, values_items, weight_items)
		all_results_decrescent.append((input_file,result_decrescent, '{0:.5}'.format(time.time()-start)))
		
		start = time.time()
		result_crescent = core.crescent(number_items, weight_max, values_items, weight_items)
		all_results_crescent.append((input_file,result_crescent, '{0:.5}'.format(time.time()-start)))

		start = time.time()
		result_efficiency = core.efficiency(number_items, weight_max, values_items, weight_items)
		all_results_efficiency.append((input_file,result_efficiency, '{0:.5}'.format(time.time()-start)))
		instance.clear()
	return all_results_decrescent, all_results_crescent, all_results_efficiency