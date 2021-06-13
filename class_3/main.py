from class_3.classes import Store, Television

store = Store()

samsung_tv = Television(name='MX5000', brand='Samsung', screen_size=65)
store.add_tv(samsung_tv)

sony_tv = Television(name='BUGH', brand='Sony', screen_size=50)
store.add_tv(sony_tv)
print(store.store_stock)

try:
    # try to sell a camera
    store.sell('Camera')
except ValueError:
    # catch the exception if there are no cameras, and buy a TV instead
    store.sell('TV')

print(store.store_stock)




