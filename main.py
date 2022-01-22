#Bankomat
choice = None
acc_balance = []
sum_cash = 0
login = 'user1'
password = '123'


log = input('Aby się zalogowac podaj Login: ')
paswd = input('Podaj Hasło: ')
if log == login and paswd == password and i != '2':
    while choice != '0':
        print('1 wplac pieniadze \n2 wyplac pieniadze \n3 stan konta \n4 historia tranzakcji \n5 zmiana loginu \n6 zmiana hasla \n7 wyloguj')
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
        if choice == '5':
            change_login = input('Na jaki login chcesz zmienic ? :')
            login = change_login
        if choice == '6':
            change_password = input('Na jakie haslo chcesz zmienic ?: ')
            change_password = password


