import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Tomas
apellido: Fernandez
DNI: 46115731
---
Examen Ingreso
---
'''
'''
De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.

Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M )
Edad(mayor a 0)

Pedir datos por prompt y mostrar por print, se debe informar:
# Informe A- Cuál fue el sexo menos ingresado (F o M)
# Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
# Informe C- El nombre y tipo de la mascota menos pesada
# Informe D- El nombre del perro más joven
# Informe E- El promedio de peso de todas las mascotas
'''

''''''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        contador_m = 0
        contador_f = 0
        contador_gato = 0
        contador_perro = 0
        contador_exotico = 0
        minimo_peso = 0
        bandera_minimo_peso = False
        minima_edad_perro = 0
        bandera_minimo_edad_perro = False
        nombre_minima_edad_perro = None
        acumulador_peso_perro = 0
        acumulador_peso_gato = 0
        acumulador_peso_exotico = 0
        
        for i in range(0,5):
            nombre = prompt("UTN","Ingrese el nombre de la mascota: ")
            tipo = prompt("UTN","Ingrese el tipo de mascota que es (gato, perro o exotico): ")
            while tipo != "gato" and tipo != "perro" and tipo != "exotico":
                tipo = prompt("UTN","Reingrese el tipo de mascota que es (gato, perro o exotico): ")
            peso = prompt("UTN","Ingrese su peso: ")
            peso = int(peso)
            while peso < 10 or peso > 80:
                peso = prompt("UTN","Reingrese su peso: ")
                peso = int(peso)
            sexo = prompt("UTN","Ingrese el sexo(M, F): ")
            while sexo != "M" and sexo != "F":
                sexo = prompt("UTN","Reingrese el sexo(M, F): ")
            edad = prompt("UTN","Ingrese su edad: ")
            edad = int(edad)
            while edad < 0:
                edad = prompt("UTN","Reingrese su edad: ")
                edad = int(edad)
            
            
            match sexo:
                case "M":
                    contador_m += 1
                case _:
                    contador_f += 1
                    
            match tipo:
                case "gato":
                    contador_gato += 1
                    acumulador_peso_gato += peso
                case "perro":
                    contador_perro += 1
                    acumulador_peso_perro += peso
                case _:
                    contador_exotico += 1
                    acumulador_peso_exotico += peso
                                   
            if contador_m < contador_f:
                sexo_menos_ingresado = "Masculino"
            else:
                sexo_menos_ingresado = "Femenino"
            
            if peso < minimo_peso or bandera_minimo_peso == False:
                minimo_peso = peso
                bandera_minimo_peso = True
                nombre_minimo_peso = nombre
                tipo_minimo_peso = tipo
                
            if (edad < minima_edad_perro or bandera_minimo_edad_perro == False) and tipo == "perro":
                minima_edad_perro = edad
                bandera_minimo_edad_perro = True
                nombre_minima_edad_perro = nombre
            
        
        
        total_mascotas = contador_gato + contador_perro + contador_exotico
        total_peso_mascotas = acumulador_peso_gato + acumulador_peso_perro + acumulador_peso_exotico
        
        porcentaje_cantidad_gato = round((contador_gato * 100) / total_mascotas,2)
        porcentaje_cantidad_perro = round((contador_perro * 100) / total_mascotas,2)
        porcentaje_cantidad_exotico = round((contador_exotico * 100) / total_mascotas,2)
                 
        promedio_peso_total_mascotas = round(total_peso_mascotas / 5,2)
    
        print(f"""
Sexo menos ingresado: {sexo_menos_ingresado}
Porcentaje de mascotas por tipo:
Gato: {porcentaje_cantidad_gato}%
Perro: {porcentaje_cantidad_perro}%
Exotico: {porcentaje_cantidad_exotico}%
Nombre y tipo de mascota menos pesada: {nombre_minimo_peso}, {tipo_minimo_peso}
Nombre del perro mas joven: {nombre_minima_edad_perro}
Promedio de peso entre TODAS las mascotas: {promedio_peso_total_mascotas} KG
""")
        
        
        
        
                    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()