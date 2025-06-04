import dash_mantine_components as dmc
from dash import Input, Output, callback, register_page, html, State
from dash_iconify import DashIconify

register_page(__name__, path="/train_controller/manual", icon="fa-solid:home")


def layout():
    controls_stack_content = [
        [
            {
                "element_id": "train_manual-header_control",
                "default_value": "header_show",
                "type": "segment",
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
                "element_id": "train_manual-light_control",
                "default_value": "light_off",
                "type": "segment",
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
        [
            {
                "element_id": "train_manual-switch_control",
                "type": "button",
            },
            {
                "icon": "icon-park-outline:switch-track",
                "tooltip_text": "Переключить ближайшую стрелку",
            },
        ],
    ]

    train_stats_table_content = [
        {"name": "Номер", "value": "959Э", "icon": "tabler:number"},
        {
            "name": "Режим управления",
            "value": "Автом.",
            "icon": "tabler:steering-wheel",
        },
        {
            "name": "Направление",
            "value": "Ст. А - Ст. Б",
            "icon": "tabler:directions-filled",
        },
        {"name": "Напряжение в КС", "value": "12 В", "icon": "mage:electricity-fill"},
        {
            "name": "Напряжение в батарее",
            "value": "0 В",
            "icon": "mage:electricity-fill",
        },
        {
            "name": "Номер участка СЦБ",
            "value": "257-01 (А - Б)",
            "icon": 'tabler:track',
        },
        {
            "name": "Ограничение",
            "value": "15/15 м/ч",
            "icon": 'mdi:car-speed-limiter',
        },
        {
            "name": "Расст. до светофора",
            "value": "20 м (НМ12)",
            "icon": 'hugeicons:traffic-light',
        },
        {
            "name": "Расст. до стрелки",
            "value": "35 м (Б1)",
            "icon": 'icon-park-outline:switch-track',
        },
    ]

    return dmc.Grid(
        [
            # dmc.GridCol("Col1", bg="rgba(255, 0, 0, 0.3)", span=2, h="100%"),
            dmc.GridCol("Col2", bg="rgba(0, 255, 0, 0.3)", span="auto"),
            dmc.GridCol(
                [
                    dmc.Stack(
                        [
                            dmc.Stack(
                                [
                                    dmc.Text(
                                        "Загрузка времени...",
                                        id="timeDisplay_manual",
                                        className="time_widget time_widget_manual",
                                        size="lg",
                                    ),
                                    dmc.Table(
                                        dmc.TableTbody(
                                            [
                                                dmc.TableTr(
                                                    [
                                                        dmc.TableTd(
                                                            dmc.Center(
                                                                DashIconify(
                                                                    icon=element[
                                                                        "icon"
                                                                    ],
                                                                    height=22,
                                                                ),
                                                            )
                                                        ),
                                                        dmc.TableTd(
                                                            dmc.Text(
                                                                element["name"],
                                                                size="md",
                                                            ),
                                                        ),
                                                        dmc.TableTd(
                                                            dmc.Text(
                                                                element["value"],
                                                                size="md",
                                                            ),
                                                        ),
                                                    ]
                                                )
                                                for element in train_stats_table_content
                                            ]
                                        ),
                                        className="train-stats-table",
                                    ),
                                ]
                                + [
                                    (
                                        dmc.SegmentedControl(
                                            id=segment[0]["element_id"],
                                            value=segment[0]["default_value"],
                                            data=[
                                                {
                                                    "value": data["id"],
                                                    "label": dmc.Tooltip(
                                                        DashIconify(
                                                            icon=data["icon"], height=24
                                                        ),
                                                        label=data["tooltip_text"],
                                                        radius="sm",
                                                        position="top",
                                                    ),
                                                }
                                                for data in segment[1:]
                                            ],
                                        )
                                        if segment[0]["type"] == "segment"
                                        else dmc.Tooltip(
                                            dmc.Button(
                                                DashIconify(
                                                    icon=segment[-1]["icon"], height=24
                                                ),
                                                id=segment[0]["element_id"],
                                                variant="default",
                                            ),
                                            label=segment[-1]["tooltip_text"],
                                            radius="sm",
                                            position="top",
                                        )
                                    )
                                    for segment in controls_stack_content
                                ],
                                gap="sm",
                                align="flex-end",
                            ),
                            dmc.Text("Элементы управления"),
                        ],
                        gap=0,
                        justify="space-between",
                        h="100%",
                        w="100%",
                    ),
                ],
                span="3",
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
