from numpy import loadtxt
from scipy.interpolate import interp1d, LinearNDInterpolator


def step_1():
    return 75 - 0.065 * VABP - 0.9 * S + 0.6 * AP - 0.26 * (AP / SG)


def step_2(conv_level, corr_fact):
    data = loadtxt('Figura 1.txt')
    inputs = data[:, :2]
    outputs = data[:, 2]
    interp = LinearNDInterpolator(inputs, outputs)
    y = interp(conv_level, corr_fact)
    return y


def step_3(corr_factor):
    data = loadtxt('Figura 2.txt')
    x = data[:, 0]
    y = data[:, 1]
    f = interp1d(x, y)
    return f(corr_factor)


def step_4():
    return step_2(conversion_level, correlation_factor) * step_3(correlation_factor)


def step_5():
    return step_2(conversion_level, correlation_factor) - step_4()


def step_6(corr_factor):
    data = loadtxt('Figura 3.txt')
    x = data[:, 0]
    y = data[:, 1]
    f = interp1d(x, y)
    return f(corr_factor)


def step_7():
    return step_5() / (1 + step_6(correlation_factor))


def step_8():
    return step_5() - step_7()


def step_9(corr_factor):
    data = loadtxt('Figura 4.txt')
    x = data[:, 0]
    y = data[:, 1]
    f = interp1d(x, y)
    c3_composition = f(corr_factor)  # Valoare luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv
    return c3_composition * step_7(), step_7() - c3_composition * step_7()


def step_10(corr_factor):
    data = loadtxt('Figura 5.txt')
    x = data[:, 0]
    y = data[:, 1]
    f = interp1d(x, y)
    butene_composition = f(corr_factor)
    butane_composition = 0.125  # Valoare luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv
    return butene_composition * step_8(), butane_composition * step_8(), step_8() - butene_composition * step_8() - butane_composition * step_8()


def step_11(conv_level, corr_fact):
    data = loadtxt('Figura 6.txt')
    inputs = data[:, :2]
    outputs = data[:, 2]
    interp = LinearNDInterpolator(inputs, outputs)
    y = interp(conv_level, corr_fact)
    return y  # 9  # Valoare luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv


def step_12(conv_level, corr_fact):
    data = loadtxt('Figura 7.txt')
    inputs = data[:, :2]
    outputs = data[:, 2]
    interp = LinearNDInterpolator(inputs, outputs)
    y = interp(conv_level, corr_fact)
    return y  # 0.675  # Valoare luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv


def step_13():
    return step_11(conversion_level, correlation_factor) * step_12(conversion_level, correlation_factor)


def step_14():
    return step_11(conversion_level, correlation_factor) - step_13()


def step_15():
    pass  # De vazut cum sa fac acest pas


def step_16(corr_factor):
    data = loadtxt('Figura 8.txt')
    x = data[:, 0]
    y = data[:, 1]
    f = interp1d(x, y)
    randament = f(corr_factor)
    return S * randament


def step_17(conv_level, corr_fact):
    data = loadtxt('Figura 9.txt')
    inputs = data[:, :2]
    outputs = data[:, 2]
    API = LinearNDInterpolator(inputs, outputs)
    gasoline_gravity = 141.5 / (API(conv_level, corr_fact) + 131.5)
    return step_4() * (gasoline_gravity / SG)


def step_18():
    return 100 - conversion_level


def factor(conv_level, corr_fact):
    data = loadtxt('Figura 10.txt')
    inputs = data[:, :2]
    outputs = data[:, 2]
    interp = LinearNDInterpolator(inputs, outputs)
    y = interp(conv_level, corr_fact)
    return y


def step_19():
    return step_18() - decant


def step_20(conv_level, corr_fact):
    data = loadtxt('Figura 11.txt')
    inputs = data[:, :2]
    outputs = data[:, 2]
    interp = LinearNDInterpolator(inputs, outputs)
    API = interp(conv_level, corr_fact)
    light_cycle_API = 25.8 - API
    light_cycle_SG = 141.5 / (light_cycle_API + 131.5)
    return step_19() * (
            light_cycle_SG / SG)  # Valoarea 0.9309 e luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv


def step_21():
    return SG * ((step_18() + factor(conversion_level, correlation_factor) - step_20(conversion_level,
                                                                                     correlation_factor)) / decant)


def step_22():
    pass


def step_23():
    pass


def step_24():
    return 81, 92.2  # Valori luate din grafice. Sa vad daca le pot discretiza


VABP = 700
SG = 0.8996
AP = 175
S = 0.8
conversion_level = 82
decant = 5

correlation_factor = step_1()
print('Factorul de corelare: ', correlation_factor)
print('Randamentul de C3 la 400F, in % volumice: ', step_2(conversion_level, correlation_factor))
print('Raportul dintre randamentul de C5, la 400F si randamentul de C3 la 400F: ', step_3(correlation_factor))
print('Randamentul de C5 la 400F, in % volumice: ', step_4())
print('Randamentul de C3+C4 la 400F, in % volumice: ', step_5())
print('Raportul dintre cantitiatea totala de C4 si cantitatea totala de C3: ', step_6(correlation_factor))
print('Randamentul total de C3, in % volumice: ', step_7())
print('Randamentul total de C4, in % volumice: ', step_8())
print('Randamentul de propena, in % volumice: ', step_9(correlation_factor))
print('Randamentul de butena, in % volumice: ', step_10(correlation_factor))
print('Randamentul de cocs, C2 si hidrocarburi usoare: ', step_11(conversion_level, correlation_factor))
print('Raportul dintre cantitatea de cocs si cantitatea de cocs, C2 si hidrocarburi usoare: ',
      step_12(conversion_level, correlation_factor))
print('Randamentul de cocs, in % volumice: ', step_13())
print('Randamentul de C2 si hidrocarburi usoare, in % volumice: ', step_14())
print('De lucrat la pasul 15')
print('Raportul de H2S, in % volumice: ', step_16(correlation_factor))
print('Cantitatea de benzina, in % masice: ', step_17(conversion_level, correlation_factor))
print('Randamentul de ulei, in % volumice: ', step_18() + factor(conversion_level, correlation_factor))
print('Randamentul de ulei usor, in % volumice: ', step_19())
print('Randamentul de ulei usor, in % masice: ', step_20(conversion_level, correlation_factor))
print('Greutatea specifica e uleiului decantat: ', step_21())
print('De rezolvat pasii 22 si 23')
print('Cifrele octanice: ', step_24())
