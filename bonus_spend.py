"""
Create a function that optimizes the spending of a bonus given a product list
"""
import itertools

product_list = {
    "i1": 100,
    "i2": 55.99,
    "i3": 129.76,
    "i4": 5,
    "i5": 3.3,
    "i6": 10.7,
    "i7": 50.7,
    "i8": 80,
    "i9": 1.3,
    "i10": 100,
    "i11": 100,
}
bonus = 300


def get_best_combination(price_list, bonus: float) -> list:
    result: dict = {}
    init: float = 0.0  # variable para poder comparar
    # Los siguientes dos FOR se utilizan para generar una combinacion
    # a partir de la lista_precios original
    for L in range(len(price_list) + 1):
        for list_combination in itertools.combinations(price_list, L):
            sum_of_prices = sum(list_combination)
            if sum_of_prices > init and sum_of_prices <= bonus:
                init = sum_of_prices
                # agrego un registro al diccionario con la llave correspondiente
                # a la suma de la lista y el valor como los elementos de la lista
                result.update({sum_of_prices: list_combination})

    # obtengo la ultima llave del diccionario ordenado de menor a mayor por llave
    last_key = list(dict(sorted(result.items())))[-1]
    # retorno la mejor combinacion
    return list(result[last_key])


def spend_bonus(products: dict, bonus: float) -> tuple:
    price_list:list = [price for price in products.values() if price <= bonus]
    best_price_combination = get_best_combination(price_list, bonus)
    # guardo la suma de la mejor lista
    total = sum(best_price_combination)
    # final_product_list  será el nuevo diccionario con los items para gastar el bono
    final_product_list = {}
    # el siguiente for se usa para recorrer la lista original de productos
    # si el precio del producto coincide con algun elemento de best_price_combination
    # se agrega ese producto con su precio a final_product_list
    for key, value in products.items():
        if value in best_price_combination:
            final_product_list.update({key: value})
            # si el valor es encontrado lo remuevo de la lista para evitar descuadres
            best_price_combination.remove(value)
    # retorno el diccionario con los items y el valor total
    return final_product_list, total


print(spend_bonus(product_list, bonus))
