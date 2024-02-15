import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Tomas
apellido: Fernandez
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
#dato = prompt("Ingrese un dato porfavor","")
#alert("alerta",dato)
    def btn_mostrar_on_click(self):
        #para saber el costo de un viaje necesitamos el siguiente algoritmo,
        # sabiendo que el precio por kilo de pasajero es 1000 pesos
        # Se ingresan todos los datos por PROMPT
        # los datos a solicitar de dos personas son,
        # nombre, edad y peso
        # se pide  armar el siguiente mensaje
        # "hola german y marina , sus pesos son 80 kilos y 60 kilos respectivamente
        # , sumados da 140 kilos , el promedio de edad es 33 y su viaje vale 140 000 pesos  
        
        nombre = prompt("Nombre","Ingrese su nombre...")
        edad = prompt("Edad","Ingrese su edad...")
        peso = prompt("Peso","Ingrese su peso(KG)...")
        
        edad_int = int(edad)
        peso_float = float(peso)
         
        nombre_2 = prompt("Nombre","Ingrese el nombre...")
        edad_2 = prompt("Edad","Ingrese la edad...")
        peso_2 = prompt("Peso","Ingrese su peso(KG)...")
        
        edad_2_int = int(edad_2)
        peso_2_float = float(peso_2)
        
        kilos_total = peso_float + peso_2_float
        costo_viaje = 1000 * kilos_total
        promedio_edad = (edad_int + edad_2_int) / 2
        promedio_edad_int = int(promedio_edad)
        
        mensaje = f"hola {nombre} y {nombre_2}, sus pesos son {peso_float} y {peso_2_float} respectivamente, sumados da {kilos_total}, el promedio de edad es {promedio_edad_int} y su viaje vale {costo_viaje}"
        
        alert("UTN",mensaje)
        
        

        
        
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()