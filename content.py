from turtle import width
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import dash_html_components as html

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
                        dcc.Graph(id="numerical_scatter_graph", config = {"displayModeBar": False}, style = {"height": "48vh"})
                    ]
                ),
                
            ],
        ),
    ],
    style = {"background-color": "#283748"}
)

card_ROC_Plot=dbc.Card(
    [
        dbc.CardBody([
                dbc.Spinner(size="md",color="light",
                    children=[
                        dcc.Graph(id="model_ROC_graph", config = {"displayModeBar": False}, style = {"height": "48vh"})
                    ]
                ),
        ])
    ],style = {"background-color": "#283748"}
)

card_featureImportance=dbc.Card(
    [
        dbc.CardBody([
                dbc.Spinner(size="md",color="light",
                    children=[
                        dcc.Graph(id="model_featureImportance", config = {"displayModeBar": False}, style = {"height": "48vh"})
                    ]
                ),
        ])
    ],style = {"background-color": "#283748"}
)

tab_modelAnalysis_features=html.Div([
    html.H4("Model Analysis", className="card-title"),
    html.Div([
        dbc.InputGroup([
            dbc.Select(                            
                options=[
                    {"label": "Logistic Regression", "value": "lr"},
                    {"label": "Support Vector Machine", "value": "svm"},
                    {"label": "Random Forest", "value": "rf"},
                    {"label": "XG Boost", "value": "xgb"},
                ], id = "model_dropdown", value="lr",
            )
        ]),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Spinner(html.H4(id="accuracy", children="-", style={'color':'#e7b328'}), size="sm", spinner_style={'margin-bottom': '5px'}),
                        html.P("Accuracy")
                    ]
                ), className="result-card", style={"height":"16vh"}
            )
        ],lg=4, sm=6, className=".card-padding-modelAnalysis"),
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Spinner(html.H4(id="sensitivity", children="-", style={'color':'#e7b328'}), size="sm", spinner_style={'margin-bottom': '5px'}),
                        html.P("Sensitivity")
                    ]
                ), className="result-card", style={"height":"16vh"}
            )
        ],lg=4, sm=6, className="card-padding-modelAnalysis"),
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Spinner(html.H4(id="specificity", children="-", style={'color':'#e7b328'}), size="sm", spinner_style={'margin-bottom': '5px'}),
                        html.P("Specificity")
                    ]
                ), className="result-card", style={"height":"16vh"}
            )
        ],lg=4, sm=6, className="card-padding-modelAnalysis"),
    ]),
   dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Spinner(html.H4(id="auc", children="-", style={'color':'#e7b328'}), size="sm", spinner_style={'margin-bottom': '5px'}),
                        html.P("AUC")
                    ]
                ), className="result-card", style={"height":"16vh"}
            )
        ],lg=4, sm=6, className="card-padding-modelAnalysis"),
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Spinner(html.H4(id="f1", children="-", style={'color':'#e7b328'}), size="sm", spinner_style={'margin-bottom': '5px'}),
                        html.P("F-1 Score")
                    ]
                ), className="result-card", style={"height":"16vh"}
            )
        ],lg=4, sm=6, className="card-padding-modelAnalysis"),
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Spinner(html.H4(id="testTrainSplit", children="20% - 80%", style={'color':'#e7b328'}), size="sm", spinner_style={'margin-bottom': '5px'}),
                        html.P("Test - Train Split")
                    ]
                ), className="result-card", style={"height":"16vh"}
            )
        ],lg=4, sm=6, className="card-padding-modelAnalysis"),
    ]),
    dbc.Row([
        dbc.Col(card_ROC_Plot, lg="6", sm=12),
        dbc.Col(card_featureImportance, lg="6", sm=12),
    ])
],className="mt-3", style = {"background-color": "#272953","padding":'10px'})


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

# tab_prediction_features = dbc.Card(
#     [
#         dbc.CardBody(
#             [
#                 html.H4("Model Prediction", className="card-title"),
#                 html.P(
#                     "Here we will give option for the user to predict the churn based on a particular model",
#                     className="card-text",
#                 ),
#                 dbc.Button("Do Something", color="primary"),
#             ]
#         ),
#     ],
#     style={"width": "18rem"},
# )

# -------------------------------------------------
tab_prediction_features = dbc.Card(
    dbc.CardBody(
        [
            # First Row

            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Gender", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_gender",
                                        options=[
                                            {"label": "Female", "value": "Female"},
                                            {"label": "Male", "value": "Male"},
                                        ], value="Male"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Partner

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Partner", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_partner",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                        ], value="Yes"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Dependents

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Dependents", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_dependents",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                        ], value="No"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # PhoneService

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Phone Service", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_phoneService",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                        ], value="Yes"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    )
                ], className="feature-row",
            ), 

            # Second Row

            dbc.Row(
                [
                    # Multiple Lines

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Multiple Lines", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_multipleLines",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                            {"label": "No phone service", "value": "No phone service"},
                                        ], value="Yes"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Internet Service

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Internet Service", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_internetService",
                                        options=[
                                            {"label": "Fiber optic", "value": "Fiber optic"},
                                            {"label": "DSL", "value": "DSL"},
                                            {"label": "No", "value": "No"},
                                        ], value="Fiber optic"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Online Security

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Online Security", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_onlineSecurity",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                            {"label": "No internet service", "value": "No internet service"},
                                        ], value="No"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Online Backup

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Online Backup", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_onlineBackup",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                            {"label": "No internet service", "value": "No internet service"},
                                        ], value="No"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    )
                ], className="feature-row",
            ),

            # Third Row

            dbc.Row(
                [
                    # Device Protection

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Device Protection", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_deviceProtection",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                            {"label": "No internet service", "value": "No internet service"},
                                        ], value="No"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Tech Support

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Tech Support", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_techSupport",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                            {"label": "No internet service", "value": "No internet service"},
                                        ], value="No"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Streaming TV

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Streaming TV", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_streamingTv",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                            {"label": "No internet service", "value": "No internet service"},
                                        ], value="No"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Streaming Movies

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Streaming Movies", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_streamingMovies",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                            {"label": "No internet service", "value": "No internet service"},
                                        ], value="No"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    )
                ], className="feature-row",
            ),

            # Fourth Row

            dbc.Row(
                [
                    # Contract

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Contract", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_contract",
                                        options=[
                                            {"label": "Month-to-month", "value": "Month-to-month"},
                                            {"label": "One year", "value": "One year"},
                                            {"label": "Two year", "value": "Two year"},
                                        ], value="Month-to-month"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),


                    # PaperlessBilling

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Paperless Billing", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_paperlessBilling",
                                        options=[
                                            {"label": "Yes", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                        ], value="Yes"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),


                    # PaymentMethod

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Payment Method", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_paymentMethod",
                                        options=[
                                            {"label": "Electronic check", "value": "Electronic check"},
                                            {"label": "Mailed check", "value": "Mailed check"},
                                            {"label": "Bank transfer (automatic)", "value": "Bank transfer (automatic)"},
                                            {"label": "Credit card (automatic)", "value": "Credit card (automatic)"}
                                        ], value="Mailed check"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # SeniorCitizen

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Senior Citizen", addon_type="prepend"),
                                    dbc.Select(
                                        id="ft_seniorCitizen",
                                        options=[
                                            {"label": "Yes", "value": "1"},
                                            {"label": "No", "value": "0"}
                                        ], value="1"
                                    )
                                ]
                            )
                        ], lg="3", sm=12
                    ),
                ], className="feature-row",
            ),

            # Fifth Row

            dbc.Row(
                [
                    # MonhtlyCharges

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Monhtly Charges ($)", addon_type="prepend"),
                                    dbc.Input(
                                        id="ft_monthlyCharges",
                                        placeholder="Amount", type="number", value="74.4"
                                    ),
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Total Charges

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Total Charges ($)", addon_type="prepend"),
                                    dbc.Input(
                                        id="ft_totalCharges",
                                        placeholder="Amount", type="number", value="306.6"
                                    ),
                                ]
                            )
                        ], lg="3", sm=12
                    ),

                    # Tenure

                    dbc.Col(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupAddon("Tenure", addon_type="prepend"),
                                    dbc.Input(
                                        id="ft_tenure",
                                        placeholder="Amount", type="number", value="4"
                                    ),
                                ]
                            )
                        ], lg="3", sm=12
                    ),
                ]
            )
        ]
    ),
    className="mt-3", style = {"background-color": "#272953"}
)

tab_prediction_result = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        dbc.Spinner(html.H4(id="lr_result", children="-", style={'color':'#e7b328'}), size="sm", spinner_style={'margin-bottom': '5px'}),
                                        html.P("Logistic Regression")
                                    ]
                                ), className="result-card", style={"height":"16vh"}
                            )
                        ], lg=3, sm=3, className="card-padding"
                    ),

                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        dbc.Spinner(html.H4(id="svm_result", children="-", style={'color':'#e7b328'}), size="sm", spinner_style={'margin-bottom': '5px'}),
                                        html.P("SVM")
                                    ]
                                ), className="result-card", style={"height":"16vh"}
                            )
                        ], lg=3, sm=3, className="card-padding"
                    ),

                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        dbc.Spinner(html.H4(id="rf_result", children="-", style={'color':'#e7b328'}), size="sm", spinner_style={'margin-bottom': '5px'}),
                                        html.P("Random Forest")
                                    ]
                                ), className="result-card", style={"height":"16vh"}
                            )
                        ], lg=3, sm=3, className="card-padding"
                    ),

                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        dbc.Spinner(html.H4(id="xgb_result", children="-", style={'color':'#e7b328'}), size="sm", spinner_style={'margin-bottom': '5px'}),
                                        html.P("XG Boost")
                                    ]
                                ), className="result-card", style={"height":"16vh"}
                            )
                        ], lg=3, sm=3, className="card-padding"
                    )


                ]
            ),

            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Button("Predict", id='btn_predict', size="lg", className="btn-predict")
                        ], lg=4, sm=4, style={"display": "flex", "align-items":"center", "justify-content":"center"},
                        className="card-padding"
                    )
                ]
            ),
        ]
    ),
    className="mt-3", style = {"background-color": "#272953"}
)

tab_prediction_content = [
    
    tab_prediction_features,
    tab_prediction_result
    
]