import dash_mantine_components as dmc
from dash import Input, Output, callback, register_page, html

register_page(__name__, path="/tests/train_lights", icon="fa-solid:home")


def light_generator(light_type: str, light_parameters: tuple):
    """Генератор светофоров в HTML

    Args:
        light_parameters (tuple): список, описывающий конструкцию светофора.

    Для вывода двухлинзового светофора следует сделать вложенный список со словарем формата `[{"red": "on", "green": "off"}]`
    Для вывода пятилинзового светофора с разделением следует сделать список словарей вида `[{"red": "on", "green": "off", "yellow": "off"}, {"red": "on", "green": "off"}]`
    """

    light_group = []

    if light_type == "diamond":
        light = light_parameters[0]
        light_color = light["color"]
        light_state = light["state"]
        light_blink = light["blink"]
        blinker_class = " train_light-blinker " if light_blink and light_state else " "
        return dmc.Flex(
            [
                html.Button(
                    className="train_light-diamond-light"
                    + blinker_class
                    + f"train_light-color-{light_color if light_state else 'off'}",
                )
            ],
            className="train_light-diamond-box",
            align="center",
            justify="center",
        )
    else:
        for lights in light_parameters:
            light_stack = []
            for light in lights:
                light_color = light["color"]
                light_state = light["state"]
                light_blink = light["blink"]
                blinker_class = (
                    " train_light-blinker " if light_blink and light_state else " "
                )

                light_stack += [
                    html.Button(
                        className="train_light-classic-light"
                        + blinker_class
                        + f"train_light-color-{light_color if light_state else 'off'}",
                    )
                ]
            light_group += [
                dmc.Stack(light_stack, gap="xs", className="train_light-classic-box")
            ]

        return dmc.Stack(
            light_group,
            gap="0",
        )


def layout():
    return dmc.Stack(
        [
            dmc.Group(
                [
                    light_generator(
                        "classic",
                        [
                            [
                                {"color": "yellow", "state": False, "blink": False},
                                {"color": "green", "state": False, "blink": False},
                            ],
                            [
                                {"color": "red", "state": False, "blink": False},
                                {"color": "yellow", "state": False, "blink": False},
                            ],
                        ],
                    ),
                    light_generator(
                        "classic",
                        [
                            [
                                {"color": "yellow", "state": False, "blink": False},
                                {"color": "green", "state": False, "blink": False},
                            ],
                            [
                                {"color": "red", "state": True, "blink": False},
                                {"color": "yellow", "state": False, "blink": False},
                            ],
                        ],
                    ),
                    light_generator(
                        "classic",
                        [
                            [
                                {"color": "yellow", "state": True, "blink": True},
                                {"color": "green", "state": False, "blink": False},
                            ],
                            [
                                {"color": "red", "state": False, "blink": False},
                                {"color": "yellow", "state": True, "blink": False},
                            ],
                        ],
                    ),
                    light_generator(
                        "classic",
                        [
                            [
                                {"color": "yellow", "state": False, "blink": True},
                                {"color": "green", "state": True, "blink": False},
                            ],
                            [
                                {"color": "red", "state": False, "blink": False},
                                {"color": "yellow", "state": False, "blink": False},
                            ],
                        ],
                    ),
                ]
            ),
            dmc.Group(
                [
                    light_generator(
                        "diamond",
                        [{"color": "yellow", "state": False, "blink": False}],
                    ),
                    light_generator(
                        "diamond",
                        [{"color": "yellow", "state": True, "blink": False}],
                    ),
                    light_generator(
                        "diamond",
                        [{"color": "yellow", "state": True, "blink": True}],
                    ),
                    light_generator(
                        "diamond",
                        [{"color": "green", "state": True, "blink": False}],
                    ),
                ],
                gap="lg",
            ),
        ]
    )
