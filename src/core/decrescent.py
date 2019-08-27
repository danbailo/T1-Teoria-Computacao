def decrescent(number_items,weight_max, values_items, weight_items):
	"""Knapsack guloso, ordena de forma decrescente os valores e os pesos dos items"""
	values_items.sort(reverse=True)
	weight_items.sort(reverse=True)
	k = []
	result = []
	for i in range(number_items):
		if weight_items[i]<weight_max and sum(k) < weight_max:
			k.append(weight_items[i])
			result.append(values_items[i])
	return sum(result)