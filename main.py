def step_1():
    return 75 - 0.065 * VABP - 0.9 * S + 0.6 * AP - 0.26 * (AP / SG)


def step_2():
    return 92.5  # Valoare luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv


def step_3():
    return 0.68  # Valoare luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv


def step_4():
    return step_2() * step_3()


def step_5():
    return step_2() - step_4()


def step_6():
    return 1.69  # Valoare luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv


def step_7():
    return step_5() / (1 + step_6())


def step_8():
    return step_5() - step_7()


def step_9():
    c3_composition = 0.705  # Valoare luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv
    return c3_composition * step_7(), step_7() - c3_composition * step_7()


def step_10():
    butene_composition = 0.505  # Valoare luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv
    butane_composition = 0.125  # Valoare luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv
    return butene_composition * step_8(), butane_composition * step_8(), step_8() - butene_composition * step_8() - butane_composition * step_8()


def step_11():
    return 9  # Valoare luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv


def step_12():
    return 0.675  # Valoare luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv


def step_13():
    return step_11() * step_12()


def step_14():
    return step_11() - step_13()


def step_15():
    pass  # De vazut cum sa fac acest pas


def step_16():
    return S * 0.34  # Valoare luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv


def step_17():
    gasoline_gravity = 0.7447  # Valoare luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv
    return step_4() * (gasoline_gravity / SG)


def step_18():
    return 100 - conversion_level


# Valoarea de 1.15 e luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv

def step_19():
    return step_18() - decant


def step_20():
    return step_19() * (
            0.9309 / SG)  # Valoarea 0.9309 e luata dintr-un grafic. Sa vad daca pot discretiza graficul respectiv


def step_21():
    return SG * (step_18() - step_20() / decant)


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

print('Factorul de corelare: ', step_1())
print('Randamentul de C3 la 400F, in % volumice: ', step_2())
print('Raportul dintre randamentul de C5, la 400F si randamentul de C3 la 400F: ', step_3())
print('Randamentul de C5 la 400F, in % volumice: ', step_4())
print('Randamentul de C3+C4 la 400F, in % volumice: ', step_5())
print('Raportul dintre cantitiatea totala de C4 si cantitatea totala de C3: ', step_6())
print('Randamentul total de C3, in % volumice: ', step_7())
print('Randamentul total de C4, in % volumice: ', step_8())
print('Randamentul de propena, in % volumice: ', step_9())
print('Randamentul de butena, in % volumice: ', step_10())
print('Randamentul de cocs, C2 si hidrocarburi usoare: ', step_11())
print('Raportul dintre cantitatea de cocs si cantitatea de cocs, C2 si hidrocarburi usoare: ', step_12())
print('Randamentul de cocs, in % volumice: ', step_13())
print('Randamentul de C2 si hidrocarburi usoare, in % volumice: ', step_14())
print('De lucrat la pasul 15')
print('Raportul de H2S, in % volumice: ', step_16())
print('Cantitatea de benzina, in % masice: ', step_17())
print('Randamentul de ulei, in % volumice: ', step_18() + 1.15)
print('Randamentul de ulei usor, in % volumice: ', step_19())
print('Randamentul de ulei usor, in % masice: ', step_20())
print('Greutatea specifica e uleiului decantat: ', step_21())
print('De rezolvat pasii 22 si 23')
print('Cifrele octanice: ', step_24())
