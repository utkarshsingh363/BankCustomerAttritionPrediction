import dash_bootstrap_components as dbc

def get_navbar():
    navbar = dbc.NavbarSimple(
        children=[
        ],
        brand="Bank Attrition Prediction",
        brand_href="#",
        color="primary",
        dark=True,
    )

    return navbar

