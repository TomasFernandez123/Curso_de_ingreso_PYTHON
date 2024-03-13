import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Nombre: Tomas
Apellido: Fernandez

Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River 
Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de 
comprar cada entrada:

Al presionar el boton se debera pedir la carga de los siguientes datos, hasta que el usuario lo desee:

Los datos que deberas pedir para los ventas son:
    * Nombre del comprador
    * Edad (no menor a 16)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Platea)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.

 * Lista de precios: 
        * General: $16000
        * Campo:   $25000
        * Platea:  $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 

Al finalizar la carga, el programa debera mostrar los siguientes informes:

    #! 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
    #!          de crédito y su edad promedio.
    #! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
    #!          pagaron con tarjeta de débito  respecto al total de personas en la lista.
    #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de 
    #!          los aplicados a tarjetas de crédito
    #! 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de 
    #!          tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
    #! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya 
    #!          edad es un número primo.
    #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        contador_masculinos_campo = 0
        contador_femeninos_campo = 0
        contador_otros_campo = 0
        
        contador_personas_campo_credito = 0
        total_edad_campo = 0
        
        bandera_primera_general_debito = True
        nombre_primera_general_debito = None
        edad_primera_general_debito = None

        contador_personas_total = 0
        
        contador_personas_platea_debito = 0
        
        descuento_total_credito = 0
        
        contador_personas_platea_primo = 0
        
        es_primo = True
        
        total_monto_platea_debito = 0
        
        
        seguir = True
        while seguir == True:
            contador_personas_total += 1
            
            nombre_comprador = input("Introduce el nombre: ")
            edad_comprador = input("Introduce la edad: ")
            edad_comprador = int(edad_comprador)
            while edad_comprador < 16:
                edad_comprador = input("Reintroduce la edad: ")
                edad_comprador = int(edad_comprador)
                     
            genero = input("Introduce el genero (Masculino, Femenino, Otro): ")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = input("Reintroduce el genero (Masculino, Femenino, Otro): ")
                
            tipo_entrada = input("Introduce el tipo de entrada (General, Campo, Platea): ")
            while tipo_entrada != "General" and tipo_entrada != "Campo" and tipo_entrada != "Platea":
                tipo_entrada = input("Reintroduce el tipo de entrada (General, Campo, Platea): ")
            
            medio_pago = input("Introduce el metodo de pago (Credito, Efectivo, Debito): ")
            while medio_pago != "Credito" and medio_pago != "Efectivo" and medio_pago != "Debito":
                medio_pago = input("Reintroduce el metodo de pago (Credito, Efectivo, Debito): ")

            match tipo_entrada:
                case "General":
                    precio_entrada = 16000
                    #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta de crédito y su edad promedio.
                    if medio_pago == "Credito":
                        contador_personas_campo_credito += 1
                        total_edad_campo += edad_comprador
                    #! 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
                    elif medio_pago == "Debito" or bandera_primera_general_debito == True:
                        nombre_primera_general_debito = nombre_comprador
                        edad_primera_general_debito = edad_comprador
                        bandera_primera_general_debito = False
                            
                        
                case "Campo": 
                    precio_entrada = 25000
                    if genero == "Masculino":
                        contador_masculinos_campo +=1
                    elif genero == "Femenino":
                        contador_femeninos_campo += 1
                    else:
                        contador_otros_campo += 1
                        
                case _:
                    precio_entrada = 30000
                    if medio_pago == "Debito":
                        contador_personas_platea_debito +=1
                        #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
                        if edad_comprador % 6 == 0:
                            total_monto_platea_debito += precio_entrada
                    
                    #! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya edad es un número primo.
                    for i in range(2, edad_comprador):
                        if edad_comprador % i == 0:
                            es_primo = False
                            break
                    if es_primo == True:
                        contador_personas_platea_primo += 1
                        
                        
            # Aplicar descuento según medio de pago
            if medio_pago == "Credito":
                descuento_aplicable = precio_entrada * 0.20
                precio_entrada -= descuento_aplicable
                #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de los aplicados a tarjetas de crédito
                descuento_total_credito += descuento_aplicable
            elif medio_pago == "Debito":
                precio_entrada -= precio_entrada * 0.15
            
            
            
                
            #Procesamiento de datos:
            #! 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo"
            if contador_masculinos_campo > contador_femeninos_campo and contador_masculinos_campo > contador_otros_campo:
                genero_frecuente_campo = "Masculino"
            elif contador_femeninos_campo > contador_otros_campo:
                genero_frecuente_campo = "Femenino"
            else:
                genero_frecuente_campo = "Otros"
                    
            seguir = question("UTN","Quieres seguir?")
        
        
        #SALIDA:
        #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta de crédito y su edad promedio.
        if contador_personas_campo_credito > 0:
            promedio_edad_general = total_edad_campo / contador_personas_campo_credito
        else:
            promedio_edad_general = "No har personas en campo que hayan pagado con credito"

        
        #! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y pagaron con tarjeta de débito respecto al total de personas en la lista.
        porcentaje_platea_debito = (contador_personas_platea_debito * 100) / contador_personas_total  
        
        #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
        total_monto_platea_debito_con_descuento = total_monto_platea_debito * 0.85
        








    #! 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
    #!          de crédito y su edad promedio.
    #! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
    #!          pagaron con tarjeta de débito  respecto al total de personas en la lista.
    #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de 
    #!          los aplicados a tarjetas de crédito
    #! 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de 
    #!          tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
    #! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya 
    #!          edad es un número primo.
    #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
    
        print(f"""
            1) El genero mas frecuente en campo es {genero_frecuente_campo}
            2) La cantidad de gente que compro General con credito es {contador_personas_campo_credito} y su promedio edad es {promedio_edad_general}.
            3) El porcentaje de personas que compraron platea con debito es del {porcentaje_platea_debito}%
            4) El total de descuento en PESOS solo a las tarjetas de creditos fue de {descuento_total_credito}.
            5) La primera persona que pago General con debito fue {nombre_primera_general_debito}, {edad_primera_general_debito} años.
            6) La cantidad de gente que compro platea cuya edad es numero primo {contador_personas_platea_primo}
            7) El monto total recaudado por gente con edad multiplo de 6 en platea es de {total_monto_platea_debito_con_descuento}""")
        
        # print(f"1.{genero_frecuente_campo}\n2.{contador_personas_campo_credito},{promedio_edad_general}\n3.{porcentaje_platea_debito}\n4.{descuento_total_credito}\n5.{nombre_primera_general_debito},{edad_primera_general_debito}\n6.{contador_personas_platea_primo}\n7.{total_monto_platea_debito_con_descuento}")
        
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()