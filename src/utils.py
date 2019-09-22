import os
from time import time
import core

def get_instances(directory):
	return sorted(os.listdir(os.path.join('..',directory)), key=lambda k:int(k.strip('input.in')))

def get_results(directory, max_it, window):	

	decrescent = {}
	crescent = {}
	efficiency = {}
	grasp = {}


	for input_file in get_instances(directory): 
		with open(os.path.join('..',directory,input_file)) as file: 
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

			start = time()
			decrescent[input_file] = [core.decrescent(number_items, weight_max, values_items, weight_items), time()-start]
			start = time()
			crescent[input_file] = [core.crescent(number_items, weight_max, values_items, weight_items), time()-start]
			start = time()
			efficiency[input_file] = [core.efficiency(number_items, weight_max, values_items, weight_items), time()-start]			
			start = time()
			grasp[input_file] = [core.grasp(max_it, window, number_items, weight_max, values_items, weight_items), time()-start]
	
	return decrescent, crescent, efficiency, grasp

def create_imgs_directory():
	if not os.path.exists(os.path.join('..','imgs')):
		os.makedirs(os.path.join('..','imgs'))

#debugger
# if __name__ == "__main__":
# 	directory = '../inputs/'
# 	print(get_results(directory))