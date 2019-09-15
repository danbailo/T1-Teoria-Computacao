import numpy as np

def efficiency(number_items, weight_max, values_items, weight_items):
	"""Knapsack guloso, utiliza a eficiência, a partir da razão "valor/peso" para selecionar os itens"""
	value_efficiency = np.array(values_items)
	weight_items_efficiency = np.array(weight_items)
	efficiency = value_efficiency/weight_items_efficiency
	efficiency = list(efficiency)
	
	items = {}
	for i in range(number_items): 
		items[i] = efficiency[i], values_items[i], weight_items[i]

	del values_items, weight_items
	del value_efficiency, weight_items_efficiency

	items = sorted(items.values(), reverse=True)

	result_final = []
	weight = []

	for _,values_items, weight_items in items:
		if weight_items+sum(weight) < weight_max and weight_items < weight_max: 
			result_final.append(values_items)
			weight.append( weight_items)		
	return sum(result_final)	
