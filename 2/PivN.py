import random
import matplotlib.pyplot as plt

n=2000         #number of pebbles
r=1.0

val=[]
for i in range(n):
    c=0
    for j in range(i+1):        
        x=r*random.random()
        y=r*random.random()
        if x*x + y*y <= r*r:
            c+=1
    pi=4.0 * (c/(i+1))          # There can't be 0 pebbles thrown case that's why (i+1) is written instead of i.Also preventing divison by 0.
    val.append(pi)

plt.plot(range(n),val, color='blue' , label='Computational Plot')
plt.plot(range(n),[3.141592653589793238]*n , color='red', label='Analytical Plot')
plt.xlabel('Number of Pebbles')
plt.ylabel('Value of Pi')
plt.title('Finding Value of Pi')
plt.legend()
plt.show()
