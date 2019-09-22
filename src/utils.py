import os
from time import time
import json
import core

max_it = 100
window = 2

hooks = [
	('Crescente', core.crescent),
	('Decrescente', core.decrescent),
	('Eficiente', core.efficiency),
	('GRASP', lambda number_items, weight_max, values_items, weight_items :core.grasp(max_it, window, number_items, weight_max, values_items, weight_items)),
	('Exato', core.exact)
]

def get_instances(directory):
	return sorted(os.listdir(os.path.join('..',directory)), key=lambda k:int(k.strip('input.in')))

def get_results(directory):	
	result = {}
	time_results = {}

	for input_file in get_instances(directory): 
		result[input_file] = {}
		time_results[input_file] = {}
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

			for name, f in hooks:
				start = time()
				result[input_file][name] = f(number_items, weight_max,values_items, weight_items)
				time_results[input_file][name] = time() - start
	with open('./result.json','w') as file: file.write(json.dumps(result,indent=4))
	with open('./time.json','w') as file: file.write(json.dumps(time_results,indent=4))
	return result,time_results

def create_imgs_directory():
	if not os.path.exists(os.path.join('..','imgs')):
		os.makedirs(os.path.join('..','imgs'))

#debugger
# if __name__ == "__main__":
# 	directory = '../inputs/'
# 	print(get_results(directory))