# Ejercicio 13: Implementa la clase “Matriz” con los atributos int rows,
# int columns e int[rows][columns] matrix, que contenga los siguientes métodos: 
# - getNumberRows(): devuelve el número de filas de la matriz.
# - getNumberColumns(): devuelve el número de columnas de la matriz.
# - setElement(int x, int j, int element): cambia el valor de la matriz en [x][j] por el
# valor de [element].
# - addMatrix(int[][] matrix): suma todos los elementos de la matriz actual a los
# elementos de [matrix], y el resultado se almacena en la matriz inicial. 
# Si [matrix] no tiene el mismo número de filas y columnas que la matriz inicial, 
# la operación no se puede realizar (notificalo).
# - multMatrix(int[][] matrix]: multiplica todos los elementos de la matriz actual
# a los elementos de [matrix], y el resultado se almacena en la matriz inicial.
# Si [matrix] no tiene el mismo número de filas y columnas que la matriz inicial,
# la operación no se puede realizar (notificalo).

class Matriz:
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.matriz = [[0] * columns for _ in range(rows)]
        
    def getNumberRows(self):
        return self.rows

    def getNumberColumns(self):
        return self.columns
    
    def setElement(self,x,j,element):
        if x >= 0 and x < self.rows and j >= 0 and j < self.columns:
            self.matriz[x][j] = element
        else:
            print("no es posible el cambio debido a la longitud introducida de la matriz")
        
    def addMatrix(self, otherMatrix):
        if len(otherMatrix) != self.rows or len(otherMatrix[0]) != self.columns:
            print("No se puede realizar la suma. Las dimensiones no coinciden.")
            return

        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] += otherMatrix[i][j]

    def multMatrix(self, otherMatrix):
        if len(otherMatrix) != self.columns:
            print("No se puede realizar la multiplicación. El número de columnas de la matriz actual no coincide con el número de filas de la matriz proporcionada.")
            return

        result = [[0] * len(otherMatrix[0]) for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(len(otherMatrix[0])):
                sum = 0
                for k in range(self.columns):
                    sum += self.matrix[i][k] * otherMatrix[k][j]
                result[i][j] = sum

        self.matrix = result
        self.columns = len(otherMatrix[0])