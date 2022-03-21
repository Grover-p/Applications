import yaml

data = {'object': ['product_1', 'product_2'],
           'object_quantity': 2,
           'object_price': {'product_1': '200₽', 'product_2': '100₽'}
           }

with open('yaml.yaml', 'w', encoding='utf-8') as f_in:
    yaml.dump(data, f_in, default_flow_style=False, allow_unicode=True, sort_keys=False)

with open("yaml.yaml", 'r', encoding='utf-8') as f_out:
    out_data = yaml.load(f_out, Loader=yaml.SafeLoader)

if data == out_data:
    print('Полное совпадение')
else:
    print('Что то пошло не так')