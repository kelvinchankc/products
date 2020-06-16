products = []
while True:
	name = input('Please enter a product name: ')
	if name == 'quit':
		break
	price = input('Please enter the price of product: ')
	p = [name, price]
	#p = []
	#p.append(name)
	#p.append(price)
	products.append(p)
print(products)

for p in products:
	print(p)
	print(p[0], '的價格是', p[1])
