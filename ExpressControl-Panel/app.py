import dash
from dash import dcc, Input, Output, State, callback, clientside_callback

import dash_mantine_components as dmc
from dash_extensions.pages import setup_page_components
import flask
from dotenv import dotenv_values
import os
from elements import elements_main

# load environment variables
config = {
    **dotenv_values("ExpressControl-Panel/.env"),  # load variables
    # **dotenv_values(".env.secret"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}

# flask and dash configuration
server = flask.Flask(config["APP_NAME"])
app = dash.Dash(
    # name=config["APP_NAME"],
    __name__,
    server=server,
    use_pages=True,
    title=config["WEB_PAGE_TITLE"],
    update_title=config["WEB_PAGE_LOADING_TITLE"],
    suppress_callback_exceptions=True,
    pages_folder=os.path.abspath("ExpressControl-Panel/pages"),
    assets_folder=os.path.abspath("ExpressControl-Panel/assets")
)



layout = dmc.AppShell(
    [
        dmc.NotificationProvider(),
        dmc.AppShellHeader(
            elements_main.get_header(brand=config["WEB_PAGE_HEADER_BRAND"])
        ),
        dmc.AppShellNavbar(
            id="navbar",
            children=elements_main.get_navbar(),
            # p="sm",
        ),
        dmc.AppShellMain(
            [
                dash.page_container,
                setup_page_components(),
            ]
        ),
    ],
    header={"height": 60, "collapsed": False},
    navbar={
        "width": 300,
        "breakpoint": "sm",
        "collapsed": {"mobile": True, "desktop": False},
    },
    padding="sm",
    id="appshell",
)

app.layout = dmc.MantineProvider(
    layout,
    id="mantine_theme",
    defaultColorScheme="light",
    theme={
        "primaryColor": "grape",
    },
)


@callback(
    Output("appshell", "navbar"),
    Input("mobile-burger", "opened"),
    Input("desktop-burger", "opened"),
    State("appshell", "navbar"),
)
def toggle_navbar(mobile_opened, desktop_opened, navbar):
    navbar["collapsed"] = {
        "mobile": not mobile_opened,
        "desktop": not desktop_opened,
    }
    return navbar

clientside_callback(
    """ 
    (switchOn) => {
       document.documentElement.setAttribute('data-mantine-color-scheme', switchOn ? 'dark' : 'light');  
       return window.dash_clientside.no_update
    }
    """,
    Output("color-scheme-toggle", "id"),
    Input("color-scheme-toggle", "checked"),
)

dev = bool(config["APP_DEBUG_ENABLED"])

if __name__ == "__main__":
    if dev:
        app.run(debug=True, host=config["APP_HOST"], port=int(config["APP_PORT"]))
    else:
        from waitress import serve

        serve(app.server, host=config["APP_HOST"], port=int(config["APP_PORT"]))
