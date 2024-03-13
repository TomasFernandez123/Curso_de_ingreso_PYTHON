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
        contador_f = 0
        contador_m = 0
        
        contador_perro = 0
        contador_gato = 0
        contador_exotico = 0
        
        
        bandera_minimo_peso = False
        minimo_peso = 0
        
        bandera_minima_edad_perro = False
        minimo_edad_perro = 0
        nombre_perro_mas_joven = None
        
        acumulador_peso_perro = 0
        acumulador_peso_gato = 0
        acumulador_peso_exotico = 0
        for i in range(0,5):
            nombre_mascota = input("Ingrese el nombre: ")
            tipo_mascota = input("Ingrese el tipo: ")
            while tipo_mascota != "gato" and tipo_mascota != "perro" and tipo_mascota != "exotico":
                tipo_mascota = input("Ingrese el tipo: ")
            peso_mascota = input("Ingrese su peso: ")
            peso_mascota = int(peso_mascota)
            while peso_mascota < 10 or peso_mascota > 80:
                peso_mascota = input("Ingrese su peso: ")
                peso_mascota = int(peso_mascota)
            sexo_mascota = input("Ingrese el sexo: ")
            while sexo_mascota != "F" and sexo_mascota != "M":
                sexo_mascota = input("Ingrese el sexo: ")
            edad_mascota = input("Ingrese la edad: ")
            edad_mascota = int(edad_mascota)
            while edad_mascota < 0:
                edad_mascota = input("Ingrese la edad: ")
                edad_mascota = int(edad_mascota)
                
            
            match sexo_mascota:
                case "F":
                    contador_f += 1
                case "M":
                    contador_m += 1
                    
            match tipo_mascota:
                case "perro":
                    contador_perro += 1
                    acumulador_peso_perro += peso_mascota
                    # Informe D- El nombre del perro más joven
                    if minimo_edad_perro > edad_mascota or bandera_minima_edad_perro == False:
                        minimo_edad_perro = edad_mascota
                        bandera_minima_edad_perro = True
                        nombre_perro_mas_joven = nombre_mascota
                        
                case "gato":
                    contador_gato += 1
                    acumulador_peso_gato += peso_mascota
                case "exotico":
                    contador_exotico += 1
                    acumulador_peso_exotico += peso_mascota
        
            # Informe C- El nombre y tipo de la mascota menos pesada
            if peso_mascota < minimo_peso or bandera_minimo_peso == False:
                minimo_peso = peso_mascota
                bandera_minimo_peso = True
                nombre_mascota_minimo_peso = nombre_mascota
                tipo_mascota_minimo_peso = tipo_mascota
                
    
        
        # Informe A- Cuál fue el sexo menos ingresado (F o M)
        if contador_f > contador_m:
            sexo_menos_ingresado = "M"
        else:
            sexo_menos_ingresado = "F"

        # Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
        contador_total = contador_gato + contador_exotico + contador_perro 
        porcentaje_perro = (contador_perro * 100) / contador_total
        porcentaje_gato = (contador_gato * 100) / contador_total
        porcentaje_exotico = (contador_exotico * 100) / contador_total    
               
        
        # Informe E- El promedio de peso de todas las mascotas
        if contador_perro > 0:
            promedio_peso_perro = acumulador_peso_perro / contador_perro
        else:
            promedio_peso_perro = "No hay perros."
        if contador_gato > 0:
            promedio_peso_gato = acumulador_peso_gato / contador_gato
        else:
            promedio_peso_gato = "No hay gatos."
        if contador_exotico > 0:
            promedio_peso_exotico = acumulador_peso_exotico / contador_exotico
        else:
            promedio_peso_exotico = "No hay exoticos."
        
               
        print(sexo_menos_ingresado)
        print(porcentaje_perro)
        print(porcentaje_gato)
        print(porcentaje_exotico)
        print(nombre_mascota_minimo_peso)
        print(tipo_mascota_minimo_peso)
        print(promedio_peso_perro)
        print(promedio_peso_gato)
        print(promedio_peso_exotico)
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()