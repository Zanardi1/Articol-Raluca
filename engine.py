import backend as b
import steps as s


def computing_engine():
    b.correlation_factor = s.step_1(VABP=b.VABP, S=b.S, AP=b.AP, SG=b.SG)
    b.c3_yield = s.step_2(b.conversion_level, b.correlation_factor)
    b.c5_c3_yield = s.step_3(b.correlation_factor)
    b.c5_yield = s.step_4()
    b.c3_c4_yield = s.step_5()
    b.c4_c3_yield = s.step_6(b.correlation_factor)
    b.c3_total_yield = s.step_7()
    b.c4_total_yield = s.step_8()
    b.propene_yield, b.propane_yield = s.step_9(corr_factor=b.correlation_factor)
    b.butene_yield, b.butane_yield, b.isobutane_yield = s.step_10(corr_factor=b.correlation_factor)
    b.coke_c2_light_yield = s.step_11(b.conversion_level, b.correlation_factor)
    b.coke_total_coke_c2_light_yield = s.step_12(b.conversion_level, b.correlation_factor)
    b.coke_yield = s.step_13()
    b.c2_light_yield = s.step_14()
    b.alimentare = s.step_15()
    b.h2s_yield = s.step_16(b.correlation_factor)
    b.gasoline_yield = s.step_17(b.conversion_level, b.correlation_factor)
    b.oil_yield = s.step_18() + b.factor(b.conversion_level, b.correlation_factor)
    b.light_oil_yield_volume = s.step_19()
    b.light_oil_yield_mass = s.step_20(b.conversion_level, b.correlation_factor)
    b.decant_oil_SPG = s.step_21()
    b.calculated_values, b.normalized_values = s.step_22()
    b.yield_wt, b.yield_lb_h, b.calc_wt, b.calc_lb_h, b.normalized_wt, b.normalized_lb_h = s.step_23()
    b.COM, b.COR = s.step_24()
