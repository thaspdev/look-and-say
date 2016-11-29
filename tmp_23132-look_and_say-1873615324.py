#!/usr/bin/python3

from time import time

n_array=[1]
time_array=[]
print("u0 =",n_array[0])
start = time()
for j in range(99):
    digits_array,weights_array=[],[]
    count=1
    
    for z in range(1,len(n_array)):
        if n_array[z]==n_array[z-1]:
            count+=1       
        else:
            digits_array.append(n_array[z-1])
            weights_array.append(count)
            count=1
    digits_array.append(n_array[len(n_array)-1])
    weights_array.append(count)
    n_array = []
    for m in range(len(digits_array)):
        n_array.append(weights_array[m])
        n_array.append(digits_array[m])
    num = 0
    for y in range(len(n_array)):
        num+=n_array[len(n_array)-y-1]*(10**y)
    #jmax = j
    time_array.append(time()-start)
    #print(j,"done")
    #print("...")
    print("u"+str(j),"=",num)
print("Time taken for calculation :",time_array)
        
        
