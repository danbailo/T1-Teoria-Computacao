import numpy as np

def fat_efficiency():
	"""Knapsack guloso, utiliza a eficiência, a partir da razão "valor/peso" para selecionar os itens"""
	value_efficiency = np.array(.get_values())
	weight_items_efficiency = np.array(.get_weight_items())
	efficiency = value_efficiency/weight_items_efficiency
	efficiency = list(efficiency)

	k = []
	result = []
	while True:
		index = efficiency.index(max(efficiency))
		if .get_weight_items()[index]<.get_weight() and sum(k)<.get_weight():
			efficiency.pop(index)
			k.append(.get_weight_items().pop(index))
			result.append(.get_values().pop(index))
		else: break			
	return sum(result)	
