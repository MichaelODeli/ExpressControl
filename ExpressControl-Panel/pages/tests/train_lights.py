import dash_mantine_components as dmc
from dash import Input, Output, callback, register_page, html

register_page(__name__, path="/tests/train_lights", icon="fa-solid:home")


def light_generator(light_type: str, light_parameters: tuple, light_size: str = "md"):
    """Генератор светофоров в HTML

    Args:
        light_type (str): строка с типом светофора ('classic', 'diamond').
        light_parameters (tuple): список, описывающий конструкцию светофора. Формат: описание огня светофора - словарь, несколько огней в одной секции светофора - список словарей, несколько секций - список списков.
    """

    light_group = []

    for lights in light_parameters:
        light_stack = []
        for light in lights:
            light_color = light["color"]
            light_state = light["state"]
            light_blink = light["blink"]
            blinker_class = (
                "train_light-blinker " if light_blink and light_state else " "
            )

            light_stack += [
                html.Button(
                    className=f"train_light-{light_type}-light "
                    + f"train_light-{light_type}-light-{light_size} "
                    + blinker_class
                    + f"train_light-color-{light_color if light_state else 'off'}",
                )
            ]

        light_group += [dmc.Flex(
            children=light_stack,
            className=f"train_light-{light_type}-box "
            + f" train_light-{light_type}-box-{light_size}",
            align="center",
            justify="center",
            gap='0' if light_type == 'diamond' else 'xs'
        )]
    

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
                ]
            ),
            dmc.Group(
                [
                    light_generator(
                        "diamond",
                        [[{"color": "yellow", "state": False, "blink": False}]],
                    ),
                    light_generator(
                        "diamond",
                        [[{"color": "yellow", "state": True, "blink": False}]],
                    ),
                    light_generator(
                        "diamond",
                        [[{"color": "yellow", "state": True, "blink": True}]],
                    ),
                    light_generator(
                        "diamond",
                        [[{"color": "green", "state": True, "blink": False}]],
                    ),
                ],
                gap="lg",
            ),
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
                                {"color": "red", "state": True, "blink": False},
                                {"color": "yellow", "state": False, "blink": False},
                            ],
                            [
                                {"color": "white", "state": True, "blink": False},
                            ],
                        ],
                    ),
                ],
                align="flex-start",
            ),
            dmc.Group(
                [
                    light_generator(
                        "classic",
                        [
                            [
                                {"color": "red", "state": False, "blink": False},
                                {"color": "purple", "state": False, "blink": False},
                            ],
                        ],
                        light_size="sm",
                    ),
                    light_generator(
                        "classic",
                        [
                            [
                                {"color": "red", "state": False, "blink": False},
                                {"color": "purple", "state": True, "blink": False},
                            ],
                        ],
                        light_size="md",
                    ),
                    light_generator(
                        "classic",
                        [
                            [
                                {"color": "red", "state": True, "blink": False},
                                {"color": "purple", "state": False, "blink": False},
                            ],
                        ],
                        light_size="lg",
                    ),
                ],
                align="flex-start",
            ),
            dmc.Group(
                [
                    light_generator(
                        "diamond",
                        [[{"color": "red", "state": True, "blink": False}]],
                        light_size="sm",
                    ),
                    light_generator(
                        "diamond",
                        [[{"color": "green", "state": True, "blink": False}]],
                        light_size="md",
                    ),
                    light_generator(
                        "diamond",
                        [[{"color": "white", "state": True, "blink": False}]],
                        light_size="lg",
                    ),
                ],
                gap="lg",
            ),
        ]
    )
