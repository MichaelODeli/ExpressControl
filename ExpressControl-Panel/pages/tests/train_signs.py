import dash_mantine_components as dmc
from dash import Input, Output, callback, register_page, html

register_page(__name__, path="/tests/train_signs", icon="fa-solid:home")


def sign_generator(sign_type: str, sign_parameters: dict, sign_data):
    if sign_type == 'text_sign':
        # verical, horizontal
        # font size
        sign = ''
    elif sign_type == 'direction_indicator':
        # ПТЭ 58
        # digit (0-9)
        # 9-segment display
        sign = ''
    elif sign_type == 'rail_barrier':
        # ПТЭ 62
        sign = ''
    elif sign_type == 'wagon_checker_light':
        # ПТЭ 64
        sign = ''
    elif sign_type == 'pantograph_down_light':
        # ПТЭ 66
        sign = ''
    elif sign_type == 'current_divide_alert':
        # ПТЭ 69
        sign = ''
    elif sign_type == 'current_divide_pant_up':
        # ПТЭ 69
        sign = ''
    elif sign_type == 'current_divide_pant_down':
        # ПТЭ 69
        sign = ''
    elif sign_type == 'unsafe_section_start':
        # ПТЭ 73
        sign = ''
    elif sign_type == 'unsafe_section_end':
        # ПТЭ 73
        sign = ''
    elif sign_type == 'sound_signal':
        # ПТЭ 74
        sign = ''
    elif sign_type == 'loco_stop':
        # ПТЭ 74
        sign = ''
    elif sign_type == 'motor_stop':
        # ПТЭ 76
        sign = ''
    elif sign_type == 'current_disable':
        # ПТЭ 75
        sign = ''
    elif sign_type == 'current_enable':
        # ПТЭ 75
        sign = ''
    else:
        raise NotImplemented
    return sign


def layout():
    return None