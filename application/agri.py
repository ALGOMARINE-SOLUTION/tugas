
import numpy as np
from matplotlib import pyplot as plt

def OlahDataAdveksi1D(L, T, dt, u, dx, angkaindices0, angkaindices1): 
 indices0=[angkaindices0]
 indices1=[angkaindices1]
 if (angkaindices0 >= 1 and angkaindices0 <= int(L//dx)) and (angkaindices1 >= 1 and angkaindices0 <= int(T//dx)):
    Mmax = int(L/dx)
    Nmax = int(T/dt)
    
    F0 = np.ones(Mmax)
    F = np.zeros(Mmax) 
    hasil = np.zeros((Nmax, Mmax))
    
    for j in range (1, Nmax):
        F0[23]=50
        for i in range (1, (Mmax-1)):
            F[i]=F0[i]-((u*dt/(2*dx))*(F0[i+1]-F0[i-1]))
            
        F[0]=F[1]
        F[Mmax-1]=F[Mmax-2]
        F[23]=50
        
        hasil [j]=F
        
        for i in range (1, Mmax):
            F0[i]=F[i]      


    fig1, ax1 = plt.subplots(figsize=(12,8))
    for i in indices0:
            line, = ax1.plot(hasil[:,i-1], label=f'n={i}')
            ax1.legend()

            ax1.set(xlabel='Waktu', ylabel='Konsentrasi',
                    title='PERUBAHAN KONSENTRASI POLUTAN VS WAKTU METODE FTCS CONTINYU')
            ax1.grid()

    fig2, ax2 = plt.subplots(figsize=(12,8))
    for i in indices1:
            line, = ax2.plot(hasil[i-1], label=f't={i}')
            ax2.legend()

            ax2.set(xlabel='Ruang', ylabel='Konsentrasi',
                    title='PERUBAHAN KONSENTRASI POLUTAN VS RUANG METODE FTCS CONTINYU')
            ax2.grid()
        
    jelly = "static/hasil/hell2.png"
    plt.savefig(fname=jelly ,format='png',dpi=900,transparent=False)
    return jelly
 else:
     return "indexnya kelebihannn"
     


    
#print('Indeks Grafik vs Waktu')
#indices0 = [int(x) for x in input(f"Index berapa saja yang ingin ditampilkan? (1<=index<={int(L//dx)}, bisa lebih dari satu)\n>>> ").split(' ')]
#print('\nIndeks Grafik vs Ruang')
#indices1 = [int(x) for x in input(f"Index berapa saja yang ingin ditampilkan? (1<=index<={int(T//dt)}, bisa lebih dari satu)\n>>> ").split(' ')]

#print(OlahDataAdveksi1D(8, 9, 1, 9, 1, 1, 1))

    