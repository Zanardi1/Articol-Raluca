import backend as b
import engine as e


def step_1(VABP, S, AP, SG):
    return 75 - 0.065 * VABP - 0.9 * S + 0.6 * AP - 0.26 * (AP / SG)


def step_2(conv_level, corr_fact):
    f = b.interp_2d('Figura 1.txt')
    return f(conv_level, corr_fact)


def step_3(corr_factor):
    f = b.interp_1d('Figura 2.txt')
    return f(corr_factor)


def step_4():
    return step_2(b.conversion_level, b.correlation_factor) * step_3(b.correlation_factor)


def step_5():
    return step_2(b.conversion_level, b.correlation_factor) - step_4()


def step_6(corr_factor):
    f = b.interp_1d('Figura 3.txt')
    return f(corr_factor)


def step_7():
    return step_5() / (1 + step_6(b.correlation_factor))


def step_8():
    return step_5() - step_7()


def step_9(corr_factor):
    f = b.interp_1d('Figura 4.txt')
    c3_composition = f(corr_factor)
    return c3_composition * step_7(), step_7() - c3_composition * step_7()


def step_10(corr_factor):
    f = b.interp_1d('Figura 5.txt')
    butene_composition = f(corr_factor)
    butane_composition = 0.125  # Valoare luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv
    return butene_composition * step_8(), butane_composition * step_8(), step_8() - step_8() * (
            butene_composition + butane_composition)


def step_11(conv_level, corr_fact):
    f = b.interp_2d('Figura 6.txt')
    return f(conv_level, corr_fact)


def step_12(conv_level, corr_fact):
    f = b.interp_2d('Figura 7.txt')
    return f(conv_level, corr_fact)


def step_13():
    return step_11(b.conversion_level, b.correlation_factor) * step_12(b.conversion_level, b.correlation_factor)


def step_14():
    return step_11(b.conversion_level, b.correlation_factor) - step_13()


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
    f = b.interp_1d('Figura 8.txt')
    return b.S * f(corr_factor)


def step_17(conv_level, corr_fact):
    API = b.interp_2d('Figura 9.txt')
    gasoline_gravity = 141.5 / (API(conv_level, corr_fact) + 131.5)
    return step_4() * (gasoline_gravity / b.SG)


def step_18():
    return 100 - b.conversion_level


def step_19():
    return step_18() - b.decant


def step_20(conv_level, corr_fact):
    f = b.interp_2d('Figura 11.txt')
    API = f(conv_level, corr_fact)
    light_cycle_API = 25.8 - API
    light_cycle_SG = 141.5 / (light_cycle_API + 131.5)
    return step_19() * (light_cycle_SG / b.SG)


def step_21():
    return b.SG * ((step_18() + b.factor(b.conversion_level, b.correlation_factor) - step_20(b.conversion_level,
                                                                                             b.correlation_factor)) / b.decant)


def step_22():
    component = ['Hidrogen', 'Metan', 'Etena', 'Etan', 'Propena', 'Propan', 'Butena', 'Izobutena', 'Butan', 'C5',
                 'Ulei usor', 'Ulei de decantare', 'Cocs', 'H2S', 'Total']
    vol = [0.0] * len(component)
    calc = [0.0] * len(component)
    normalized = [0.0] * len(component)
    specific_gravity = [0.0] * 4 + [0.522, 0.5077, 0.6013, 0.5631, 0.5844, 0.7447, 0.9309, 1.0255] + [0.0] * 3
    vol[4] = b.propene_yield
    vol[5] = b.propane_yield
    vol[6] = b.butene_yield
    vol[7] = b.isobutane_yield
    vol[8] = b.butane_yield
    vol[9] = step_4()
    vol[10] = step_19()
    vol[11] = b.decant
    vol[14] = sum(vol[i] for i in range(len(vol) - 1))
    specific_gravity[14] = sum(specific_gravity[i] * vol[i] for i in range(len(vol) - 1)) / 100
    for i in range(4):
        calc[i] = b.alimentare[i]
    for i in range(4, 9):
        calc[i] = vol[i] * specific_gravity[i]
    calc[9] = step_17(conv_level=b.conversion_level, corr_fact=b.correlation_factor)
    calc[10] = step_20(conv_level=b.conversion_level, corr_fact=b.correlation_factor)
    calc[11] = (step_18() + b.factor(b.conversion_level, b.correlation_factor) - step_20(b.conversion_level,
                                                                                         b.correlation_factor))
    calc[12] = step_13()
    calc[13] = step_16(corr_factor=b.correlation_factor)
    calc[14] = sum(calc[i] for i in range(len(calc) - 1))
    for i in range(len(normalized) - 1):
        normalized[i] = calc[i] * 100 / calc[14]
    normalized[14] = sum(normalized[i] for i in range(len(normalized) - 1))
    return calc, normalized


def step_23():
    component = ['Benzina', 'Ulei usor', 'Ulei de decantare', 'Cocs', 'Total', 'Sulf in H2S', 'Total sulf']
    feed_rate = b.feed * 7.491 * 42 / 24
    sulfur_in_feed = feed_rate * b.S / 100
    H2S_yield = feed_rate * step_16(corr_factor=b.correlation_factor) / 100
    sulfur_in_H2S = H2S_yield * 32 / 34
    yield_wt = [0.0] * len(component)
    yield_lb_h = [0.0] * len(component)
    calc_wt = [0.1, 1, 2.5, 2.5]
    calc_lb_h = [0.0] * len(component)
    normalized_wt = [0.0] * len(component)
    normalized_lb_h = [0.0] * len(component)
    for i in range(4):
        yield_wt[i] = b.calculated_values[i + 9]
        yield_lb_h[i] = feed_rate * yield_wt[i] / 100
        calc_lb_h[i] = yield_lb_h[i] * calc_wt[i] / 100
    yield_wt[4] = sum(yield_wt[i] for i in range(4))
    yield_lb_h[4] = sum(yield_lb_h[i] for i in range(4))
    calc_lb_h[4] = sum(calc_lb_h[i] for i in range(4))
    normalized_lb_h[5] = sulfur_in_H2S
    normalized_lb_h[6] = sulfur_in_feed
    normalized_lb_h[4] = normalized_lb_h[6] - normalized_lb_h[5]
    for i in range(4):
        normalized_wt[i] = calc_wt[i] * normalized_lb_h[4] / calc_lb_h[4]
        normalized_lb_h[i] = calc_lb_h[i] * normalized_lb_h[4] / calc_lb_h[4]
    return yield_wt, yield_lb_h, calc_wt, calc_lb_h, normalized_wt, normalized_lb_h


def step_24():
    return b.compute_MON(corr_level=b.conversion_level, corr_fact=b.correlation_factor), b.compute_RON(
        corr_level=b.conversion_level,
        corr_fact=b.correlation_factor)
