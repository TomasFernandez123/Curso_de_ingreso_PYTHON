#Nombre: Tomas
#Apellido : Apellido

# Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:

# Nombre

# Importe ganado (mayor o igual $1000)

# Género (“Femenino”, “Masculino”, “Otro”)

# Juego (Ruleta, Poker, Tragamonedas)

# Necesitamos saber:

# Nombre y género de la persona que más ganó.

# Promedio de dinero ganado en Ruleta.

# Porcentaje de personas que jugaron en el Tragamonedas.

# Cuál es el juego menos elegido por los ganadores.

# Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000

# Porcentaje de dinero en función de cada juego

cantidad_ganadores = input("Cuantos ganadores hubo?: ")
cantidad_ganadores = int(cantidad_ganadores)
contador = 0
maximo_ganador = 0

dinero_acumulado_ruleta = 0
cantidad_juegos_ruleta = 0
cantidad_juegos_tragamonedas = 0
cantidad_juegos_poker = 0

cantidad_juegos_no_poker = 0
dinero_acumulado_no_poker = 0

dinero_acumulado_poker = 0
dinero_acumulado_tragamonedas = 0

dinero_total_casino = 0

promedio_no_poker = 0


while contador < cantidad_ganadores:
        
    nombre = input("Ingrese su nombre: ")
    importe_ganado = input("Ingrese el importe que gano: ")
    importe_ganado = int(importe_ganado)
    while importe_ganado < 1000:
        importe_ganado = input("Reingrese el importe que gano: ")
        importe_ganado = int(importe_ganado)
    genero = input("Ingrese el genero(Femenino, Masculino, Otro): ")
    while genero != "Femenino" and genero != "Masculino" and genero != "Otro":
        genero = input("Reingrese el genero(Femenino, Masculino, Otro): ")
    juego_casino = input("Ingrese en que juego gano(Ruleta, Poker, Tragamonedas): ")
    while juego_casino != "Ruleta" and juego_casino != "Poker" and juego_casino != "Tragamonedas":
        juego_casino = input("Reingrese en que juego gano(Ruleta, Poker, Tragamonedas): ")
    
    if importe_ganado > maximo_ganador or contador == 0:
        maximo_ganador = importe_ganado
        nombre_mas_ganador = nombre
        genero_mas_ganador = genero
    
    
    match juego_casino:
        case "Ruleta":
            dinero_acumulado_ruleta += importe_ganado
            cantidad_juegos_ruleta += 1
            
            dinero_total_casino += dinero_acumulado_ruleta
            
            if importe_ganado > 15000:
                cantidad_juegos_no_poker += 1  
                dinero_acumulado_no_poker += importe_ganado
        case "Tragamonedas":
            cantidad_juegos_tragamonedas += 1
            dinero_acumulado_tragamonedas = importe_ganado
            
            dinero_total_casino += dinero_acumulado_tragamonedas
            
            if importe_ganado > 15000:
                cantidad_juegos_no_poker += 1
                dinero_acumulado_no_poker += importe_ganado
        case _:
            dinero_acumulado_poker = importe_ganado
            cantidad_juegos_poker += 1
            dinero_total_casino += dinero_acumulado_poker
    
    
    contador += 1


#Salidas:
if cantidad_juegos_ruleta > 0:
    promedio_ruleta = dinero_acumulado_ruleta / cantidad_juegos_ruleta

#Porcentaje tragamonedas respecto al total de jugadores:
porcentaje_cantidad_tragamonedas = round((cantidad_juegos_tragamonedas * 100) / contador,2)

#Juego menos elegido:
if cantidad_juegos_ruleta < cantidad_juegos_tragamonedas and cantidad_juegos_ruleta < cantidad_juegos_poker:
    juego_menos_jugado = "Ruleta"
elif cantidad_juegos_tragamonedas < cantidad_juegos_ruleta and cantidad_juegos_tragamonedas < cantidad_juegos_poker:
    juego_menos_jugado = "Tragamonedas"
else:
    juego_menos_jugado = "Poker" 
    
#Promedio NO poker:
if cantidad_juegos_no_poker > 0:
    promedio_no_poker = dinero_acumulado_no_poker / cantidad_juegos_no_poker
    
#Porcentaje de importe por juego:
if cantidad_juegos_poker > 0:
    porcentaje_dinero_poker = (dinero_acumulado_poker / dinero_total_casino) * 100 
else:
    porcentaje_dinero_poker = "No hubo ganadores en poker"

if cantidad_juegos_tragamonedas > 0:
    porcentaje_dinero_tragamonedas = (dinero_acumulado_tragamonedas / dinero_total_casino) * 100 
else:
    porcentaje_dinero_tragamonedas = "No hubo ganadores en tragamonedas"

if cantidad_juegos_ruleta > 0:
    porcentaje_dinero_ruleta = (dinero_acumulado_ruleta / dinero_total_casino) * 100 
else:
    porcentaje_dinero_ruleta = "No hubo ganadores en ruleta"



# Nombre y género de la persona que más ganó.

# Promedio de dinero ganado en Ruleta.

# Porcentaje de personas que jugaron en el Tragamonedas.

# Cuál es el juego menos elegido por los ganadores.

# Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000

# Porcentaje de dinero en función de cada juego

print(f"""
      Nombre y genero del mas ganador: {nombre_mas_ganador}, {genero_mas_ganador}
      Promedio de dinero ganado en Ruleta: {promedio_ruleta}
      Porcentaje de personas que jugaron Tragamonedas: {porcentaje_cantidad_tragamonedas}%
      Juego menos elegido por los ganadores: {juego_menos_jugado}
      Promedio Importe de personas que no jugaron poker y su importe fue mayor a 15000: {promedio_no_poker}
      Porcentaje de dinero en función de cada juego:
      Ruleta: {porcentaje_dinero_ruleta}%
      Tragamonedas: {porcentaje_dinero_tragamonedas}%
      Poker: {porcentaje_dinero_poker}%
      """)


        


