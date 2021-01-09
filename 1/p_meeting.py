import math
import random
import matplotlib.pyplot as plt

sim=2000        #number of times we have to do simulation
n=100           #number of steps taken by drunken

def comb(n,r):               #combination function nCr
    return math.factorial(n)/(math.factorial(r) * math.factorial(n-r))


#Plot for Probability that 2 drunken meet at same position after N steps i.e P(N) vs. N
x=[]
for i in range(n):          #number of steps the drunken will take
    c=0
    for j in range(sim):    #we will do simulations sim times and value of c/sim will tell us the probability of 2 drunken to meet at same position after traversing i steps
        pos1=0
        pos2=0
        for k in range(i):
            pos1+=random.choice([-1,1])
            pos2+=random.choice([-1,1])
        if pos1==pos2:
            c+=1
    x.append(c/sim)

plt.plot(range(n),x, color='blue' , label='Computational Plot')
plt.plot(range(n),[comb(2*k,k)/2**(2*k) for k in range(n)], color='red' , label='Analytical Plot')
plt.xlabel('N')
plt.ylabel('P(N)')
plt.title('Probability that 2 drunken meet at same position after N steps')
plt.legend()
plt.show()