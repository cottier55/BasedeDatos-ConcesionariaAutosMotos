import sqlite3
from Automoviles import Automovil
from Motocicletas import Motocicleta
from Conexion import Conexiones
from dataclasses import dataclass

class ProgramaPrincipal:
    def menu(self):
        while True:
            print("Menu de opciones Concesionaria")
            print("8- Mostrar los datos anteriores a una fecha especifica")
            print("7- Modificar precio Motocicleta")
            print("6- Cargar Motocicleta")
            print("5- Listado de automoviles")
            print("4- Cargar disponibilidad")
            print("3- Borrar datos del automovil")
            print("2- Modificar Automovil")
            print("1- Cargar Automovil")
            print("0- Salir de menu")
            try:
                nro = int(input("Por favor ingrese un numero"))
                if nro < 0 or nro > 8:
                    print("Ingrese un numero entre 0 y 8")
                    input()
                    continue
                if nro == 1:
                    marca = input("Por favor ingrese la marca del automovil: ")
                    modelo = input("Por favor ingrese el modelo del automovil: ")
                    precio = int(input("Por favor ingrese el precio del automovil: "))
                    cantidadDisponibles = int(input("Por favor ingrese la cantidad de unidades disponibles: "))
                    nuevo_automovil = Automovil(marca,modelo,precio,cantidadDisponibles)
                    nuevo_automovil.cargar_automovil()
                if nro == 2:
                    marca = input("Por favor ingrese el nombre de la marca: ")
                    modelo = input("Por favor ingrese el nombre del modelo: ")
                    precio = int(input("Por favor ingrese el nuevo precio: "))
                    automovil_a_modificar=Automovil(marca,modelo,precio)
                    automovil_a_modificar.modificar_automoviles()
                if nro == 3:
                    marca = input("Por favor ingrese el nombre de la marca: ")
                    modelo = input("Por favor ingrese el nombre del modelo: ")
                    automovil_a_eliminar=Automovil(marca,modelo)
                    automovil_a_eliminar.delete_automoviles()
                if nro == 4:
                    disponibilidad = Automovil(marca,modelo)
                    disponibilidad.cargar_disponibilidad()
                if nro == 5:
                    print("Marca" " " "Modelo" " " "Precio" " " "Cantidad disponible")
                    Automovil.listado_automoviles()
                if nro == 6:
                    modelo = input("Por favor ingrese el modelo de la motocicleta: ")
                    marca = input("Por favor ingrese la marca de la motocicleta: ")
                    cilindrada = int(input("Por favor ingrese la cilindrada de la motocicleta: "))
                    precio = int(input("Por favor ingrese el precio de la motocicleta: "))
                    color = input("Por favor ingrese el color de la motocicleta: ")
                    crear_tabla_motocicleta= Motocicleta(modelo, marca, cilindrada, precio, color)
                    crear_tabla_motocicleta.cargar_motocicleta()
                if nro == 7:
                    Motocicleta.listado_motocicleta()
                if nro == 8:
                    fecha = input("Por favor ingrese la fecha: (formato: AAAA-MM-DD)")
                    Motocicleta.registro_historial(Motocicleta, fecha)                
                if nro == 0:
                    print("Gracias por elegirnos!\nSalindo del programa...")
                    break
            except: 
                print('Por favor ingrese numeros donde corresponda y letras donde corresponda')
                input()
                continue     

    #TABLA DE AUTOMOVILES
    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS AUTOMOVILES")
        conexion.miCursor.execute("CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")    
        conexion.miCursor.execute("DROP TABLE IF EXISTS MOTOCICLETA")                      #autoincrementa
        conexion.miCursor.execute("CREATE TABLE MOTOCICLETA (id_moto INTEGER PRIMARY KEY , modelo  VARCHAR(30) , marca  VARCHAR(30), cilindrada VARCHAR(30), precio INTEGER NOT NULL, color VARCHAR(30), fechaUltimoPrecio DATETIME DEFAULT CURRENT_TIMESTAMP)") 
        conexion.miCursor.execute("DROP TABLE IF EXISTS HISTORICO_MOTOCICLETA")
        conexion.miCursor.execute("CREATE TABLE HISTORICO_MOTOCICLETA (id_moto INTEGER, modelo  VARCHAR(30) , marca  VARCHAR(30), cilindrada VARCHAR(30), precio INTEGER NOT NULL, color VARCHAR(30), fechaUltimoPrecio DATETIME)") 
        conexion.miConexion.commit()       
        conexion.cerrarConexion()
            
programa = ProgramaPrincipal()
programa.crearTablas()
programa.menu()
