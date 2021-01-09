import math
import random
import matplotlib.pyplot as plt

sim=2000        #number of times we have to do simulation
n=100           #number of steps taken by drunken

def comb(n,r):               #combination function nCr
    return math.factorial(n)/(math.factorial(r) * math.factorial(n-r))


#Plot for Mean Squared Displacement of drunken after N steps i.e. Mean Squared Displacement vs. N
x=[]
for i in range(n):          #number of steps the drunken will take
    c=0
    for j in range(sim):   
        pos=0
        for k in range(i):
            pos+=random.choice([-1,1])
        c+=pos*pos
    x.append(c/sim)

plt.plot(range(n),x, color='blue' , label='Computational Plot')
plt.plot(range(n),range(n), color='red' , label='Analytical Plot') 
plt.xlabel('N')
plt.ylabel('Mean Squared Displacement')
plt.title('Mean Squared Displacement of drunken after N steps')
plt.legend()
plt.show()