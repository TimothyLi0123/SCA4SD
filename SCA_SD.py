#!/usr/bin/env python
# coding: unicode_escape

import csv
import numpy.matlib 
import numpy as np
import pandas as pd
import copy
import time

from input_file import *
from func import *

time_stamp = int(time.time())

###############################################################
## Function: Transformation of equation matrix to 0-1 matrix ##
###############################################################
num_all = len(Mtx_Al_eq)
Mtx_Al = np.matrix(np.where(Mtx_Al_eq != '0', 1, 0))
output = pd.DataFrame(Mtx_Al)
output.to_csv('output/' + str(time_stamp) + '_Matrix_A.csv') 

##############################################################################
## Function: Transitive closure/reachability determination (Floyd-Warshall) ##
##############################################################################
Mtx_R = copy.copy(Mtx_Al)
for k in range(num_all):
    for i in range(num_all):
        for j in range(num_all):
            if (Mtx_R[i,k] == 1 & Mtx_R[k,j] == 1):
                Mtx_R[i,j] = 1
                
output = pd.DataFrame(Mtx_R)
output.to_csv('output/' + str(time_stamp) + '_Matrix_R.csv') 

############################################
## Function: Control input identification ##
############################################
PorC = [-1]*num_all
control_matrix = np.matrix(np.zeros((num_all,num_all)))

for k in range(num_all):                                 # k is the variable in discussion
    if k in ind_stock:                                   # if k is a stock, continue
        continue
        
    PorC_i = [-1234567]*len(ind_stock) 
    
    for i in ind_stock:
        if Mtx_R[k,i] == 0:                              # if i is not accessible from k; continue
            control_matrix[k,i] = 0                      # k cannot access i
            PorC_i[i] = 0
            continue
            
        local_C = Mtx_Al[k,i]
        
        PorC_i_temp = 0
        for j in ind_stock:
            if Mtx_Al_eq_type[k,i] == 'd':
                partial = abs(sympy.diff(Mtx_Al_eq[k,i],variable_name[j]))
            if Mtx_Al_eq_type[k,i] == 'o':
                print('Error: Stock variables should have differential equations as input.')
           
            PorC_i_temp = PorC_i_temp + partial
        
        if PorC_i_temp  == 0:
            PorC_i_temp = int(0)
        PorC_i[i] = PorC_i_temp       
        
        if (PorC_i_temp == 0) & (local_C != 0):          # if LocalC condition satisfied
            control_matrix[k,i] = 1                      # k is control input for i
        else:
            control_matrix[k,i] = -1                     # k is parameter for i
        
    PorC[k] = sum(PorC_i) 
    if PorC[k] == 0:                                     # k is global control input
        for i in ind_stock:
            if Mtx_R[k,i] == 1:
                control_matrix[k,i] = 1                  # it is control input for all its accessible stocks

output = pd.DataFrame(control_matrix.astype(int))
output.to_csv('output/' + str(time_stamp) + '_Control_matrix.csv')        
output = pd.DataFrame(PorC)
output.to_csv('output/' + str(time_stamp) + '_PorC.csv')

#######################################
## Function: Dilation identification ##
#######################################
global_control_input = [k for k in range(len(PorC)) if PorC[k] == 0]
dilation_record = [-1]*num_all

for k in global_control_input:
    
    k_accessible = [i for i in range(len(ind_stock)) if Mtx_R[k,i] == 1]
    all_s = list(powerset(k_accessible))
    dilation_flag = 0
    all_s = all_s[1:]
    
    for kk in range(len(all_s)):
        s_temp = all_s[kk]
        t_temp = []
        for kkk in range(len(k_accessible)):
            if sum([Mtx_Al[k_accessible[kkk],kkkk] for kkkk in s_temp]) > 0:
                t_temp.append(k_accessible[kkk])

        if len(t_temp) < len(s_temp):
            dilation_flag = 1
            break
            
    dilation_record[k] = dilation_flag
    
output = pd.DataFrame(dilation_record)
output.to_csv('output/' + str(time_stamp) + '_Dilation_record.csv')
print('Finished. Please see output files in the folder.')