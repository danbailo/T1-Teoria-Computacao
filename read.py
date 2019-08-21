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
	with open('./entradas/input1.in') as file: instance = list(map(lambda line:line.split(),file.read().splitlines()))
	print(instance)		
	state = 0
	weigth = []
	value = []
	for inst in instance:
		if state == 0:
			n = int(inst[0])
			state = 1
		elif state == 1:			
			value.append(int(inst[1]))
			weigth.append(int(inst[2]))
			item_id = int(inst[0])
			if item_id == n: state = 2
		elif state == 2:
			w = int(inst[0])

	print('n:',n)	
	print('value:',value)
	print('weigth:',weigth)
	print('item_id:',item_id)

	print(knapSack(w, weigth, value, n))
	