import numpy as np

def efficiency(number_items, weight_max, values_items, weight_items):
	"""Knapsack guloso, utiliza a eficiência, a partir da razão "valor/peso" para selecionar os itens"""
	efficiency = np.divide(values_items, weight_items)
	items = {}

	for i in range(number_items): items[i] = efficiency[i], values_items[i], weight_items[i]
	items = sorted(items.values(), reverse=True)
	result_final = 0
	weight = 0

	for _,values_items, weight_items in items:
		if weight_items+weight <= weight_max: 
			result_final += values_items
			weight += weight_items
	return result_final	