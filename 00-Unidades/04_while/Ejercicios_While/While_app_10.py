import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Tomas
apellido: Fernandez
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos
    
    #Agregado con el profe german:
    G. El maximo 
    H: El minimo, mostrando en que número de iteración se encontró.
    I: El minimo positivo

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        cantidas_positivos = 0
        cantidad_negativos = 0
        cantidad_ceros = 0
        suma_positivos = 0
        suma_negativos = 0
        
        maximo = 0
        minimo = 0
        contador = 0
        
        minimo_positivo = 0
                
        while True:
            numero = prompt("UTN","Ingrese numero:")
            if numero == None:
                break
            
            numero = float(numero)
            
            contador += 1
            
            if numero > 0:
                suma_positivos +=  numero
                cantidas_positivos += 1
                
                if numero < minimo_positivo or contador == 1:
                    minimo_positivo = numero
                    
            elif numero == 0:
                cantidad_ceros += 1
            else:
                suma_negativos += numero
                cantidad_negativos += 1
                
            
            if numero > maximo or contador == 1:
                maximo = numero
                
            if numero < minimo or contador == 1:
                minimo = numero
                posicion_encontrada = contador
                    
        diferencia_positivos_negativos = abs(cantidas_positivos - cantidad_negativos)
        
        alert("UTN",f"""
    A. La suma acumulada de los negativos: {suma_negativos}
    B. La suma acumulada de los positivos: {suma_positivos}
    C. Cantidad de números positivos ingresados: {cantidas_positivos}
    D. Cantidad de números negativos ingresados: {cantidad_negativos}
    E. Cantidad de ceros: {cantidad_ceros}
    F. Diferencia entre la cantidad de los números positivos 
       ingresados y los negativos: {diferencia_positivos_negativos}
    G. Numero maximo encontrado: {maximo}
    H. Numero minimo encontrado: {minimo}, en la iteracion: {posicion_encontrada}
    I. El minimo positivo es: {minimo_positivo}""")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
