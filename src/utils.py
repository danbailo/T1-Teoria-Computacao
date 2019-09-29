import os
from time import time
import json
from collections import defaultdict
import core

hooks = [
	('Crescente', core.crescent),
	('Decrescente', core.decrescent),
	('Eficiente', core.efficiency)
]

def create_imgs_directory():
	if not os.path.exists(os.path.join('..','imgs')):
		os.makedirs(os.path.join('..','imgs'))

def create_results_directory():
	if not os.path.exists(os.path.join('..','results')):
		os.makedirs(os.path.join('..','results'))

def get_instances(directory):
	return sorted(os.listdir(os.path.join('..',directory)), key=lambda k:int(k.strip('input.in')))

def get_exact_results(directory):	
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
			start = time()
			result[input_file]["Exato"] = core.exact(number_items, weight_max,values_items, weight_items)
			time_results[input_file]["Exato"] = time() - start
			
	with open(os.path.join('..','results','result_exact.json'),'w') as file: file.write(json.dumps(result,indent=4))
	with open(os.path.join('..','results','time_exact.json'),'w') as file: file.write(json.dumps(time_results,indent=4))

def get_greedy_results(directory):	
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
	with open(os.path.join('..','results','result.json'),'w') as file: file.write(json.dumps(result,indent=4))
	with open(os.path.join('..','results','time.json'),'w') as file: file.write(json.dumps(time_results,indent=4))

def get_GRASP_results(directory):	
	result = {}
	time_results = {}

	windows = [2,3,4,5,6,7,8,9]
	iters = [10,100,1000,10000]

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
			for max_it in iters:
				result[input_file]["Máx Iterações - "+str(max_it)] = {}
				time_results[input_file]["Máx Iterações - "+str(max_it)] = {}
				for window in windows:
					start = time()
					result[input_file]["Máx Iterações - "+str(max_it)]["Janela - "+str(window)] = core.grasp(max_it, window, number_items, weight_max, values_items, weight_items)
					time_results[input_file]["Máx Iterações - "+str(max_it)]["Janela - "+str(window)] = time() - start

	with open(os.path.join('..','results','result_GRASP.json'),'w', encoding='utf8') as file: file.write(json.dumps(result,indent=4, ensure_ascii=False))
	with open(os.path.join('..','results','time_GRASP.json'),'w', encoding='utf8') as file: file.write(json.dumps(time_results,indent=4, ensure_ascii=False))