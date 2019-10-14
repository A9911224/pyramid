# coding: utf-8
get_ipython().magic('pylab inline')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
def tree(a):
    for i in range(a+1):
        print(" "*(a-i)+"* "*i)
b = int(input("你想蓋幾層的金字塔："))
tree(b)
