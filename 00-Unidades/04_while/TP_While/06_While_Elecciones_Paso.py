import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Tomas
apellido: Fernandez
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        contador = 0
        candidato_mas_votos = ""
        candidato_menos_votos = ""
        edad_menos_votos = 0
        total_edades = 0
        total_votos = 0
        min_votos = 0
        max_votos = 0
        seguir = True
        
        while seguir == True:
            candidato_nombre = prompt("UTN","Ingrese el nombre del candidato:")
            
            edad = prompt("UTN","Ingrese la edad del candidato:")
            edad = int(edad)
            
            while edad < 25:
                edad = prompt("UTN","La edad debe ser mayor que 25:")
                edad = int(edad)
                
            votos = prompt("UTN","Ingrese la cantidad de votos recibidos del candidato:")
            votos = int(votos)
            
            while votos < 0:
                votos = prompt("UTN","La cantidad de votos no puede ser menor a 0:")
                votos = int(votos)
                
            seguir = question("UTN","Desea seguir?")
              
              
            
            if votos > max_votos or contador == 0:
                max_votos = votos
                candidato_mas_votos = candidato_nombre
            
            if votos < min_votos or contador == 0:
                min_votos = votos
                candidato_menos_votos = candidato_nombre
                edad_menos_votos = edad
            
            contador += 1
            total_edades += edad
            total_votos += votos
        
        promedio_edades = total_edades / contador
                        
        mensaje = f"""
        A)El candidato con mas votos es:
        {candidato_mas_votos} con {max_votos}.
        
        B)El candidato con menos votos es:
        {candidato_menos_votos}, {edad_menos_votos} años con {min_votos} votos.
        
        C)El promedio de edades entre los candidatos es de: 
        {promedio_edades}.
        
        D)El total de todos los votos en general da una suma de: 
        {total_votos} votos."""
        alert("UTN",mensaje)
                

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
