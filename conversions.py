def convert_api_to_specific_gravity(api_value):
    return 141.5 / (api_value + 131.5)


def convert_tonnes_per_year_to_bpsd(amount_to_convert, density):
    amount_to_convert *= 2205
    density *= 0.0083 * 1000
    amount_to_convert /= density
    amount_to_convert /= 42
    amount_to_convert /= 365
    return amount_to_convert


def convert_c_to_f(amount_to_convert):
    return 9 / 5 * amount_to_convert + 32
