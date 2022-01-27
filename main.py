from numpy import loadtxt
from scipy.interpolate import interp1d, LinearNDInterpolator


def step_1():
    return 75 - 0.065 * VABP - 0.9 * S + 0.6 * AP - 0.26 * (AP / SG)


def step_2(conv_level, corr_fact):
    data = loadtxt('Figura 1.txt')
    inputs = data[:, :2]
    outputs = data[:, 2]
    interp = LinearNDInterpolator(inputs, outputs)
    return interp(conv_level, corr_fact)


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
    c3_composition = f(corr_factor)
    return c3_composition * step_7(), step_7() - c3_composition * step_7()


def step_10(corr_factor):
    data = loadtxt('Figura 5.txt')
    x = data[:, 0]
    y = data[:, 1]
    f = interp1d(x, y)
    butene_composition = f(corr_factor)
    butane_composition = 0.125  # Valoare luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv
    return butene_composition * step_8(), butane_composition * step_8(), step_8() - step_8() * (
            butene_composition + butane_composition)


def step_11(conv_level, corr_fact):
    data = loadtxt('Figura 6.txt')
    inputs = data[:, :2]
    outputs = data[:, 2]
    interp = LinearNDInterpolator(inputs, outputs)
    return interp(conv_level, corr_fact)


def step_12(conv_level, corr_fact):
    data = loadtxt('Figura 7.txt')
    inputs = data[:, :2]
    outputs = data[:, 2]
    interp = LinearNDInterpolator(inputs, outputs)
    return interp(conv_level, corr_fact)


def step_13():
    return step_11(conversion_level, correlation_factor) * step_12(conversion_level, correlation_factor)


def step_14():
    return step_11(conversion_level, correlation_factor) - step_13()


def step_15():
    names = []
    avg = []
    feed = []
    total = round(step_14(), 2)
    with open('Tabelul 2.txt', 'r') as f:
        for line in f:
            if "#" not in line:
                names.append(line.split()[0])
                avg.append(float(line.split()[1]))
    for i in range(len(names)):
        feed.append(round(avg[i] * total / avg[len(avg) - 1], 2))
    return feed


def step_16(corr_factor):
    data = loadtxt('Figura 8.txt')
    x = data[:, 0]
    y = data[:, 1]
    f = interp1d(x, y)
    return S * f(corr_factor)


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
    return interp(conv_level, corr_fact)


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
    return step_19() * (light_cycle_SG / SG)


def step_21():
    return SG * ((step_18() + factor(conversion_level, correlation_factor) - step_20(conversion_level,
                                                                                     correlation_factor)) / decant)


def step_22():
    component = ['Hidrogen', 'Metan', 'Etena', 'Etan', 'Propena', 'Propan', 'Butena', 'Izobutena', 'Butan', 'C5',
                 'Ulei usor', 'Ulei de decantare', 'Cocs', 'H2S', 'Total']
    vol = calc = normalized = [0] * len(component)
    SG = [0.0] * 4 + [0.522, 0.5077, 0.6013, 0.5631, 0.5844, 0.7447, 0.9309, 1.0255] + [0.0] * 2 + [0.8996]
    vol[4] = propene_yield
    vol[5] = propane_yield
    vol[6] = butene_yield
    vol[7] = isobutane_yield
    vol[8] = butane_yield
    vol[9] = step_4()
    vol[10] = step_19()
    vol[11] = decant
    vol[14] = sum(vol[i] for i in range(len(vol) - 1))
    print(vol)


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
propene_yield, propane_yield = step_9(corr_factor=correlation_factor)
print('Randamentul de propena, in % volumice: ', propene_yield)
print('Randamentul de C3, mai putin propena: ', propane_yield)
butene_yield, butane_yield, isobutane_yield = step_10(corr_factor=correlation_factor)
print('Randamentul de butena, in % volumice: ', butene_yield)
print('Randamentul de butan, in % volumice: ', butane_yield)
print('Randamentul de izobutan, in %volumice: ', isobutane_yield)
print('Randamentul de cocs, C2 si hidrocarburi usoare: ', step_11(conversion_level, correlation_factor))
print('Raportul dintre cantitatea de cocs si cantitatea de cocs, C2 si hidrocarburi usoare: ',
      step_12(conversion_level, correlation_factor))
print('Randamentul de cocs, in % volumice: ', step_13())
print('Randamentul de C2 si hidrocarburi usoare, in % volumice: ', step_14())
alimentare = step_15()
print('Alimentarea cu hidrogen: ', alimentare[0])
print('Alimentarea cu metan: ', alimentare[1])
print('Alimentarea cu etena: ', alimentare[2])
print('Alimentarea cu etan:', alimentare[3])
print('Total in alimentare: ', alimentare[4])
print('Raportul de H2S, in % volumice: ', step_16(correlation_factor))
print('Cantitatea de benzina, in % masice: ', step_17(conversion_level, correlation_factor))
print('Randamentul de ulei, in % volumice: ', step_18() + factor(conversion_level, correlation_factor))
print('Randamentul de ulei usor, in % volumice: ', step_19())
print('Randamentul de ulei usor, in % masice: ', step_20(conversion_level, correlation_factor))
print('Greutatea specifica e uleiului decantat: ', step_21())
print('De rezolvat pasii 22 si 23', step_22())
COM, COR = step_24()
print('COM: ', COM)
print('COR: ', COR)
