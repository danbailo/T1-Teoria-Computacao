import numpy as np

def efficiency(number_items,weight_max, values_items, weight_items):
	"""Knapsack guloso, utiliza a eficiência, a partir da razão "valor/peso" para selecionar os itens"""
	value_efficiency = np.array(values_items)
	weight_items_efficiency = np.array(weight_items)
	efficiency = value_efficiency/weight_items_efficiency
	efficiency = list(efficiency)

	k = []
	result = []
	while True:
		index = efficiency.index(max(efficiency))
		if weight_items[index]<weight_max and sum(k)<weight_max:
			efficiency.pop(index)
			k.append(weight_items.pop(index))
			result.append(values_items.pop(index))
		else: break			
	return sum(result)	
