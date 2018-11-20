# -*- coding: utf-8 -*-
"""
Created on Fri May 11 12:25:58 2018
RSA d finder
@author: future
"""
p = int(input("Enter the value of p : "))
q = int(input("Enter the value of q : "))
phi = (p-1)*(q-1)
e = int(input("Enter the value of e : "))
d = []
for k in range(0,e):
    tmp = (1+(k*phi))/e
    d.append(tmp)
x = 0
for i in range(0,e) :
     if (int(d[i]-0.001) == int(d[i])):
        pass
     else:
        x = d[i]
        break

print(d)
print("d is "+str(x) + " at k = " + str(i))
print('phi = ',phi)