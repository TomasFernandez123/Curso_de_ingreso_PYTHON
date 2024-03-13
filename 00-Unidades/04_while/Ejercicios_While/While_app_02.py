import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Nombre: Tomas
Apellido: Fernandez

Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la bolsa de 
valores:

Para ello deberás programar el botón  para poder cargar 10 operaciones de compra con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    
Realizar los siguientes informes:
 
    #! 1) - Tipo de instrumento que menos se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion del usuario que invirtio menos dinero
    #! 6) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 7) - Promedio de cantidad de instrumentos  MEP vendidos en total

'''



class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Operar", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        contador = 0
        contador_cedear = 0
        contador_bonos = 0
        contador_mep = 0
        cantidad_mep_rango = 0
        cantidad_usuarios_sin_cedear = 0
        
        bandera_primer_cedear_bono = False
        
        posicion_menos_invertido = 0
        menos_invertido = 0
        
        total_cedear = 0
        total_cantidad_mep = 0
        
        while contador < 10:
            
            contador += 1  
            #CARGA DE DATOS:  
            nombre = input("Ingrese el nombre: ")
            monto_pesos = input("Ingrese el monto en pesos: ")
            monto_pesos = float(monto_pesos)
            while monto_pesos < 10000:
                monto_pesos = input("Reingrese el monto en pesos: ")
                monto_pesos = float(monto_pesos)
            tipo_instrumento = input("Ingrese el tipo de instrumento (CEDEAR, BONOS, MEP): ")
            while tipo_instrumento != "CEDEAR" and tipo_instrumento != "BONOS" and tipo_instrumento != "MEP":
                tipo_instrumento = input("Reingrese el tipo de instrumento (CEDEAR, BONOS, MEP): ")
                
            cantidad_de_instrumento = input("Ingrese cuanta cantidad del instrumento quieres comprar: ")
            cantidad_de_instrumento = int(cantidad_de_instrumento)
            while cantidad_de_instrumento < 0:
                cantidad_de_instrumento = input("Ingrese cuanta cantidad del instrumento quieres comprar: ")
                cantidad_de_instrumento = int(cantidad_de_instrumento)
                
                
            #PROCESAMIENTO DE DATOS:
            #! 1) - Tipo de instrumento que menos se operó en total.
            match tipo_instrumento:
                case "CEDEAR":
                    contador_cedear += 1
                    total_cedear += monto_pesos
                case "BONOS":
                    contador_bonos += 1 
                    #! 3) - Cantidad de usuarios que no compraron CEDEAR
                    cantidad_usuarios_sin_cedear += 1
                case _:
                    contador_mep += 1 
                    total_cantidad_mep += cantidad_de_instrumento
                    #! 3) - Cantidad de usuarios que no compraron CEDEAR
                    cantidad_usuarios_sin_cedear += 1
                    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP:
                    if cantidad_de_instrumento > 50 and cantidad_de_instrumento < 200:
                        cantidad_mep_rango += 1
            
            
            #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
            if (tipo_instrumento == "CEDEAR" or tipo_instrumento == "BONOS") and bandera_primer_cedear_bono == False:
                nombre_primer_cedear_bono = nombre
                cantidad_primer_cedear_bono = cantidad_de_instrumento
                bandera_primer_cedear_bono = True
                
            #! 5) - Nombre y posicion del usuario que invirtio menos dinero
            if cantidad_de_instrumento < menos_invertido or contador == 1:
                menos_invertido = cantidad_de_instrumento
                nombre_menos_invertido = nombre
                posicion_menos_invertido = contador
        
        
                
        #SALIDAS:
        if contador_cedear < contador_bonos and contador_cedear < contador_mep:
            intrumento_menos_operado = "CEDEAR"
        elif contador_bonos < contador_mep:
            intrumento_menos_operado = "BONOS"
        else:
            intrumento_menos_operado = "MEP"
            
        #! 6) - Promedio de dinero en CEDEAR  ingresado en total.
        promedio_cedear = total_cedear / contador_cedear
        
        #! 7) - Promedio de cantidad de instrumentos  MEP vendidos en total
        promedio_cantidad_mep = total_cantidad_mep / contador_mep
        
        
        
            
        mensaje = f"\n1.El tipo de instrumento que menos se opero es {intrumento_menos_operado}\n2.La cantidad de usuarios que compraron entre 50 y 200 MEP son {cantidad_mep_rango}\n3.La cantidad de usuarios que no compraron CEDEARS son {cantidad_usuarios_sin_cedear}\n4.Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR {nombre_primer_cedear_bono},{cantidad_primer_cedear_bono}\n5.Nombre y posicion del usuario que invirtio menos dinero {nombre_menos_invertido},{posicion_menos_invertido}\n6.Promedio de dinero en CEDEAR {promedio_cedear}\n7.Promedio de cantidad de instrumentos  MEP vendidos en total {promedio_cantidad_mep}"
        
        print(mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()