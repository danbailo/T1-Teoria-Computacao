def crescent(weight_max, values_items, weight_items):
	"""Knapsack guloso, ordena de forma crescente os valores e os pesos dos items"""
	items = dict(zip(values_items, weight_items))
	items = sorted(items.items())
	result_final = []
	weight = []

	for values_items,weight_items in items:
		if weight_items+sum(weight) < weight_max and weight_items < weight_max: 
			result_final.append(values_items)
			weight.append(weight_items)	
	return sum(result_final)