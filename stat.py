import sys

system_arv = sys.argv

if (len(system_arv) <= 1):
    print("Please specify the file name")
else:
    try:
        file = open(system_arv[1], "r")
        data = file.readlines()
        row = ["mean", "std", "min", "max"]
        print("Statistics Summary")
        for i in range(len(row)):
            if (len(data) > i):
                print(row[i] + ":", data[i].strip())
            else: 
                print(row[i] + ": N/A")
    except FileNotFoundError:
        print("No such file")
