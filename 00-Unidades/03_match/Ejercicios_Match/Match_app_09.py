import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Tomas
apellido: Fernandez
---
Ejercicio: Match_09
---
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        estacion = self.combobox_estaciones.get()
        destino = self.combobox_destino.get()
        ESTADIA_BASE = 15000
        aumento = 0
        descuento = 0
        
        match estacion:
            case "Invierno":
                if destino == "Bariloche":
                    aumento = 1.20
                elif destino in ["Cataratas", "Cordoba"]:
                    descuento = 0.10
                else:
                    descuento = 0.20

            case "Verano":
                if destino == "Bariloche":
                    descuento = 0.20
                elif destino in ["Cataratas", "Cordoba"]:
                    aumento = 1.10
                else:
                    aumento = 1.20
                    
            case "Primavera" | "Otoño":
                if destino == "Cordoba":
                    ESTADIA_BASE = ESTADIA_BASE
                else:
                    aumento = 1.10
            
        #Calculo del precio total:
        precio_aumento = aumento * ESTADIA_BASE
        descuento_aplicable = descuento * ESTADIA_BASE
        precio_descuento = ESTADIA_BASE - descuento_aplicable
        
        if descuento > 0:
            mensaje = f"El precio de la estadia con el {descuento * 100}% de descuento queda en un total de {precio_descuento}"
        elif aumento > 0:
            mensaje = f"El precio de la estadia con el {(aumento - 1) * 100}% de aumento queda en un total de {precio_aumento}"
            
        alert("ESTADIA",mensaje)
        
        
        
        
        
                    
                    
                
                
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()