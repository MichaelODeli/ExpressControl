import dash_mantine_components as dmc
from dash import Input, Output, callback, register_page

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
        light_color = list(light.keys())[0]
        return dmc.Flex(
            [
                dmc.Box(
                    style={
                        "animation": (
                            "pulse 1.3s infinite"
                            if light[light_color] == "blink"
                            else "none"
                        ),
                    },
                    bg="white" if light[light_color] == "off" else light_color,
                    className="train_light-diamond-light",
                )
            ],
            className="train_light-diamond-box",
            align="center",
            justify="center",
        )
    else:
        for light in light_parameters:
            light_stack = []
            for light_color in light.keys():
                light_stack += [
                    dmc.Box(
                        style={
                            "animation": (
                                "pulse 1.3s infinite"
                                if light[light_color] == "blink"
                                else "none"
                            ),
                        },
                        bg="white" if light[light_color] == "off" else light_color,
                        className="train_light-classic-light",
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
                            {"yellow": "on", "green": "on"},
                            {"red": "on", "yellow": "on"},
                        ],
                    ),
                    light_generator(
                        "classic",
                        [
                            {"yellow": "off", "green": "on"},
                            {"red": "off", "yellow": "off"},
                        ],
                    ),
                    light_generator(
                        "classic",
                        [
                            {"yellow": "blink", "green": "off"},
                            {"red": "off", "yellow": "off"},
                        ],
                    ),
                    light_generator(
                        "classic",
                        [
                            {"yellow": "on", "green": "off"},
                            {"red": "off", "yellow": "off"},
                        ],
                    ),
                    light_generator(
                        "classic",
                        [
                            {"yellow": "blink", "green": "off"},
                            {"red": "off", "yellow": "on"},
                        ],
                    ),
                    light_generator(
                        "classic",
                        [
                            {"yellow": "on", "green": "off"},
                            {"red": "off", "yellow": "on"},
                        ],
                    ),
                    light_generator(
                        "classic",
                        [
                            {"yellow": "off", "green": "off"},
                            {"red": "on", "yellow": "off"},
                        ],
                    ),
                ]
            ),
            dmc.Group(
                [
                    light_generator(
                        "diamond",
                        [{"yellow": "off"}],
                    ),
                    light_generator(
                        "diamond",
                        [{"yellow": "on"}],
                    ),
                    light_generator(
                        "diamond",
                        [{"yellow": "blink"}],
                    ),
                    light_generator(
                        "diamond",
                        [{"green": "on"}],
                    ),
                ],
                gap='lg'
            ),
        ]
    )
