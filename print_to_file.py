import backend as b


def print_to_file():
    print('Factorul de corelare: ', b.correlation_factor)
    print('Randamentul de C3 la 400F, in % volumice: ', b.c3_yield)
    print('Raportul dintre randamentul de C5, la 400F si randamentul de C3 la 400F: ', b.c5_c3_yield)
    print('Randamentul de C5 la 400F, in % volumice: ', b.c5_yield)
    print('Randamentul de C3+C4 la 400F, in % volumice: ', b.c3_c4_yield)
    print('Raportul dintre cantitatea totala de C4 si cantitatea totala de C3: ', b.c4_c3_yield)
    print('Randamentul total de C3, in % volumice: ', b.c3_total_yield)
    print('Randamentul total de C4, in % volumice: ', b.c4_total_yield)
    print('Randamentul de propena, in % volumice: ', b.propene_yield)
    print('Randamentul de C3, mai putin propena: ', b.propane_yield)
    print('Randamentul de butena, in % volumice: ', b.butene_yield)
    print('Randamentul de butan, in % volumice: ', b.butane_yield)
    print('Randamentul de izobutan, in %volumice: ', b.isobutane_yield)
    print('Randamentul de cocs, C2 si hidrocarburi usoare: ', b.coke_c2_light_yield)
    print('Raportul dintre cantitatea de cocs si cantitatea totala de cocs, C2 si hidrocarburi usoare: ',
          b.coke_total_coke_c2_light_yield)
    print('Randamentul de cocs, in % volumice: ', b.coke_yield)
    print('Randamentul de C2 si hidrocarburi usoare, in % volumice: ', b.c2_light_yield)
    print('Alimentarea cu hidrogen: ', b.alimentare[0])
    print('Alimentarea cu metan: ', b.alimentare[1])
    print('Alimentarea cu etena: ', b.alimentare[2])
    print('Alimentarea cu etan:', b.alimentare[3])
    print('Total in alimentare: ', b.alimentare[4])
    print('Raportul de H2S, in % volumice: ', b.h2s_yield)
    print('Cantitatea de benzina, in % masice: ', b.gasoline_yield)
    print('Randamentul de ulei, in % volumice: ', b.oil_yield)
    print('Randamentul de ulei usor, in % volumice: ', b.light_oil_yield_volume)
    print('Randamentul de ulei usor, in % masice: ', b.light_oil_yield_mass)
    print('Greutatea specifica e uleiului decantat: ', b.decant_oil_SPG)
    print('Valori calculate: ', b.calculated_values)
    print('Valori normalizate: ', b.normalized_values)
    print('Randament, %masice: ', b.yield_wt)
    print('Randament, lb/h: ', b.yield_lb_h)
    print('Valori calculate, % masice: ', b.calc_wt)
    print('Valori calculate, lb/h: ', b.calc_lb_h)
    print('Valori normalizate, %masice: ', b.normalized_wt)
    print('Valori normalizate, lb/h: ', b.normalized_lb_h)
    print('COM: ', b.COM)
    print('COR: ', b.COR)
