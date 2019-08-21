from os import listdir
from os.path import isfile, join

def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
    return K[n][W] 

if __name__ == "__main__":
	with open('./entradas/input1.in') as instance: 
		instance = list(map(lambda x: x.split(), instance.read().splitlines()))

	state = 0
	weigth = []
	value = []
	# for inst in range(len(instance)):
	# 	if len(instance[inst]) == 1:
	# 		n = int(instance[0][0])
	# 		w = int(instance[-1][0])
	# 		state = 1
	# 	else:
	# 		value.append(int(instance[inst][1]))
	# 		weigth.append(int(instance[inst][2]))
	for inst in instance:
		if state == 0:
			n = inst[0]
			state = 1
		elif state == 1:			
			value.append((inst[1]))
			weigth.append((inst[2]))
			item_id = inst[0]
			if item_id == n: state = 2
		elif state == 2:
			w = inst[0]

	
	print('n:',n)	
	print('value:',value)
	print('weigth:',weigth)
	print('item_id:',item_id)
	# print('n: {}, w: {}'.format(n,w))
	# print('value: {}, weigth: {}'.format(value, weigth))

	# print(knapSack(w, weigth, value, n)) 


	# val = [60, 100, 120] 
	# wt = [10, 20, 30] 
	# W = 50
	# n = len(val) 



	# mylist = []
	# all_files = [f for f in listdir('./entradas/') if isfile(join('./entradas/', f))]
	# for file in all_files:
	# 	with open('./entradas/'+file) as f: 
	# 		for line in f.read().split(): mylist.append(line)

	# i = 1
	# while True:
	# 	# print(mylist.pop(i))
	# 	i += 2
	# 	if i > len(mylist)-3: break
	# print(len(mylist))

	# print(mylist)


	# print(all_files)

	# print(read_instances('./entradas/'))
