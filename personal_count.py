def refill(count_zero):
    e = float(input('Введите сумму, на которую вы хотите пополнить счет: '))
    count_zero = count_zero + e
    print(f'На вашем счету {count_zero} рублей')
    return count_zero


def purchase(count_zero, history_zero):
    summ_of_purchase = float(input('Введите сумму покупки: '))
    if summ_of_purchase > count_zero:
        print('Недостаточно средств')
    else:
        purchase = input('Введите наименование покупки')
        count_zero = count_zero - summ_of_purchase
        history_zero.append({'purchase': purchase, 'summ_of_purchase': summ_of_purchase})
        print(f'У вас осталось {count_zero} рублей')
    return count_zero, history_zero


def print_history(history_zero):
    print('История покупок: ')
    for i in history_zero:
        print(f'Товар : {i["purchase"]}; Цена: {i["summ_of_purchase"]}')


def call_personal_count():
    count = 0.0
    history = []

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            count = refill(count)
        elif choice == '2':
            count, history = purchase(count, history)
        elif choice == '3':
            print_history(history)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')