import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pip._internal.commands import download

def process(datasuhu):
  df= pd.read_excel (datasuhu)
  df
  df2 = pd.DataFrame({'Depth(olah)' : [-61,-61],'T(olah)' : [0,30]})
  fig = plt.figure()
  ax1 = fig.add_subplot()
  ax1.set_ylabel('Kedalaman')
  ax1.set_title('Suhu')
  ax1.plot('T(olah)', 'Depth(olah)', data = df, label = 'Grafik Temperature vs Kedalaman')
  ax1.plot('T(olah)', 'Depth(olah)', data = df2, label = 'Termoklin')
  ax1.legend(loc='best')
  plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
  plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
  
  grafiksuhu ='static/download.png'
  plt.savefig(fname=grafiksuhu)
  return grafiksuhu



