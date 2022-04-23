from ctypes.wintypes import RGB
from matplotlib.colors import rgb2hex
import pandas as pd
import copy
import plotly.figure_factory as ff
import scipy
import plotly.express as px

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

# read data
df = pd.read_csv('data/bank_user_data.csv')

cat_features = df.drop(['Geography','Gender', 'HasCrCard', 'IsActiveMember', 'Exited'],axis=1).columns

# Encoding categorical features
# from sklearn.preprocessing import OneHotEncoder
# ohe = OneHotEncoder(sparse=False)

def dist_plot(feature):
    x1 = df[df['Exited'] == 0][feature].to_list()
    x2 = df[df['Exited'] == 1][feature].to_list()

    fig = ff.create_distplot([x1,x2],
    group_labels= ['No', 'Yes'],
    #  bin_size=3,
    curve_type='normal',
    show_rug=False,
                             show_hist=False,
                             show_curve=True,
                             colors=['#47acb1','#f26522']
                            )
    
    
    layout_count = copy.deepcopy(layout)
    fig.update_layout(layout_count)
    
    fig.update_layout(
        title = {'text': f"KDE of {feature}", 'x': 0.5},
        legend = {'x': 0.25}
    )
    

    return fig

def box_plot(feature):
    fig = px.box(df,x='Exited', y=feature, color='Exited')
    
    layout_count = copy.deepcopy(layout)
    fig.update_layout(layout_count)
    
    fig.update_layout(
        title = {'text': f"Box plot of {feature}", 'x': 0.5},
        legend = {'x': 0.25}
    )
    

    return fig

def scatter_plot(feature):


    if feature == "Age":
        temp = df[[feature, 'Exited', 'CreditScore']]
        fig = px.scatter(temp,x=feature, y='CreditScore',color=temp['Exited'].map({1: 'Churn', 0: 'NoChurn'}),
             color_discrete_map={"Churn": RGB(99,110,250), "NoChurn": "#da6750"})
    else:
        temp = df[[feature, 'Exited', 'Age']]
        fig = px.scatter(temp,x='Age', y=feature,color=temp['Exited'].map({1: 'Churn', 0: 'NoChurn'}),
             color_discrete_map={"Churn": RGB(99,110,250), "NoChurn": "#da6750"})
    
    layout_count = copy.deepcopy(layout)
    fig.update_layout(layout_count)
    
    fig.update_layout(
        title = {'text': f"Scatter plot of {feature}", 'x': 0.5},
        legend = {'x': 0.25}
    )
    

    return fig
    