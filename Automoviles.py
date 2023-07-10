from Conexion import Conexiones
from dataclasses import dataclass

class Automovil:
    def __init__(self, marca, modelo,precio=None,cantidadDisponibles=None):
        self.marca = marca
        self.modelo = modelo
        self.precio=precio
        self.cantidadDisponibles=cantidadDisponibles
        
    def cargar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:                                                                                                    
            conexion.miCursor.execute("INSERT INTO AUTOMOVILES(marca,modelo,precio,cantidadDisponibles) VALUES('{}', '{}','{}','{}')".format(self.marca, self.modelo,self.precio,self.cantidadDisponibles))
            conexion.miConexion.commit()
            print("Automovil cargado exitosamente")
            input()
        except:
            print("Error al agregar un automovil")
        finally:
            conexion.cerrarConexion()

    def modificar_automoviles(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET precio='{}' where marca='{}' and modelo='{}' ".format(self.precio,self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automovil modificado correctamente")
            input()
        except:
            print('Error al actualizar un automovil')
        finally:
            conexion.cerrarConexion()  
    
    def delete_automoviles(self): #Consigna nro3
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DELETE FROM AUTOMOVILES  where marca='{}' and modelo='{}' ".format(self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automovil eliminado correctamente")
            input()
        except:
            print('Error al eliminar un automovil')
        finally:
            conexion.cerrarConexion()

    def cargar_disponibilidad(self): #Consigna nro4
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET cantidadDisponibles=cantidadDisponibles+1 where marca='{}' and modelo='{}' ".format(self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automovil modificado correctamente")
            input()
        except:
            print('Error al actualizar un automovil')
        finally:
            conexion.cerrarConexion()  
    
    @classmethod
    def listado_automoviles(cls): #Consigna nro5
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM AUTOMOVILES")
            autos=conexion.miCursor.fetchall()
            for auto in autos: 
                a,b,c,d,*rest = auto
                concatenado=f"{a} {b} {c} {d}"
                print(concatenado)
            input()
        except:     
            print('Error al ejecutar')
        finally:
            conexion.cerrarConexion()