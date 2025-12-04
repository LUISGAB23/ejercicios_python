class Vehiculo
def __init__ (self, marca, tipo_combustible):
    self.marca = marca
    self._tipo_combustible = tipo_combustible
    self.__velocidad = 0
    
    
    #Metodo común
    def encender (self):
        return "El vehículo está encendido"
    
    def acelerar (self, cantidad):
        self.__velocidad += cantidad
        
        def frenar(self, cantidad):
            self.__velocidad -= cantidad
            if self.__velocidad < 0:
             self.__velocidad = 0
             
             def obtener_velocidad(self):
                    return self.__velocidad
class Auto (Vehiculo):
       
        