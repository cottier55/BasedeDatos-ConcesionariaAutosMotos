from Conexion import Conexiones
from dataclasses import dataclass

class Motocicleta:
    def __init__(self, modelo, marca, cilindrada, precio, color):
        self.modelo = modelo
        self.marca = marca
        self.cilindrada = cilindrada
        self.precio = precio
        self.color = color

    def cargar_motocicleta(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:                                                                                                    
            conexion.miCursor.execute("INSERT INTO MOTOCICLETA(modelo,marca,cilindrada,precio,color) VALUES('{}','{}','{}','{}','{}')".format(self.modelo, self.marca, self.cilindrada, self.precio, self.color))
            conexion.miConexion.commit()
            print("Motocicleta cargada exitosamente")
            input()
        except:
            print("Error al agregar una motocicleta")
        finally:
            conexion.cerrarConexion()

    @classmethod
    def listado_motocicleta(self):   #ejercicio 7
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETA")
            motos=conexion.miCursor.fetchall()
            for moto in motos: 
                id_moto, modelo, marca, cilindrada, precio, color, fechaUltimoPrecio = moto
                conexion.miCursor.execute("INSERT INTO HISTORICO_MOTOCICLETA (id_moto,modelo,marca,cilindrada,precio,color,fechaUltimoPrecio) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(id_moto, modelo, marca, cilindrada, precio, color, fechaUltimoPrecio))
            conexion.miCursor.execute("UPDATE MOTOCICLETA SET precio=precio+precio*0.1, fechaUltimoPrecio=CURRENT_TIMESTAMP")
            conexion.miConexion.commit()
            print("Motocicleta modificada exitosamente!")        
        except:     
            print('Error al ejecutar')
        finally:
            conexion.cerrarConexion()

    def registro_historial(self, fecha):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETA WHERE fechaUltimoPrecio >= '{}' ".format(fecha))
            fechas = conexion.miCursor.fetchall()
            for moto in fechas:
                print(f'{"ID: ", moto[0],"Modelo: ", moto[1],"Marca: ", moto[2],"Cilindrada: ", moto[3],"Precio: ", moto[4],"Color: ", moto[5],"Fecha último precio: ", moto[6]}')
                input() 
        except:
            print("Error al Ejecutar")
        finally:
            conexion.cerrarConexion()