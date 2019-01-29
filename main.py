#!/home/jptboy/anaconda3/bin/python
from generateData import gen, getData, gen_test, getData_test
from plotData import plot, plot_test
from NeuralNetwork import NeuralNetwork
import sys
import os
net = NeuralNetwork()

def train(data):
    weights = data[0]
    heights = data[1]
    labels = data[2]
    
    
def test(data):
    weights = data[0]
    heights = data[1]
    labels = data[2]

def main():
    assert len(sys.argv) == 3, "Please input valid data size, and whether or not you want to plot"
    DATA_SIZE = int(sys.argv[1])
    if sys.argv[2] == "plot": plot()
    elif sys.argv[2] == "gen": gen(DATA_SIZE)
    elif sys.argv[2] == "train":
        data = getData()
        train(data)
    elif sys.argv[2] == "gen_test": gen_test(DATA_SIZE)
    elif sys.argv[2] == "test":
        data = getData_test()#weights, heights, labels
        test(data)
    elif sys.argv[2] == "plot_test": plot_test()
    elif sys.argv[2] == "run": pass
    else: print("Please enter valid option",file = sys.stderr)

if __name__ == '__main__':
    main()
