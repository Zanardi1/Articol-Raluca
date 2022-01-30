import backend as b
import tabulate as t


def print_to_file():
    with open('Rezultate.txt', 'w') as f:
        header, data = b.generate_non_tabular_content()
        f.write(t.tabulate(tabular_data=data.items(), headers=header, tablefmt='github', floatfmt='.2f') + '\n\n')

        headers_table_2, table_2 = b.generate_table_2_content()
        f.write('Tabelul 2: \n')
        f.write(t.tabulate(tabular_data=table_2, headers=headers_table_2, floatfmt='.2f', tablefmt='github') + '\n\n')

        headers_table_3, table_3 = b.generate_table_3_content()
        f.write('Tabelul 3: \n')
        f.write(t.tabulate(tabular_data=table_3, headers=headers_table_3, tablefmt='github', floatfmt='.2f') + '\n\n')

        headers_table_4, table_4 = b.generate_table_4_content()
        f.write('Tabelul 4: \n')
        f.write(t.tabulate(tabular_data=table_4, headers=headers_table_4, tablefmt='github', floatfmt='.2f') + '\n\n')
        f.write('A = Randament (% masice)\n')
        f.write('B = Debit (lb/h)\n')
        f.write('C = Continutul calculat de sulf (% masice)\n')
        f.write('D = Debitul calculat de sulf (lb/h)\n')
        f.write('E = Continutul normalizat de sulf (% masice)\n')
        f.write('F = Debitul normalizat de sulf (lb/h)')
