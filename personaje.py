class personaje :
    #Atributos
    def __init__(self,esp,nom,alt):
        
        self.__especie=esp

        self.__nombre=nom

        self.__altura=alt
        
    
 

    #metodos
    def correr(self,status):
        if(status):
            print("el personaje"+self.__nombre+"Esta corriendo")
        else : 
            print("el personaje"+self.__nombre+"se detuvo")

    #metodos 
    def lanzarGranadas(self):
        print("el personaje"+self.__nombre+"lanzo la granda")
        
    def recargar(self,municiones):
        cargador=10
        cargador=cargador+municiones
        print("el arma recargada tiene "+ str(cargador)+"balas")




    def __pensar(self):
        print("Toy pensando............................")
        
    def getEspecie(self):
            return self.__especie
        
    def setEspecie(self,esp):
            self.__especie = esp
    ############################################
    def getNombre(self):
            return self.__nombre
        
    def setNombre(self,nom):
            self.__nombre = nom
    ############################################
    def getAltura(self):
            return self.__altura
        
    def setNombre(self,alt):
            self.__altura = alt   
            
    
            
            
                    
        
     
            
    
        



