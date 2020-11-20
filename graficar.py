import pandas as pd
import matplotlib.pyplot as plt




df = pd.read_csv("uma_02.csv",sep=",")



plt.plot(df['time'],df['mp25'])

plt.show()