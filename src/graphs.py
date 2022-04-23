from ctypes.wintypes import RGB
from matplotlib.colors import rgb2hex
import pandas as pd
import copy
import plotly.figure_factory as ff
import scipy
import plotly.express as px
import joblib
import pickle
from sklearn import metrics

# Model Read
svm_path = 'data/svm_model.sav'
with open(svm_path, "rb") as f:
    svm_Model = pickle.load(f)
    svm_accuracy = pickle.load(f)
    svm_f1=pickle.load(f)
    svm_specificity = pickle.load(f)
    svm_sensitivity = pickle.load(f)
    svm_auc = pickle.load(f)
    svm_feat_importances = pickle.load(f)
    svm_fpr = pickle.load(f)
    svm_tpr = pickle.load(f)

xgb_path = 'data/xgb_model.sav'
with open(xgb_path, "rb") as f:
    xgb_Model = pickle.load(f)
    xgb_accuracy = pickle.load(f)
    xgb_f1=pickle.load(f)
    xgb_specificity = pickle.load(f)
    xgb_sensitivity = pickle.load(f)
    xgb_auc = pickle.load(f)
    xgb_feat_importances = pickle.load(f)
    xgb_fpr = pickle.load(f)
    xgb_tpr = pickle.load(f)

lr_path = 'data/lr_model.sav'
with open(lr_path, "rb") as f:
    lr_Model = pickle.load(f)
    lr_accuracy = pickle.load(f)
    lr_f1=pickle.load(f)
    lr_specificity = pickle.load(f)
    lr_sensitivity = pickle.load(f)
    lr_auc = pickle.load(f)
    lr_feat_importances = pickle.load(f)
    lr_fpr = pickle.load(f)
    lr_tpr = pickle.load(f)

rf_path = 'data/rf_model.sav'
with open(rf_path, "rb") as f:
    rf_Model = pickle.load(f)
    rf_accuracy = pickle.load(f)
    rf_f1=pickle.load(f)
    rf_specificity = pickle.load(f)
    rf_sensitivity = pickle.load(f)
    rf_auc = pickle.load(f)
    rf_feat_importances = pickle.load(f)
    rf_fpr = pickle.load(f)
    rf_tpr = pickle.load(f)


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
    
def roc_plot(feature):
    if feature=='lr':
        print("LR")
        fpr=lr_fpr
        tpr=lr_tpr
    elif feature=='svm':
        print('SVM')
        fpr=svm_fpr
        tpr=svm_tpr
    elif feature=='rf':
        print("RF")
        fpr=rf_fpr
        tpr=rf_tpr
    else:
        print("XGB")
        fpr=xgb_fpr
        tpr=xgb_tpr

    score = metrics.auc(fpr, tpr)
    
    fig = px.area(
        x=fpr, y=tpr,
        title=f'ROC Curve',
        labels=dict(
            x='False Positive Rate', 
            y='True Positive Rate'))
    fig.add_shape(
        type='line', line=dict(dash='dash'),
        x0=0, x1=1, y0=0, y1=1)

    return fig

def featureImportance_plot(feature):
    if feature=='lr':
        print("LR")
        featureImportance=lr_feat_importances
    elif feature=='svm':
        print('SVM')
        featureImportance=svm_feat_importances
    elif feature=='rf':
        print("RF")
        featureImportance=rf_feat_importances
    else:
        print("XGB")
        featureImportance=xgb_feat_importances

    featureImportance_Frame=featureImportance.to_frame().reset_index()

    fig = px.bar(featureImportance_Frame[::-1], x=0, y='index')


    return fig

def accuracyResult(feature):
    if feature=='lr':
        return lr_accuracy
    elif feature=='svm':
        return svm_accuracy
    elif feature=='rf':
        return rf_accuracy
    else:
        return xgb_accuracy

def sensitivityResult(feature):
    if feature=='lr':
        return lr_sensitivity
    elif feature=='svm':
        return svm_sensitivity
    elif feature=='rf':
        return rf_sensitivity
    else:
        return xgb_sensitivity


def specificityResult(feature):
    if feature=='lr':
        return lr_specificity
    elif feature=='svm':
        return svm_specificity
    elif feature=='rf':
        return rf_specificity
    else:
        return xgb_specificity

def aucResult(feature):
    if feature=='lr':
        return lr_auc
    elif feature=='svm':
        return svm_auc
    elif feature=='rf':
        return rf_auc
    else:
        return xgb_auc

def f1Result(feature):
    if feature=='lr':
        return lr_f1
    elif feature=='svm':
        return svm_f1
    elif feature=='rf':
        return rf_f1
    else:
        return xgb_f1


        
        
