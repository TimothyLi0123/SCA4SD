import csv
import numpy.matlib 
import numpy as np
import sympy

variable_name = ['SS','SL','SLT','AL','SAT','SLAT','S_star','SL_star']
ind_stock = [0,1]

Mtx_Al_eq = np.matrix([['-1/SLT','1/AL','SS/SLT**2','-SL/AL**2','0','0','0','0'], 
                          ['1/SLT-1/SAT','-1/SLAT-1/AL','-SS/SLT**2','SL/AL**2','(SS-S_star)/SAT**2','(SL-SL_star)/SLAT**2','-1/SAT**2','-1/SLAT**2'], 
                          ['0','0','0','0','0','0','0','0'], 
                          ['0','0','0','0','0','0','0','0'], 
                          ['0','0','0','0','0','0','0','0'], 
                          ['0','0','0','0','0','0','0','0'], 
                          ['0','0','0','0','0','0','0','0'], 
                          ['0','0','0','0','0','0','0','0']])
Mtx_Al_eq_type = np.matrix([['d','d','d','d','d','d','d','d'], 
                           ['d','d','d','d','d','d','d','d'], 
                           ['o','o','o','o','o','o','o','o'], 
                           ['o','o','o','o','o','o','o','o'], 
                           ['o','o','o','o','o','o','o','o'], 
                           ['o','o','o','o','o','o','o','o'], 
                           ['o','o','o','o','o','o','o','o'], 
                           ['o','o','o','o','o','o','o','o']])

Mtx_Al_eq = Mtx_Al_eq.transpose()
Mtx_Al_eq_type = Mtx_Al_eq_type.transpose()

symbol_string = ''
for i in range(len(variable_name)):
    symbol_string = symbol_string + str(variable_name[i]) + ' '
sympy.symbols(symbol_string[:-1])