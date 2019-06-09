import pandas as pd
import numpy as np
import datetime

df = pd.read_csv('Data/data.csv')

df['available'] = df['balance'].str.replace('€','').str.replace(',','').astype(float)
df['date'] = pd.to_datetime(df["date"])
df['outcomes'] = np.random.uniform(-1999999.0,0,len(df['available']))
df['incomes'] = df['available'] + df['outcomes']


date0 = 0
date1 = 0

def timePeriod(df):
    """Filter a time period of interest, it takes all dataset otherwise"""
    if (date0 != 0) & (date1 != 0):
        df = df[(df['date']>=date0) & (df['date']<=date1)]
    elif date0 != 0:
        df = df[(df['date']>=date0)]
    elif date1 != 0:
        df = df[(df['date']<=date1)]

    return df
timePeriod(df)



"""Rules:
Estatistical: mean, max, min, sd (numerical)
Info: count, unique, top, freq, null
Comparative: equal, greater or less than
Histogram: plot"""


df['balance'].describe()
df['balance'].dtype
df.columns

# Create tables and reset
estTable = pd.DataFrame(columns=['mean', 'max', 'min', 'sd', 'date0', 'date1', 'date'])
infTable = pd.DataFrame(columns=['count', 'unique', 'top', 'null','date0', 'date1', 'date'])
comTable = pd.DataFrame(columns=['greater', 'lesser', 'equal', 'date0', 'date1', 'date'])
totalResults = pd.DataFrame(columns=['control_id', 'result', 'date0', 'date1', 'date'])


def estatistical(df,col):
    mean = df[col].mean()
    max = df[col].max()
    min = df[col].min()
    sd = df[col].std()
    date0 = df['date'].min()
    date1 = df['date'].max()
    date = datetime.datetime.now()

    Table = pd.DataFrame(columns=['mean', 'max', 'min', 'sd', 'date0', 'date1', 'date'])
    Table = Table.append({'mean':mean, 'max':max, 'min':min, 'sd':sd, 'date0':date0, 'date1':date1, 'date':date}, ignore_index= True)
    return Table

TableEst = estatistical(df,'available')

estTable= estTable.append(TableEst)
estTable



def info(df,col):
    count = df[col].count()
    reps = df[col].value_counts()
    unique = (reps == 1).all()
    top = max(reps)
    null =  df[col].isna().count()
    date0 = df['date'].min()
    date1 = df['date'].max()
    date = datetime.datetime.now()

    Table = pd.DataFrame(columns=['count', 'unique', 'top', 'null', 'date0', 'date1', 'date'])
    Table = Table.append({'count':count, 'unique':unique, 'top':top, 'null':null, 'date0':date0, 'date1':date1, 'date':date}, ignore_index= True)
    return Table

TableInf = info('city')

infTable = infTable.append(TableInf)
infTable



def comparative(df,col1, col2):
    greater = col1 > col2
    lesser = col1 < col2
    equal = col1 == col2
    date0 = df['date'].min()
    date1 = df['date'].max()
    date = datetime.datetime.now()

    Table = pd.DataFrame(columns=['greater', 'lesser', 'equal', 'date0', 'date1', 'date'])
    Table = Table.append({'greater':greater, 'lesser':lesser, 'equal':equal, 'date0':date0, 'date1':date1, 'date':date}, ignore_index= True)
    return Table

TableCom = comparative('incomes', 'outcomes')

comTable = comTable.append(TableCom)
comTable


# hisTable = pd.DataFrame(columns=['x', 'y', 'label'])
# def histogram(col):
#
#     date0 = df['date'].min()
#     date1 = df['date'].max()
#     date = datetime.datetime.now()





# Simulation of timePeriod with variations in our dataset

df0 = pd.read_csv('Data/data0.csv')

df0['available'] = df0['balance'].str.replace('€','').str.replace(',','').astype(float)
df0['date'] = pd.to_datetime(df0["date"])
df0['outcomes'] = np.random.uniform(-1999999.0,0,len(df0['available']))
df0['incomes'] = df0['available'] + df0['outcomes']

df1 = pd.read_csv('Data/data1.csv')

df1['available'] = df1['balance'].str.replace('€','').str.replace(',','').astype(float)
df1['date'] = pd.to_datetime(df1["date"])
df1['outcomes'] = np.random.uniform(-1999999.0,0,len(df1['available']))
df1['incomes'] = df1['available'] + df1['outcomes']

df2 = pd.read_csv('Data/data2.csv')

df2['available'] = df2['balance'].str.replace('€','').str.replace(',','').astype(float)
df2['date'] = pd.to_datetime(df2["date"])
df2['outcomes'] = np.random.uniform(-1999999.0,0,len(df2['available']))
df2['incomes'] = df2['available'] + df2['outcomes']

df3 = pd.read_csv('Data/data3.csv')

df3['available'] = df3['balance'].str.replace('€','').str.replace(',','').astype(float)
df3['date'] = pd.to_datetime(df3["date"])
df3['outcomes'] = np.random.uniform(-1999999.0,0,len(df3['available']))
df3['incomes'] = df3['available'] + df3['outcomes']

df4 = pd.read_csv('Data/data4.csv')

df4['available'] = df4['balance'].str.replace('€','').str.replace(',','').astype(float)
df4['date'] = pd.to_datetime(df4["date"])
df4['outcomes'] = np.random.uniform(-1999999.0,0,len(df4['available']))
df4['incomes'] = df4['available'] + df4['outcomes']


# Rules and working through the timePeriod
rules = pd.read_csv('Data/Rules.csv')
rules.head()



def rulesApp(df):
    for x, y, z in zip(rules['Code'], rules['Col1'], rules['Col2']):
        if x == 1:
            TableEst = estatistical(df, y)

        elif x == 2:
            TableInf = info(df, y)

        elif x == 3:
            TableCom = comparative(df, y, z)

    return TableEst, TableInf, TableCom

rulesApp(df0)


estTable = estTable.append(TableEst)
infTable = infTable.append(TableInf)
comTable = comTable.append(TableCom)

estTable
infTable
comTable





    for y in rules['CodeRule']:
        if y == 11:
            result =





totalResults

TableEst = estatistical(df0,'available')
estTable= estTable.append(TableEst)

TableInf = info('city')

infTable = infTable.append(TableInf)
infTable

TableCom = comparative('incomes', 'outcomes')

comTable = comTable.append(TableCom)
comTable
