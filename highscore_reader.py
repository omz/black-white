import pickle

with open("bwsave.dat", "rb") as in_file:
	test = pickle.load(in_file)

for x in sorted(test, reverse=True):
	print('{} - {}'.format(*x))
