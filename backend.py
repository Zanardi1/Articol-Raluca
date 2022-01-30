from numpy import loadtxt
from scipy.interpolate import interp1d, LinearNDInterpolator

import steps as s

feed = 7500
VABP = 700
SG = 0.8996
AP = 175
S = 0.8
conversion_level = 82
decant = 5
correlation_factor = 0
c3_yield = 0
c5_c3_yield = 0
c5_yield = 0
c3_c4_yield = 0
c4_c3_yield = 0
c3_total_yield = 0
c4_total_yield = 0
propene_yield = 0
propane_yield = 0
butene_yield = 0
butane_yield = 0
isobutane_yield = 0
coke_c2_light_yield = 0
coke_total_coke_c2_light_yield = 0
coke_yield = 0
c2_light_yield = 0
alimentare = [0] * 5
h2s_yield = 0
gasoline_yield = 0
oil_yield = 0
light_oil_yield_volume = 0
light_oil_yield_mass = 0
decant_oil_SPG = 0
calculated_values = 0
normalized_values = 0
yield_wt = 0
yield_lb_h = 0
calc_wt = 0
calc_lb_h = 0
normalized_wt = 0
normalized_lb_h = 0
COM = 0
COR = 0


def interp_1d(filename):
    data = loadtxt(filename)
    inputs = data[:, 0]
    outputs = data[:, 1]
    f = interp1d(inputs, outputs)
    return f


def interp_2d(filename):
    data = loadtxt(filename)
    inputs = data[:, :2]
    outputs = data[:, 2]
    interp = LinearNDInterpolator(inputs, outputs)
    return interp


def compute_MON(corr_level, corr_fact):
    f = interp_2d('Figura 12.txt')
    y = f(corr_level, corr_fact)
    return y


def compute_RON(corr_level, corr_fact):
    f = interp_2d('Figura 13.txt')
    y = f(corr_level, corr_fact)
    return y


def factor(conv_level, corr_fact):
    f = interp_2d('Figura 10.txt')
    return f(conv_level, corr_fact)


def read_table_2():
    names = []
    avg = []
    with open('Tabelul 2.txt', 'r') as f:
        for line in f:
            if "#" not in line:
                names.append(line.split()[0])
                avg.append(float(line.split()[1]))
    return names, avg


def compute_vol(list_length):
    vol = [0.0] * list_length
    vol[4] = propene_yield
    vol[5] = propane_yield
    vol[6] = butene_yield
    vol[7] = isobutane_yield
    vol[8] = butane_yield
    vol[9] = s.step_4()
    vol[10] = s.step_19()
    vol[11] = decant
    vol[14] = sum(vol[i] for i in range(len(vol) - 1))
    return vol


def compute_specific_gravity(vol):
    specific_gravity = [0.0] * 4 + [0.522, 0.5077, 0.6013, 0.5631, 0.5844, 0.7447, 0.9309, 1.0255] + [0.0] * 3
    specific_gravity[14] = sum(specific_gravity[i] * vol[i] for i in range(len(vol) - 1)) / 100
    return specific_gravity


def compute_calc(list_length, vol, specific_gravity):
    calc = [0.0] * list_length
    for i in range(4):
        calc[i] = alimentare[i]
    for i in range(4, 9):
        calc[i] = vol[i] * specific_gravity[i]
    calc[9] = s.step_17(conv_level=conversion_level, corr_fact=correlation_factor)
    calc[10] = s.step_20(conv_level=conversion_level, corr_fact=correlation_factor)
    calc[11] = (s.step_18() + factor(conversion_level, correlation_factor) - s.step_20(conversion_level,
                                                                                       correlation_factor))
    calc[12] = s.step_13()
    calc[13] = s.step_16(corr_factor=correlation_factor)
    calc[14] = sum(calc[i] for i in range(len(calc) - 1))
    return calc


def compute_normalized(list_length, calc):
    normalized = [0.0] * list_length
    for i in range(len(normalized) - 1):
        normalized[i] = calc[i] * 100 / calc[14]
    normalized[14] = sum(normalized[i] for i in range(len(normalized) - 1))
    return normalized


def compute_yield_wt(list_length):
    yield_wt = [0.0] * list_length
    for i in range(4):
        yield_wt[i] = calculated_values[i + 9]
    yield_wt[4] = sum(yield_wt[i] for i in range(4))
    return yield_wt


def compute_yield_lb_h(list_length, feed_rate, yield_wt):
    yield_lb_h = [0.0] * list_length
    for i in range(4):
        yield_lb_h[i] = feed_rate * yield_wt[i] / 100
    yield_lb_h[4] = sum(yield_lb_h[i] for i in range(4))
    return yield_lb_h


def compute_calc_wt():
    calc_wt = [0.1, 1, 2.5, 2.5]
    return calc_wt


def compute_calc_lb_h(list_length, yield_lb_h, calc_wt):
    calc_lb_h = [0.0] * list_length
    for i in range(4):
        calc_lb_h[i] = yield_lb_h[i] * calc_wt[i] / 100
    calc_lb_h[4] = sum(calc_lb_h[i] for i in range(4))
    return calc_lb_h


def compute_normalized_wt(list_length, calc_wt, normalized_lb_h, calc_lb_h):
    normalized_wt = [0.0] * list_length
    for i in range(4):
        normalized_wt[i] = calc_wt[i] * normalized_lb_h[4] / calc_lb_h[4]
    return normalized_wt


def compute_normalized_lb_h(list_length, sulfur_in_H2S, sulfur_in_feed, calc_lb_h):
    normalized_lb_h = [0.0] * list_length
    normalized_lb_h[5] = sulfur_in_H2S
    normalized_lb_h[6] = sulfur_in_feed
    normalized_lb_h[4] = normalized_lb_h[6] - normalized_lb_h[5]
    for i in range(4):
        normalized_lb_h[i] = calc_lb_h[i] * normalized_lb_h[4] / calc_lb_h[4]
    return normalized_lb_h
