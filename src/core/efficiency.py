import numpy as np

def efficiency(number_items, weight_max, values_items, weight_items):
	"""Knapsack guloso, utiliza a eficiência, a partir da razão "valor/peso" para selecionar os itens"""
	value_efficiency = np.array(values_items)
	weight_items_efficiency = np.array(weight_items)
	efficiency = value_efficiency/weight_items_efficiency
	efficiency = list(efficiency)
	
	items = {}

	for i in range(number_items): 
		items[efficiency[i]] = values_items[i],weight_items[i]

	items = sorted(items.items(), reverse=True)

	result_final = []
	weight = []

	for _,result in items:
		if result[1]+sum(weight) < weight_max and result[1] < weight_max: 
			result_final.append(result[0])
			weight.append(result[1])		
	return sum(result_final)	
