import os
import time
import core

def get_instances(directory):
	return sorted(os.listdir(directory), key=lambda k:int(k.strip('input.in')))

def make_test(function,number_items, weight_max, values_items, weight_items):
	start = time.time()
	answer = function(number_items, weight_max, values_items, weight_items)
	t = time.time()-start
	return answer, t

def get_results(directory):	

	decrescent = []
	crescent = []
	efficiency = []

	for input_file in get_instances(directory): 
		with open(os.path.join(directory,input_file)) as file: 
			state = 0
			weight_items = []
			values_items = []
			for line in file: 
				inst = line.split()
				if state == 0:
					number_items = int(inst[0])
					state = 1
				elif state == 1:
					item_id = int(inst[0])
					values_items.append(int(inst[1]))
					weight_items.append(int(inst[2]))
					if item_id == number_items: state = 2
				elif state == 2:
					weight_max = int(inst[0])
			decrescent.append((input_file,make_test(core.decrescent,number_items, weight_max, values_items, weight_items)))
			crescent.append((input_file,make_test(core.crescent,number_items, weight_max, values_items, weight_items)))
			efficiency.append((input_file,make_test(core.efficiency,number_items, weight_max, values_items, weight_items)))	
	
	return decrescent, crescent, efficiency

#debugger
# if __name__ == "__main__":
# 	directory = '../inputs/'
# 	print(get_results(directory))