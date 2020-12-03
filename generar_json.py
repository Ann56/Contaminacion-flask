import pandas as pd
import json


df = pd.read_csv("uma_02.csv",sep=",")

col = list(df.columns[4:len(df.columns)-1])


d = {}

#Guarda los datos
lat  = list(df['lat'])
lng  = list(df['lon'])
time = list(df['time'])


#Añade los datos del material particulado
for i in range(len(col)):
	x = time ; y = list(df[col[i]])
	d[col[i]] = {'time':x , 'valor':y}

coord = []
#Establece coord en una matriz [lat , long ]
for i in range(len(lat)):
	coord.append([lat[i],lng[i]])

#print (coord)
d_final = {"particulas":d,'Coord':coord}




json_object = json.dumps(d_final,indent=4)

#Genera json
with open("static/js/uma.json","w") as outfile:
	outfile.write(json_object)



