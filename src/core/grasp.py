import numpy as np
import random
from time import time
import os

random.seed(42)

def semi_greedy_construction(window, number_items, weight_max, values_items, weight_items):
	efficiency = np.divide(values_items, weight_items)
	items = {}
	for i in range(number_items): 
		items[i] = efficiency[i], values_items[i], weight_items[i]
	items = sorted(items.values(), reverse=True)
	result_final = []
	value = 0
	weight = 0
	aux = items[:]
	while len(items) > 0 and weight < weight_max:
		if len(items) >= window: tmp_window = window 
		else: tmp_window = len(items)
		index = random.randint(0,tmp_window-1)
		value_item = items[index][1]
		weight_item = items[index][2]
		if weight_item+weight <= weight_max: 
			result_final.append(items[index][1])
			value += value_item
			weight += weight_item
		del items[index]
	solution = np.zeros(number_items,dtype=np.int16)
	for item in values_items:
		if item in result_final: solution[values_items.index(item)] = 1
	return solution, value

# def local_search(solution, values_items,weight_items, value, weight_max):
# 	all_solutions = []
# 	temp = solution[:]

# 	for i in range(len(solution)):
# 		if solution[i] == 1: 
# 			solution[i] = 0
# 			for k in range(len(solution)):
# 				print(solution[k], end=' ')
# 			solution[i] = 1
# 		elif solution[i] == 0: 
# 			solution[i] = 1
# 			for k in range(len(solution)): temp[k] = solution[k]
# 			solution[i] = 0
# 	print(temp, sep='\n')
# 	exit()
# 		# all_solutions.append(temp)

# 	for solution in all_solutions:
# 		print(solution)
# 		new_value = 0
# 		new_weight = 0		
# 		for j in range(len(solution)):
# 			if solution[j] == 1:
# 				new_value += values_items[j]
# 				new_weight += weight_items[j]
# 		if new_weight <= weight_max and new_value > value:
# 			new_solution = solution[:]
# 			value = new_value
# 	if new_solution.all() == solution_aux.all(): return value
# 	return local_search(solution, values_items,weight_items, value, weight_max)

#SE A BUSCA LOCAL NAO ACHAR NENHUM VIZINHO MELHOR, A SOLUCAO VAI
#ATUALIZAR POR CAUSA DAS ITERACOES DO GRASP?
def local_search(solution, values_items,weight_items, value, weight_max):
	temp = np.zeros(len(solution), dtype=np.int16)
	length = len(solution)
	print(f'value original {value}')
	print('-'*50)

	for i in range(length):
		new_weight = 0
		new_value = 0
		if solution[i] == 1: 
			solution[i] = 0
			for j in range(length):
				if solution[j] == 1:
					new_value += values_items[j]
					new_weight += weight_items[j]
					for k in range(length): temp[k] = solution[k]
			solution[i] = 1
		elif solution[i] == 0: 
			solution[i] = 1
			for j in range(length):
				if solution[j] == 1:
					new_value += values_items[j]
					new_weight += weight_items[j]
					for k in range(length): temp[k] = solution[k]			
			solution[i] = 0
		if new_value > value and new_weight <= weight_max:
			print(f'new value: {new_value}')
			print(f'new weight: {new_weight}\n')
			print('entrei')
			value = new_value
			solution = temp[:]
	return value

def local_searcha(solution, values_items, weight_items, value, weight_max):
	all_solutions = []
	solution_aux = solution.copy()
	for i in range(len(solution)):
		if solution[i] == 1: solution_aux[i] = 0
		elif solution[i] == 0: solution_aux[i] = 1
		all_solutions.append(solution_aux)
		solution_aux = solution.copy()
	print(*all_solutions, sep='\n')
	exit()
	new_solution = solution_aux[:]
	for solution in all_solutions:
		new_value = 0
		new_weight = 0		
		for j in range(len(solution)):
			if solution[j] == 1:
				new_value += values_items[j]
				new_weight += weight_items[j]
		if new_weight <= weight_max and new_value > value:
			new_solution = solution[:]
			value = new_value
	if new_solution.all() == solution_aux.all(): return value
	return local_search(solution, aux, value, weight_max)	

def grasp(max_it, window, number_items, weight_max, values_items, weight_items):
	best_solution = 0
	for i in range(max_it):
		solution, value = semi_greedy_construction(window, number_items, weight_max, values_items, weight_items)
		solution = local_searcha(solution, values_items, weight_items, value, weight_max)			
		if solution > best_solution: 
			best_solution = solution
		# 	verify = 0
		# if solution != best_solution:
		# 	verify += 1
		# 	if verify == max_it*0.1: return best_solution
	return best_solution

def get_instances(directory):
	return sorted(os.listdir(os.path.join('..',directory)), key=lambda k:int(k.strip('input.in')))

def get_data(directory):	

	grasp_results = {}

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
		grasp_results[input_file] = [grasp(1, 2, number_items, weight_max, values_items, weight_items), time() - start]
	return grasp_results	

if __name__ == "__main__":	
	print(*get_data('../inputs').items(), sep='\n')