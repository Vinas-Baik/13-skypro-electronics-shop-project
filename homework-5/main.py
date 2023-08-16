from src.keyboard import Keyboard

if __name__ == '__main__':

    #
    # НАЧАЛО ПРОГРАММЫ
    #

    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.language) == "EN"
    print(kb.my_str())
    print()
    print(' \033[33mМеняем язык на RU \033[39m')
    kb.change_lang()
    assert str(kb.language) == "RU"
    print(kb.my_str())
    # Сделали RU -> EN -> RU
    # kb.change_lang()
    # kb.change_lang()
    print()
    print(' \033[33mМеняем язык на EN -> RU\033[39m')
    kb.change_lang().change_lang()
    print(kb.my_str())
    print()
    assert str(kb.language) == "RU"
    print(' \033[33mМеняем язык на CH\033[39m')
    try:
        kb.language = 'CH'
        # AttributeError: property 'language' of 'Keyboard' object has no setter
    except ValueError as v_err:
        print(f'\033[31m{v_err.args[0]}\033[39m')

    #
    # КОНЕЦ ПРОГРАММЫ
    #
