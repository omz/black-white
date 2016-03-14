import pickle

file = open("bwsave.dat", "rb")
test = pickle.load(file)
file.close()

test.sort(reverse=True)

for x in test:
	print x[0], "-", x[1]