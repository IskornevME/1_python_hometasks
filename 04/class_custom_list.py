'''
This programm realizes Customlist class
'''
class Customlist(list):
    '''
    This is Customlist class inherited from list
    '''
    def __init__(self, iterable):
        for item in iterable:
            self.check_number(item) 
        super().__init__(int(item) for item in iterable)


    def check_number(self, item):
        '''
        Check that our data is numbers
        '''
        if not isinstance(item, (int, float)):
            raise TypeError("Список должен состоять из чисел")
            
            
    @classmethod
    def check_data(cls, other):
        '''
        Check that our data has type list or Customlist
        '''
        if not isinstance(other, (list, Customlist)):
            raise TypeError("Объект должен иметь тип list или Customlist")  


    def __add__(self, other):
        self.check_data(other)
        res = []
        diff = len(self) - len(other)
        if (diff > 0):
            for i in range(diff):
                other.append(0)
        else:
            for i in range(-diff):
                self.append(0)

        for i, ele in enumerate(self):
            res.append(ele + other[i])
            
        if (diff > 0):
            del other[len(other) - diff: len(other)]
        elif diff != 0:
            del self[len(self) + diff: len(self)]
        
        return Customlist(res)


    def __sub__(self, other):
        self.check_data(other)
        res = []
        diff = len(self) - len(other)
        if (diff > 0):
            for i in range(diff):
                other.append(0)
        else:
            for i in range(-diff):
                self.append(0)
        
        for i, ele in enumerate(self):
            res.append(ele - other[i])
            
        if (diff > 0):
            del other [len(other) - diff: len(other)]
        elif diff != 0:
            del self[len(self) + diff: len(self)]
        return Customlist(res)
    
    
    def neg(self):
        '''
        Change sign of all elements
        '''
        for i, ele in enumerate(self):
            self[i] = -ele
        return self


    def __radd__(self, other):
        return self + other


    def __iadd__(self, other):
        diff = len(self) - len(other)
        if (diff > 0):
            for i in range(diff):
                other.append(0)
        else:
            for i in range(-diff):
                self.append(0)
        for i, ele in enumerate(other):
            self[i] += ele
        if (diff > 0):
            del other[len(other) - diff: len(other)]
        return self


    def __isub__(self, other):
        self.check_data(other)
        diff = len(self) - len(other)
        if (diff > 0):
            for i in range(diff):
                other.append(0)
        else:
            for i in range(-diff):
                self.append(0)
        for i, ele in enumerate(other):
            self[i] -= ele
        if (diff > 0):
            del other[len(other) - diff: len(other)]
        return self


    def __rsub__(self, other):
        return (self - other).neg()

    
    def __eq__(self, other):
        self.check_data(other)
        return sum(self) == sum(other)
    
    
    def __ne__(self, other):
        self.check_data(other)
        return sum(self) != sum(other)
    
    
    def __lt__(self, other):
        self.check_data(other)
        return sum(self) < sum(other)
    
    
    def __gt__(self, other):
        self.check_data(other)
        return sum(self) > sum(other)   

    
    def __le__(self, other):
        self.check_data(other)
        return sum(self) <= sum(other)
    

    def __ge__(self, other):
        self.check_data(other)
        return sum(self) >= sum(other)   


    def __str__(self):
        return f"({super().__str__()}, {sum(self)})"
