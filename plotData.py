#!/home/jptboy/anaconda3/bin/python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def plot():
    allData = pd.read_csv('data/data.csv')
    weights = np.array(allData['weight'])
    heights = np.array(allData['height'])
    z_or_b = np.array(allData['Zorb_or_Borb'])
    plt.scatter(weights,heights, c = z_or_b)
    plt.show()
def plot_test():
    allData = pd.read_csv('data/test_data.csv')
    weights = np.array(allData['Test: weight'])
    heights = np.array(allData['height'])
    z_or_b = np.array(allData['Zorb_or_Borb'])
    plt.scatter(weights,heights, c = z_or_b)
    plt.show()