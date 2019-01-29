#!/home/jptboy/anaconda3/bin/python
import numpy as np
import pandas as pd
import time

def gen(DATA_SIZE):
    X = [np.random.ranf() * 15 for i in range(DATA_SIZE)]

    X = [x for x in X if x > 3]#weight vals, kg

    while len(X) < DATA_SIZE:
        val = np.random.ranf() * 15
        if val > 3:
            X.append(val)

    Y = []# height vals, dc
    while(len(Y) < len(X)):
        temp = np.random.ranf() * 15
        if temp > 3: Y.append(temp)
    Z = list(zip(X,Y))
    data = [[x[0],x[1],None] for x in Z]
    for item in data:
        if 80/item[0] < item[1]: item[2] = 1# above curve
        else: item[2] = 0 #below curve
    data = np.array(data)

    time.sleep(2)
    np.savetxt("data/data.csv",data,delimiter=',')

    with open('data/data.csv','r+') as f:
        content = f.read()
        f.seek(0,0)
        f.write("weight,height,Zorb_or_Borb" + '\n' + content)
def gen_test(DATA_SIZE):
    X = [np.random.ranf() * 15 for i in range(DATA_SIZE)]

    X = [x for x in X if x > 3]#weight vals, kg

    while len(X) < DATA_SIZE:
        val = np.random.ranf() * 15
        if val > 3:
            X.append(val)

    Y = []# height vals, dc
    while(len(Y) < len(X)):
        temp = np.random.ranf() * 15
        if temp > 3: Y.append(temp)
    Z = list(zip(X,Y))
    data = [[x[0],x[1],None] for x in Z]
    for item in data:
        if 80/item[0] < item[1]: item[2] = 1# above curve
        else: item[2] = 0 #below curve
    data = np.array(data)

    time.sleep(2)
    np.savetxt("data/test_data.csv",data,delimiter=',')

    with open('data/test_data.csv','r+') as f:
        content = f.read()
        f.seek(0,0)
        f.write("Test: weight,height,Zorb_or_Borb" + '\n' + content)
def getData():
    allData = pd.read_csv('data/data.csv')
    weights = np.array(allData['weight'])
    heights = np.array(allData['height'])
    z_or_b = np.array(allData['Zorb_or_Borb'])
    return weights,heights,z_or_b
def getData_test():
    allData = pd.read_csv('data/test_data.csv')
    weights = np.array(allData['Test: weight'])
    heights = np.array(allData['height'])
    z_or_b = np.array(allData['Zorb_or_Borb'])
    return weights,heights,z_or_b