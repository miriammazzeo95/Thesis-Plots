# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 16:01:02 2020

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
    
palette=sns.color_palette("RdBu_r",8)

for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename, '*68*wo water*1 h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False,  encoding= 'unicode_escape')
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax2.scatter(Re, Im, color=palette[0],label = '1h', marker='o',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*68*wo water*18h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax2.scatter(Re, Im, color=palette[1], label='18h', linestyle='-', marker='o',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*68*wo water*49h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax2.scatter(Re, Im, color=palette[2], label='49h', linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*68*wo water*97h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax2.scatter(Re, Im, color=palette[3], label='97h', linestyle='-', marker='*',s=ms, linewidth=0.5)
    if fnmatch.fnmatch(filename, '*68*wo water*169h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax2.scatter(Re, Im, color=palette[4], label='169h',linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*68*wo water*194h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax2.scatter(Re, Im,color=palette[5], label=' 194h', linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*68*wo water*240h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax2.scatter(Re, Im,color=palette[6], label=' 240h', linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*68*wo water*264h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax2.scatter(Re, Im,color=palette[7], label=' 264h', linestyle='-', marker='*',s=ms,linewidth=0.5)

         
ax2.set_ylim(0,0.12)  
ax2.set_xlim(0,0.40) 
ax2.set_title('MEA068, no water' , fontsize=fs) 
#ax4.set_aspect('equal')      
ax2.set_xlabel('Re(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax2.set_ylabel('-Im(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
#ax2.legend(loc='upper left', horiz = T)
handles, labels = ax2.get_legend_handles_labels()
order = [0,1,4,5,6,7,2,3]
ax2.legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc="upper left",ncol=4, columnspacing=1,handletextpad=0.1, fontsize=small, labelspacing=0.2)
# ncol=len(ax.lines)
ax2.tick_params( labelsize=ls)
#sns.set_palette("RdBu_r", 7)

    
    
    
palette=sns.color_palette("RdBu_r",10)

for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename, '*68*with water*1h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False,  encoding= 'unicode_escape')
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax1.scatter(Re, Im, color=palette[0],label = '1h', marker='o',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*68*with water*18h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax1.scatter(Re, Im, color=palette[1], label='18h', linestyle='-', marker='o',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*68*with water*27h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax1.scatter(Re, Im, color=palette[2], label='27h', linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*68*with water*49h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax1.scatter(Re, Im, color=palette[3], label='49h', linestyle='-', marker='*',s=ms, linewidth=0.5)
    if fnmatch.fnmatch(filename, '*68*with water*97h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax1.scatter(Re, Im, color=palette[4], label='97h', linestyle='-', marker='*',s=ms, linewidth=0.5)
    if fnmatch.fnmatch(filename, '*68*with water*169h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax1.scatter(Re, Im, color=palette[5], label='169h',linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*68*with water*194h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax1.scatter(Re, Im,color=palette[6], label='194h', linestyle='-', marker='*',s=ms,linewidth=0.5)
        print(filename)
    if fnmatch.fnmatch(filename, '*68*with water*218h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax1.scatter(Re, Im,color=palette[7], label='218h', linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*68*with water*264h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax1.scatter(Re, Im,color=palette[8], label='264h', linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*68*with water*336h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax1.scatter(Re, Im,color=palette[9], label='336h', linestyle='-', marker='*',s=ms,linewidth=0.5)
 
ax1.set_ylim(0,0.12)  
ax1.set_xlim(0,0.40)  
#ax4.set_aspect('equal')      
ax1.set_xlabel('Re(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax1.set_ylabel('-Im(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax1.set_title('MEA068' , fontsize=fs) 
#ax1.legend(loc='upper left')
handles, labels1 = ax1.get_legend_handles_labels()
order = [0,1,3,4,6,7,8,10,2,5]
ax1.legend([handles[idx] for idx in order],[labels1[idx] for idx in order],loc="upper left", ncol=5,columnspacing=1, fontsize=small,labelspacing=0.2, handletextpad=0.1)

ax1.tick_params( labelsize=ls)
#sns.set_palette("RdBu_r", 7) 
















palette=sns.color_palette("RdBu_r",9)

for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename, '*69*wo water*1 h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False,  encoding= 'unicode_escape')
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax4.scatter(Re, Im, color=palette[0],label = '1h', marker='o',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*69*wo water*18h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax4.scatter(Re, Im, color=palette[1], label='18h', linestyle='-', marker='o',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*69*wo water*27h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax4.scatter(Re, Im, color=palette[2], label='27h', linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*69*wo water*97h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax4.scatter(Re, Im, color=palette[3], label='97h', linestyle='-', marker='*',s=ms, linewidth=0.5)
    if fnmatch.fnmatch(filename, '*69*wo water*169h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax4.scatter(Re, Im, color=palette[4], label='169h',linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*69*wo water*194h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax4.scatter(Re, Im,color=palette[5], label='194h', linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*69*wo water*240h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax4.scatter(Re, Im,color=palette[6], label='240h', linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*69*wo water*264h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax4.scatter(Re, Im,color=palette[7], label='264h', linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*69*wo water*336h*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax4.scatter(Re, Im,color=palette[8], label='336h', linestyle='-', marker='*',s=ms,linewidth=0.5)
         
ax4.set_ylim(0,0.12)  
ax4.set_xlim(0,0.40)
ax4.set_title('MEA069, no water' , fontsize=fs) 
#ax4.set_aspect('equal')      
ax4.set_xlabel('Re(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax4.set_ylabel('-Im(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
#ax.legend(loc='upper left')
handles, labels = ax4.get_legend_handles_labels()
order = [0,1,2,3,4,5,6,7,8]
ax4.legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc="upper left", ncol=5, columnspacing=1,fontsize=small, labelspacing=0.2, handletextpad=0.1)

ax4.tick_params( labelsize=ls)
#sns.set_palette("RdBu_r", 7)

    
    
    
palette=sns.color_palette("RdBu_r",10)

for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename, '*69*with water*1 h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False,  encoding= 'unicode_escape')
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax3.scatter(Re, Im, color=palette[0],label = '1h', marker='o',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*69*with water*18h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax3.scatter(Re, Im, color=palette[1], label='18h', linestyle='-', marker='o',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*69*with water*27h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax3.scatter(Re, Im, color=palette[2], label='27h', linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*69*with water*49h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax3.scatter(Re, Im, color=palette[3], label='49h', linestyle='-', marker='*',s=ms, linewidth=0.5)
    if fnmatch.fnmatch(filename, '*69*with water*97h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax3.scatter(Re, Im, color=palette[4], label='97h', linestyle='-', marker='*',s=ms, linewidth=0.5)
    if fnmatch.fnmatch(filename, '*69*with water*169h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax3.scatter(Re, Im, color=palette[5], label='169h',linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*69*with water*194h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax3.scatter(Re, Im,color=palette[6], label='194h', linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*69*with water*218h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax3.scatter(Re, Im,color=palette[7], label='218h', linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*69*with water*264h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax3.scatter(Re, Im,color=palette[8], label='264h', linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*69*with water*336h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax3.scatter(Re, Im,color=palette[9], label='336h', linestyle='-', marker='*',s=ms,linewidth=0.5)
         
ax3.set_ylim(0,0.12)  
ax3.set_xlim(0,0.40)  
ax3.set_title('MEA069' , fontsize=fs) 
#ax4.set_aspect('equal')      
ax3.set_xlabel('Re(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax3.set_ylabel('-Im(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
#ax.legend(loc='upper left')
handles, labels = ax3.get_legend_handles_labels()
order = [0,2,3,4,5,6,7,1]
ax3.legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc="upper left", ncol=4,columnspacing=1, fontsize=small, labelspacing=0.2,handletextpad=0.1)

ax3.tick_params( labelsize=ls)
#sns.set_palette("RdBu_r", 7) 
    
    
   


















fig, [ax6, ax7] = plt.subplots(nrows=1, ncols=2, figsize=(11,4.5))
fs=15
ls=13
small=11
ms=10




###############################################################
#####    MEA RD-20-071    TR6/2    RESISTANCE=0.005382   ######
###############################################################
r= 0.005382
mea = 71


palette=sns.color_palette("RdBu_r",6)

for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename, '*71*with water*18h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False,  encoding= 'unicode_escape')
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax6.scatter(Re, Im, color=palette[0],label = '18h', marker='o',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*71*with water*24h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax6.scatter(Re, Im, color=palette[1], label='24h',  marker='o',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*71*with water*69h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax6.scatter(Re, Im, color=palette[2], label='69h', marker='o',s=ms,linewidth=0.5)   
    if fnmatch.fnmatch(filename, '*71*with water*94h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax6.scatter(Re, Im, color=palette[3], label='94h', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*71*with water*191h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax6.scatter(Re, Im, color=palette[4], label='191h', marker='*',s=ms, linewidth=0.5)
    if fnmatch.fnmatch(filename, '*71*with water*213h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax6.scatter(Re, Im, color=palette[5], label='213h', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*71*with water*238h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax6.scatter(Re, Im,color=palette[5], label='238h',  marker='*',s=ms,linewidth=0.5)
   
ax6.set_ylim(0,0.12) 
ax6.set_xlim(0,0.40)        
#ax1.set_aspect('equal')
ax6.tick_params( labelsize=ls)
ax6.set_xlabel('Re(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax6.set_ylabel('-Im(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
#ax1.legend(loc='upper left',ncol=4, fontsize=small)
handles, labels = ax6.get_legend_handles_labels()
order = [0,4,5,1,2,3]
ax6.legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc='upper left',ncol=3,columnspacing=1, fontsize=small, labelspacing=0.2,handletextpad=0.1)



palette=sns.color_palette("RdBu_r",6)

for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename, '*71*wo water*18h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False,  encoding= 'unicode_escape')
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax7.scatter(Re, Im, color=palette[0],label = '18h',linestyle='-', marker='o',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*71*wo water*69h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax7.scatter(Re, Im, color=palette[1], label='69h', linestyle='-', marker='o',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*71*wo water*94h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax7.scatter(Re, Im, color=palette[2], label='94h', linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*71*wo water*191h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax7.scatter(Re, Im, color=palette[3], label='191h', linestyle='-', marker='*',s=ms, linewidth=0.5)
    if fnmatch.fnmatch(filename, '*71*wo water*213h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax7.scatter(Re, Im, color=palette[4], label=' 213h',linestyle='-', marker='*',s=ms,linewidth=0.5)
    if fnmatch.fnmatch(filename, '*71*wo water*238h*corrected*.txt'):
        df= pd.read_csv(filename,  delimiter=';', header=0, index_col=False)
        Re = df['Re(Z)'].values
        Im = df['Im(Z)'].values
        ax7.scatter(Re, Im,color=palette[5], label=' 238h', linestyle='-', marker='*',s=ms,linewidth=0.5)
        
        
ax7.set_ylim(0,0.12)  
ax7.set_xlim(0,0.40) 
#ax2.set_aspect('equal')      
ax7.set_xlabel('Re(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
ax7.set_ylabel('-Im(z)[\u03A9\xb7cm\u00b2]', fontsize=fs)
#ax2.legend(loc="upper left", ncol=4, fontsize=small)
handles, labels = ax7.get_legend_handles_labels()
order = [0,4,5,1,2,3]
ax7.legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc="upper left", ncol=3, columnspacing=1, fontsize=small,labelspacing=0.2, handletextpad=0.1)

ax7.tick_params( labelsize=ls)
#sns.set_palette("RdBu_r", 7)
 
    
    