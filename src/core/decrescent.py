def decrescent(number_items, weight_max, values_items, weight_items):
	"""Knapsack guloso, ordena de forma decrescente os valores e os pesos dos items"""
	items = {}
	for i in range(number_items): items[i] = values_items[i],weight_items[i]	
	
	items = sorted(items.values(), reverse=True)
	result_final = 0
	weight = 0
	
	for values_items,weight_items in items:
		if weight_items+weight <= weight_max:
			result_final += values_items
			weight += weight_items
	return result_final