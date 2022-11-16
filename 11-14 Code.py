# -*- coding: utf-8 -*-

import scipy.stats
import pandas
import random
from math import trunc

class Bootstrap():
    
    def __init__(self):

        self.data_list = []
        self.bootstrap = []
        self.trim_data = []

    
    def gen_bootstrap(self, data_list, boot_numb):
        
        
            
        #self.list = self.dat.tolist()
        self.bootstrap = random.choices(self.data_list, k = boot_numb)
        
        return self.bootstrap

    def trim_mean(self, percentage):
        
        self.gen_bootstrap()
        
        obs_trim = trunc(int(percentage*len(self.bootstrap)))
        
        self.bootstrap.sort()
        
        for i in range(obs_trim):
            min_val = obs_trim[0]
            max_val = obs_trim[len(self.bootstrap)]
            
            self.bootstrap.remove(min_val, max_val)
            
            
        return self.bootstrap.mean()
            
l = [2,3,4,5,67,8,2,34,12,455,4]
test = Bootstrap()
test.gen_bootstrap(l, 2)            
