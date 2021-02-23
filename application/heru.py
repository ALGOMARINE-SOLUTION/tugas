from windrose import WindroseAxes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def buat_windrose(lokasi, bln, thn, uploaded):
    df=pd.read_excel(uploaded)
    day=df['time']
    u=df['u']
    v=df['v']
    ws=np.sqrt(u**2+v**2)*(1.94384)
    kw=np.where((u >= 0) & (v >= 0), 'K1', np.where((u >= 0) & (v < 0), 'K2', np.where((u < 0) & (v < 0), 'K3', 'K4')))

    wd=np.where(kw=='K1',np.degrees(np.arctan(u/v)),
            np.where(kw=='K2',180+np.degrees(np.arctan(u/v)),
                np.where(kw=='K3',180+np.degrees(np.arctan(u/v)),360+np.degrees(np.arctan(u/v)))))
    
    #Output
    wrf = plt.figure(figsize=(7,7), dpi=100)
    wrf.clear()
    rect = [0.1,0.1,0.8,0.8]
    wa = WindroseAxes(wrf, rect)
    wrf.add_axes(wa)
    wa.bar(wd, ws, normed=True, opening=1.0)
    wa.legend(loc='best', title = 'Kecepatan (Knots)')
    n_wr=f'Mawar Angin Perairan {lokasi} Bulan {bln} Tahun {thn}'
    plt.title(f'Mawar Angin Perairan {lokasi} Bulan {bln} Tahun {thn}')
    iya = "static/hasil/hell.png"
    plt.savefig(fname=iya ,format='png',dpi=900,transparent=False)
    return iya

#buat_windrose("huhh", "januari", 2000, "static/buat windrose.xls")