#!/usr/bin/env python
# coding: utf-8

# In[70]:
#============================ Inputan Excel ===========================
#Input Library
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd

#Input Data
def semangat(tapiboong):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    z_data= pd.read_excel(tapiboong)

#Data
    X = np.arange(1, 16, 1)
    Y = np.arange(1, 16, 1)
    X, Y = np.meshgrid(X, Y)

#Cek datanya panjangnya sama apa engga
#print(len(X))
#print(len(Y))
#print(len(z_data))

#Bikin Grafiknya
    surf = ax.plot_surface(X, Y, Z=z_data, cmap=cm.gist_earth,
                       linewidth=0, antialiased=True)


    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.title("Peta Batimetri\n Perairan Semarang")

    boongbeneran = 'static/Batimetri.png'
    plt.savefig(fname= boongbeneran)
    return boongbeneran