from librip.gens import field

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'color': 'white'}
]
goods2 = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': None}]
# Реализация задания 1

print(", ".join([str(i) for i in field(goods, "title")]))
print(", ".join([str(i) for i in field(goods, "title", "price")]))
print(", ".join([str(i) for i in field(goods2, "title","price","color")]))
