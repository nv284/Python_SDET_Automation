# Small project: Inventory processing and simple report (no functions used)
print('=== Inventory Processor ===')

items = [
    {'id': 1, 'name': 'pen', 'qty': 10, 'price': 1.5},
    {'id': 2, 'name': 'notebook', 'qty': 5, 'price': 3.0},
    {'id': 3, 'name': 'eraser', 'qty': 0, 'price': 0.5},
    {'id': 4, 'name': 'marker', 'qty': 2, 'price': 2.0}
]

# Restock low items (qty <=2) by adding a restock amount
restock_amount = 10
for it in items:
    if it['qty'] <= 2:
        print('Restocking', it['name'], 'from', it['qty'], 'by', restock_amount)
        it['qty'] = it['qty'] + restock_amount

# Build inventory report
total_value = 0
out_of_stock = []
for it in items:
    value = it['qty'] * it['price']
    total_value += value
    if it['qty'] == 0:
        out_of_stock.append(it['name'])

print('\nInventory Report')
for it in items:
    print(it['id'], it['name'], 'qty=', it['qty'], 'value=', it['qty'] * it['price'])
print('Total inventory value:', total_value)
if out_of_stock:
    print('Out of stock items:', out_of_stock)
else:
    print('No out-of-stock items')
