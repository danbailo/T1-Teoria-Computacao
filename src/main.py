from utils import get_results

if __name__ == "__main__":
	directory = '../entradas/'

	decrescent = get_results(directory)[0]
	crescent = get_results(directory)[1]
	efficiency = get_results(directory)[2]


	print('DECRESCENTE: {}\n'.format(decrescent))
	print('CRESCENTE: {}\n'.format(crescent))
	print('EFICIENTE: {}\n'.format(efficiency))