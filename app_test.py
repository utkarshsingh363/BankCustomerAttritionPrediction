import pandas as pd
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import matplotlib as plt
import copy

from src.navbar import get_navbar
from src.graphs import df,layout,dist_plot,box_plot, scatter_plot,roc_plot,featureImportance_plot,accuracyResult,sensitivityResult,specificityResult,f1Result,aucResult
import plotly.express as px
from content import tab_prediction_features,tab_dataAnalysis_features,tab_modelAnalysis_features,tab_prediction_content
import time


app = Dash(__name__,external_stylesheets = [dbc.themes.SUPERHERO,'/assets/styles.css'])

layout = dict(
    autosize=True,
    #automargin=True,
    margin=dict(l=20, r=20, b=20, t=30),
    hovermode="closest",
    plot_bgcolor="#16103a",
    paper_bgcolor="#16103a",
    legend=dict(font=dict(size=10), orientation="h"),
    title="Satellite Overview",
    font_color ="#e0e1e6",
    xaxis_showgrid=False,
    yaxis_showgrid=False
)

# Layout

tabs = dbc.Tabs(
    [
        dbc.Tab(tab_dataAnalysis_features, label="Data Analysis"),
        dbc.Tab(tab_modelAnalysis_features, label="Model Analysis"),
        dbc.Tab(tab_prediction_content, label="Prediction"),
        
    ]
)

app.layout = html.Div([
    get_navbar(),
    html.H4("Analysis and Prediction", className="cover"),
    html.Div(
        dbc.Row(dbc.Col(tabs, width=12)),
        id="mainContainer",
        style={"display": "flex", "flex-direction": "column"}
    ),
])

# callbacks

@app.callback(
    Output("categorical_pie_graph", "figure"),
    [
        Input("categorical_dropdown", "value"),
    ],
)

def donut_categorical(feature):

    time.sleep(0.2)

    temp = df.groupby([feature]).count()['Exited'].reset_index()

    fig = px.pie(temp, values="Exited", names=feature, hole=.5)

    layout_count = copy.deepcopy(layout)
    fig.update_layout(layout_count)
    
    _title = (feature[0].upper() + feature[1:]) + " Percentage"

    if(df[feature].nunique() == 2):
        _x = 0.3
    elif(df[feature].nunique() == 3):
        _x = 0.16
    else:
        _x = 0

    fig.update_layout(
        title = {'text': _title, 'x': 0.5},
        legend = {'x': _x}
    )

    return fig

@app.callback(
    Output("categorical_bar_graph", "figure"),
    [
        Input("categorical_dropdown", "value"),
    ],
)

def bar_categorical(feature):

    time.sleep(0.2)

    temp = df.groupby([feature, 'Exited']).count()['CustomerId'].reset_index()
    
    fig = px.bar(temp, x=feature, y="CustomerId",
             color=temp['Exited'].map({1: 'Churn', 0: 'NoChurn'}),
             color_discrete_map={"Churn": "#47acb1", "NoChurn": "#f26522"},
             barmode='group')
    
    layout_count = copy.deepcopy(layout)
    fig.update_layout(layout_count)
    
    _title = (feature[0].upper() + feature[1:]) + " Distribution by Churn"
    
    fig.update_layout(
        title = {'text': _title, 'x': 0.5},
        #xaxis_visible=False,
        xaxis_title="",
        yaxis_title="Count",
        legend_title_text="",
        legend = {'x': 0.16}
    )
    return fig


@app.callback(
    Output("numerical_density_graph", "figure"),
    [
        Input("numerical_dropdown", "value"),
    ],
)

def density_numerical(feature):
    time.sleep(0.2)
    fig=dist_plot(feature)
    return fig


@app.callback(
    Output("numerical_box_graph", "figure"),
    [
        Input("numerical_dropdown", "value"),
    ],
)

def box_numerical(feature):
    time.sleep(0.2)
    fig=box_plot(feature)
    return fig


@app.callback(
    Output("numerical_scatter_graph", "figure"),
    [
        Input("numerical_dropdown", "value"),
    ],
)

def scatter_numerical(feature):
    time.sleep(0.2)
    fig=scatter_plot(feature)
    return fig



@app.callback(
    Output("model_ROC_graph", "figure"),
    [
        Input("model_dropdown", "value"),
    ],
)

def ROC_model(feature):
    time.sleep(0.2)
    fig=roc_plot(feature)
    return fig

@app.callback(
    Output("model_featureImportance", "figure"),
    [
        Input("model_dropdown", "value"),
    ],
)

def featuteImportance_model(feature):
    time.sleep(0.2)
    fig=featureImportance_plot(feature)
    return fig

@app.callback(
    Output("accuracy", "children"),
    [
        Input("model_dropdown", "value"),
    ],
)

def updateAccuracy(feature):
    time.sleep(0.2)
    return f"{round(accuracyResult(feature)*100,1)}%"

@app.callback(
    Output("sensitivity", "children"),
    [
        Input("model_dropdown", "value"),
    ],
)

def updateSensitivity(feature):
    time.sleep(0.2)
    return f"{round(sensitivityResult(feature)*100,1)}%"

@app.callback(
    Output("specificity", "children"),
    [
        Input("model_dropdown", "value"),
    ],
)

def updateSpecificity(feature):
    time.sleep(0.2)
    return f"{round(specificityResult(feature)*100,1)}%"

@app.callback(
    Output("f1", "children"),
    [
        Input("model_dropdown", "value"),
    ],
)

def updateF1(feature):
    time.sleep(0.2)
    return f"{round(f1Result(feature),3)}"


@app.callback(
    Output("auc", "children"),
    [
        Input("model_dropdown", "value"),
    ],
)

def updateAuc(feature):
    time.sleep(0.2)
    return f"{round(aucResult(feature),3)}"


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=3001,debug=True)