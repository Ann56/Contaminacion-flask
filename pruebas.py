import pandas as pd
import matplotlib.pyplot as plt


# Archivo para ver forma de datos 

df = pd.read_csv("uma_02.csv",sep=",")


col = df.columns[4:len(df.columns)-1]

col = list(col)

print (col)

#plt.plot(df['time'],df['mp25'])

#plt.show()





