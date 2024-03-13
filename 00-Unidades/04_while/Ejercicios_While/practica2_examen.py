import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Tomas
apellido: Fernandez
---
Ejercicio: while_01
---
'''
'''
Enunciado:
De los 11 Jugadores de fútbol se debe ingresar los siguientes datos:
# Nombre
# Categoría (amateur - profesional - retirado )
# Edad (entre 18 y 99 inclusive)
# goles puede ser cero
# Número de camiseta del 0 al 100
Pedir datos por prompt y mostrar por print, se debe informar:
# Informe A- Cuál hay más , mayores a 25 años o menores
# Informe B- El Porcentaje de jugadores con más de dos goles
# Informe C- El nombre y número del jugador de la categoría retirado más joven
# Informe D- los goles y nombre del profesional con más goles
# Informe E- Promedio de goles de los jugadores mayores a 25.
Condiciones de aprobación:
Se debe realizar el ingreso de datos de manera correcta con las validaciones correspondientes siguiendo las
reglas de estilo de la cátedra y al menos uno de los informes solicitados de manera perfecta para obtener una
nota 6(seis)
Cada informe adicional logrado correctamente suma un punto más hasta obtener nota 10
'''

''''''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        contador_edad_mayores = 0
        contador_edad_menores = 0
        acumulador_goles_mayor = 0
        
        
        for i in range(0,11):
            nombre = input("Ingrese el nombre: ")
            categoria = input("Ingrese la categoria: ")
            while categoria != "amateur" and categoria != "profesional" and categoria != "retirado":
                categoria = input("Ingrese la categoria: ")
            edad = input("Ingrese la edad: ")
            edad = int(edad)
            while edad < 18 or edad > 100:
                edad = input("Ingrese la edad: ")
                edad = int(edad)
            goles = input("Ingrese los goles anotados: ")
            goles = int(goles)    
            while goles < 0:
                goles = input("Ingrese los goles anotados: ")
                goles = int(goles)
            numero_camiseta = input("Ingrese el numero de camiseta: ")
            numero_camiseta = int(numero_camiseta)            
            while numero_camiseta < 0 or numero_camiseta > 100:
                numero_camiseta = input("Ingrese el numero de camiseta: ")
                numero_camiseta = int(numero_camiseta) 
                
                
            # Informe A- Cuál hay más , mayores a 25 años o menores
            # Informe B- El Porcentaje de jugadores con más de dos goles
            # Informe C- El nombre y número del jugador de la categoría retirado más joven
            # Informe D- los goles y nombre del profesional con más goles
            # Informe E- Promedio de goles de los jugadores mayores a 25.
            
            #Dentro del bucle, definimos los contadores antes:
            if edad > 25:
                contador_edad_mayores += 1
                #Esto
                acumulador_goles_mayor += goles
            else:
                contador_edad_menores += 1
                
                
                
        #Fuera del bucle:
        #Y esto:
        if contador_edad_mayores > 0:
            promedio_goles_edad_mayores = acumulador_goles_mayor / contador_edad_mayores
            
        
        if contador_edad_mayores > contador_edad_menores:
            edad_mayor = "Hay mas jugadores de mas de 25 años"
        else:
            edad_mayor = "Hay mas jugadores de menos de 25 años"
            

                
                
                
                
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()