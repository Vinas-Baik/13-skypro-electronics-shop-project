from src.item import Item

if __name__ == '__main__':

    # Файл ..\src\items.csv - оригинал
    # Файл ..\src\items-space_upper.csv - поля написаны с большой и маленькой
    #                                     буквы с пробелами справа и слева,
    #                                     значения полей также с пробелами
    # Файл ..\src\item.csv - не существует
    # Файл ..\src\items-err.csv - с ошибкой в имени поля
    # Файл ..\src\items-err01.csv - нет одного из полей
    # Файл ..\src\items-err02.csv - нет значений цены и количества
    # Файл ..\src\items-err03.csv - поле цены - не число
    for csv_name in ['..\src\items.csv',
                     '..\src\items-space_upper.csv',
                     '..\src\item.csv',
                     '..\src\items-err.csv',
                     '..\src\items-err01.csv',
                     '..\src\items-err02.csv',
                     '..\src\items-err03.csv']:
        print(f'\033[33mРаботаем с файлом: \033[34m{csv_name}\033[39m')
        print(Item.instantiate_from_csv(csv_name))
        if Item.all != []:
            print('Прочитано из файла:', end='\n\t')
            print('\n\t'.join(t_item.my_str() for t_item in Item.all))

