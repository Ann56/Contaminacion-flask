from flask import Flask , render_template
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

@app.route("/datos")

def datos():
	return render_template('datos.html')