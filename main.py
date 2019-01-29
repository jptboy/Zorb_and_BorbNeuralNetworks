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
    
    print(net.getWeightsandBias())
    net.train(weights,heights,labels, debug = True)
    print(net.getWeightsandBias())

def test(data):
    weights = data[0]
    heights = data[1]
    labels = data[2]

    net.test(weights,heights,labels)
def main():
    assert len(sys.argv) == 3, "Please input valid data size, and whether or not you want to plot"
    DATA_SIZE = int(sys.argv[1])
    cmd = sys.argv[2]
    if cmd == "plot": plot()
    elif cmd == "gen": gen(DATA_SIZE)
    elif cmd == "train":
        data = getData()
        train(data)
    elif cmd == "gen_test": gen_test(DATA_SIZE)
    elif cmd == "test":
        data = getData_test()#weights, heights, labels
        test(data)
    elif cmd == "plot_test": plot_test()
    elif cmd == "run": pass
    else: print("Please enter valid option",file = sys.stderr)

if __name__ == '__main__':
    main()
