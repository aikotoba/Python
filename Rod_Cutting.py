# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:11:28 2018

@author: aikotoba
"""

# solve rod-cutting problem


def Rod_Cut( price=[], length=int):

    v = [0]
    I=[]
    c=list([0])*length
    for i in range(1,length+1):
        
        L=list()
        
        for j in range(i):
            
            L.append(price[j]+v[i-j-1])
        
        a=max(L)
        v.append(a) 
        I0=L.index(a)+1
        I.append(I0)
   

    while length>0:
        
        c[I[length-1]-1]+=1
        length=length-I[length-1]
       

    return v,c  
'''v is value function 
The index of c plus 1 is the length I want to cut,and the corresponding value
is the cutting time(s).'''

    
    
    
    
    




    
    

            





        


















