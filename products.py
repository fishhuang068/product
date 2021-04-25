# 建立記帳程式專案 (二維清單)

products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    price = int(price)
    #p = []
    #p.append(name)
    #p.append(price)
    
    products.append([name, price])
# print(products)
  
# print(products[0])
# print(products[0][0])
# print(products[0][1])

for p in products:
    print(p[0], '的價格', p[1])
  
with open('products.csv', 'w', encoding = 'utf-8') as f:
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')
        