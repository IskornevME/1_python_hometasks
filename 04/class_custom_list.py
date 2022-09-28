'''
This programm realizes Customlist class
'''
class Customlist(list):
    '''
    This is Customlist class inherited from list
    '''
    def __init__(self, lst):
        if not isinstance(lst, list):
            raise TypeError("Аргумент должен иметь тип list")
        self.lst = lst


    @classmethod
    def modify_data(cls, other):
        '''
        Modify data if we use list
        '''
        if isinstance(other, Customlist):
            obj2 = other.lst
        else:
            obj2 = other
        return obj2


    @classmethod
    def check_data(cls, other):
        '''
        Check that our data has type list or Customlist
        '''
        if not isinstance(other, (list, Customlist)):
            raise TypeError("Объект должен иметь тип list или Customlist")


    def __add__(self, other):
        self.check_data(other)
        obj2 = self.modify_data(other)
        res = []
        diff = len(self.lst) - len(obj2)
        if diff > 0:
            for i in range(diff):
                obj2.append(0)
        else:
            for i in range(-diff):
                self.lst.append(0)

        for i, ele in enumerate(self.lst):
            res.append(ele + obj2[i])

        if diff > 0:
            del obj2[len(obj2) - diff: len(obj2)]
        elif diff != 0:
            self.lst = self.lst[0:diff]

        return Customlist(res)


    def __sub__(self, other):
        self.check_data(other)
        obj2 = self.modify_data(other)
        res = []
        diff = len(self.lst) - len(obj2)
        if diff > 0:
            for i in range(diff):
                obj2.append(0)
        else:
            for i in range(-diff):
                self.lst.append(0)

        for i, ele in enumerate(self.lst):
            res.append(ele - obj2[i])

        if diff > 0:
            del obj2 [len(obj2) - diff: len(obj2)]
        elif diff != 0:
            self.lst = self.lst[0:diff]
        return Customlist(res)


    def neg(self):
        '''
        Change sign of all elements
        '''
        for i, ele in enumerate(self.lst):
            self.lst[i] = -ele
        return self


    def __radd__(self, other):
        return self + other


    def __iadd__(self, other):
        self.check_data(other)
        obj2 = self.modify_data(other)
        diff = len(self.lst) - len(obj2)
        if diff > 0:
            for i in range(diff):
                obj2.append(0)
        else:
            for i in range(-diff):
                self.lst.append(0)
        for i, ele in enumerate(obj2):
            self.lst[i] += ele
        if diff > 0:
            del obj2[len(obj2) - diff: len(obj2)]
        return self


    def __isub__(self, other):
        self.check_data(other)
        obj2 = self.modify_data(other)
        diff = len(self.lst) - len(obj2)
        if diff > 0:
            for i in range(diff):
                obj2.append(0)
        else:
            for i in range(-diff):
                self.lst.append(0)
        for i, ele in enumerate(obj2):
            self.lst[i] -= ele
        if diff > 0:
            del obj2[len(obj2) - diff: len(obj2)]
        return self


    def __rsub__(self, other):
        return (self - other).neg()


    def customsum(self):
        '''
        Return sum of all elements
        '''
        res = 0
        for ele in self.lst:
            res += ele
        return res


    def __eq__(self, other):
        self.check_data(other)
        obj2 = self.modify_data(other)
        return self.customsum() == sum(obj2)


    def __ne__(self, other):
        self.check_data(other)
        obj2 = self.modify_data(other)
        return self.customsum() != sum(obj2)


    def __lt__(self, other):
        self.check_data(other)
        obj2 = self.modify_data(other)
        return self.customsum() < sum(obj2)


    def __gt__(self, other):
        self.check_data(other)
        obj2 = self.modify_data(other)
        return self.customsum() > sum(obj2)


    def __le__(self, other):
        self.check_data(other)
        obj2 = self.modify_data(other)
        return self.customsum() <= sum(obj2)


    def __ge__(self, other):
        self.check_data(other)
        obj2 = self.modify_data(other)
        return self.customsum() >= sum(obj2)


    def __str__(self):
        return f"({self.lst}, {self.customsum()})"
