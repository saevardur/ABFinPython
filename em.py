# Euler-Maruyama
import numpy as np
import matplotlib.pyplot as plt
import math
import random
 
tBegin=0
tEnd=2
dt=.00001
 
t = np.arange(tBegin, tEnd, dt)
N = t.size 
IC=0
theta=1
mu=1.2
sigma=0.3
 
sqrtdt = math.sqrt(dt)
y = np.zeros(N)
y[0] = IC
for i in xrange(1,N):
    y[i] = y[i-1] + dt*(theta*(mu-y[i-1])) + sigma*sqrtdt*random.gauss(0,1)
 
ax = plt.subplot(111)
ax.plot(t,y)
plt.show()

#####################

import numpy as np 
import matplotlib.pyplot as plt 
np.random.seed(100)  
 
gamma=2; mu=1; Xzero=1 
T=1; N=2**8; dt = float(T)/N 
t=np.linspace(0,T,N+1)  
 
dW=np.sqrt(dt)*np.random.randn(1,N) 
W=np.cumsum(dW)  
 
Xtrue=Xzero*np.exp((gamma-0.5*mu**2)*t[1:]+mu*W); Xtrue=np.insert(Xtrue,0,Xzero) 
ax=plt.subplot(111) 
ax.plot(t,Xtrue)  
 
R=4; Dt=R*dt; L=float(N)/R 
Xem=np.zeros(L+1); Xem[0] = Xzero  
 
for j in xrange(1,int(L)+1): 
    Winc=np.sum(dW[0][range(R*(j-1),R*j)]) 
    Xem[j] = Xem[j-1] + Dt*gamma*Xem[j-1] + mu*Xem[j-1]*Winc  
 
emerr=np.abs(Xem[-1]-Xtrue[-1]) 
print("Error at endpoint: ", emerr)  
 
ax.plot(np.linspace(0,T,L+1),Xem,'r--*') 
ax.legend(("exact","em"),loc=2) 
plt.show() 

##################
def EulerMaruyama(xstart, ystart, xfinish, nsteps, f1, f2): 
    sol = [ystart] 
    xvals = [xstart] 
    h = N((xfinish-xstart)/nsteps) 
    for step in range(nsteps): 
        sol.append(sol[-1] + h*f1(sol[-1]) + h^(.5)*f2(sol[-1])*normalvariate(0,1)) 
        xvals.append(xvals[-1] + h) 
    return zip(xvals,sol)
    
out = Graphics()
save(out,'temp')
@interact
def EulerMaruyamaExample(mu = slider(srange(0,10,.1),default=2.0),
                        sigma = slider(srange(0,10,.1),default=0.5),
                        plots_at_a_time = slider(range(1,100),default=10), 
                        number_of_steps = slider(range(1,1000),default=100), 
                        clear_plot = checkbox(True), 
                        auto_update=False):
    html('<center>Example of the Euler-Maruyama method applied to<br>the stochastic differential equation for geometric Brownian motion</center>')
    html('<center>$S = S_0 + \int_0^t \mu S dt + \int_0^t \sigma S dW$</center>')
    emplot = list_plot(EulerMaruyama(0,1,1,number_of_steps,lambda x: mu*x,lambda x:sigma*x),plotjoined=True)
    for i in range(1,plots_at_a_time):
        emplot = emplot + list_plot(EulerMaruyama(0,1,1,100,lambda x: mu*x,lambda x:sigma*x),plotjoined=True)
    if clear_plot:
        out = emplot
        save(out,'temp')
    else:
        out = load('temp')
        out = out + emplot
        save(out,'temp')
    show(out, figsize = [8,5])