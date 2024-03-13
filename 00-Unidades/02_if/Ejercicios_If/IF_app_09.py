import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
nombre: Tomas 
apellido: Fernandez
---
En un prestigioso torneo de ajedrez, se lleva a cabo un seguimiento detallado de los jugadores y sus partidas. Para cada participante se registran los siguientes datos:
Nombre del jugador
Puntuación obtenida en el torneo (debe ser un número entero)
Edad del jugador
Color de las piezas que prefirió usar en las partidas (Blancas o Negras)

Se requiere analizar la información recopilada para obtener estadísticas relevantes del torneo. Específicamente, se necesita conocer:
1. El nombre y la edad del jugador que obtuvo la puntuación más alta.
2. El promedio de puntuación de los jugadores menores de 18 años.
3. El porcentaje de jugadores que prefirieron usar las piezas negras en sus partidas.
4. Determinar qué color de piezas fue menos preferido por los jugadores.
5. Calcular el promedio de puntuación de los jugadores que jugaron con piezas blancas y que obtuvieron una puntuación mayor a 5.
6. Proporcionar un desglose del porcentaje de puntuación total en función del color de las piezas.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        seguir = True
        maxima_puntuacion = 0
        bandera_maxima_puntuacion = False
        
        contador_menor_edad = 0
        acumulador_puntuacion_menor_edad = 0
        
        contador_piezas_negras = 0
        contador_piezas_blancas = 0
        
        contador_piezas_blancas_puntuacion_mayor = 0
        acumulador_puntuacion_piezas_blanca_mayor = 0
        
        while seguir:
            #Ingreso y verificacion de datos:
            nombre = input("Ingrese el nombre: ")
            puntuacion_obtenida = input("Ingrese la puntuación obtenida en el torneo: ")
            puntuacion_obtenida = int(puntuacion_obtenida)
            edad = input("Ingrese la edad: ")
            edad = int(edad)
            color_piezas_usado = input("Ingrese el color de piezas que eligio (Blancas o Negras): ")
            while color_piezas_usado != "Blancas" and color_piezas_usado != "Negras":
                color_piezas_usado = input("Reingrese el color de piezas que eligio (Blancas o Negras): ")
            
            seguir = question("","Quieres ingresar otro jugador?") 
            
            #Analisis:
            #El nombre y la edad del jugador que obtuvo la puntuación más alta:
            if puntuacion_obtenida > maxima_puntuacion or bandera_maxima_puntuacion == False:
                maxima_puntuacion = puntuacion_obtenida
                nombre_maxima_puntuacion = nombre
                edad_maxima_puntuacion = edad
                bandera_maxima_puntuacion = True
                
            #El promedio de puntuación de los jugadores menores de 18 años.
            if edad < 18:
                contador_menor_edad += 1
                acumulador_puntuacion_menor_edad += puntuacion_obtenida
            
            #El porcentaje de jugadores que prefirieron usar las piezas negras en sus partidas.
            match color_piezas_usado:
                case "Negras":
                    contador_piezas_negras += 1
                case "Blancas":
                    contador_piezas_blancas += 1
                    #Calcular el promedio de puntuación de los jugadores que jugaron con piezas blancas y que obtuvieron una puntuación mayor a 5.
                    if puntuacion_obtenida > 5:
                        contador_piezas_blancas_puntuacion_mayor += 1
                        acumulador_puntuacion_piezas_blanca_mayor += puntuacion_obtenida
                        
        
            #Determinar qué color de piezas fue menos preferido por los jugadores:
            if contador_piezas_blancas < contador_piezas_negras:
                color_piezas_menos_usado = "Blancas"
            else:
                color_piezas_menos_usado = "Negras"
        
        
        
        
        
        






        #Salidas y procesos fuera del while:
        total_piezas = contador_piezas_negras + contador_piezas_blancas
        #El promedio de puntuación de los jugadores menores de 18 años.      
        if contador_menor_edad > 0:      
            promedio_puntuacion_menor_edad = acumulador_puntuacion_menor_edad / contador_menor_edad
        else:
            promedio_puntuacion_menor_edad = "No se ingreso ningun menor de 18 años."
        
        #El porcentaje de jugadores que prefirieron usar las piezas negras en sus partidas:
        porcentaje_piezas_negras = (contador_piezas_negras * 100) / total_piezas
            
        #6. Proporcionar un desglose del porcentaje de puntuación total en función del color de las piezas:
        porcentaje_piezas_blancas = (contador_piezas_blancas * 100) / total_piezas    
            
        #Calcular el promedio de puntuación de los jugadores que jugaron con piezas blancas y que obtuvieron una puntuación mayor a 5.
        if contador_piezas_blancas_puntuacion_mayor > 0:
            promedio_blancas_mayor = acumulador_puntuacion_piezas_blanca_mayor / contador_piezas_blancas_puntuacion_mayor
        else:
            promedio_blancas_mayor = "Ningun jugador con piezas blancas obtuvo una puntuacion mayor a 5"
        
        print(nombre_maxima_puntuacion,edad_maxima_puntuacion)
        print(promedio_puntuacion_menor_edad)
        print(porcentaje_piezas_negras)
        print(color_piezas_menos_usado)
        print(promedio_blancas_mayor)
        print(f"Porcentajes piezas:\nPiezas negras: {porcentaje_piezas_negras}% \n Piezas blancas: {porcentaje_piezas_blancas}%")
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()