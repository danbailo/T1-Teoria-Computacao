import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import utils

if __name__ == "__main__":
	directory = 'inputs'
	utils.create_imgs_directory()
	utils.create_results_directory()
	utils.get_results(directory)