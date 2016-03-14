import pickle

scores = [
[100, "Player"],
[200, "Player"],
[300, "Player"],
[400, "Player"],
[500, "Player"],
[600, "Player"],
[700, "Player"],
[800, "Player"],
[900, "Player"],
[1000, "Player"]
]

file = open("bwsave3.dat", "wb")
pickle.dump(scores, file)
file.close()