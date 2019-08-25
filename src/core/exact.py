import numpy as np

def knapsack(W, wt, val, n):
    K = np.zeros((n+1, W+1), dtype=np.int32)
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: K[i][w] = 0 
            elif wt[i-1] <= w: K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else: K[i][w] = K[i-1][w]    
    return K[n][W]		

if __name__ == "__main__":
	weight = [50,20,10,40,8]
	value = [100,60,40,40,4]
	w=60
	n=5
	print(knapsack(w,weight,value,n))
