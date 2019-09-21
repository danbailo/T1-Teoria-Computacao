import numpy as np
import random

def semi_greedy_construction(window, number_items, weight_max, values_items, weight_items):
	efficiency = np.divide(values_items, weight_items)
	items = {}
	for i in range(number_items): 
		items[i] = efficiency[i], values_items[i], weight_items[i]
	items = sorted(items.values(), reverse=True)

	result_final = []
	weight = 0

	aux = items[:]
	while len(items) > 0 and weight < weight_max:
		if len(items) >= window: tmp_window = window 
		else: tmp_window = len(items)
		
		index = random.randint(0,tmp_window-1)
		weight_item = items[index][2]
		
		if weight_item+weight <= weight_max: 
			result_final.append(items.pop(index))
			weight += weight_item
		else: items.pop(index)

	solution = [0 for i in range(number_items)]

	for value in aux:
		if value in result_final: solution[aux.index(value)] = 1
	return solution, aux

def local_search(solution, aux, weight_max):
	default_value = 0
	default_weight = 0

	for i in range(len(solution)):
		if solution[i] == 1:
			default_value += aux[i][1]
			default_weight += aux[i][2]

	all_solutions = []
	solution_aux = solution[:]
	for i in range(len(solution)):
		if solution[i] == 1: solution[i] = 0
		elif solution[i] == 0: solution[i] = 1
		all_solutions.append(solution[:])
		solution[:] = solution_aux		

	new_solution = solution_aux[:]
	for solution in all_solutions:
		value = 0
		weight = 0		
		for j in range(len(solution)):
			if solution[j] == 1:
				value += aux[j][1]
				weight += aux[j][2]
		if weight <= weight_max and value > default_value:
			new_solution = solution[:]
			default_value = value

	if new_solution == solution_aux: 
		return default_value
	return local_search(new_solution,aux,weight_max)

def grasp(max_it, seed, window, number_items, weight_max, values_items, weight_items):
	best_solution = 0
	random.seed(seed)
	for i in range(max_it):
		solution, aux = semi_greedy_construction(window, number_items, weight_max, values_items, weight_items)
		solution = local_search(solution, aux, weight_max)
		if solution > best_solution: best_solution = solution
	return best_solution			


	