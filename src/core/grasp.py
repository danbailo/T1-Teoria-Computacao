import numpy as np
import random
from time import time

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
	return solution, value, weight

def local_search(solution, values_items, weight_items, value, weight, weight_max):
	length = len(solution)
	neighbor = (solution.copy(), value, weight)
	for i in range(length):
		new_weight = 0
		new_value = 0
		if solution[i] == 0: 
			if weight+weight_items[i] <= weight_max:
				if value+values_items[i] > neighbor[1]:
					temp = solution.copy()
					temp[i] = 1
					neighbor = temp, weight+weight_items[i], value+values_items[i]
	if value == neighbor[1] :return value
	return local_search(neighbor[0], values_items, weight_items, neighbor[1], neighbor[2], weight_max)

def grasp(max_it, window, number_items, weight_max, values_items, weight_items):
	best_solution = 0
	for i in range(max_it):
		solution, value, weight = semi_greedy_construction(window, number_items, weight_max, values_items, weight_items)
		solution = local_search(solution, values_items, weight_items, value, weight, weight_max)			
		if solution > best_solution: best_solution = solution
	return best_solution