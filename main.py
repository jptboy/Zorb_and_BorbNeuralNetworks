#!/home/jptboy/anaconda3/bin/python
from generateData import gen, getData, gen_test, getData_test
from plotData import plot, plot_test
from NeuralNetwork import NeuralNetwork
import sys
import os
net = NeuralNetwork()
#good weights 1.376251933672288263e+00,1.463446384097069508e+00,-2.715993104639005651e+01

def train(data,debug_ = False):
    weights = data[0]
    heights = data[1]
    labels = data[2]
    
    print(net.getWeightsandBias())
    net.train(weights,heights,labels,debug=debug_)
    print(net.getWeightsandBias())

def test(data):
    weights = data[0]
    heights = data[1]
    labels = data[2]

    with open("weights.csv","r") as f:
        contents = f.read()
    contents = list(map(float,contents.split(",")))
    w1 = contents[0]
    w2 = contents[1]
    bias = contents[2]

    net.setWeightsAndBias(w1,w2,bias)

    cost = net.test(weights,heights,labels)
    print("Average cost is %s" % (cost))
def run():
    with open("weights.csv","r") as f:
        contents = f.read()
    contents = list(map(float,contents.split(",")))
    w1 = contents[0]
    w2 = contents[1]
    bias = contents[2]
    weight = float(input("Weight:\n"))
    height = float(input("Height:\n"))
    ret = net.classify(w1,w2,bias,weight,height)
    if ret < 0.5: os.system("say ZORB")#value closer to 0, below the 80/x curve
    else: os.system("say BORB") #value closer to 1, over the 80/x curve 

    

def main():
    assert len(sys.argv) == 3, "Please input valid data size, and whether or not you want to plot"
    DATA_SIZE = int(sys.argv[1])
    cmd = sys.argv[2]
    if cmd == "plot": plot()
    elif cmd == "gen": gen(DATA_SIZE)
    elif cmd == "train":
        data = getData()
        train(data)
    elif cmd == "train_plt":
        data = getData()
        train(data,debug_= True)
    elif cmd == "gen_test": gen_test(DATA_SIZE)
    elif cmd == "test":
        data = getData_test()#weights, heights, labels
        test(data)
    elif cmd == "plot_test": plot_test()
    elif cmd == "run":
        run()
    else: print("Please enter valid option",file = sys.stderr)

if __name__ == '__main__':
    main()
