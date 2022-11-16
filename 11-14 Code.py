# -*- coding: utf-8 -*-

import scipy.stats
import pandas
import random
from math import trunc
from statistics import mean

class Bootstrap():
    
    def __init__(self, data_list, boot_numb):
        self.data_list = data_list
        self.boot_numb = boot_numb
        self.bootstrap = []
        self.trim_data = []

    
    def gen_bootstrap(self):
        
        
            
        #self.list = self.dat.tolist()
        self.bootstrap = random.choices(self.data_list, k = self.boot_numb)
        
        return self.bootstrap

    def trim_mean(self, percentage):
        
        self.gen_bootstrap()
        
        obs_trim = trunc(percentage*len(self.data_list))
        
        self.data_list.sort()
        
        for i in range(obs_trim):
            min_val = self.data_list[0]
            max_val = self.data_list[len(self.data_list) - 1]
            
            self.data_list.remove(min_val)
            self.data_list.remove(max_val)

        mean1 = mean(self.data_list)
        return mean1
    
l = [2,3,4,5,67,8,2,34,12,455,4]
test = Bootstrap(l, 7)
test.gen_bootstrap()            


test.trim_mean(.2)