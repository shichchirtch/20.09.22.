class Vector:

    def __init__(self, *args):
        self.arr = list(args)

    def __len__(self):
        return len(self.arr)

    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other):
                new_arr = zip(self.arr, other.arr)
                f_arr = []
                for x in new_arr:
                    f_arr.append(sum(x))
                return Vector(*f_arr)
            else:
                raise TypeError('размерности векторов не совпадают')

    def __sub__(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other):
                new_arr = zip(self.arr, other.arr)
                f_arr = []
                for x in new_arr:
                    f_arr.append(x[0] - x[1])
                return Vector(*f_arr)
            else:
                raise TypeError('размерности векторов не совпадают')

    def get_coords(self):
        return tuple(self.arr)


class VectorInt(Vector):

    def __init__(self, *args):
        if all(type(x) == int for x in args):
            super().__init__(*args)
        else:
            raise ValueError('координаты должны быть целыми числами')

    def __add__(self, other):
        if isinstance(other, VectorInt):
            if len(self) == len(other):
                new_arr = zip(self.arr, other.arr)
                f_arr = []
                for x in new_arr:
                    f_arr.append(sum(x))
                return VectorInt(*f_arr)
            else:
                raise TypeError('размерности векторов не совпадают')
        elif isinstance(other, Vector) and not all(type(x) == int for x in other.arr):
            if len(self) == len(other):
                new_arr = zip(self.arr, other.arr)
                f_arr = []
                for x in new_arr:
                    f_arr.append(sum(x))
                return Vector(*f_arr)
            else:
                raise TypeError('размерности векторов не совпадают')

        elif isinstance(other, Vector) and all(type(x) == int for x in other.arr):
            if len(self) == len(other):
                new_arr = zip(self.arr, other.arr)
                f_arr = []
                for x in new_arr:
                    f_arr.append(sum(x))
                return VectorInt(*f_arr)
            else:
                raise TypeError('размерности векторов не совпадают')

    def __sub__(self, other):
        if isinstance(other, VectorInt):
            if len(self) == len(other):
                new_arr = zip(self.arr, other.arr)
                f_arr = []
                for x in new_arr:
                    f_arr.append(x[0] - x[1])
                return VectorInt(*f_arr)
            else:
                raise TypeError('размерности векторов не совпадают')
        elif isinstance(other, Vector) and not all(type(x) == int for x in other.arr):
            if len(self) == len(other):
                new_arr = zip(self.arr, other.arr)
                f_arr = []
                for x in new_arr:
                    f_arr.append(x[0] - x[1])
                return Vector(*f_arr)
            else:
                raise TypeError('размерности векторов не совпадают')
        elif isinstance(other, Vector) and  all(type(x) == int for x in other.arr):
            if len(self) == len(other):
                new_arr = zip(self.arr, other.arr)
                f_arr = []
                for x in new_arr:
                    f_arr.append(x[0] - x[1])
                return VectorInt(*f_arr)
            else:
                raise TypeError('размерности векторов не совпадают')


v = VectorInt(1, 2, 3)
d = Vector(4, 5, 6)
s = v - d
print(s.get_coords())
# v = VectorInt(1, 2, 3, 4)
# v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')
