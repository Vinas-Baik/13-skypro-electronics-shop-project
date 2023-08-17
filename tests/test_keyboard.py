import src.keyboard as my_kb
import src.item as my_item
import pytest


def test_class_phone():
    temp_kb = my_kb.Keyboard('Logitech', 2000, 5)
    assert temp_kb.language == 'EN'
    assert repr(temp_kb) == "Keyboard('Logitech', 2000, 5, EN)"

    assert temp_kb.change_lang().language == 'RU'
    assert temp_kb.change_lang().change_lang().language == 'RU'
    assert temp_kb.my_str() == 'Logitech в количестве 5 шт по цене 2 000 руб. ' \
                               '- итоговая сумма 10 000 руб., установлен язык - RU'

    for t_lang in ('12    ', '   ch', ' '):
        with pytest.raises(ValueError):
            temp_kb.language = t_lang
