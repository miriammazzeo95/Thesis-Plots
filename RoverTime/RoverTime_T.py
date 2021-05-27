# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 17:45:11 2020

@author: Miriam
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
#import datetime
#import math
#shepherd = "Mary"
#string_in_string = "Shepherd {} is on duty.".format(shepherd)
#globals()[name] = vc
#data = {'First Column Name':  ['First value', 'Second value',...],
#        'Second Column Name': ['First value', 'Second value',...], ....}
#df = pd.DataFrame (data, columns = ['First Column Name','Second Column Name',...])
import os  
           
all_files = os.listdir("/Users/miria/OneDrive - Danmarks Tekniske Universitet/thesis/temperature test/RoverTime")   # imagine you're one directory above test dir
#txt_files = filter(lambda x: x[-1:] == 'h', all_files)
print(all_files)  # won't necessarily be sorted



i= 1
df = pd.read_csv(all_files[i],  delimiter="\t", header=0, index_col=False, encoding= 'unicode_escape')
Re68_w = df['Rd_w']
t68_w = df['x_w']

i= 3
df = pd.read_csv(all_files[i],  delimiter="\t", header=0, index_col=False, encoding= 'unicode_escape')
Re69_w = df['Rd_w']
t69_w = df['x_w']

i= 5
df = pd.read_csv(all_files[i],  delimiter="\t", header=0, index_col=False, encoding= 'unicode_escape')
Re71_w = df['Rd_w']
t71_w = df['x_w']





plt.figure(figsize=(7,4))
# PLOT
plt.plot(t68_w, Re68_w*21, color='blue', linestyle='-', marker='o',linewidth=1, label='MEA068')
plt.plot(t69_w, Re69_w*21, color='red', linestyle='-', marker='o',linewidth=1,label='MEA069')
plt.plot(t71_w, Re71_w*21, 'm',linewidth=1,label='MEA071 - STD')
letter=''
plt.ylim(0,0.08) 
xlim=200
#plt.xlim(0,xlim)
#plt.xticks(np.arange(0, xlim+10, 10))
#plt.yticks(np.arange(0.3, 0.65, 0.05))
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.xlabel('Time [h]', fontsize=16)
plt.ylabel('Areal Re(Z) [Ohm*cm2]', fontsize=16)
plt.title('Ohmic Resistance vs Time', fontsize=17)
plt.legend(fontsize=15, loc='upper right',mode = "expand", ncol = 3)
#plt.legend(fontsize=10)

plt.text(10, 0.57, letter, verticalalignment='top', horizontalalignment='left', fontsize=20, fontweight='bold')
plt.grid()
plt.show()

i= 0
df = pd.read_csv(all_files[i],  delimiter="\t", header=0, index_col=False, encoding= 'unicode_escape')
Re68_nw = df['Rd_nw']
t68_nw = df['x_nw']

i= 2
df = pd.read_csv(all_files[i],  delimiter="\t", header=0, index_col=False, encoding= 'unicode_escape')
Re69_nw = df['Rd_nw']
t69_nw = df['x_nw']

i= 4
df = pd.read_csv(all_files[i],  delimiter="\t", header=0, index_col=False, encoding= 'unicode_escape')
Re71_nw = df['Rd_nw']
t71_nw = df['x_nw']



plt.figure(figsize=(7,4))
# PLOT
# PLOT
plt.plot(t68_nw, Re68_nw*21, color='blue', linestyle='-', marker='o',linewidth=1, label='MEA068 ')
plt.plot(t69_nw, Re69_nw*21, color='red', linestyle='-', marker='o',linewidth=1,label='MEA069')
plt.plot(t71_nw, Re71_nw*21, 'm',linewidth=1,label='MEA071 - STD')
letter=''
plt.ylim(0,0.08) 
xlim=200
#plt.xlim(0,xlim)
#plt.xticks(np.arange(0, xlim+10, 10))
#plt.yticks(np.arange(0.3, 0.65, 0.05))
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.xlabel('Time [h]', fontsize=16)
plt.ylabel('Areal Re(Z) [Ohm*cm2]', fontsize=16)
plt.title('Ohmic Resistance vs Time, no water', fontsize=17)
plt.legend(fontsize=15, loc='upper right',mode = "expand", ncol = 3)
#plt.legend(fontsize=10)

plt.text(10, 0.57, letter, verticalalignment='top', horizontalalignment='left', fontsize=20, fontweight='bold')
plt.grid()
plt.show()
















