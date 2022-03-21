import json

def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', encoding='utf-8') as f_n:
        OBJ = json.load(f_n)

    dict_to_write = {}
    dict_to_write['товар'] = item
    dict_to_write['количество'] = quantity
    dict_to_write['цена'] = price
    dict_to_write['покупатель'] = buyer
    dict_to_write['дата'] = date

    OBJ['orders'].append(dict_to_write)

    with open('orders.json', 'w', encoding='utf-8') as f_n:
        json.dump(OBJ, f_n, indent=4, ensure_ascii=False)

write_order_to_json(1, 2, 3, 4, 5)
write_order_to_json('жёсткий диск', '8', '1000', 'Андрей Боеголов', '01.01.1970')