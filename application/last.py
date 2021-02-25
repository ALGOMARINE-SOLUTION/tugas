import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def TSdiagram(fileawal):
   df=pd.read_excel(fileawal)
   
   def _dens0(S,T):
     a0 = 999.842594
     a1 =   6.793952e-2
     a2 =  -9.095290e-3
     a3 =   1.001685e-4
     a4 =  -1.120083e-6
     a5 =   6.536332e-9
     
     b0 =   8.24493e-1
     b1 =  -4.0899e-3
     b2 =   7.6438e-5
     b3 =  -8.2467e-7
     b4 =   5.3875e-9
     
     c0 =  -5.72466e-3
     c1 =   1.0227e-4
     c2 =  -1.6546e-6
     
     d0 =   4.8314e-4
     
     SMOW = a0 + (a1 + (a2 + (a3 + (a4 + a5*T)*T)*T)*T)*T
     
     RB = b0 + (b1 + (b2 + (b3 + b4*T)*T)*T)*T
     RC = c0 + (c1 + c2*T)*T
     
     return SMOW + RB*S + RC*(S**1.5) + d0*S*S
     
   def _seck(S, T, P=0):
     h0 =  3.239908
     h1 =  1.43713E-3
     h2 =  1.16092E-4
     h3 = -5.77905E-7
     AW = h0 + (h1 + (h2 + h3*T)*T)*T
       
     k0 =  8.50935E-5
     k1 = -6.12293E-6
     k2 =  5.2787E-8
     BW = k0 + (k1 + k2*T)*T
       
     e0 = 19652.21
     e1 = 148.4206
     e2 = -2.327105
     e3 =  1.360477E-2
     e4 = -5.155288E-5
     KW = e0 + (e1 + (e2 + (e3 + e4*T)*T)*T)*T
       
     SR = S**0.5
       
     i0 =  2.2838E-3
     i1 = -1.0981E-5
     i2 = -1.6078E-6
     j0 =  1.91075E-4
     A  = AW + (i0 + (i1 + i2*T)*T + j0*SR)*S
       
     f0 = 54.6746
     f1 = -0.603459
     f2 =  1.09987E-2
     f3 = -6.1670E-5
     g0 =  7.944E-2
     g1 =  1.6483E-2
     g2 = -5.3009E-4
     K0 = KW + (f0 + (f1 + (f2 + f3*T)*T)*T  \
          + (g0 + (g1 + g2*T)*T)*SR)*S
       
     m0 = -9.9348E-7
     m1 =  2.0816E-8
     m2 =  9.1697E-10
     B = BW + (m0 + (m1 + m2*T)*T)*S
       
     K = K0 + (A + B*P)*P
     return K
       
   def dens(S, T, P=0):
       P = 0.1*P
       return _dens0(S,T)/(1 - P/_seck(S,T,P))
         
   def svan(S,T,P=0):
       return 1.0/dens(S,T,P) - 1.0/dens(35,0,P)
           
   def sigma(S,T,P=0):
       return dens(S,T,P) - 1000.0
           
   def drhodt(S,T,P=0):
       a1 =  6.793952e-2
       a2 = -1.819058e-2
       a3 =  3.005055e-4
       a4 = -4.480332e-6
       a5 =  3.268166e-8
               
       b1 = -4.0899e-3
       b2 =  1.52876e-4
       b3 = -2.47401e-6
       b4 =  2.155e-8
               
       c1 =  1.0227e-4
       c2 = -3.3092e-6
               
       e1 =  148.4206
       e2 = -4.65421
       e3 =  4.081431e-2
       e4 = -2.0621152e-4
               
       f1 = -0.603459
       f2 =  2.19974e-2
       f3 = -1.8501e-4
               
       g1 =  1.6483e-2
       g2 = -1.06018e-3
               
       h1 =  1.43713e-3
       h2 =  2.32184e-4
       h3 = -1.733715e-6
               
       i1 = -1.0981e-5
       i2 = -3.2156e-6
               
       k1 = -6.12293e-6
       k2 =  1.05574e-7
               
       m1 = 2.0816e-8
       m2 = 1.83394e-9
               
       P = P/10.0
               
       DSMOV = a1 + (a2 + (a3 + (a4 + a5*T)*T)*T)*T
       DRHO0 = DSMOV + (b1 + (b2 + (b3 + b4*T)*T)*T)*S + (c1 + c2*T)*S**1.5
               
       DAW = h1 + (h2 + h3*T)
       DA  = DAW + (i1 + i2*T)*S
               
       DBW = k1 + k2*T
       DB  = DBW + (m1 + m2*T)*S
               
       DKW = e1 + (e2 + (e3 + e4*T)*T)*T
       DK0 = DKW + (f1 + (f2 + f3*T)*T)*S + (g1 + g2*T)*S**1.5
       DK  = DK0 + (DA + DB*P)*P
               
       K    = _seck(S,T,P)
       RHO0 = _dens0(S,T)
       denom  = 1. - P/K
       return (DRHO0 * denom - RHO0 * P * DK / (K*K)) / (denom*denom)
               
   def alpha(S,T,P=0):
       ALPHA = - drhodt(S,T,P) / dens(S,T,P)
       return ALPHA
                 
   def drhods(S,T,P=0):
       b0 =  8.24493e-1
       b1 = -4.0899e-3
       b2 =  7.6438e-5
       b3 = -8.2467e-7
       b4 =  5.3875e-9
                   
       c0 = -5.72466e-3
       c1 =  1.0227e-4
       c2 = -1.6546e-6
                   
       d0 =  9.6628e-4
                   
       f0 = 54.6746
       f1 = -0.603459
       f2 =  1.09987e-2
       f3 = -6.1670e-5
       
       g0 =  7.944e-2
       g1 =  1.6483e-2
       g2 = -5.3009e-4
                   
       i0 =  2.2838e-3
       i1 = -1.0981e-5
       i2 = -1.6078e-6
                   
       j0 =  2.866125e-4
                   
       m0 = -9.9348e-7
       m1 =  2.0816e-8
       m2 =  9.1697e-10
                   
       P = 0.1*P # Convert to bar
       DRHO0 = b0 + T*(b1 + T*(b2 + T*(b3 + T*b4))) +   \
               1.5*S**0.5*(c0 + T*(c1 + T*c2)) + S*d0
       DK0 = f0 + T*(f1 + T*(f2 + T*f3)) +              \
             1.5*S**0.5*(g0 + T*(g1 + T*g2))
       DA = i0 + T*(i1 + T*i2) + j0*S**0.5
       DB = m0 + T*(m1 + T*m2)
       DK = DK0 + P*(DA + P*DB)
       RHO0 = _dens0(S,T)
       K = _seck(S,T,P)
       denom  = 1. - P/K
       DRHO = (DRHO0 * denom - RHO0 * P * DK / (K*K)) / (denom*denom)
       return DRHO
                   
   def beta(S,T,P=0):
       BETA = drhods(S,T,P) / dens(S,T,P)
       return BETA
                     
   T=df[['Temperature']]
   S=df[['Salinity']]
   #P=df[['Pressure']]
   S =np.array(S)
   T =np.array(T)
   mint=np.min(df['Temperature'])
   maxt=np.max(df['Temperature'])
   mins=np.min(df['Salinity'])
   maxs=np.max(df['Salinity'])
   tempL = np.linspace(mint-0.7,maxt+0.3)
   salL = np.linspace(mins-0.7,maxs+0.3)
   X, Y = np.meshgrid(tempL,salL)
   sigma_theta = sigma(Y,X,P=0)
   cnt = np.linspace(sigma(S,T,P=0).min(), sigma(S,T,P=0).max(),200)
   dens = _dens0(32,28)
   dens0 = _dens0(X,Y)
   fig,ax=plt.subplots(figsize=(10,10))
   cs=ax.contour(Y, X, sigma_theta, colors='grey', zorder=10)
   cl=plt.clabel(cs,fontsize=10,inline=False,fmt='%.1f')
   sc=plt.scatter(df['Salinity'],df['Temperature'],s=10)
   cb=plt.colorbar(sc)
   ax.set_xlabel('Salinity [$‰$]')
   ax.set_ylabel('Temperature[$^\circ$C]')
   ax.set_title('Temperature and salinity (T-S) Diagram',fontsize=20, fontweight='bold')
   ax.xaxis.set_major_locator(MaxNLocator(nbins=20))
   ax.yaxis.set_major_locator(MaxNLocator(nbins=40))
   ax.tick_params(direction='out')
   cb.ax.tick_params(direction='out')
   cb.set_label('Density[Kg/m$^{-3}$]')
   plt.tight_layout()
   hasilfile = 'static/ts_diagram.png'
   plt.savefig(fname= hasilfile ,format='png',dpi=900,transparent=False)
   return hasilfile
