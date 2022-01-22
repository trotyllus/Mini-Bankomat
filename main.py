#Bankomat
choice = None
acc_balance = []
sum_cash = 0
while choice != '0' :
    print('1 wplac pieniadze \n2 wyplac pieniadze \n3 stan konta \n4 historia tranzakcji')
    choice = input('Co chcesz zrobic ?')
    if choice == '1':
        choice = input('Ile chcesz wplacic pieniazkow ?: ')
        acc_balance.append(int(choice))
    elif choice == '2':
        choice = input('Ile chcesz wyplacic pln ? : ')
        if int(choice) > int(sum(acc_balance)):
            print('Niestety nie mozesz wyplacic wiecej niz masz :(')
        else:
            acc_balance.append(-int(choice))
    if choice == '3' :
        print(sum(acc_balance))
    if choice == '4' :
        print(acc_balance)