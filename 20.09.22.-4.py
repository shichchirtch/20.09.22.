class Thing:
    def __init__(self, name, price, weight):
        self.name, self.price, self.weight = name, price, weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))

class DictShop(dict):
    def __init__(self, obj = None):
        obj = {} if obj == None else obj
        if not isinstance(obj, dict):
            raise TypeError('аргумент должен быть словарем')

        if obj and not all(isinstance(key, Thing) for key in obj):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__init__(obj)

    def __setitem__(self, key, value):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key, value)


