#Создайте программу для игры в "Крестики-нолики".
doska = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
win = [(7, 4, 1), (8, 5, 2), (9, 6, 3), (1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (7, 5, 3)] 

def doska_view(): 
    print('___________________')
    for i in range(2, -1, -1):
        print('| ', doska[0 + i*3], ' | ',
              doska[1 + i*3], ' | ', doska[2 + i*3], ' |')
        print('___________________')

def input_cell(user_tag): 
    while True:
        cell = input("выберите свободную клетку для " + user_tag + ' - ')
        if cell not in '123456789':
            print('Неверный ввод!')
            continue
        if str(doska[int(cell) - 1]) in 'X0':
            print('Клетка занята!')
            continue
        doska[int(cell)-1] = user_tag
        break

def winner():  
    for cort in win:
        if doska[cort[0]-1] == doska[cort[1]-1] == doska[cort[2]-1]:
            return doska[cort[0]-1]
    else:
        return False

def main():
    count = 0
    while True:
        doska_view()
        if count % 2 == 0:
            input_cell('X')
        else:
            input_cell('0')
        if count > 3:
            who = winner()
            if who:
                doska_view()
                print('Победа!', who)
                break
        count += 1
        if count > 8:
            doska_view()
            print('Ничья!')  
            break

if __name__ == '__main__':
    main()
