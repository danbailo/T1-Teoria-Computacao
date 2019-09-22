import os
from time import time
import json
import core


def get_instances(directory):
	return sorted(os.listdir(os.path.join('..',directory)), key=lambda k:int(k.strip('input.in')))

def get_results(directory, max_it, window):	

	result = {}
	time_results = {}

	for input_file in get_instances(directory): 
		with open(os.path.join('..',directory,input_file)) as file: 
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

			start = time()
			crescent = core.crescent(number_items, weight_max, values_items, weight_items)
			time_crescent = time()-start
			
			start = time()			
			decrescent= core.decrescent(number_items, weight_max, values_items, weight_items)
			time_decrescent = time()-start

			start = time()
			efficiency = core.efficiency(number_items, weight_max, values_items, weight_items)		
			time_efficiency = time()-start
			
			start = time()
			grasp = core.grasp(max_it, window, number_items, weight_max, values_items, weight_items)
			time_grasp = time()-start
			
			start = time()
			exact = int(core.exact(number_items, weight_max, values_items, weight_items))
			time_exact = time()-start

			result[input_file] = {
				'1. Crescente': crescent, 
				'2. Decrescente': decrescent,
				'3. Eficiente': efficiency,
				'4. GRASP': grasp,
				'5. Exato': exact
			}

			time_results[input_file] = {
				'1. TEMPO-Crescente': time_crescent,
				'2. TEMPO-Decrescente': time_decrescent,
				'3. TEMPO-Eficiente': time_efficiency,
				'4. TEMPO-GRASP': time_grasp,
				'5. TEMPO-Exato': time_exact
			}

	with open('./result.json','w') as file: file.write(json.dumps(result,indent=4))
	with open('./time.json','w') as file: file.write(json.dumps(time_results,indent=4))

	return result,time_results



def create_imgs_directory():
	if not os.path.exists(os.path.join('..','imgs')):
		os.makedirs(os.path.join('..','imgs'))

#debugger
# if __name__ == "__main__":
# 	directory = '../inputs/'
# 	print(get_results(directory))