# -*- coding: utf-8 -*-

import pandas as pd
import random
from math import trunc
from statistics import mean
from plotnine import *

class Bootstrap():
    
    def __init__(self, data_list, boot_numb, percentage):
        self.data_list = data_list
        self.boot_numb = boot_numb
        self.percentage = percentage
        self.bootstrap = []
        self.trim_data = []
        self.means_list = []

    
    def gen_bootstrap(self):
        
        #self.list = self.dat.tolist()
        self.bootstrap = random.choices(self.data_list, k = self.boot_numb)
        
        return self.bootstrap

    def trim_mean(self):
        
        self.gen_bootstrap()
        
        obs_trim = trunc(self.percentage*len(self.bootstrap))
        
        self.bootstrap.sort()
        
        for i in range(obs_trim):
            min_val = self.bootstrap[0]
            max_val = self.bootstrap[len(self.bootstrap) - 1]
            
            self.bootstrap.remove(min_val)
            self.bootstrap.remove(max_val)

        mean1 = mean(self.bootstrap)
        return mean1
    
    def sim(self, n_sim):
        
        for i in range(n_sim):
            mean1 = self.trim_mean()
            
            self.means_list.append(mean1)
        
        return self.means_list
    
    
    def means_histogram(self):
        """ """
        # try:
        means_df = pd.DataFrame(self.means_list, columns = ["means"])
        
        if means_df.empty == False:
            plt = (ggplot(data = means_df) +
                   aes(x = "means") +
                   geom_histogram(bins = 50) +
                   labs(title = "cool histogram")
                   )
            return plt
        
        else:
            print("No simulations have run yet.")
            print("sim method needs to be run first.")
            


l2 = [1,2,3,4,5,6,7,8,9,10]
l = [2,3,4,5,67,8,2,34,12,455,4, 13, 24, 433, 123, 176, 0, -4]
test = Bootstrap(l2, 10, .2)
test.gen_bootstrap()            


test.trim_mean()
test.sim(10000)
test.means_histogram()
