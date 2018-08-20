from pprint import pprint
import os

targets = ['O', 'PER', 'ORG', 'MISC', 'LOC']

for i in range(1,3): # train1, train2
	folder = 'train'+str(i)
	dataset_types = ['train', 'valid', 'test']
	dic = {}
	for dataset_type in dataset_types:
		fname = os.path.join('.', folder , dataset_type+'.txt')
		d = {}
		for target in targets:
			d[target] = 0

		with open(fname, 'r') as f:
			for line in f:
				tags = line.strip().split('\t')[-1].split(' ')
				for tag in tags:
					for target in targets:
						if tag.endswith(target):
							d[target] += 1
		dic[dataset_type] = d
		# print(fname)
		# pprint(d)
	# pprint(dic)
	res = {}
	for target in targets:
		n = 0
		for dataset_type in ['valid']: # dataset_types
			n += dic[dataset_type][target]
		res[target] = n
	print(i)
	pprint(res)