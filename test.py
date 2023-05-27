from clasePersona import Persona
def test(mT):
    matias = Persona("Matias Rios", "Nueve de julio", "43488804")  ##SE CREAN LAS PERSONAS
    mT.inscribir(3, matias) ##SE REGISTRAN LAS PERSONAS PUNTO 2
    lionel = Persona("Lio Messi", "Barcelona", "10101010") ##SE CREAN LAS PERSONAS
    mT.inscribir(1, lionel)  ##SE REGISTRAN LAS PERSONAS PUNTO 2
    kylian = Persona("K Mbappe", "Paris", "77777777")  ##SE CREAN LAS PERSONAS
    mT.inscribir(2, kylian)  ##SE REGISTRAN LAS PERSONAS PUNTO 2
    kuni = Persona("Kuni Aguero", "Barcelona", "16161616")  ##SE CREAN LAS PERSONAS
    mT.inscribir(3, kuni)  ##SE REGISTRAN LAS PERSONAS PUNTO 2
    diego = Persona("Dieguito Maradona", "Cielito", "19861010")  ##SE CREAN LAS PERSONAS
    mT.inscribir(1, diego)  ##SE REGISTRAN LAS PERSONAS PUNTO 2
    
    mT.consultarInscripcion("43488804")  ##PRUEBA PUNTO 3
    mT.consultarInscripcion("00000646") ##PRUBA ERRONEA PUNTO 3
    mT.consultarInscripcion("19861010") ##PRUEBA PUNTO 3
    
    mT.listarAlumnos(1)  ##PRUEBA PUNTO 4
    
    mT.registrarPago("43488804") ##PRUEBA PUNTO 5
    mT.registrarPago("16161616") ##PRUEBA PUNTO 5
    mT.consultarInscripcion("43488804") ##VERIFICACION PUNTO 5
    mT.consultarInscripcion("16161616") ##VERIFICACION PUNTO 5
    
    