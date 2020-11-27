from flask import Flask , render_template,request,json,request
import pandas as pd
import plotly
import plotly.graph_objs as go
import json as js

app = Flask(__name__)

df = pd.read_csv("uma_02.csv",sep=",")

col = df.columns[4:len(df.columns)-1]
col = list(col)

@app.route("/")
def index():

	return render_template('index.html',col=col)

@app.route("/datos")
def datos():
	return render_template('datos.html',col=col)

@app.route("/getdata",methods=['POST'])
def getData():
	#Obtiene el nombre de las columnas de csv 
	name = request.form['name']

	with open("static/js/uma.json") as file:
		d = js.load(file)
		d = d['particulas']
	d = d[name]
	return json.dumps({'status':'Ok','data':{'time':d['time'],'valor':d['valor']}})
	


@app.route("/getbar",methods=['POST'])
def getBar():
	name = request.form['name']

	with open("static/js/uma.json") as file:
		d = js.load(file)
		d = d['particulas'][name]

	x = d['time']
	y = d['valor']

	return json.dumps({'status':'Ok','data':{'x':x,'y':y}})


@app.route("/simulacion")
def simulacion():
	return render_template('Simulacion.html')

@app.route("/data",methods=['POST'])
def data():

	aConstantes = request.form['c']
	aValores    = request.form['v']

	print(request.form)
	return json.dumps({'status':'Ok'})


if __name__ == '__main__':
	app.run(debug=True)