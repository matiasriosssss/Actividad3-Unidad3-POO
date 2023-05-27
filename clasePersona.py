

class Persona:
    def __init__(self, in1, in2, in3):
        self.__nombre = in1
        self.__direccion = in2
        self.__DNI = in3
        
    def getNombre(self):
        return self.__nombre
    
    def getDire (self):
        return self.__direccion
    
    def getDNI(self):
        return self.__DNI