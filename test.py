import pandas as pd
import numpy as np
import datetime

df = pd.read_csv('Data/data.csv')

df.head(5)
df.columns


def AA(x):
    maximo = max(df[x])
    minimo = min(df[x])
    media = np.mean(df[x])
    desv = np.std(df[x])
    var = np.var(df[x])
    nulos = df[x].isnull().sum()
    po_tot = df[x].count()
    po_inc = nulos
    po_corr = po_tot - po_inc


    return maximo, minimo, media, desv, var, nulos, po_tot, po_inc, po_corr

AA('card')

def AB(x):
    nulos = df[x].isnull().sum()
    po_tot = df[x].count()
    po_inc = nulos
    po_corr = po_tot - po_inc

    return nulos, po_tot, po_inc, po_corr

AB('first_name')
