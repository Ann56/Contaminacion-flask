import pandas as pd
import matplotlib.pyplot as plt
import json
import plotly
import plotly.graph_objs as go


# Archivo para ver forma de datos 

df = pd.read_csv("uma_02.csv",sep=",")

col = list(df.columns[4:len(df.columns)-1])

d = {}
time = list(df['time'])



for i in range(len(col)):
	x = time ; y = list(df[col[i]])
	data = [go.Bar(x=x,y=y)]

	d[col[i]] = data


d_final = {"particulas":d}




json_object = json.dumps(d_final,indent=4)

with open("static/js/uma.json","w") as outfile:
	outfile.write(json_object)


#with open("static/js/uma.json") as file:
#	d = json.load(file)
#	d = d['particulas']

#print(d)