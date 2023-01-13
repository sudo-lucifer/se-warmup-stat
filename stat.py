import sys
import numpy as np

system_arv = sys.argv

def print_data(lst):
    print("mean:", np.mean(lst), end=' ')
    print("std:", np.std(lst), end=' ')
    print("min:", np.min(lst), end=' ')
    print("max:", np.max(lst), end=' ')
    print("n:", len(lst))


def read_files(lst):
    combined = []
    for i in range(1,len(lst)):
        file = open(lst[i], "r")
        data = file.readlines()
        num_data = [int(i) for i in data if (i.strip().isnumeric()) ]
        combined += num_data

        print("Statistics Summary")
        print_data(num_data)

        file.close()

    return combined



if (len(system_arv) <= 1):
    print("Please specify the file name")
else:
    try:
        combined_data = read_files(system_arv)
        print("combined")
        print_data(combined_data)

    except FileNotFoundError:
        print("No such file")
