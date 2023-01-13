import sys
import numpy as np

system_arv = sys.argv

if (len(system_arv) <= 1):
    print("Please specify the file name")
else:
    try:
        file = open(system_arv[1], "r")
        data = file.readlines()
        num_data = [int(i) for i in data if (i.strip().isnumeric()) ]

        print("Statistics Summary")
        print("mean:", np.mean(num_data))
        print("std:", np.std(num_data))
        print("min", np.min(num_data))
        print("max", np.max(num_data))
    except FileNotFoundError:
        print("No such file")
