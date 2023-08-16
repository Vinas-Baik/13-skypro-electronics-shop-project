from src.item import Item

class Keyboard(Item):

    def __init__(self, name: str, price: float, quantity=1, language='EN'):
        super().__init__(name, price, quantity)
        self.language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, new_lng:str):
        if new_lng.upper() not in ('RU', 'EN'):
            raise ValueError('язык клавиатуры должен быть или RU или EN')
        self.__language = new_lng.upper()

    def change_lang(self):
        if self.language.upper() == 'RU':
            self.language = 'EN'
        if self.language.upper() == 'EN':
            self.language = 'RU'

    def __repr__(self):
        """
        метод __repr___
        """
        return (f"Keyboard('{self.name}', {self.price}, {self.quantity}, "
                f"{self.__language})")
