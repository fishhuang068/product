# 建立記帳程式專案 (二維清單)

#讀取檔案
products = []
with open('products.csv', 'r', encoding = 'big5') as f:
    for line in f:
        if '商品,價格' in line:
            continue
        #s = line.strip().split(',')
        #print(s)
        name, price = line.strip().split(',')
        products.append([name, price])
print(products)
        
#讓使用者輸入        
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
print(products)
  
# print(products[0])
# print(products[0][0])
# print(products[0][1])

# 印出所有購買紀錄
for p in products:
    print(p[0], '的價格', p[1])
 
# 寫入檔案 
with open('products.csv', 'w', encoding = 'utf-8') as f:
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')
        