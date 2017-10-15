import numpy as np

def readNN(fname):
    f = open(fname, "r")
    data = f.read()
    NN = [float(i) for i in data.split(",")]
    NN = np.array(NN)
    return NN

def writeNN(fname, nodeWeights):
    f = open(fname, "w")
    for i in nodeWeights:
        f.write(str(i) + " ")


# nodeWeights = np.array([1.2, 3.4, 5.6])

# nodeWeights = readNN("NN2.txt")
# writeNN("NN2.txt", nodeWeights)
