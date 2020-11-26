import numpy as np 
import matplotlib.pyplot as plt 


def euler(u1_initial,u2_initial,u3_initial,u4_initial,u5_initial,u6_initial) :

  tf = 3 
  dt = 0.22 #@param {type:"slider", min:0, max:1, step:0.01}
  t= np.arange(0,tf,dt)
  n=len(t)

  u1 = np.zeros(n)
  u2 = np.zeros(n)
  u3 = np.zeros(n)
  u4 = np.zeros(n)
  u5 = np.zeros(n)
  u6 = np.zeros(n)

  u1[0]= u1_initial
  u2[0]= u2_initial
  u3[0]= u3_initial
  u4[0]= u4_initial
  u5[0]= u5_initial
  u6[0]= u6_initial  
  for i in range(1,n):

    u1[i] = (c_1_2*(u2[i-1]-u1[i-1]))*dt + u1[i-1]

    u2[i] = ((c_1_2*(u1[i-1]-u2[i-1]))+
            (c_2_3*(u3[i-1]-u2[i-1]))+
            (c_2_5*(u5[i-1]-u2[i-1]))+
            (c_2_6*(u6[i-1]-u2[i-1]))
            )*dt + u2[i-1]

    u3[i] = ((c_2_3*(u2[i-1]-u3[i-1]))+
            (c_3_4*(u4[i-1]-u3[i-1]))
            )*dt + u3[i-1]

    u4[i] = ((c_3_4*(u3[i-1]-u4[i-1]))+
            (c_4_5*(u5[i-1]-u4[i-1]))
            )*dt + u4[i-1]

    u5[i] = ((c_2_5*(u2[i-1]-u5[i-1]))+
            (c_4_5*(u4[i-1]-u5[i-1]))+
            (c_5_6*(u6[i-1]-u5[i-1]))
            )*dt + u5[i-1]

    u6[i] = ((c_2_6*(u1[i-1]))+
            (c_5_6*(u5[i-1]-u6[i-1]))
            )*dt + u6[i-1]
          
  #plotting the
  plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
  plt.subplot(2,1,1)
  plt.plot(t,u1,'r',label='U1',linewidth=1.0)
  plt.plot(t,u2,'b',label='U2',linewidth=1.0)
  plt.plot(t,u3,'g',label='U3',linewidth=1.0)
  plt.plot(t,u4,'c',label='U4',linewidth=1.0)
  plt.plot(t,u5,'k',label='U5',linewidth=1.0)
  plt.plot(t,u6,'y',label='U6',linewidth=1.0)
  plt.legend(loc='best')