import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Tomas
apellido: Fernandez
---
Ejercicio: for_07
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = input("Ingres un numero: ")
        numero = int(numero)
        bandera_es_primo = True
        
        for i in range(2,numero):
            if numero % i == 0:
                bandera_es_primo = False
                break
            
        if bandera_es_primo == True:
            print("El numero es primo")
        else:
            print("El numero no es primo")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()