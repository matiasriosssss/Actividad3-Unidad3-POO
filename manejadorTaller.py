from claseTaller import Taller
import csv

class manejador1:
    
    def __init__(self):
        self.__listaManejador1 = []
        
    def agregar(self, nuevo):
        self.__listaManejador1.append(nuevo)
    
    def getLista(self):
        return self.__listaManejador1
        
    def lecArchivo(self):
        archivo = open('talleres.csv')
        reader = csv.reader(archivo, delimiter=(';'))
        next(reader)
        for fila in reader:
            nuevoObjeto = Taller(fila[0], fila[1], fila[2], fila[3])
            self.agregar(nuevoObjeto)
        
    def inscribir(self, numId, persona):
        i=0
        centinela=True
        while i < len(self.getLista()) and centinela:
            if numId == self.getLista()[i].getId() and self.getLista()[i].getVacantes() > 0:
                self.getLista()[i].inscribir2(persona)
                centinela = False
            i+=1
        if centinela:
            print("El taller solicitado no existe o ya no tiene vacantes disponibles...")
    
    def consultarInscripcion(self, dni):
        i=0
        centinela=True
        while i < len(self.getLista()) and centinela:
            centinela = self.getLista()[i].buscarPersona(dni, False) ##CUANDO BUSCA A UNA PERSONA ENVIAMOS FALSE PARA PODER REUTILIZAR CODIGO EN LA FUNCION buscarPersona2
            i+=1
        if centinela:
            print("No se encontro a la persona...")
    
    def listarAlumnos(self, id):
        i=0
        centinela=True
        while i < len(self.getLista()) and centinela:
            if id == self.getLista()[i].getId():
                self.getLista()[i].listar()
                centinela = False
            i+=1
    def registrarPago(self, dni):
        i=0
        centinela=True
        while i < len(self.getLista()) and centinela:
            centinela = self.getLista()[i].buscarPersona(dni, True) ##CUANDO REGISTRAMOS UN PAGO ENVIAMOS TRUE PARA REUTILIZAR CODIGO EN LA FUNCION buscarPersona2
            i+=1
        if centinela:
            print("No se encontro a la persona...")
            
        
        