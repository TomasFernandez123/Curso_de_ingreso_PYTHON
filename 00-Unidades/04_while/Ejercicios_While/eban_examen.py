import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Juan Esteban
Apellido: Rios Paz
Instancia: Examen
46199075
7/3/2024
TTF


---
Enunciado:
De los 11 Jugadores de fútbol se debe ingresar los siguientes datos:
Nombre
Categoría (amateur - profesional - retirado )
Edad (entre 18 y 99 inclusive)
goles puede ser cero
Número de camiseta del 0 al 100
Pedir datos por prompt y mostrar por print, se debe informar:
# Informe A- Cuál hay más , mayores a 25 años o menores
# Informe B- El Porcentaje de jugadores con más de dos goles
# Informe C- El nombre y número del jugador de la categoría retirado más joven
# Informe D- los goles y nombre del profesional con más goles
# Informe E- Promedio de goles de los jugadores mayores a 25.
Condiciones de aprobación:
Se debe realizar el ingreso de datos de manera correcta con las validaciones correspondientes siguiendo las
reglas de estilo de la cátedra y al menos uno de los informes solicitados de manera perfecta para obtener una
nota 6(seis)
Cada informe adicional logrado correctamente suma un punto más hasta obtener nota 10(diez)


'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):

        contador_mayores = 0
        contador_menores = 0
        contador_mas_de_dos = 0
        contador_menos_de_dos = 0


        bandera_mas_joven = False
        edad_mas_joven = 0
        nombre_masculino_joven = None
        edad_mas_joven = 0
        numero_mas_joven = 0

        bandera_profesional_mas_goles = False
        nombre_profesional = None 
        goles_profesional = 0

        acumulador_goles = 0
        
        

        for i in range(0 ,11):
            nombre = prompt(None , "Ingrese su nombre")
            categoria = prompt(None , "Ingrese su categoria (Amateur, Profesional , Retirado):")
            while categoria != "Amateur" and categoria != "Profesional" and categoria != "Retirado":
                categoria = prompt(None , "Ingrese su categoria (Amateur, Profesional , Retirado):")
            edad = prompt(None , "Ingrese su edad") 
            edad = int(edad)
            while edad < 18 or edad > 99:
                edad = prompt(None , "Ingrese su edad") 
                edad = int(edad)
            goles = prompt(None, "Ingrese sus goles")
            goles= int(goles)
            while goles < 0:
                goles = prompt(None, "Ingrese sus goles")
                goles= int(goles)
            numero_camiseta = prompt(None, "Ingrese su camiseta")
            numero_camiseta = int(numero_camiseta)
            while numero_camiseta < 0 or numero_camiseta > 99:
                numero_camiseta = prompt(None, "Ingrese su camiseta")
                numero_camiseta = int(numero_camiseta)


# Informe A- Cuál hay más , mayores a 25 años o menores
# Informe B- El Porcentaje de jugadores con más de dos goles
# Informe C- El nombre y número del jugador de la categoría retirado más joven
# Informe D- los goles y nombre del profesional con más goles
# Informe E- Promedio de goles de los jugadores mayores a 25.

            if edad >= 25:
                contador_mayores += 1
                acumulador_goles += goles
            else:
                contador_menores += 1
            

            if goles > 2:
                contador_mas_de_dos += 1
            else: 
                contador_menos_de_dos += 1
            
            match categoria:
                case "Retirado":
                    if edad < edad_mas_joven or bandera_mas_joven == False:
                        edad_mas_joven = edad
                        bandera_mas_joven = True
                        nombre_masculino_joven = nombre
                        numero_mas_joven = numero_camiseta
                case "Profesional":
                    if goles_profesional < goles or bandera_profesional_mas_goles == False:
                        goles_profesional = goles
                        bandera_profesional_mas_goles = True
                        nombre_profesional = nombre
        
            if contador_mayores > contador_menores:
                edad_superior = "Hay mas mayores de 25"
            else: 
                edad_superior = "Hay mas menores de 25"

        if contador_mayores > 0: 
            promedio_goles_mayores = acumulador_goles / contador_mayores

        


        porcentaje_mas_dos = (contador_mas_de_dos * 100) / 11
        
        print(edad_superior)
        print("El porcentaje de los jugadores con mas de 2 goles es" , porcentaje_mas_dos)
        print("El nombre del mas joven es" , nombre_masculino_joven)
        print("El numero del retirado mas joven es" , numero_mas_joven)
        print("Los goles del profesional con mas goles son" , goles_profesional)
        print("El nombre del profesional con mas goles es" , nombre_profesional)
        print("El promedio de los goles de los jugadores mayores de 25 es" , promedio_goles_mayores )

    


   

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
