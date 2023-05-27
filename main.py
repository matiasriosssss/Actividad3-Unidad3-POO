from manejadorTaller import manejador1
from test import test
if __name__ == '__main__':
    mT=manejador1()
    mT.lecArchivo()
    
    test(mT)