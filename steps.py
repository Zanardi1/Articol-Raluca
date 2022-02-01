import backend as b
import conversions as c


def step_1(VABP, S, AP, SG):
    return 75 - 0.065 * VABP - 0.9 * S + 0.6 * AP - 0.26 * (AP / SG)


def step_2(conv_level, corr_fact):
    f = b.interp_2d('Figura 1.txt')
    return f(conv_level, corr_fact)


def step_3(corr_factor):
    f = b.interp_1d('Figura 2.txt')
    return f(corr_factor)


def step_4():
    return b.c3_yield * b.c5_c3_yield


def step_5():
    return b.c3_yield - b.c5_yield


def step_6(corr_factor):
    f = b.interp_1d('Figura 3.txt')
    return f(corr_factor)


def step_7():
    return b.c3_c4_yield / (1 + b.c4_c3_yield)


def step_8():
    return b.c3_c4_yield - b.c3_total_yield


def step_9(corr_factor):
    f = b.interp_1d('Figura 4.txt')
    c3_composition = f(corr_factor)
    return c3_composition * b.c3_total_yield, b.c3_total_yield - c3_composition * b.c3_total_yield


def step_10(corr_factor):
    f = b.interp_1d('Figura 5.txt')
    butene_composition = f(corr_factor)
    butane_composition = 0.125  # Valoare luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv
    return butene_composition * b.c4_total_yield, butane_composition * b.c4_total_yield, b.c4_total_yield - b.c4_total_yield * (
            butene_composition + butane_composition)


def step_11(conv_level, corr_fact):
    f = b.interp_2d('Figura 6.txt')
    return f(conv_level, corr_fact)


def step_12(conv_level, corr_fact):
    f = b.interp_2d('Figura 7.txt')
    return f(conv_level, corr_fact)


def step_13():
    return b.coke_c2_light_yield * b.coke_total_coke_c2_light_yield


def step_14():
    return b.coke_c2_light_yield - b.coke_yield


def step_15():
    feed = []
    total = round(step_14(), 2)
    names, avg = b.read_table_2()
    for i in range(len(names)):
        feed.append(round(avg[i] * total / avg[len(avg) - 1], 2))
    return names, avg, feed


def step_16(corr_factor):
    f = b.interp_1d('Figura 8.txt')
    return b.initial_sulfur_content * f(corr_factor)


def step_17(conv_level, corr_fact):
    API = b.interp_2d('Figura 9.txt')
    gasoline_gravity = 141.5 / (API(conv_level, corr_fact) + 131.5)
    return b.c5_yield * (gasoline_gravity / b.initial_specific_gravity)


def step_18():
    return 100 - b.conversion_level


def step_19():
    return step_18() - b.decant


def step_20(conv_level, corr_fact):
    f = b.interp_2d('Figura 11.txt')
    API = f(conv_level, corr_fact)
    light_cycle_API = 25.8 - API
    light_cycle_SG = c.convert_API_to_SG(light_cycle_API)
    return b.light_oil_yield_volume * (light_cycle_SG / b.initial_specific_gravity)


def step_21():
    return b.initial_specific_gravity * (
            (step_18() + b.factor(b.conversion_level, b.correlation_factor) - b.light_oil_yield_mass) / b.decant)


def step_22():
    component = ['Hidrogen', 'Metan', 'Etena', 'Etan', 'Propena', 'Propan', 'Butena', 'Izobutena', 'Butan', 'C5',
                 'Ulei usor', 'Ulei de decantare', 'Cocs', 'H2S', 'Total']

    vol = b.compute_vol(len(component))
    specific_gravity = b.compute_specific_gravity(vol)
    calc = b.compute_calc(len(component), vol=vol, specific_gravity=specific_gravity)
    normalized = b.compute_normalized(len(component), calc=calc)
    return component, vol, specific_gravity, calc, normalized


def step_23():
    component = ['Benzina', 'Ulei usor', 'Ulei de decantare', 'Cocs', 'Total', 'Sulf in H2S', 'Total sulf']
    feed_rate = b.feed_rate * 7.491 * 42 / 24
    sulfur_in_feed = feed_rate * b.initial_sulfur_content / 100
    H2S_yield = feed_rate * step_16(corr_factor=b.correlation_factor) / 100
    sulfur_in_H2S = H2S_yield * 32 / 34

    yield_wt = b.compute_yield_wt(len(component))
    yield_lb_h = b.compute_yield_lb_h(len(component), feed_rate=feed_rate, yield_wt=yield_wt)
    calc_wt = b.compute_calc_wt()
    calc_lb_h = b.compute_calc_lb_h(len(component), yield_lb_h=yield_lb_h, calc_wt=calc_wt)
    normalized_lb_h = b.compute_normalized_lb_h(len(component), sulfur_in_H2S=sulfur_in_H2S,
                                                sulfur_in_feed=sulfur_in_feed, calc_lb_h=calc_lb_h)
    normalized_wt = b.compute_normalized_wt(len(component), calc_wt=calc_wt, normalized_lb_h=normalized_lb_h,
                                            calc_lb_h=calc_lb_h)

    return component, yield_wt, yield_lb_h, calc_wt, calc_lb_h, normalized_wt, normalized_lb_h


def step_24():
    return b.compute_MON(corr_level=b.conversion_level, corr_fact=b.correlation_factor), b.compute_RON(
        corr_level=b.conversion_level,
        corr_fact=b.correlation_factor)
