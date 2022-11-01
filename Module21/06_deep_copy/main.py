import json
import copy
site = {
	'html': {
		'head': {
			'title': 'Куплю/продам телефон недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на iphone',
			'div': 'Купить',
			'p': 'продать'
		}
	}
}
def find_word(struct, find, meaning):
    if find in struct:
        struct[find] = meaning
        return site
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_word(sub_struct, find, meaning)
            if result:
                return site
numbers_sities = int(input('Сколько сайтов: '))
d_copy = {}
goods = {}
for _ in range(numbers_sities):
    product_name = input('Введите название продукта для нового сайта: ')
    check = {'title': f'Куплю/продам {product_name} недорого', 'h2': f'У нас самая низкая цена на {product_name}'}
    for count in check:
        find_word(site, count, check[count])
    name_of_product = f'Сайт для {product_name}:'
    d_copy = copy.deepcopy(site)
    goods[name_of_product] = d_copy
    for key, value in goods.items():
        print(key)
        print('site = ', end=' ')
        print(json.dumps(value, indent=8, ensure_ascii=False))