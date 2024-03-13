import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Tomas
apellido: Fernandez
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
# a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
# cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
# b. Nombre del postulante Jr con menor edad.
# c. Promedio de edades por género.
# d. Tecnologia con mas postulantes (solo hay una).
# e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        contador_postulantes_nb_asp_js = 0
        
        primer_jr = False
        minimo_edad_jr = 0
        nombre_postulante_jr_min_edad = None
        
        acumulador_nb = 0
        contador_nb = 0
        acumulador_m = 0
        contador_m = 0
        acumulador_f = 0
        contador_f = 0
        
        contador_py = 0
        contador_js = 0
        contador_asp = 0
        
        porcentaje_m = 0
        porcentaje_f = 0
        porcentaje_nb = 0
        
        
        for i in range(1,5+1):
            nombre_postulante = input("\nIngrese el nombre: ")
            edad_postulante = input("Ingrese la edad: ")
            edad_postulante = int(edad_postulante)
            while edad_postulante < 18:
                edad_postulante = input("Reingrese la edad: ")
                edad_postulante = int(edad_postulante)
            genero_postulante = input("Ingrese el genero (F, M, NB): ")
            while genero_postulante != "F" and genero_postulante != "M" and genero_postulante != "NB":
                genero_postulante = input("Reingrese el genero (F, M, NB): ")
            tecnologia_postulante = input("Ingrese la tecnologia (PYTHON, JS, ASP.NET): ")
            while tecnologia_postulante != "PYTHON" and tecnologia_postulante != "JS" and tecnologia_postulante != "ASP.NET":
                tecnologia_postulante = input("Reingrese la tecnologia (PYTHON, JS, ASP.NET): ")
            puesto_postulante = input("Ingrese el puesto(Jr, Ssr, Sr): ")
            while puesto_postulante != "Jr" and puesto_postulante != "Ssr" and puesto_postulante != "Sr":
                puesto_postulante = input("Reingrese el puesto(Jr, Ssr, Sr): ")
            
            match genero_postulante:
                case "NB":
                    # a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
                    # cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
                    if (tecnologia_postulante == "ASP.NET" or tecnologia_postulante == "JS") and (edad_postulante > 25 and edad_postulante < 40) and (puesto_postulante == "Ssr"):
                        contador_postulantes_nb_asp_js += 1
                    acumulador_nb += edad_postulante
                    contador_nb += 1                
                case "M":
                    acumulador_m += edad_postulante
                    contador_m += 1
                case _:
                    acumulador_f += edad_postulante
                    contador_f += 1
                    
                        
            match puesto_postulante:
                case "Jr":
                    # b. Nombre del postulante Jr con menor edad.
                    if edad_postulante < minimo_edad_jr or primer_jr == False:
                        minimo_edad_jr = edad_postulante
                        primer_jr = True
                        nombre_postulante_jr_min_edad = nombre_postulante
                        
            match tecnologia_postulante:
                case "PYTHON":
                    contador_py += 1
                case "JS":
                    contador_js += 1
                case _:
                    contador_asp += 1
                    
            # d. Tecnologia con mas postulantes (solo hay una).
            if contador_py > contador_js and contador_py > contador_asp:
                tecnologia_mas_postulante = "Python"
            elif contador_js > contador_py and contador_js > contador_asp:
                tecnologia_mas_postulante = "Java Script"
            else:
                tecnologia_mas_postulante = "ASP.NET"
    
    
        #Salidas:
        # c. Promedio de edades por género.
        if contador_m > 0:
            promedio_edad_m = acumulador_m / contador_m
        else:
            promedio_edad_m = "No se ingreso ningún masculino"
        
        if contador_f > 0:
            promedio_edad_f = acumulador_f / contador_f
        else:
            promedio_edad_f = "No se ingreso ningún femenino"
            
        if contador_nb > 0:
            promedio_edad_nb = acumulador_nb / contador_nb
        else:
            promedio_edad_nb = "No se ingreso ningún no binario"
            
        # e. Porcentaje de postulantes de cada genero.
        porcentaje_m = round((contador_m * 100) / 5,2)
        porcentaje_f = round((contador_f * 100) / 5,2)
        porcentaje_nb = round((contador_nb * 100) / 5,2)
        
        
        
        print(f"{contador_postulantes_nb_asp_js},{nombre_postulante_jr_min_edad}, promedio M:{promedio_edad_m}, promedio f: {promedio_edad_f}, promedio nb: {promedio_edad_nb}, Tecnologia mas postulante: {tecnologia_mas_postulante}, porcentajes respecto al total de postulantes: porcentaje M: {porcentaje_m}, porcentaje F: {porcentaje_f}, porcentaje NB: {porcentaje_nb}")
        
        print(f"""
              La cantidad de postulantes que son no binarios, programadores ASP.NET o JS entre 25 y 40 años y semi seniors son {contador_postulantes_nb_asp_js}.
              El nombre del postulante programador Junior con menor edad es: {nombre_postulante_jr_min_edad}
              Promedio edades:
              Promedio masculinos: {promedio_edad_m}.
              Promedio femeninos: {promedio_edad_f}.
              Promedio no binarios: {promedio_edad_nb}.
              La tecnologia con mas postulantes es: {tecnologia_mas_postulante}
              Porcentajes de cantidad de postulantes respecto al total:
              Porcentaje masculinos: {porcentaje_m}
              Porcentaje femenino: {porcentaje_f}
              Porcentaje no binario: {porcentaje_nb}
              """)
        
        
            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
