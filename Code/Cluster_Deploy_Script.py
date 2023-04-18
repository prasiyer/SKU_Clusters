import flask
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import json
import plotly

cmd_output = pd.read_csv('/data2/home/prasannaiyer/Projects/SKU_Cluster_Local/SKU_Clusters/Code/cmd_data_output.csv')

kmeans_centroids = pd.read_csv('/data2/home/prasannaiyer/Projects/SKU_Cluster_Local/SKU_Clusters/Code/centroids_kmeans.csv')

attr_input_subset = ['Attr1_Str_qu', 'Attr2_OpPr_qu', 'Attr3_Costamount_norm',
       'Attr4_RdDi_norm', 'Attr5_BrDi_norm', 'Attr9_Frctn0', 'Attr9_Frctn1']


cluster_app = flask.Flask(__name__)
@cluster_app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'GET':
        # show a form to input the cluster number
        return(flask.render_template('index.html'))
    if flask.request.method == 'POST':
        # get the cluster number from the form
        cluster_number = flask.request.form['cluster_number']
        print(cluster_number)
        data = [go.Bar(x=['A', 'B', 'C'], y=[1, 2, 3])]
    #layout = go.Layout(title='Bar Chart')
    layout = go.Layout(title = cluster_number)
    fig = go.Figure(data=data, layout=layout)

    # Convert the chart into JSON
    chart_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # Render the HTML template with the JSON data
    return flask.render_template('chart.html', chart_json=chart_json)
        # return '<img src="wallpaper.jpg">'
        

if __name__ == "__main__":
    cluster_app.run(debug=True, host='localhost', port=8082)