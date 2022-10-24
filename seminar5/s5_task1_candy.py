def players_mode(player1, player2):
    candy = int(input('Введите количество конфет: '))
    while candy > 0:
        take1 = int(input('Количество конфет, которое берет первый игрок (не более 28): '))
        while take1 <= 0 or take1 > 28:
            print('Брать можно не более 28 конфет!')
            take1 = int(input('Введите количество конфет, которое берет первый игрок: '))
        else:
            if 0 <= take1 <= 28:
                player1 = player1 + take1
                candy = candy - take1
                print(f'У первого игрока - {player1} конфет')
                print(f'В стопке осталось конфет: {candy}')
                if candy == 0:
                    player1 = player1 + player2
                    print(f'Первый игрок победил!\n Количество конфет: {player1}')
                    return
        take2 = int(input('Количество конфет, которое берет второй игрок: '))
        while take2 <= 0 or take2 > 28:
            print('Брать можно не более 28 конфет!')
            take2 = int(input('Количество конфет, которое берет второй игрок: '))
        else:
            if 0 <= take2 <= 28:
                player2 = take2 + player2
                candy = candy - take2
                print(f'У второго игрока - {player2} конфет')
                print(f'В стопке осталось конфет: {candy}')
                if candy == 0:
                    player2 = player2 + player1
                    print(f'Второй игрок победил!\n Количество конфет: {player2}')
                    return
                    
