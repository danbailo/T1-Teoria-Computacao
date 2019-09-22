import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import utils

if __name__ == "__main__":
	directory = 'inputs'
	utils.create_imgs_directory()

	decrescent, crescent, efficiency, grasp = utils.get_results(directory, 100, 2)
	exact = {'input1.in': 31621, 'input2.in': 67829, 'input3.in': 143449, 'input4.in': 28840, 'input5.in': 15785, 'input6.in': 99861, 'input7.in': 1940, 'input8.in': 741, 'input9.in': 10281, 'input10.in': 20149, 'input11.in': 30001, 'input12.in': 49885, 'input13.in': 49398, 'input14.in': 20880, 'input15.in': 20676, 'input16.in': 46281}

	print('decrescent')
	for i,j in decrescent.items():
		print(i,j)
	print('\ncrescent')
	for i,j in crescent.items():
		print(i,j)
	print('\nefficiency')
	for i,j in efficiency.items():
		print(i,j)
	print('\ngrasp')
	for i,j in grasp.items():
		print(i,j)