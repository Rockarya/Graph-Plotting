import math
import random
import matplotlib.pyplot as plt

sim=2000        #number of times we have to do simulation
n=100           #number of steps taken by drunken

def comb(n,r):               #combination function nCr
    return math.factorial(n)/(math.factorial(r) * math.factorial(n-r))


#Plot for Probability that drunken lands on origin after N steps i.e P(N) vs. N
x=[]
for i in range(n):          #number of steps the drunken will take
    c=0
    for j in range(sim):    #we will do simulations sim times and value of c/sim will tell us the probability of drunken to land at origin after i steps
        pos=0
        for k in range(i):
            pos+=random.choice([-1,1])
        if pos==0:
            c+=1
    x.append(c/sim)

plt.plot(range(n),x, color='blue' , label='Computational Plot')
plt.plot(range(n),[comb(k,k/2)/2**(k) if k%2==0 else 0 for k in range(n)], color='red' , label='Analytical Plot')
plt.xlabel('N')
plt.ylabel('P(N)')
plt.title('Probability that drunken lands at origin after N steps')
plt.legend()
plt.show()