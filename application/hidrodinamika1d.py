import matplotlib.pyplot as plt
import numpy as np
#--------------------------------------------------------------------------------------------------   
#                                           Fungsi Utama
#--------------------------------------------------------------------------------------------------   
def OlahDataHD1D(p, T, A, D, dt, To, dx, indices0, indices1):
    if (indices0 >= 1 and indices0 <= int(p//dx)) and (indices1 >= 1 and indices0 <= int(T//dt)):
        g = 9.8
        pi = np.pi
        C = np.sqrt(g*D)
        s = 2*pi/To
        L = C*To
        k = 2*pi/L
        Mmax = int(p//dx)
        Nmax = int(T//dt)

        zo = [None for _ in range(Mmax)]
        uo = [None for _ in range(Mmax)]

        hasilu = [None for _ in range(Nmax)]
        hasilz = [None for _ in range(Nmax)]

        for num in range(1, Mmax+1):
            zo[num-1] = A*np.cos(k*(num)*dx)
            uo[num-1] = A*C*np.cos(k*((num)*dx+(0.5)*dx))/(D+zo[num-1])
        for val in range(1, Nmax+1):
            zb = [None for _ in range(Mmax)]
            ub = [None for _ in range(Mmax)]
            zb[0] = A*np.cos(s*(val)*dt)
            ub[-1] = A*C*np.cos(k*L-s*(val)*dt)/(D+zo[-1])
            for num in range(1, Mmax):
                ub[num-1] = uo[num-1]-g*(dt/dx)*(zo[num]-zo[num-1])
            for num in range(2, Mmax+1):
                zb[num-1] = zo[num-1]-(D+zo[num-1])*(dt/dx)*(ub[num-1]-ub[num-2])
                hasilu[val-1] = ub
                hasilz[val-1] = zb
            for num in range(0, Mmax):
                uo[num] = ub[num]
                zo[num] = zb[num]
        #------------------------------------------------------------------------------------  
        #                                           PEMBUATAN GRAFIK
        #------------------------------------------------------------------------------------   
        def rand_col_hex_string():
            return f'#{format(np.random.randint(0,16777215), "#08x")[2:]}'

        hasilu_np = np.array(hasilu)
        hasilz_np = np.array(hasilz)

        fig0, ax0 = plt.subplots(figsize=(12,8))
        for i in indices0:
            col0 = rand_col_hex_string()
            line, = ax0.plot(hasilu_np[:,i-1], c=col0, label=f'n={i}')
            ax0.legend()

            ax0.set(xlabel='Waktu', ylabel='Kecepatan',
                    title='Perubahan Kecepatan Massa Air Dalam Grid Tertentu di sepanjang Waktu')
            ax0.grid()

        fig1, ax1 = plt.subplots(figsize=(12,8))
        for i in indices0:
            col1 = rand_col_hex_string()
            line, = ax1.plot(hasilz_np[:,i-1], c=col1, label=f'n={i}')
            ax1.legend()

            ax1.set(xlabel='Waktu', ylabel='Elevasi',
                    title='Perubahan Elevasi Permukaan Air Dalam Grid Tertentu di sepanjang Waktu')
            ax1.grid()

        fig2, ax2 = plt.subplots(figsize=(12,8))
        for i in indices1:
            col2 = rand_col_hex_string()
            line, = ax2.plot(hasilu_np[i-1], c=col2, label=f't={i}')
            ax2.legend()

            ax2.set(xlabel='Grid', ylabel='Kecepatan',
                    title='Perubahan Kecepatan Massa Air Dalam Waktu Tertentu di sepanjang Grid')
            ax2.grid()

        fig3, ax3 = plt.subplots(figsize=(12,8))
        for i in indices1:
            col3 = rand_col_hex_string()
            line, = ax3.plot(hasilz_np[i-1], c=col3, label=f't={i}')
            ax3.legend()

            ax3.set(xlabel='Grid', ylabel='Elevasi',
                    title='Perubahan Elevasi Permukaan Air Dalam Waktu Tertentu di sepanjang Grid')
            ax3.grid()
        boonglagi = 'static/HasilHidro.png'
        plt.savefig(fname= boonglagi)
        return boonglagi
    else: 
        return '404'
#----------------------------------------------------------------------
#                           Akhir dari Fungsi
#----------------------------------------------------------------------
#----------------------------------------------------------------------
#                            Contoh Input
#----------------------------------------------------------------------
#p, T, A, D, dt, To, dx = [float(x) for x in input('masukkan 7 nilai untuk: p, T, A, D, dt, To, dx : ').split(' ')]
#print('Perubahan Elevasi Permukaan Air Dalam Waktu Tertentu di sepanjang Grid dan Perubahan Elevasi Permukaan Air Dalam Grid Tertentu di sepanjang Waktu')
#indices0 = [int(x) for x in input(f"Index berapa saja yang ingin ditampilkan? (1<=index<={int(p//dx)}, bisa lebih dari satu)\n>>> ").split(' ')]
#print('\nPerubahan Kecepatan Massa Air Dalam Waktu Tertentu di sepanjang Grid dan Perubahan Elevasi Permukaan Air Dalam Waktu Tertentu di sepanjang Grid')
#indices1 = [int(x) for x in input(f"Index berapa saja yang ingin ditampilkan? (1<=index<={int(T//dt)}, bisa lebih dari satu)\n>>> ").split(' ')]
#OlahDataHD1D(p, T, A, D, dt, To, dx, indices0, indices1)