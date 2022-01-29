from numpy import loadtxt
from scipy.interpolate import interp1d, LinearNDInterpolator

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
