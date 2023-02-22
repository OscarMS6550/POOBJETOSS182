class personaje :
    #Atributos
    def __init__(self,esp,nom,alt):
        
        self.especie=esp

        self.nombre=nom

        self.altura=alt
        
    
 

    #metodos
    def correr(self,status):
        if(status):
            print("el personaje"+self.nombre+"Esta corriendo")
        else : 
            print("el personaje"+self.nombre+"se detuvo")

    #metodos 
    def lanzarGranadas(self):
        print("el personaje"+self.nombre+"lanzo la granda")
        
    def recargar(self,municiones):
        cargador=10
        cargador=cargador+municiones
        print("el arma recargada tiene "+ str(cargador)+"balas")
        
     
            
    
        



