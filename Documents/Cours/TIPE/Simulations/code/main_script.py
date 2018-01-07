#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 19:28:37 2018

@author: jojo
"""

import selection_naturelle as sn
from matplotlib import pyplot as plt

'''graphe'''

e, n, s, p = 70, 30, 1000, 0.5
strat=["naif", "traitre", "rancunnier", "lunatique", "donnant_donnant",
       "per_cct","per_ttc"]
gen, pop = sn.arene(e, n, s, p)


for k in range(len(strat)):
    plt.plot(gen,pop[k],label=strat[k])
    
plt.xlabel('génération')
plt.ylabel('effectif')
plt.legend()
plt.show()