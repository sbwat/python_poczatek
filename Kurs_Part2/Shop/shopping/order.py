from .inventory import stan

orders=[]
def create_new_order():
    name=input("Co chcesz włożyć do koszyka?")
    volume=int(input(f"Ile {name} chcesz wziąć?"))
    # return (name, volume)
    price=stan[name]["price"]
    availible = stan[name]["quantity"]

    if availible<volume:
        print("Brak tego towaru w sklepie.")
        return None

    total_price=price*volume
    new_order={
        "product": name,
        "quantity": volume,
        "total_price":total_price
    }
    orders.append(new_order)
    print(orders)
    return new_order
