import pandas as pd

print('----'*28)
print('Информация о классах')

class_card = {
        'Номер кабинета': ['178','23','25','132','57'],
        'Номер парты' : ['1','2','3','4','5'],
        'Ряд': ['1','2','3','4','5'],
        'ID' : ['01','02','03','04','05']
}
    
cc = pd.DataFrame(data = class_card)

with open('cabinet.csv', 'a', encoding='UTF-8') as cl:
        cl.write(f'{cc}')
        cl.write('\n')
    
print(cc)