#Создайте программу для игры с конфетами человек против человека.
import random
candy = 100 

def take_candy(candy_left): 
    while True:
        candy_taken = int(input('сколько конфет берём?'))
        if 0 <= candy_taken <= 28 and candy_taken <= candy_left:
            return candy_taken

        else:
            print('Можно брать от 1 до 28, но не больше, чем осталось')
            continue

def who_first():                  
    if random.randint(0, 1) == 1:
        user_tag = 'игрок_1'
        print('Первый ход', user_tag)
        return user_tag
    else:
        user_tag = 'игрок_2'
        print('Первый ход', user_tag)
        return user_tag

def desk_view(user_tag, candy):  
    print('*'*80)
    print('Осталось', candy, 'конфет, ход ', user_tag)
    print('_'*80)

def move():  
    print('@'*80)
    user_tag = who_first()
    candy_left = candy
    desk_view(user_tag, candy_left)
    while candy_left > 0:
        candy_left = candy_left - take_candy(candy_left)
        if candy_left <= 0:
            break
        if user_tag == 'игрок_1':
            user_tag = 'игрок_2'
        else:
            user_tag = 'игрок_1'
        desk_view(user_tag, candy_left)
    desk_view(user_tag, 0)
    print('Победил: ', user_tag)

if __name__ == '__main__':
    move()                    
