import dash_mantine_components as dmc
from dash import Input, Output, callback, register_page, html, State
import dash_daq as daq
from dash_iconify import DashIconify

register_page(__name__, path="/train_controller/manual", icon="fa-solid:home")


def layout():
    controls_stack_content = [
        [
            {
                "segment_id": "train_manual-header_control",
                "default_value": "header_show",
            },
            {
                "id": "header_show",
                "icon": "octicon:fold-down-24",
                "tooltip_text": "Показать хедер",
            },
            {
                "id": "header_hide",
                "icon": "octicon:fold-up-24",
                "tooltip_text": "Скрыть хедер",
            },
        ],
        [
            {
                "segment_id": "train_manual-light_control",
                "default_value": "light_off",
            },
            {
                "id": "light_on",
                "icon": "mdi:car-light-high",
                "tooltip_text": "Включить свет",
            },
            {
                "id": "light_off",
                "icon": "mdi:car-light-fog",
                "tooltip_text": "Выключить свет",
            },
        ],
    ]

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
                # dmc.Flex(
                #     [
                #         daq.Knob(
                #             size=150,
                #             value=0,
                #             color={
                #                 "gradient": True,
                #                 "ranges": {
                #                     "darkblue": [-10, -7],
                #                     "cyan": [-7, 0],
                #                     "green": [0, 4],
                #                     "yellow": [4, 8],
                #                     "red": [8, 10],
                #                 },
                #             },
                #             scale={
                #                 "labelInterval": 2,
                #                 "interval": 1,
                #             },
                #             max=10,
                #             min=-10,
                #             digits=0,
                #             # showCurrentValue=True,
                #             # label="Скорость",
                #             # labelPosition="bottom",
                #         )
                #     ],
                #     className="manage-controller_column",
                # ),
                [
                    dmc.Stack(
                        [
                            dmc.SegmentedControl(
                                id=segment[0]["segment_id"],
                                value=segment[0]["default_value"],
                                data=[
                                    {
                                        "value": data["id"],
                                        "label": dmc.Tooltip(
                                            DashIconify(icon=data["icon"], height=24),
                                            label=data["tooltip_text"],
                                            radius="sm",
                                            position="top",
                                        ),
                                    }
                                    for data in segment[1:]
                                ],
                            )
                            for segment in controls_stack_content
                        ],
                        gap="sm",
                    )
                ],
                span="content",
                bg="rgba(255, 0, 217, 0.3)",
            ),
        ],
        className="manage-grid",
        align="stretch",
        # maw="100vw",
    )


@callback(
    Output("appshell", "header"),
    Input("train_manual-header_control", "value"),
    State("appshell", "header"),
)
def hide_header(header_control, header):
    header["collapsed"] = True if header_control == "header_hide" else False
    return header
