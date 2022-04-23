from turtle import width
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc


tab_modelAnalysis_features = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Model Analysis", className="card-title"),
                html.P(
                    "Here we will have Results of different models",
                    className="card-text",
                ),
                dbc.Button("Do Something", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

card_donut = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Spinner(size="md",color="light",
                    children=[
                        dcc.Graph(id="categorical_pie_graph", config = {"displayModeBar": False}, style = {"height": "48vh"})
                    ]
                ),
                
            ],
        ),
    ],
    style = {"background-color": "#283748"}
)

card_barChart= dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Spinner(size="md",color="light",
                    children=[
                        dcc.Graph(id="categorical_bar_graph", config = {"displayModeBar": False}, style = {"height": "48vh"})
                    ]
                ),
                
            ],
        ),
    ],
    style = {"background-color": "#283748"}
)

card_boxPlot = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Spinner(size="md",color="light",
                    children=[
                        dcc.Graph(id="numerical_box_graph", config = {"displayModeBar": False}, style = {"height": "48vh"})
                    ]
                ),
            ],
        ),
    ],
    style = {"background-color": "#283748"}
)

card_densityPlot = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Spinner(size="md",color="light",
                    children=[
                        dcc.Graph(id="numerical_density_graph", config = {"displayModeBar": False}, style = {"height": "48vh"})
                    ]
                ),
                
            ],
        ),
    ],
    style = {"background-color": "#283748"}
)

card_scatter = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Spinner(size="md",color="light",
                    children=[
                        html.Div("Scatter Plot")
                    ]
                ),
                
            ],
        ),
    ],
    style = {"background-color": "#283748"}
)

tab_dataAnalysis_features = html.Div(
            [
                html.H4("Categorical Attribute", className="card-title"),
                html.Div(
                    [
                    dbc.InputGroup([
                        dbc.Select(
                            options=[
                                {"label": "Gender", "value": "Gender"},
                                {"label": "Geography", "value": "Geography"},
                                {"label": "Has Credit Card", "value": "HasCrCard"},
                                {"label": "Is Active", "value": "IsActiveMember"},
                            ], id = "categorical_dropdown", value="Gender",
                        ),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                html.Div([
                                    html.Img(src="../assets/customer.jpeg", className="customer-img")
                                ])
                                ],style = {"background-color": "#283748"})
                            ])
                        ],lg="4", sm=12,),
                        dbc.Col(card_donut, lg="4", sm=12),
                        dbc.Col(card_barChart, lg="4", sm=12),
                    ]),
                ],
                ),
                html.H4("Numerical Attribute", className="card-title"),
                    html.Div(
                        [
                        dbc.InputGroup([
                            dbc.Select(
                                options=[
                                    {"label": "Credit Score", "value": "CreditScore"},
                                    {"label": "Balance", "value": "Balance"},
                                    {"label": "Estimated Salary", "value": "EstimatedSalary"},
                                    {"label": "Age", "value": "Age"},
                                ], id = "numerical_dropdown", value="CreditScore",
                            ),
                        ]),
                        dbc.Row([
                            dbc.Col(card_densityPlot, lg="4", sm=12),
                            dbc.Col(card_scatter, lg="4", sm=12),
                            dbc.Col(card_boxPlot, lg="4", sm=12),
                        ]),
                    ],
                    ),
            ]
        ),

tab_prediction_features = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Model Prediction", className="card-title"),
                html.P(
                    "Here we will give option for the user to predict the churn based on a particular model",
                    className="card-text",
                ),
                dbc.Button("Do Something", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

