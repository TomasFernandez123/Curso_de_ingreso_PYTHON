import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Tomas
apellido: Fernandez
---
Ejercicio: Match_06
---
Enunciado:
Obtener la hora ingresada en el cuadro de texto txt_hora. 
Al presionar el botón ‘Informar’ mostrar mediante alert alguno de los 
siguientes mensajes según la hora ingresada:
    Si está entre las 7 y las 11: ‘Es de mañana’
    Si está entre las 12 y las 19: ‘Es de tarde’
    Si está entre las 20 y las 24 o entre las 0 y las 6: ‘Es de noche’
    Si no está entre 0 y las 24: ‘La hora no existe’
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_hora = customtkinter.CTkLabel(master=self, text="Hora")
        self.label_hora.grid(row=0, column=0, padx=20, pady=10)
        self.txt_hora = customtkinter.CTkEntry(master=self)
        self.txt_hora.grid(row=0, column=1)
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        hora = self.txt_hora.get()
        hora_int = int(hora)
        #Nose si esta permitido que usemos if dentro de los case, entonces lo hice de esta forma:
        # match hora_int:
        #     case 7|8|9|10|11:
        #         mensaje = "Es de mañana"
        #     case 12|13|14|15|16|17|18|19:
        #         mensaje = "Es de tarde"
        #     case 0|1|2|3|4|5|6|20|21|22|23|24:
        #         mensaje = "Es de noche"
        #     case _:
        #         mensaje = "La hora no existe"
                
        #En caso que este permitido quedaria algo asi:
        match hora_int:
            case x if (0 <= x <= 6) or (20 <= x <= 24):
                mensaje = "Es de noche"
            case x if x >= 12:
                mensaje = "Es de tarde"
            case x if x >= 7:
                mensaje = "Es de mañana"
            case _:
                mensaje = "La hora no existe"             
                 
        alert("HORA",mensaje)
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()