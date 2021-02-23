import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as ani

def diffusion_FTCS(dt,dx,T,L,Ad,F0):
    dt = float (dt)
    dx = float (dx)
    Ad = float (Ad)
    L = float (L)
    F0 = float (F0)
    T = float (T)
    a = Ad*dt/dx**2 
    x = np.arange(0,L+dx,dx) 
    t = np.arange(0,T+dt,dt)
    r = len(t)
    c = len(x)
    F = np.zeros([r,c])
    F[:,0] = F0
    for n in range(0,r-1): # time
        for j in range(1,c-1): # space
            F[n+1,j] = F[n,j] + a*(F[n,j-1] - 2*F[n,j] + F[n,j+1]) 
    
    plt.figure(figsize=(7,5))
    plot_times = np.arange(0.2,1.0,0.05)
    for t in plot_times:
        plt.plot(x,F[int(t/dt),:],'Blue',label='model numerik')
        if t==0.2:
            plt.legend(fontsize=10)
    plt.xlabel('Jarak (m)',fontsize=10)
    plt.ylabel('Konsentrasi (g/L)',fontsize=10)
    plt.axis([0,L,0,F0])
    plt.grid(True, which='both')
    plt.title('Grafik Pemodelan Difusi 1 Dimensi Metode FTCS \n Laju Konsentrasi Polutan dalam Meter')

    x_data = []
    y_data = []

    fig, ax = plt.subplots()
    ax.set_xlim(0, L)
    ax.set_ylim(0, F0)
    line, = ax.plot(0, 0)

    def animation_frame(i):
        x_data.append(i)
        y_data.append(i)
        line.set_xdata(x_data)
        line.set_ydata(y_data)
        return line,1

    anime = ani.FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 10, 0.1), interval=10)
    writer = ani.PillowWriter(fps=30) 
    jelly = "static/hasil/im.gif"
    anime.save(jelly, writer=writer)
    return jelly


#diffusion_FTCS(4, 2, 1, 3, 5, 8)