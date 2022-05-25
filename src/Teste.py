"""
El siguiente código es el desarrollo de un juego de enfrentamientos entre héroes
y villanos, basado en los personajes de DC's Legends Of Tomorrow
"""


from Juego import Equipo
from Juego import Integrante
from Juego import Enfrentamiento
from Juego import Habilidad

if __name__ == '__main__':
    
    # ---------------------------Objetos predeterminados----------------------------
    """
    Las siguientes lineas de código son para crear de forma predeterminada equipos e
    integrantes de 
    """

    global equipos
    equipos = []

    Leyendas = Equipo("Leyendas del mañana", "Heroes")
    equipos.append(Leyendas)

    Sara = Integrante("Sara Lance", "Canario Blanco", "Clon humano - Alien",
                    "Lider de las leyendas", 4, 6, 5,
                    "Paragon del destino", 8, "Muerte")
    Leyendas.integrantes.append(Sara)

    Ray = Integrante("Ray Palmer", "Atom", "Humano",
                    "Ingeniero", 5, 5, 3,
                    "Exo-traje A.T.O.M", 7, "Agua")
    Leyendas.integrantes.append(Ray)

    Legion = Equipo("La legión del mal", "Villanos")
    equipos.append(Legion)

    Damien = Integrante("Damien Darhk", "Dark Knight", "Humano",
                        "Asesino", 3, 4, 5,
                        "Magia Negra", 9, "Fuego")
    Legion.integrantes.append(Damien)

    Eobard = Integrante("Eobard Thawne", "Reverse Flash", "Meta-Humano",
                        "Criminal del tiempo", 6, 4, 5,
                        "Correr a la velocidad de la luz", 8, "Animal")
    Legion.integrantes.append(Eobard)


    # ------------------Enfrentamientos al azar entre dos equipos-------------------
    enfrentamiento = Enfrentamiento()
    ejecutar = True
    while ejecutar == True:
        x = int(input("\n¡A pelear >:)!\n1.Continuar\n2.Salir\n"))
        if x == 1:
            enfrentamiento.peleadores(Leyendas, Legion)
            ejecutar = True
        else:
            ejecutar = False


    # --------------Métodos y funciones disponibles para ejecutar-------------------
    """Mostrar la ficha técnica de objeto tipo integrante"""
    # Sara.ficha_tecnica()
    # Eobard.ficha_tecnica()

    """Registrar un integrante dependiendo el equipo"""
    # Leyendas.registrar_integrante()
    # Legion.registrar_integrante()
    """
    Se puede copiar y pegar en orden las siguientes lineas:

    Zari Tarazi, Chica Dragón, Humano, Influencer / Hacker
    2, 3, 4, Control del viento, 7, Viento
    Nate Heywood, Steel, Meta-Humano, Historiador
    3, 6, 2, Piel de Acero, 8, Tierra
    """

    """Mostrar información de la pelea y generar una especifica"""
    # enfrentamiento.peleadores(Leyendas, Legion)
    # enfrentamiento.pelea(Ray, Damien)
    # enfrentamiento.mostrar_peleadores(Leyendas, Legion)
