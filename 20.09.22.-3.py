class ListInteger(list):
    def __init__(self, data=None):
        if data == None:
            self.arr = list()
        elif all(type(x) == int for x in data):
            super().__init__(data)
            self.arr = list(data)
        else:
            raise TypeError('можно передавать только целочисленные значения')

    def __str__(self):
        return f'{self.arr}'

    def __len__(self):
        return len(self.arr)

    def __getitem__(self, num):
        if num >= len(self):
            raise IndexError
        return self.arr[num]

    def __setitem__(self, num, value):
        if num >= len(self):
            raise IndexError
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')
        self.arr[num] = value

    def append(self, taily):
        if not isinstance(taily, int):
            raise TypeError('можно передавать только целочисленные значения')
        new_arr = [x for x in range(len(self) + 1)]
        for x in range(len(new_arr) - 1):
            new_arr[x] = self.arr[x]
        new_arr[-1] = taily
        self.arr = new_arr


d = ListInteger()
print(d)
s = ListInteger((1, 2, 3, 4, 5, 6, 7, 7))
# print(s)
s[1] = 10
print(s)
s.append(11)

s[0] = -10 # TypeError
print(s)
print(s[0])
