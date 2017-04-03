from sympy import liealgebras
from liealgebras.SU import is_SU

#This module will take some Lie group, and, if it is possible, search
#for mainfold for it

def find_mainfold(matr, matr_size, matr_number):
    su_flag=1
    for i in range(matr_number):
        su_flag=su_flag*is_SU(matr[i],matr_size)
    if (su_flag==0):
        print('SU(',matr_size,')')  
    else:
        print('No mainfold was found')
        
#Example no. 1
#We will find mainfold for some points we have
find_mainfold([[[0,1],[1,0]],[[0,0+1j],[0+1j,0]]],2,2)
