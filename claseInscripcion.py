
class Inscripcion:
    def __init__(self, in1, in2):
        self.__persona = in1
        self.__fecha = in2
        self.__pago = False
    
    def getFecha(self):
        return self.__fecha
    
    def getPago (self):
        return self.__pago
    
    def getPersona(self):
        return self.__persona
    def confirmarPago(self):
        self.__pago = True
        print(f"Se confirmo el pago de {self.getPersona().getNombre()}")
    