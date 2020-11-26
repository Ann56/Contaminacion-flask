from flask import Flask , render_template,request
import pandas as pd
import plotly
import plotly.graph_objs as go
import json


app = Flask(__name__)

df = pd.read_csv("uma_02.csv",sep=",")




@app.route("/",methods=['GET', 'POST'])
def index():
	col = df.columns[4:len(df.columns)-1]
	col = list(col)
	return render_template('index.html',col=col)

@app.route("/datos",methods=['GET', 'POST'])
def datos():
	#Obtiene el nombre de las columnas de csv 
	col = df.columns[4:len(df.columns)-1]
	col = list(col)
	select = "None"
	if(request.form.get('select1') != None):
		select= request.form.get('select1')
	
		
	return render_template('datos.html',options=col,select=str(select))
@app.route("/simuacion")
def simulacion():
	return render_template('Simulacion.html')


if __name__ == '__main__':
	app.run(debug=True)