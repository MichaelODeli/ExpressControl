import dash_mantine_components as dmc
from dash import Input, Output, callback, register_page, html
import dash_daq as daq

register_page(__name__, path="/train_controller/manual", icon="fa-solid:home")


def layout():
    return dmc.Grid(
        [
            dmc.GridCol("Col1", bg="rgba(255, 0, 0, 0.3)", span=2, h="100%"),
            dmc.GridCol("Col2", bg="rgba(0, 255, 0, 0.3)", span="auto"),
            dmc.GridCol(
                dmc.Stack(["A"], h="100%", justify="flex-end"),
                bg="rgba(0, 255, 255, 0.3)",
                span=1,
            ),
            dmc.GridCol(
                dmc.Flex(
                    [
                        daq.Knob(
                            size=150,
                            value=0,
                            color={
                                "gradient": True,
                                "ranges": {
                                    "darkblue": [-10, -7],
                                    "cyan": [-7, 0],
                                    "green": [0, 4],
                                    "yellow": [4, 8],
                                    "red": [8, 10],
                                },
                            },
                            scale={
                                "labelInterval": 2,
                                "interval": 1,
                            },
                            max=10,
                            min=-10,
                            digits=0,
                            # showCurrentValue=True,
                            # label="Скорость",
                            # labelPosition="bottom",
                        )
                    ],
                    className="manage-controller_column",
                ),
                span="content",
                pe='0px'
            ),
        ],
        className="manage-grid",
        align="stretch",
        maw="100vw",
    )
