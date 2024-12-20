menu = {
    'Hamburguesa' : 8.50,
    'Pizza' : 12.00,
    'Ensalada' : 7.00,
    'Sopa' : 5.00,
    'Refresco' : 2.50,
    'Cafe' : 1.80
}

pedidos = {
  'Juan':{'Hamburguesa': 2, 'Refresco': 1},
  'Ana':{'Cafe':3,'Sopa':4},
  'Paco':{'Cafe':3,'Sopa':1,'Hamburguesa': 5},
  'Luis':{'Ensalada':2,'Hot Dog': 2}
}


print ("Menú del restaurante")
for plato, precio in menu.items():
    print(f"{plato}: {precio} euros")
print("\n")


for cliente,pedido in pedidos.items():
    print(f"Pedido de: {cliente}")
    total_cliente = 0;

    for plato, cantidad in pedido.items():
        if plato in menu:
            precio = menu[plato] # acceder al precio de ese plato
            subtotal = precio * cantidad
            total_cliente += subtotal
            print(f" -  {cantidad}x{plato}: {subtotal}")
        else:
            print(f"El plato {plato} no está disponible")
    print(f" -  El pedido total del cliente es: {total_cliente} euros")