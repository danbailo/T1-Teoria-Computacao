import utils

if __name__ == "__main__":
	directory = '../inputs/'

	decrescent = utils.get_results(directory)[0]
	crescent = utils.get_results(directory)[1]
	efficiency = utils.get_results(directory)[2]
	exact = [('input15.in', 20676, '5.5823'), ('input7.in', 1940, '0.84025'), ('input1.in', 31621, '0.40869'), ('input3.in', 143449, '2.81'), ('input11.in', 30001, '8.4843'), ('input12.in', 49885, '2343.9'), ('input9.in', 10281, '13.927'), ('input8.in', 741, '0.56339'), ('input14.in', 20880, '519.17'), ('input6.in', 99861, '33.931'), ('input5.in', 15785, '2.7625'), ('input2.in', 67829, '1.1453'), ('input16.in', 46281, '5.5514'), ('input10.in', 20149, '5.6126'), ('input13.in', 49398, '1041.3'), ('input4.in', 28840, '2.7862')]
	exact.sort(key=lambda x:int(x[0].strip('input.in')))

	print('\nDECRESCENTE')
	for i in decrescent: print(i)
	print('\nCRESCENTE')
	for i in crescent: print(i)
	print('\nEFICIENTE')
	for i in efficiency: print(i)
	print('\nEXATO')	
	for i in exact: print(i)