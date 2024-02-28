class Lavatrastos:
    def __init__(self,Depositos,aguaCaliente) :
     self.__Depositos=Depositos
     self.__aguaCaliente=aguaCaliente
     
def getDepositos(self):
     return self.__Depositos
 
def setDepositos(self,Depositos):
     self.__Depositos=Depositos
     
def getaguaCaliente(self):
    return self.__aguaCaliente

def setaguaCaliente(self,aguaCaliente):
    self.__aguaCaliente
    
class Estados:
    def __init__(self,nombre,fecha) :
        self.__nombre=nombre
        self.__fecha=fecha
        
def getnombre(self):
    return self.__nombre
        
def setnombre(self,nombre):
    self.__nombre=nombre
    
def getfecha(self):
    return self.__fecha
        
def setfecha(self,fecha):
    self.__fecha=fecha 
    
class Patios:
    def __init__(self,areaSocial,medidasPatio,descripcionPatio) :
        self.__areaSocial=areaSocial
        self.__medidasPatio=medidasPatio
        self.__descripcionPatio=descripcionPatio
        
def getareaSocial(self):
    return self.__areaSocial
        
def setareaSocial(self,areaSocial):
    self.__areaSocial=areaSocial
    
def getmedidasPatio(self):
    return self.__medidasPatio
        
def setmedidasPatio(self,medidasPatio):
    self.__medidasPatio=medidasPatio

def getdescripcionPatio(self):
    return self.__descripcionPatio
        
def setdescripcionPatio(self,descripcionPatio):
    self.__descripcionPatio=descripcionPatio
    
class Sala:
    def __init__(self,Chimenea,DescripcionSala) :
        self.__chimenea=Chimenea
        self.__DescripcionSala=DescripcionSala
        
def getChimenea(self):
    return self.__Chimenea
        
def setChimenea(self,Chimenea):
    self.__Chimenea=Chimenea
    
def getDescripcionSala(self):
        return self.__DescripcionSala
        
def setDescripcionSala(self,DescripcionSala):
    self.__DescripcionSala=DescripcionSala

class Cuarto:
    def __init__(self,numVentanas,medidaCuartos):
        self.__numVentanas=numVentanas
        self.__medidaCuartos=medidaCuartos
        
def getnumVentana(self):
    return self.__numVentana
        
def setnombre(self,numVentana):
    self.__numVentana=numVentana
    
def getmedidaCuartos(self):
    return self.__medidaCuartos
        
def setmedidaCuartos(self,medidaCuartos):
    self.__medidaCuartos=medidaCuartos
    
class Cocina(Lavatrastos):
    def __init__(self,electrodomesticos,medidasCocina,materialDesayunador) :
     self.__electrodomesticos=electrodomesticos
     self.__medidasCocina=medidasCocina
     self.__materialDesayunador=materialDesayunador
     self.Lavatrastes=[]
     
def getelectrodomesticos(self):
    return self.__electrodomesticos
        
def setelectrodomesticos(self,electrodomesticos):
    self.__electrodomesticos=electrodomesticos
    
def getmedidasCocina(self):
    return self.__medidasCocina
        
def setmedidasCocina(self,medidasCocina):
    self.__medidasCocina=medidasCocina
    
def getmaterialDesayunador(self):
    return self.__materialDesayunador
        
def setmaterialDesayunador(self,materialDesayunador):
    self.__materialDesayunador=materialDesayunador
    
class Casa(Cuarto,Sala,Cocina,Patios,Estados):
    def __init__(self,direccion,descripcionCasa) :
        self.__direccion=direccion
        self.__descripcionCasa=descripcionCasa
        self.Cuarto=[]
        self.salas=[]
        self.Cocina=[]
        self.Patios=[]
        self.Estados=[]
        
def getdireccion(self):
    return self.__direccion
        
def setdireccion(self,direccion):
    self.__direccion=direccion
    
def getdescripcionCasa(self):
    return self.__descripcionCasa
        
def setdescripcionCasa(self,descripcionCasa):
    self.__descripcionCasa=descripcionCasa
       
    
    
        