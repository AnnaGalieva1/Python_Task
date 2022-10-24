from dataclasses import Field, field


def playing_field(field):
    print('-' * 13)
    for i in range(3):
        print('|', field[0+i*3], '|', field[1+i*3], '|', field[2+i*3], '|')
        print('-' * 13)

def game_move(players):
    valid = False
    while not valid:
        player_answer = input('Куда поставим' + players+'?')
        try:
            player_answer = int(player_answer)
        except:
            print('Вводить числа от 1 до 9')
            continue
        if 1 <= player_answer <= 9:
            if str(field[player_answer-1]) not in 'xo':
                field[player_answer-1] = players
                valid = True
            else:
                print('Эта клетка уже занята!')
        else:
            print('Ввод чисел от 1 до 9')
def win(field):
    coordinates = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in coordinates:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False
def main(field):
    count = 0
    win = False
    while not win:
        playing_field(field)
        if count % 2 == 0:
            take_input('x')
        else:
            take_input('0')
        count += 1
        if count > 4:
            tmp = win(field)
            if tmp:
                print(tmp, 'Победа!')
                win = True
                break
        if count == 9:
            print('Ничья!')
            break
    playing_field(field)

if __name__ == '__main__':
    print('Игра крестики-нолики')
    field = list(range(1, 10))
    main(field)
            