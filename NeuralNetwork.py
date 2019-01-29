#!/home/jptboy/anaconda3/bin/python
import numpy as np
from matplotlib import pyplot as plt
class NeuralNetwork:
    __weight1 = 0
    __weight2 = 0
    __bias = 0

    def setWeightsAndBias(self,w1,w2,bias):
        self.__weight1 = w1
        self.__weight2 = w2
        self.__bias = bias

    def getWeightsandBias(self): return self.__weight1, self.__weight2, self.__bias

    def __init__(self):
        self.__weight1 = np.random.randn()
        self.__bias = np.random.randn()
        self.__weight2 = np.random.randn()

    def test(self,weights,heights,labels,graph = False): 
        data = np.array(list(zip(weights,heights,labels)))
        costs = []
        for org in data:
            org_mass = org[0]
            org_height = org[1]
            real_org_type = org[2]
            ORG_weight_vec = np.array([org_mass,org_height])
            NN_weight_matrix = np.array([self.__weight1,self.__weight2])
            org_weighted_sum = ORG_weight_vec.dot(NN_weight_matrix) + self.__bias
            
            pred_activation = self.__sigmoid(org_weighted_sum)

            cost = (pred_activation - real_org_type) ** 2
            costs.append(cost)
        if graph:
            plt.plot(costs)
            plt.show()
        return np.average(costs)

    def __sigmoid(self,x): return (1/(1+np.exp(-1*x)))

    def __sigmoid_p(self,x):
        val = self.__sigmoid(x)
        return val * (1 - val)

    def train(self,weights,heights,labels,debug = False):
        data = np.array(list(zip(weights,heights,labels)))
        learning_rate = 0.01
        if debug: costs = []
        for i in range(2000000):
            randIdx = np.random.randint(0, high = len(data))
            org = data[randIdx]
            org_mass = org[0]
            org_height = org[1]
            real_org_type = org[2]
            
            ORG_weight_vec = np.array([org_mass,org_height])
            NN_weight_matrix = np.array([self.__weight1,self.__weight2])
            
            org_weighted_sum = ORG_weight_vec.dot(NN_weight_matrix) + self.__bias
            
            
            pred_activation = self.__sigmoid(org_weighted_sum)

            cost = (pred_activation - real_org_type) ** 2
            
            if debug and i % 5000 == 0:
                c = 0
                for j in range(len(data)):
                    item = data[j]
                    pred = self.__sigmoid(
                        (self.__weight1 * item[0] + self.__weight2 * item[1]) + self.__bias
                    )
                    c += (pred - item[2]) ** 2
                costs.append(c)
                

            d_cost_d_pred = 2 * (pred_activation - real_org_type)

            d_pred_d_org_weighted_sum = self.__sigmoid_p(org_weighted_sum)

            d_org_weighted_sum_d_w1 = org_mass
            d_org_weighted_sum_d_w2 = org_height

            d_org_weighted_sum_d_bias = 1

            d_cost_d_org_weighted_sum = d_cost_d_pred * d_pred_d_org_weighted_sum

            d_cost_d_w1 = d_cost_d_org_weighted_sum * d_org_weighted_sum_d_w1
            d_cost_d_w2 = d_cost_d_org_weighted_sum * d_org_weighted_sum_d_w2
            d_cost_d_bias = d_cost_d_org_weighted_sum * d_org_weighted_sum_d_bias

            self.__weight1 -= learning_rate * d_cost_d_w1
            self.__weight2 -= learning_rate * d_cost_d_w2
            self.__bias -= learning_rate * d_cost_d_bias
        save = np.array([self.__weight1,self.__weight2,self.__bias])
        np.savetxt("weights.csv",save,delimiter=',')
        if debug: 
            plt.plot(costs)
            plt.show()