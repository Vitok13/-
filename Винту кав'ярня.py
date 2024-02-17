def display_menu(menu):
    print("Меню:")
    for item, price in menu.items():
        print(f"{item}: {price} грн")


def add_new_item_to_menu(menu):
    while True:
        new_item = input("Введіть назву нового товару (або 'готово', щоб завершити): ")
        if new_item.lower() == 'готово':
            break
        price = float(input(f"Запропонуйте ціну '{new_item}': "))
        menu[new_item] = price
    print("Меню кав'ярні:")
    display_menu(menu)


def place_order(menu):
    order = {}
    total_cost = 0
    
    while True:
        item = input("Введіть назву товару (або 'готово', щоб завершити замовлення): ")
        if item.lower() == 'готово':
            break

        if item not in menu:
            print("Товар відсутній.")
            add_item = input("Бажаєте додати до меню? (так/ні): ")
            if add_item.lower() == 'так':
                price = float(input(f"Ціна за одиницю товару '{item}': "))
                menu[item] = price
            else:
                continue
        
        quantity = int(input(f"Введіть кількість '{item}': "))
        order[item] = quantity
        total_cost += menu[item] * quantity
    
    print("\nВаше замовлення:")
    for item, quantity in order.items():
        cost = menu[item] * quantity
        print(f"{item}: {quantity} шт. - {cost} грн")
    
    print(f"Загальна вартість замовлення: {total_cost} грн")

def main():
    menu = {
        "Американо": 45,
        "Еспресо": 25,
        "Чай": 25,
        "Латте": 40,
        "Капучіно": 28,
        "Какао": 35,
    }

    display_menu(menu)
    while True:
        choice = input("\nВведіть 'замовити' для оформлення замовлення, 'додати' для додавання нового товару, або 'готово' для виходу: ")
        if choice == 'замовити':
            place_order(menu)
        elif choice == 'додати':
            add_new_item_to_menu(menu)
        elif choice.lower() == 'готово':
            break
        else:
            print("Неправильний ввід. Спробуйте ще раз.")


if __name__ == "__main__":
    main()