import dash_mantine_components as dmc
from dash_iconify import DashIconify


def get_icon(icon):
    return DashIconify(icon=icon, height=16)


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
        checked=True
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
                        persistence_type="session",
                    ),
                    dmc.Burger(
                        id="desktop-burger",
                        size="sm",
                        visibleFrom="sm",
                        opened=False,
                        pt="7px",
                        persistence=True,
                        persistence_type="session",
                    ),
                    dmc.NavLink(
                        label=dmc.Title(brand, order=3),
                        href="/",
                    ),
                ],
                h="100%",
                px="md",
                wrap="nowrap",
            ),
            dmc.Group(
                [
                    dmc.Text(
                        "Загрузка времени...",
                        id="timeDisplay",
                        visibleFrom='sm',
                        className='time_widget'
                    ),
                    theme_toggle,
                ]
            ),
        ],
        justify="space-between",
        style={"flex": 1},
        h="100%",
        px="md",
    )


def get_navbar():
    return dmc.ScrollArea(
        [
            dmc.NavLink(
                label=dmc.Text("Управление макетом", fw=600),
                leftSection=get_icon(icon="tabler:gauge"),
                childrenOffset=28,
                active="partial",
                persistence=True,
                persistence_type="session",
                children=[
                    dmc.NavLink(
                        label="Автоуправление поездами",
                        active="exact",
                        href="/train_controller/auto",
                    ),
                    dmc.NavLink(
                        label="Ручное управление",
                        active="exact",
                        href="/train_controller/manual",
                    ),
                    dmc.NavLink(
                        label="Карта",
                        active="exact",
                        href="/map",
                    ),
                ],
            ),
            dmc.NavLink(
                label=dmc.Text("Управление сервером", fw=600),
                leftSection=get_icon(icon="tabler:gauge"),
                childrenOffset=28,
                active="partial",
                persistence=True,
                persistence_type="session",
                children=[
                    dmc.NavLink(
                        label="Параметры сервера",
                        active="exact",
                        href="/server/manage",
                    ),
                ],
            ),
            dmc.NavLink(
                label=dmc.Text("Инвентаризация", fw=600),
                leftSection=get_icon(icon="tabler:fingerprint"),
                childrenOffset=28,
                active="partial",
                persistence=True,
                persistence_type="session",
                children=[
                    dmc.NavLink(
                        label="Поезда", active="exact", href="/inventory/trains"
                    ),
                    dmc.NavLink(
                        label="Напольные устройства",
                        childrenOffset=28,
                        active="partial",
                        persistence=True,
                        persistence_type="session",
                        children=[
                            dmc.NavLink(
                                label="Светофоры",
                                active="exact",
                                href="/inventory/outdoor/light",
                            ),
                            dmc.NavLink(
                                label="Стрелки",
                                active="exact",
                                href="/inventory/outdoor/switch",
                            ),
                        ],
                    ),
                    dmc.NavLink(
                        label="Строения", active="exact", href="/inventory/buildings"
                    ),
                ],
            ),
        ],
        scrollbarSize=3,
        scrollHideDelay=300,
    )
