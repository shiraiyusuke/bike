import numpy as np
import sys


input_file = sys.argv[1]
test_ratio = float(sys.argv[2])

data = np.loadtxt(input_file, dtype="string")
l = len(data)
idx = np.arange(l)
np.random.shuffle(idx)

tmp = int(round(l*test_ratio))
test = data[idx[:tmp],:]
train = data[idx[tmp:],:]


np.savetxt("./data/train_lst.txt", train, fmt="%s")
np.savetxt("./data/test_lst.txt", test, fmt="%s")
