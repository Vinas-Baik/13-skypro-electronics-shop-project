from src.keyboard import Keyboard
from src.phone import Phone
from src.item import Item, nice_number_output

if __name__ == '__main__':

    #
    # НАЧАЛО ПРОГРАММЫ
    #

    print('\n\t\033[33mСоздаем описание клавиатуры: \033[39m')
    kb = Keyboard('Logitech', 2000)
    assert kb.language == 'EN'
    assert kb.quantity == 1
    print(repr(kb))
    print(kb.my_str())
    print()

    kb = Keyboard('Dark Project KD87A', 9600, 5)
    print(repr(kb))
    print()
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"
    print(kb.my_str())

    print('\n\t\033[33mМеняем язык на RU \033[39m')
    kb.change_lang()
    assert str(kb.language) == "RU"

    print(kb.my_str())
    # Сделали RU -> EN -> RU
    print('\n\t\033[33mМеняем язык на EN -> RU\033[39m')
    kb.change_lang().change_lang()
    print(kb.my_str())
    assert str(kb.language) == "RU"

    for t_lang in ('12    ', '   ch', 'en', 'EN', 'eN  ', '     Ru    ',
                   '   ru ', ' r u ', ' '):
        print(f'\n\t\033[33mМеняем язык на ({t_lang})\033[39m')
        try:
            kb.language = t_lang
            # AttributeError: property 'language' of 'Keyboard' object has no setter
        except ValueError as v_err:
            print(f'\t\033[31m{v_err.args[0]}\033[39m')
        finally:
            print(kb.my_str())

    print()
    phone1 = Phone("iPhone 14", 120_000, 15, 2)
    for item in Item.all:
        print(f'\033[33m{item.name}\033[39m '
              f'в количестве \033[33m{item.quantity} шт.\033[39m '
              f'по цене \033[32m{nice_number_output(item.price)} руб.\033[39m '
              f'Итоговая сумма = '
              f'\033[32m{nice_number_output(item.calculate_total_price())}'
              f' руб.\033[39m')
    print()
    assert kb + phone1 == 20
    print(f'Количество устройств \033[33m{kb}\033[39m и '
          f'\033[33m{phone1}\033[39m = \033[32m{kb + phone1}\033[39m')

    #
    # КОНЕЦ ПРОГРАММЫ
    #
