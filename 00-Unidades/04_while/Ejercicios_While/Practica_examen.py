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
De los 50 participantes del torneo de UTN-TETRIS, se debe ingresar los siguientes datos:
Nombre
Categoría (Principiante - Intermedio - Avanzado)
Edad (entre 18 y 99 inclusive)
Score (mayor que 0)
Nivel alcanzado (1 , 2 o 3)

# Pedir datos por prompt y mostrar por print, se debe informar:
# Informe A- Cuál es la categoría que tiene más participantes.
# Informe B- El Porcentaje de jugadores de la categoría avanzado sobre el total
# Informe C- La categoría del participante de menor Score
# Informe D- El score y nombre del avanzado con mayor edad
# Informe E- Promedio de score de los participantes principiantes.
'''

''''''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    def btn_mostrar_iteracion_on_click(self):
        contador_principiante = 0
        contador_intermedio = 0
        contador_avanzado = 0
        
        
        bandera_menor_score = False
        minimo_score = 0
        
        bandera_mayor_edad_avanzado = False
        maxima_edad_avanzado = 0
        nombre_avanzado_mayor = None
        score_avanzado_mayor = 0
        
        score_principiante = 0
        
        for i in range(0, 1):
            nombre = input("Ingrese el nombre: ")
            categoria = input("Ingrese la categoria: ")
            while categoria != "Principiante" and categoria != "Intermedio" and categoria != "Avanzado":
                categoria = input("Ingrese la categoria: ")
            edad = input("Ingrese la edad: ")
            edad = int(edad)
            while edad < 18 or edad > 99:
                edad = input("Ingrese la edad: ")
                edad = int(edad)
            score = input("Ingrese el score: ")
            score = int(score)
            while score < 0:
                score = input("Ingrese el score: ")
                score = int(score)
            nivel_alcanzado = input("INgrese el nivel: ")
            nivel_alcanzado = int(nivel_alcanzado)
            while nivel_alcanzado != 1 and nivel_alcanzado != 2 and nivel_alcanzado != 3:
                nivel_alcanzado = input("INgrese el nivel: ")
                nivel_alcanzado = int(nivel_alcanzado)
                
                
            # Pedir datos por prompt y mostrar por print, se debe informar:
            
            
            # Informe A- Cuál es la categoría que tiene más participantes.
            match categoria:
                case "Principiante":
                    contador_principiante += 1
                    score_principiante += score
                case "Intermedio":
                    contador_intermedio += 1
                case "Avanzado":
                    contador_avanzado += 1
                    if edad > maxima_edad_avanzado or bandera_mayor_edad_avanzado == False:
                        maxima_edad_avanzado = edad
                        bandera_mayor_edad_avanzado = True
                        nombre_avanzado_mayor = nombre
                        score_avanzado_mayor = score

            # Informe C- La categoría del participante de menor Score
            if score < minimo_score or bandera_menor_score == False:
                minimo_score = score
                categoria_menor_score = categoria
                bandera_menor_score = True
        
        
        
        
        
        
        if contador_principiante > contador_intermedio and contador_principiante > contador_avanzado:
            categoria_mas_participantes = "Principiante"
        elif contador_intermedio > contador_avanzado:
            categoria_mas_participantes = "Intermedio"
        else:
            categoria_mas_participantes = "Avanzado"
        
        
        # Informe B- El Porcentaje de jugadores de la categoría avanzado sobre el total
        contador_total = contador_avanzado + contador_intermedio + contador_principiante
        porcentaje_avanzado = (contador_avanzado * 100) / contador_total
        
        
        # Informe E- Promedio de score de los participantes principiantes.
        if contador_principiante > 0:
            promedio_score_principiante = score_principiante / contador_principiante
        else:
            promedio_score_principiante = "No se ingresaron principiantes."
        
        
        print(categoria_mas_participantes)
        print(porcentaje_avanzado)
        print(categoria_menor_score)
        print(nombre_avanzado_mayor)
        print(score_avanzado_mayor)
        print(promedio_score_principiante)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()