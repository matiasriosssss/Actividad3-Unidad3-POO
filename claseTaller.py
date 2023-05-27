from claseInscripcion import Inscripcion

class Taller:
    def __init__(self, in1, in2, in3, in4):
        self.__id = int(in1)
        self.__nombre = in2
        self.__vacantes = int(in3)
        self.__valor = in4
        self.__inscripciones = []
    def getId(self):
        return self.__id
    
    def getNomTaller (self):
        return self.__nombre
    
    def getVacantes(self):
        return self.__vacantes
    def modVacantes(self):
        self.__vacantes -= 1
    
    def getValor (self):
        return self.__valor
    
    def getListaInscriptos(self):
        return self.__inscripciones
    def agregarIns(self, nuevo):
        self.__inscripciones.append(nuevo)
    
    def inscribir2(self, persona):
        from claseInscripcion import Inscripcion
        self.modVacantes()
        nuevaInscripcion = Inscripcion(persona, "fecha")
        self.agregarIns(nuevaInscripcion)
        print(f"{persona.getNombre()} fue inscripto/a con exito a el taller {self.getNomTaller()}")
    def buscarPersona(self, dni, pago): ##CUANDO PAGO ES FALSE SE REALIZA EL PUNTO 3 Y CUANDO ES TRUE SE REALIZA EL PUNTO 5, DE ESTA FORMA REUTILIZAMOS EL CODIGO DE BUSCAR EL ALUMNO
        i=0
        centinela=True
        while i < len(self.getListaInscriptos()) and centinela:
            if dni == self.getListaInscriptos()[i].getPersona().getDNI():
                if pago:
                    self.getListaInscriptos()[i].confirmarPago()
                else:
                    if self.getListaInscriptos()[i].getPago():
                        print(f"{self.getListaInscriptos()[i].getPersona().getNombre()} esta inscripto en {self.getNomTaller()} y no debe el pago...")
                    else:
                        print(f"{self.getListaInscriptos()[i].getPersona().getNombre()} esta inscripto en {self.getNomTaller()} y debe {self.getValor()}")
                centinela = False
            i+=1
        return centinela
    def listar(self):
        for i in range(len(self.getListaInscriptos())):
            print(f"{self.getListaInscriptos()[i].getPersona().getNombre()}")
    
    
    