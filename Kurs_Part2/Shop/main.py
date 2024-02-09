from shopping.order import create_new_order


def shop():
    print("Symulator sklepu.")
    total_price=0
    while True:
        mode = input("Rozpoczynamy zamawianie- wciśnij dowolny przycisk aby kontyunować, aby przerwać wpisz 'X'.")
        if mode == 'X':
            break
        result = create_new_order()
        if result is not None:
            total_price+=result['total_price']
            print(f"Łączny koszt twoich zakupów wyniesie {total_price} zł.")

if __name__ == '__main__':
    shop()
