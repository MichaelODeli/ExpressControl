import dash_mantine_components as dmc
from dash_iconify import DashIconify


def get_header(brand):
    theme_toggle = dmc.Switch(
        offLabel=DashIconify(
            icon="radix-icons:sun",
            width=15,
            color=dmc.DEFAULT_THEME["colors"]["yellow"][8],
        ),
        onLabel=DashIconify(
            icon="radix-icons:moon",
            width=15,
            color=dmc.DEFAULT_THEME["colors"]["yellow"][6],
        ),
        id="color-scheme-toggle",
        persistence=True,
        color="grey",
    )

    return dmc.Group(
        [
            dmc.Group(
                [
                    dmc.Burger(
                        id="mobile-burger",
                        size="sm",
                        hiddenFrom="sm",
                        opened=False,
                        pt="7px",
                        persistence=True,
                        persistence_type='session'
                    ),
                    dmc.Burger(
                        id="desktop-burger",
                        size="sm",
                        visibleFrom="sm",
                        opened=False,
                        pt="7px",
                        persistence=True,
                        persistence_type='session'
                    ),
                    dmc.Title(brand, order=3),
                ],
                h="100%",
                px="md",
            ),
            theme_toggle,
        ],
        justify="space-between",
        style={"flex": 1},
        h="100%",
        px="md",
    )


def get_navbar():
    return dmc.ScrollArea(
        [
            "60 links in a scrollable section",
            *[dmc.Skeleton(height=28, mt="sm", animate=False) for _ in range(60)],
        ],
        scrollbarSize=3,
        scrollHideDelay=300
    )
