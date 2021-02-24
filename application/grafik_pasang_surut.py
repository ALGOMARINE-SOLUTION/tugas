import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def process(datapasut):
  df1= pd.read_excel (datapasut)
  fig = plt.figure()
  ax1 = fig.add_subplot()
  ax1.set_xlabel('Time (in hours)')
  ax1.set_ylabel('Elevation (in meters)')
  ax1.set_title('Grafik Pasang Surut Bulan September Tahun 2020 Perairan Tanjung Emas')
  ax1.plot('time', 'UTC', data = df1, label = 'Pasang Surut')
  ax1.legend(loc='best')
  namadarifile = 'static/datapasut.png'
  plt.savefig(fname= namadarifile ,format='png',dpi=900,transparent=False)
  return namadarifile
