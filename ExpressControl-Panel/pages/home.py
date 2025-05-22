import dash_mantine_components as dmc
from dash import Input, Output, callback, register_page

register_page(__name__, path="/", icon="fa-solid:home")

def layout():
    return 'Hi!'