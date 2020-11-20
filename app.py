from flask import Flask , render_template,request
import pandas as pd
import plotly
import plotly.graph_objs as go
import json


app = Flask(__name__)

df = pd.read_csv("uma_02.csv",sep=",")

def grafico_mp25():
	
	x = df['time']
	y = df['mp25']

	data = [
			go.Bar(x=x,
				   y=y
				   )

	]

	graphJson=json.dumps(data , cls=plotly.utils.PlotlyJSONEncoder)

	return graphJson

def grafico_d03():
	
	x = df['time']
	y = df['d03']

	data = [
			go.Bar(x=x,
				   y=y,
				   )

	]

	graphJson=json.dumps(data , cls=plotly.utils.PlotlyJSONEncoder)

	return graphJson

@app.route("/")
def index():

	bar  = grafico_mp25()
	bar2 = grafico_d03()
	return render_template('index.html',bar=[bar,bar2])

@app.route("/datos",methods=['GET', 'POST'])
def datos():
	#Obtiene el nombre de las columnas de csv 
	col = df.columns[4:len(df.columns)-1]
	col = list(col)
	select = "None"
	if(request.form.get('select1') != None):
		select= request.form.get('select1')
	
		
	return render_template('datos.html',options=col,select=str(select))
