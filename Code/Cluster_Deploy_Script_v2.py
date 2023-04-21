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
        cluster_number = int(flask.request.form['cluster_number'])
        # cluster_number = 1
        print(cluster_number)
        # data = [go.Bar(x=['A', 'B', 'C'], y=[1, 2, 3])]
        chart1_df = cmd_output[cmd_output['Experiment_1.2_labels'] == cluster_number].groupby(['p_bu'])['partnumber'].count().reset_index()
        chart1_df.columns = ['p_bu', 'SKU_count']
        chart1_data = [go.Bar(x=chart1_df['p_bu'].values, y=chart1_df['SKU_count'].values)]
        chart2_df = cmd_output[cmd_output['Experiment_1.2_labels'] == cluster_number].groupby(['p_region'])['partnumber'].count().reset_index()
        chart2_df.columns = ['p_region', 'SKU_count']
        chart2_data = [go.Bar(x=chart2_df['p_region'].values, y=chart2_df['SKU_count'].values)]
        
        

    chart1_title = 'SKU Count by BU for Cluster ' + str(cluster_number)
    chart2_title = 'SKU Count by Region for Cluster ' + str(cluster_number)
    chart1_layout = go.Layout(title = chart1_title, width=1000, height=600)
    chart2_layout = go.Layout(title = chart2_title, width=1000, height=600)
    #fig = go.Figure(data=data, layout=layout)
    fig1 = go.Figure(data=chart1_data, layout=chart1_layout)
    fig2 = go.Figure(data=chart2_data, layout=chart2_layout)

    # Convert the chart into JSON
    #chart_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    chart_json1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    chart_json2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    # Render the HTML template with the JSON data
    #return flask.render_template('chart.html', chart_json=chart_json)
    return flask.render_template('chart_4.html', chart_json1=chart_json1, chart_json2=chart_json2)
        # return '<img src="wallpaper.jpg">'
        

if __name__ == "__main__":
    cluster_app.run(debug=True, host='localhost', port=8082)