import numpy as np

def exact(number_items, weight_max, values_items, weight_items):
    K = np.zeros((number_items+1, weight_max+1), dtype=np.int32)
    for i in range(number_items+1): 
        for weight in range(weight_max+1): 
            if i==0 or weight==0: K[i][weight] = 0 
            elif weight_items[i-1] <= weight: K[i][weight] = max(values_items[i-1] + K[i-1][weight-weight_items[i-1]], K[i-1][weight])
            else: K[i][weight] = K[i-1][weight]    
    return K[number_items][weight_max]		