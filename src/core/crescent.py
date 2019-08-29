def crescent(number_items, weight_max, values_items, weight_items):
	"""Knapsack guloso, ordena de forma crescente os valores e os pesos dos items"""
	items = {}
	for it in range(number_items): items[it] = values_items[it],weight_items[it]	
	del values_items, weight_items
	
	items = sorted(items.values())
	result_final = []
	weight = []
	
	for values_items,weight_items in items:
		if weight_items+sum(weight) < weight_max and weight_items < weight_max: 
			result_final.append(values_items)
			weight.append(weight_items)	
	return sum(result_final)