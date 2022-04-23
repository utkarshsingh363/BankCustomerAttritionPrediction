import pandas as pd

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