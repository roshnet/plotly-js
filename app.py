#! /usr/bin/python3

from flask import Flask
from flask import render_template

# plotly libraries
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
import json

app = Flask(__name__)


@app.route('/')
def index():
	# Generating variables for graph:
	count = 500
	xScale = np.linspace(0, 100, count)
	yScale = np.random.randn(count)

	# Create a trace:
	trace = go.Scatter(
		x = xScale,
		y = yScale
	)

	data = [trace]

	graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

	# Pass data on to template:
	return render_template('index.html',
						   graphJSON=graphJSON)



if __name__ == '__main__':
	app.run(debug=True)