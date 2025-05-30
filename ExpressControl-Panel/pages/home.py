import dash_mantine_components as dmc
from dash import Input, Output, callback, register_page, html

register_page(__name__, path="/", icon="fa-solid:home")

def layout():
    return dmc.Stack(
        [
            html.A('Тесты светофоров', href='/tests/train_lights'),
            html.A('Тесты знаков', href='/tests/train_signs')
        ]
    )