# -*- coding: utf-8 -*-
"""
Created on 19/05/2020

@author: Miriam
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import fnmatch
#import datetime
#import math
#shepherd = "Mary"
#string_in_string = "Shepherd {} is on duty.".format(shepherd)
#globals()[name] = vc
#data = {'First Column Name':  ['First value', 'Second value',...],
#        'Second Column Name': ['First value', 'Second value',...], ....}
#df = pd.DataFrame (data, columns = ['First Column Name','Second Column Name',...])
import os  
           
all_files = os.listdir('.')   # imagine you're one directory above test dir
#txt_files = filter(lambda x: x[-1:] == 'h', all_files)
from mpl_toolkits import mplot3d
import seaborn as sns

print(all_files)  # won't necessarily be sorted


###############################################################
#####    MEA RD-20-071    TR6/2    RESISTANCE=0.005382   ######
###############################################################
r= 0.005382
mea = 71

def EIScorrection(filename,r, ax=None):
    # Use skiprows to choose starting point and nrows to choose number of rows
    #data = pd.read_csv(infile, skiprows = 50, nrows=10)
    df = pd.read_csv(filename,  delimiter="\t", header=0, index_col=False, encoding= 'unicode_escape')
    df=df.rename(columns={df.columns[1]: 'Re(Z)'})
    df=df.rename(columns={df.columns[2]: 'Im(Z)'})
    [nr,nc]=df.shape
    Re = df['Re(Z)']
    Im = df['Im(Z)']
    Freq=df['freq/Hz']
    # voltage correction
    Im = -Im.values[:]*21
    Re = Re.values[:]
    Re = (Re - r)*21
    Or=min(Re[np.where(Im>=0)])
#    if ax == None:
#        fig,ax = plt.subplots(1,1)
#    ax.plot(Re, Im, 'rx', markersize=3)
##    ax.plot(t, fit(t) , 'r', label='FIT1-slope={} mV/h'.format(round(slope, 3)))
##    ax.set_ylim(y_lim);
##    ax.set_xlim(x_lim);
##    ax.set_xlabel('Time [h]');ax.set_ylabel('[V]');
#    ax.set_title('EIS {} {}'.format(filename[:-4], round(Or, 5)))
##    ax.set_xticks(np.arange(x_lim[0], x_lim[1]+10, 10))
##    ax.set_yticks(np.arange(y_lim[0], y_lim[1]+0.1, 0.1))
##    ax.legend(loc='upper left');
#    ax.grid();
#    plt.show()
    d = {'freq/Hz':Freq,
         'Re(Z)': Re,
         'Im(Z)': Im,
         'r': r,
         'Or': Or}   
    dataframe = pd.DataFrame (d, columns = ['freq/Hz','Re(Z)','Im(Z)','r','Or'])  
    return Re, Im, Or, df, dataframe

title = {'Ohmic Resistance': np.zeros(len(all_files))}   
Rdata = pd.DataFrame (title, columns = [ 'Ohmic Resistance']) 
#title = {'Re(z)[\u03A9\xb7cm\u00b2]': np.zeros(len(all_files))} 


for i in range(1,len(all_files)):
    Re, Im, Or, df, dataframe= EIScorrection(all_files[i], r)
    Rdata['Ohmic Resistance'][all_files[i]]= Or
    dataframe.to_csv('{} corrected.txt'.format(all_files[i][:-4]), sep=';')
    
Rdata = Rdata.iloc[1:,]

Rd = Rdata['Ohmic Resistance']
Rd = Rd.values[:]

#remember to unpack the array!!! otherwise u create an object!!!
Rd_w = np.array([Rd[0],Rd[4], Rd[5],Rd[6],Rd[1],Rd[2],Rd[3]] )
Rd_nw = np.array([Rd[7],*Rd[11:13],*Rd[8:11]])
x_w = np.array([18,24,69,94,191,213,238])
x_nw = np.array([18, 69, 94, 191, 213, 238])

col = {'Rd_w':Rd_w,
         'x_w': x_w}   
xy = pd.DataFrame (col, columns = ['Rd_w', 'x_w'])
xy.to_csv('Rd{}_w.txt'.format(mea), sep=';')
col = {'Rd_nw':Rd_nw,
         'x_nw': x_nw}   
xy = pd.DataFrame (col, columns = ['Rd_nw', 'x_nw'])
xy.to_csv('Rd{}_nw.txt'.format(mea), sep=';')










plt.figure(figsize=(11,4))
# PLOT
plt.plot(x_w, Rd_w, 'b',linewidth=1, label='MEA067 with water')
plt.plot(x_nw, Rd_nw, 'r',linewidth=1,label='MEA067 without water')
letter=''
#plt.ylim(0.3,0.6) 
xlim=200
#plt.xlim(0,xlim)
#plt.xticks(np.arange(0, xlim+10, 10))
#plt.yticks(np.arange(0.3, 0.65, 0.05))
plt.xlabel('Time [h]', fontsize=14)
plt.ylabel('Resistance [Ohm]', fontsize=14)
plt.title('Water Test: low water content ', fontsize=17)
plt.legend(fontsize=10, loc='upper right')
#plt.legend(fontsize=10)

plt.text(10, 0.57, letter, verticalalignment='top', horizontalalignment='left', fontsize=20, fontweight='bold')
plt.grid()
plt.show()













