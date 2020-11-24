import pandas as pd
import matplotlib.pyplot as plt


# Archivo para ver forma de datos 

df = pd.read_csv("uma_02.csv",sep=",")


col = df.columns[4:len(df.columns)-1]

col = list(col)


def data(data):
	print(df[data])


data('mp25')
data('time')




#plt.plot(df['time'],df['mp25'])

#plt.show()





