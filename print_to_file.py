import backend as b
import tabulate as t


def print_to_file():
    with open('Rezultate.txt', 'w') as f:
        header, data = b.generate_non_tabular_content()
        f.write(t.tabulate(tabular_data=data.items(), headers=header, tablefmt='github') + '\n\n')

        headers_table_2, table_2 = b.generate_table_2_content()
        f.write(t.tabulate(tabular_data=table_2, headers=headers_table_2) + '\n\n')

        headers_table_3, table_3 = b.generate_table_3_content()
        f.write(t.tabulate(tabular_data=table_3, headers=headers_table_3) + '\n\n')

        headers_table_4, table_4 = b.generate_table_4_content()
        f.write(t.tabulate(tabular_data=table_4, headers=headers_table_4) + '\n\n')
