import numpy as np
import random

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
			result_final.append(items.pop(index))
			value += value_item
			weight += weight_item
		else: items.pop(index)

	solution = [0 for i in range(number_items)]

	for aux_value in aux:
		if aux_value in result_final: solution[aux.index(aux_value)] = 1
	return solution, aux, value

def local_search(solution, aux, value, weight_max):
	all_solutions = []
	solution_aux = solution[:]
	for i in range(len(solution)):
		if solution[i] == 1: solution[i] = 0
		elif solution[i] == 0: solution[i] = 1
		all_solutions.append(solution[:])
		solution[:] = solution_aux		

	new_solution = solution_aux[:]
	for solution in all_solutions:
		new_value = 0
		new_weight = 0		
		for j in range(len(solution)):
			if solution[j] == 1:
				new_value += aux[j][1]
				new_weight += aux[j][2]
		if new_weight <= weight_max and new_value > value:
			new_solution = solution[:]
			value = new_value

	if new_solution == solution_aux: 
		return value
	return local_search(solution, aux, value, weight_max)

def grasp(max_it, window, number_items, weight_max, values_items, weight_items):
	best_solution = 0
	for i in range(max_it):
		solution, aux, value = semi_greedy_construction(window, number_items, weight_max, values_items, weight_items)
		solution = local_search(solution, aux, value, weight_max)
		print(solution)
		if solution > best_solution: best_solution = solution
	return best_solution			


