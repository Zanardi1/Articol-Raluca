import backend as b
import tabulate as t


def print_to_file():
    header = ['Marime', 'Valoare']
    data = {'Factorul de corelare: ': b.correlation_factor, 'Randamentul de C3 la 400F, in % volumice: ': b.c3_yield,
            'Raportul dintre randamentul de C5, la 400F si randamentul de C3 la 400F: ': b.c5_c3_yield,
            'Randamentul de C5 la 400F, in % volumice: ': b.c5_yield,
            'Randamentul de C3+C4 la 400F, in % volumice: ': b.c3_c4_yield,
            'Raportul dintre cantitatea totala de C4 si cantitatea totala de C3: ': b.c4_c3_yield,
            'Randamentul total de C3, in % volumice: ': b.c3_total_yield,
            'Randamentul total de C4, in % volumice: ': b.c4_total_yield,
            'Randamentul de propena, in % volumice: ': b.propene_yield,
            'Randamentul de C3, mai putin propena: ': b.propane_yield,
            'Randamentul de butena, in % volumice: ': b.butene_yield,
            'Randamentul de butan, in % volumice: ': b.butane_yield,
            'Randamentul de izobutan, in %volumice: ': b.isobutane_yield,
            'Randamentul de cocs, C2 si hidrocarburi usoare: ': b.coke_c2_light_yield,
            'Raportul dintre cantitatea de cocs si cantitatea totala de cocs, C2 si hidrocarburi usoare: ': b.coke_total_coke_c2_light_yield,
            'Randamentul de cocs, in % volumice: ': b.coke_yield,
            'Randamentul de C2 si hidrocarburi usoare, in % volumice: ': b.c2_light_yield,
            'Alimentarea cu hidrogen: ': b.alimentare[0],
            'Alimentarea cu metan: ': b.alimentare[1],
            'Alimentarea cu etena: ': b.alimentare[2],
            'Alimentarea cu etan:': b.alimentare[3],
            'Total in alimentare: ': b.alimentare[4],
            'Raportul de H2S, in % volumice: ': b.h2s_yield,
            'Cantitatea de benzina, in % masice: ': b.gasoline_yield,
            'Randamentul de ulei, in % volumice: ': b.oil_yield,
            'Randamentul de ulei usor, in % volumice: ': b.light_oil_yield_volume,
            'Randamentul de ulei usor, in % masice: ': b.light_oil_yield_mass,
            'Greutatea specifica e uleiului decantat: ': b.decant_oil_SPG,
            'COM: ': b.COM,
            'COR: ': b.COR}

    print(t.tabulate(tabular_data=data.items(), headers=header, tablefmt='github'))
    print('Valori calculate: ', b.calculated_values)
    print('Valori normalizate: ', b.normalized_values)
    print('Randament, %masice: ', b.yield_wt)
    print('Randament, lb/h: ', b.yield_lb_h)
    print('Valori calculate, % masice: ', b.calc_wt)
    print('Valori calculate, lb/h: ', b.calc_lb_h)
    print('Valori normalizate, %masice: ', b.normalized_wt)
    print('Valori normalizate, lb/h: ', b.normalized_lb_h)
