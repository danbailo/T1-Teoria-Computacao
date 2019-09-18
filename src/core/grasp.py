import numpy as np
import random

random.seed(0)

def exact(number_items, weight_max, values_items, weight_items):
    K = np.zeros((number_items+1, weight_max+1), dtype=np.int32)
    for i in range(number_items+1): 
        for weight in range(weight_max+1): 
            if i==0 or weight==0: K[i][weight] = 0 
            elif weight_items[i-1] <= weight: K[i][weight] = max(values_items[i-1] + K[i-1][weight-weight_items[i-1]], K[i-1][weight])
            else: K[i][weight] = K[i-1][weight]    
    return K[number_items][weight_max]

def efficiency(number_items, weight_max, values_items, weight_items):
	"""Knapsack guloso, utiliza a eficiência, a partir da razão "valor/peso" para selecionar os itens"""
	efficiency = np.divide(values_items, weight_items)
	items = {}
	for i in range(number_items): 
		items[i] = efficiency[i], values_items[i], weight_items[i]
	items = sorted(items.values(), reverse=True)
	result_final = 0
	weight = 0
	for _,values_items, weight_items in items:
		if ((weight_items+weight) < weight_max) and (weight_items < weight_max): 
			result_final += values_items
			weight += weight_items
	return result_final	

def get_result():
	exact_dict = {}
	efficiency_dict = {}
	grasp_dict = {}

	with open('../../inputs/input1.in') as file:
		state = 0
		weight_items = []
		values_items = []
		for line in file: 
			inst = line.split()
			if state == 0:
				number_items = int(inst[0])
				state = 1
			elif state == 1:
				item_id = int(inst[0])
				values_items.append(int(inst[1]))
				weight_items.append(int(inst[2]))
				if item_id == number_items: state = 2
			elif state == 2:
				weight_max = int(inst[0])
	return number_items, weight_max, values_items, weight_items

def semi_greedy_construction(number_items, weight_max, values_items, weight_items):
	efficiency = np.divide(values_items, weight_items)
	items = {}
	for i in range(number_items): 
		items[i] = efficiency[i], values_items[i], weight_items[i]
	items = sorted(items.values(), reverse=True)

	# print(items)

	window = 2
	# print(items[random.randint(0,window-1)])
	result_final = []
	weight = 0

	aux = items[:]

	while len(items)>=window:
		index = random.randint(0,window-1)
		weight_item = items[index][2]
		if ((weight_item+weight) < weight_max) and (weight_item < weight_max): 
			result_final.append(items.pop(index))
			weight += weight_item
		else: break
		#tratar o caso onde o tamanho dos itens sao menores do q a janela
	solution = [0 for i in range(number_items)]

	# print(aux)
	# print(result_final)

	for i in aux:
		if i in result_final: 
			# print(aux.index(i))
			solution[aux.index(i)] = 1
			# print(aux.index(i))
		else: 
			pass
			# print(i)
			# print('not in')
	# print(solution)
	return solution, aux

def local_search(solution, aux, weight_max):
	default_value = 0
	default_weight = 0
	# default_value = []
	# default_weight = []


	for i in range(len(solution)):
		if solution[i] == 1:
			default_value += aux[i][1]
			default_weight += aux[i][2]
			# value.append(aux[i][1])
			# default_weight.append(aux[i][2])
			# print(aux[i][1])

	print('default solution for value:',default_value)
	print('default solution for weight:',default_weight)

###########
#PRECISO OTIMIZAR ESSE CODIGO
###########

	all_solutions = []

	solution_aux = solution[:]
	for i in range(len(solution)):
		if solution[i] == 1:
			solution[i] = 0
		elif solution[i] == 0:
			solution[i] = 1
		# print(f'iteration:{i}, solution:{solution}')
		all_solutions.append(solution[:])
		solution[:] = solution_aux		

	for solution in all_solutions:
		value = 0
		weight = 0		
		for j in range(len(solution)):
			if solution[j] == 1:
				value += aux[j][1]
				weight += aux[j][2]
		print('value:',value)
		print('weight:',weight)				
		print()



if __name__ == "__main__":
	number_items, weight_max, values_items, weight_items = get_result()

	# print(exact(number_items, weight_max, values_items, weight_items))
	# print(efficiency(number_items, weight_max, values_items, weight_items))


	solution, aux = (semi_greedy_construction(number_items, weight_max, values_items, weight_items))
	local_search(solution, aux, weight_max)
	# print(semi_greedy_construction(number_items, weight_max, values_items, weight_items))
	# for i in semi_greedy_construction(number_items, weight_max, values_items, weight_items):
		# print(i)

	# random.seed(1)
	# print(random.randint(1,100))		

	