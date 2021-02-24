import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def process1(natuna,sulawesi):
  df1= pd.read_excel (natuna)
  df1
  df2= pd.read_excel (sulawesi)
  df2
  fig = plt.figure()
  ax1 = fig.add_subplot()
  ax1.set_xlabel('Hari')
  ax1.set_ylabel('SST')
  ax1.set_title('SST Timeseries 2 Wilayah')
  ax1.plot('Hari', 'SST Laut Natuna', data = df1, label = 'SST Laut Natuna')
  ax1.plot('Hari', 'SST Laut Sulawesi', data =df2, label = 'SST Laut Sulawesi')
  ax1.legend(loc='best')
  judulfile = 'static/hasilsst_2_wilayah.png'
  plt.savefig(fname= judulfile ,format='png',dpi=900,transparent=False)
  return judulfile

