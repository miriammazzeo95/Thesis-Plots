# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:26:50 2020

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
# We'll use the same fake ScalarMappable and colormap for each example
from matplotlib.colors import  ListedColormap
import seaborn as sns

print(all_files)  # won't necessarily be sorted



###########################################################################################################
###################################### 3D !!!
#ax = plt.axes(projection='3d')
#
#for filename in os.listdir('.'):
#    if fnmatch.fnmatch(filename, '*wo water*18h*corrected*.txt'):
#        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False,  encoding= 'unicode_escape')
#        Re = df['Re(Z)'].values
#        Im = df['Im(Z)'].values
#        ax.plot3D(Re, Im, 18,linestyle='-', marker='o',linewidth=1)
#    if fnmatch.fnmatch(filename, '*wo water*69h*corrected*.txt'):
#        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
#        Re = df['Re(Z)'].values
#        Im = df['Im(Z)'].values
#        ax.plot3D(Re, Im, 69, linestyle='-', marker='o',linewidth=1)
#    if fnmatch.fnmatch(filename, '*wo water*94h*corrected*.txt'):
#        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
#        Re = df['Re(Z)'].values
#        Im = df['Im(Z)'].values
#        ax.plot3D(Re, Im, 94, linestyle='-', marker='o',linewidth=1)
#    if fnmatch.fnmatch(filename, '*wo water*191h*corrected*.txt'):
#        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
#        Re = df['Re(Z)'].values
#        Im = df['Im(Z)'].values
#        ax.plot3D(Re, Im, 191, linestyle='-', marker='o',linewidth=1)
#    if fnmatch.fnmatch(filename, '*wo water*213h*corrected*.txt'):
#        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
#        Re = df['Re(Z)'].values
#        Im = df['Im(Z)'].values
#        ax.plot3D(Re, Im, 213,linestyle='-', marker='o',linewidth=1)
#    if fnmatch.fnmatch(filename, '*wo water*238h*corrected*.txt'):
#        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
#        Re = df['Re(Z)'].values
#        Im = df['Im(Z)'].values
#        ax.plot3D(Re, Im, 238, linestyle='-', marker='o',linewidth=1)
#        
#        
#ax.set_ylim(0,0.10)        
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z');
#
#ax.view_init(120,-90)




fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(nrows=2, ncols=2, figsize=(12,60))
fs=15
ls=13
small=11
ms=10

##################################################################################################################################
########################################################################################################  
   ############################ mea 68 - ax1 - 8 files - wo water  
palette=sns.color_palette("RdBu_r",8)
time = pd.Series(['1 h', '18h', '49h','97h','169h','194h','240h','264h'])
j=0
for i, value in time.items():

    for filename in os.listdir('.'):
        if fnmatch.fnmatch(filename, '*68*wo water*{}*corrected*.txt'.format(time[i])):
            df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False,  encoding= 'unicode_escape')
            Re = df['Re(Z)'].values
            Im = df['Im(Z)'].values
            ax2.scatter(Re, Im, color=palette[j],label = '{}'.format(time[i]), marker='o',s=ms,linewidth=0.5)
            j=j+1
         
ax2.set_ylim(0,0.12)  
ax2.set_xlim(0,0.40) 
ax2.set_title('MEA068, no water' , fontsize=fs) 
#ax4.set_aspect('equal')      
ax2.set_xlabel('Re(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax2.set_ylabel('-Im(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax2.legend(['1 h', '18h', '49h','97h','169h','194h','240h','264h'],loc="upper left",ncol=4, columnspacing=1,handletextpad=0.1, fontsize=small, labelspacing=0.2)

# ncol=len(ax.lines)
#handles, labels = ax2.get_legend_handles_labels()
#order = [0,1,4,5,6,7,2,3]
#ax2.legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc="upper left",ncol=4, columnspacing=1,handletextpad=0.1, fontsize=small, labelspacing=0.2)

ax2.tick_params( labelsize=ls)
#sns.set_palette("RdBu_r", 7)

##################################################################################################################################
########################################################################################################  
   ############################ mea 68 - ax1 - 10 files - with water      
    
palette=sns.color_palette("RdBu_r",11)
time = pd.Series(['1h', '2 18h', '27h','49h','97h','169h','194h','218h','264h','336h'])
j=0
for i, value in time.items():

    for filename in os.listdir('.'):
        if fnmatch.fnmatch(filename, '*68*with water*{}*corrected*.txt'.format(time[i])):
            df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False,  encoding= 'unicode_escape')
            Re = df['Re(Z)'].values
            Im = df['Im(Z)'].values
            ax1.scatter(Re, Im, color=palette[j],label = '{}'.format(time[i]), marker='o',s=ms,linewidth=0.5)
            j=j+1

ax1.set_ylim(0,0.12)  
ax1.set_xlim(0,0.40)  
#ax4.set_aspect('equal')      
ax1.set_xlabel('Re(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax1.set_ylabel('-Im(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax1.set_title('MEA068' , fontsize=fs) 
ax1.legend(['1h', '18h', '27h','49h','97h','169h','194h','218h','264h','336h'],loc="upper left", ncol=5,columnspacing=1, fontsize=small,labelspacing=0.2, handletextpad=0.1)
#handles, labels1 = ax1.get_legend_handles_labels()
#order = [0,1,2,3,4,5,6,7,8,9]
#ax1.legend([handles[idx] for idx in order],[labels1[idx] for idx in order],loc="upper left", ncol=5,columnspacing=1, fontsize=small,labelspacing=0.2, handletextpad=0.1)

ax1.tick_params( labelsize=ls)
#sns.set_palette("RdBu_r", 7) 




##################################################################################################################################
########################################################################################################  
   ############################ mea 69 - ax4 - 9 files - wo water      
    
palette=sns.color_palette("RdBu_r",9)
time = pd.Series(['1 h', '18h', '27h','97h','169h','194h','240h','264h','336h'])
j=0
for i, value in time.items():

    for filename in os.listdir('.'):
        if fnmatch.fnmatch(filename, '*69*wo water*{}*corrected*.txt'.format(time[i])):
            df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False,  encoding= 'unicode_escape')
            Re = df['Re(Z)'].values
            Im = df['Im(Z)'].values
            ax4.scatter(Re, Im, color=palette[j],label = '{}'.format(time[i]), marker='o',s=ms,linewidth=0.5)
            j=j+1

ax4.set_ylim(0,0.12)  
ax4.set_xlim(0,0.40)
ax4.set_title('MEA069, no water' , fontsize=fs) 
#ax4.set_aspect('equal')      
ax4.set_xlabel('Re(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax4.set_ylabel('-Im(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax4.legend(['1h', '18h', '27h','97h','169h','194h','240h','264h','336h'],loc="upper left", ncol=5, columnspacing=1,fontsize=small, labelspacing=0.2, handletextpad=0.1)

#handles, labels = ax4.get_legend_handles_labels()
#order = [0,1,2,3,4,5,6,7,8]
#ax4.legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc="upper left", ncol=5, columnspacing=1,fontsize=small, labelspacing=0.2, handletextpad=0.1)

ax4.tick_params( labelsize=ls)
#sns.set_palette("RdBu_r", 7)



##################################################################################################################################
########################################################################################################  
   ############################ mea 69 - ax3 - 10 files - with water      
    
palette=sns.color_palette("RdBu_r",10)
time = pd.Series(['1 h', '2 18h', '27h','49h', '97h','169h','194h','218h','264h','336h'])
j=0
for i, value in time.items():

    for filename in os.listdir('.'):
        if fnmatch.fnmatch(filename, '*69*with water*{}*corrected*.txt'.format(time[i])):
            df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False,  encoding= 'unicode_escape')
            Re = df['Re(Z)'].values
            Im = df['Im(Z)'].values
            ax3.scatter(Re, Im, color=palette[j],label = '{}'.format(time[i]), marker='o',s=ms,linewidth=0.5)
            j=j+1


ax3.set_ylim(0,0.12)  
ax3.set_xlim(0,0.40)  
ax3.set_title('MEA069' , fontsize=fs) 
#ax4.set_aspect('equal')      
ax3.set_xlabel('Re(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax3.set_ylabel('-Im(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax3.legend(['1h', '18h', '27h','49h', '97h','169h','194h','218h','264h','336h'],loc="upper left", ncol=5,columnspacing=1, fontsize=small, labelspacing=0.2,handletextpad=0.1)

#handles, labels = ax3.get_legend_handles_labels()
#order = [0,2,3,4,5,6,7,1]
#ax3.legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc="upper left", ncol=4,columnspacing=1, fontsize=small, labelspacing=0.2,handletextpad=0.1)

ax3.tick_params( labelsize=ls)
#sns.set_palette("RdBu_r", 7) 
#    
#    
#   
#
#
#
#
#
#
#
#

fig, [ax6, ax7] = plt.subplots(nrows=1, ncols=2, figsize=(11,4.5))
fs=15
ls=13
small=11
ms=10
##################################################################################################################################
########################################################################################################  
   ############################ mea 71 - ax6 - 7 files - with water      
    
palette=sns.color_palette("RdBu_r",7)
time = pd.Series([ '18h', '24h','69h', '94h','191h','213h','238h'])
j=0
for i, value in time.items():

    for filename in os.listdir('.'):
        if fnmatch.fnmatch(filename, '*71*with water*{}*corrected*.txt'.format(time[i])):
            df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False,  encoding= 'unicode_escape')
            Re = df['Re(Z)'].values
            Im = df['Im(Z)'].values
            ax6.scatter(Re, Im, color=palette[j],label = '{}'.format(time[i]), marker='o',s=ms,linewidth=0.5)
            j=j+1


ax6.set_ylim(0,0.12) 
ax6.set_xlim(0,0.40)   
ax6.set_title('MEA071' , fontsize=fs)      
#ax1.set_aspect('equal')
ax6.tick_params( labelsize=ls)
ax6.set_xlabel('Re(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax6.set_ylabel('-Im(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax6.legend([ '18h', '24h','69h', '94h','191h','213h','238h'],loc='upper left',ncol=4,columnspacing=1, fontsize=small, labelspacing=0.2,handletextpad=0.1)

#handles, labels = ax6.get_legend_handles_labels()
#order = [0,4,5,1,2,3]
#ax6.legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc='upper left',ncol=3,columnspacing=1, fontsize=small, labelspacing=0.2,handletextpad=0.1)

ax6.tick_params( labelsize=ls)



##################################################################################################################################
########################################################################################################  
   ############################ mea 71 - ax7 - 6 files - wo water      
    
palette=sns.color_palette("RdBu_r",6)
time = pd.Series([ '18h', '69h', '94h','191h','213h','238h'])
j=0
for i, value in time.items():

    for filename in os.listdir('.'):
        if fnmatch.fnmatch(filename, '*71*wo water*{}*corrected*.txt'.format(time[i])):
            df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False,  encoding= 'unicode_escape')
            Re = df['Re(Z)'].values
            Im = df['Im(Z)'].values
            ax7.scatter(Re, Im, color=palette[j],label = '{}'.format(time[i]), marker='o',s=ms,linewidth=0.5)
            j=j+1



    
ax7.set_ylim(0,0.12)  
ax7.set_xlim(0,0.40) 
ax7.set_title('MEA071, no water' , fontsize=fs) 
#ax2.set_aspect('equal')      
ax7.set_xlabel('Re(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax7.set_ylabel('-Im(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax7.legend([ '18h', '69h', '94h','191h','213h','238h'], loc="upper left",ncol=3, columnspacing=1, fontsize=small,labelspacing=0.2, handletextpad=0.1)

#handles, labels = ax7.get_legend_handles_labels()
#order = [0,4,5,1,2,3]
#ax7.legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc="upper left", ncol=3, columnspacing=1, fontsize=small,labelspacing=0.2, handletextpad=0.1)

ax7.tick_params( labelsize=ls)
#sns.set_palette("RdBu_r", 7)
 
ax7.tick_params( labelsize=ls)
  