def fat_decrescent(self):
'''Knapsack guloso, ordena de forma decrescente os valores e os pesos dos items'''
	self.get_values().sort(reverse=True)
	self.get_weight_items().sort(reverse=True)
	k = []
	result = []
	for i in range(self.get_number_items()):
		if self.get_weight_items()[i] <self.get_weight() and sum(k) < self.get_weight(): 
			k.append(self.get_weight_items()[i])
			result.append(self.get_values()[i])
	return sum(result)