from flask import Flask , render_template,request
import pandas as pd
import plotly
import plotly.graph_objs as go
import json


app = Flask(__name__)

df = pd.read_csv("uma_02.csv",sep=",")

def create_plot(data):
	x = df[data]
	y = df['time']

	data = [go.Bar(x=x,y=y)]

	graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

	return graphJSON



@app.route("/",methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		respuesta = request.args['dato']
		print(respuesta)
	bar = create_plot('mp01')
	col = df.columns[4:len(df.columns)-1]
	col = list(col)
	return render_template('index.html',col=col,bar=bar)

@app.route("/datos",methods=['GET', 'POST'])
def datos():
	#Obtiene el nombre de las columnas de csv 
	col = df.columns[4:len(df.columns)-1]
	col = list(col)
	select = "None"
	if(request.form.get('select1') != None):
		select= request.form.get('select1')
	
		
	return render_template('datos.html',options=col,select=str(select))



if __name__ == '__main__':
	app.run(debug=True)