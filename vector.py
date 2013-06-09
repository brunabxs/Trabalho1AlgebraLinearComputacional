import math
from matrix import Matrix

class Vector:
    
    def __init__(self, values, column=True):
        self.__values = values
        self.__rows, self.__columns = len(self.__values), 1

        if not column:
            self.__rows, self.__columns = self.__columns, self.__rows
        
        # converte valores para float
        for i in xrange(len(self.__values)):
            self.__values[i] = float(self.__values[i])
            
    def rows(self):
        return self.__rows
        
    def columns(self):
        return self.__columns
        
    def get(self, position):
        return self.__values[position]
        
    def set(self, position, value):
        self.__values[position] = value
        
    def copy(self):
        return Vector(self.__values[:], (False if self.rows() == 1 else True))
        
    def transpose(self):
        return Vector(self.__values[:], (True if self.rows() == 1 else False))
        
    def dot_product(self, vector):
        if self.columns() != vector.rows():
            raise ValueError('Dot product error')
            
        result = 0
        for j in xrange(0, self.columns()):
            result += self.get(j) * vector.get(j)
        return math.sqrt(result)
        
    def __rmul__(self, value):
        if (type(value) == int or type(value) == float):
            return self.__mul__(value)
        
    def __mul__(self, value):
        # multiplicacao por int / float
        if (type(value) == int or type(value) == float):
            result = self.copy()
            for i in xrange(max(result.rows(), result.columns())):
                result.set(i, result.get(i) * value)
            return result
        else:
            #multiplicacao por vector
            vector = value
            if self.rows() == 1 and vector.columns() == 1 and self.columns() == vector.rows():
                return self.dot_product(vector)
                
            if self.rows() != vector.columns():
                raise ValueError('Product error')
                
            result = Matrix.zeros(self.rows(), vector.columns())
            for i in xrange(result.rows()):
                for j in xrange(result.columns()):
                    result.set(i, j, self.get(i) * vector.get(j))
            return result