import random


'''Clase de habilidades posibles que puede tener un Integrante'''
class Habilidad():
    def __init__(self, velocidad: int, fuerza: int, resistencia: int,
                 poder: str, cant_poder: int, totem: str) -> None:
        self.velocidad = velocidad
        self.fuerza = fuerza
        self.resistencia = resistencia
        self.poder = poder
        self.cant_poder = cant_poder
        self.totem = totem

    def mostrar_habilidad(self) -> None:
        print("\nHabilidades:")
        print(f"Velocidad: {self.velocidad}")
        print(f"fuerza: {self.fuerza}")
        print(f"Resistencia: {self.resistencia}")
        print(f"podercant_poder: {self.poder} = {self.cant_poder}")
        print(f"Totem: {self.totem}")


'''Clase que contiene la información de cada objeto Integrante'''
class Integrante(Habilidad):
    def __init__(self, nombre: str, alias: str, especie: str, ocupacion: str,
                 velocidad: int, fuerza: int,
                 resistencia: int, poder: str, cant_poder: int, totem: str) -> None:
        super().__init__(velocidad, fuerza,
                         resistencia, poder, cant_poder, totem)
        self.nombre = nombre
        self.alias = alias
        self.especie = especie
        self.ocupacion = ocupacion
        self.habilidades = []  # Lista de habilidades de cada objeto integrante
        self.lista_habilidad()

    def lista_habilidad(self) -> None:
        '''Esta subrutina lista las habilidades de cada integrantes por categoria'''
        self.habilidades.append(Habilidad(self.velocidad, self.fuerza,
                                          self.resistencia, self.poder,
                                          self.cant_poder, self.totem))

    def ficha_tecnica(self) -> None:
        print(f"\nFicha técnica:")
        print(f"Nombre: {self.nombre}")
        print(f"Alias: {self.alias}")
        print(f"Especie: {self.especie}")
        print(f"Ocupacion: {self.ocupacion}")

        self.mostrar_habilidad()


'''La clase Equipo contiene los integrantes pertenecientes a al objeto Equipo'''


class Equipo(Integrante, Habilidad):
    def __init__(self, nombre_equipo: str, idiologia: str) -> None:
        self.nombre_equipo = nombre_equipo
        self.idiologia = idiologia
        self.integrantes = []  # Lista de objetos de los miembros de cada equipo

    def registrar_integrante(self) -> None:
        '''Esta subrutina permite agregar un nuevo integrante al equipo'''
        print("Nombre, alias, especie, ocupacion")
        datos = input()
        nombre, alias, especie, ocupacion = datos.split(', ')

        print("velocidad, fuerza, resistencia, poder, cant_poder, totem")
        datos = input()
        velocidad, fuerza, resistencia, poder, cant_poder, totem = datos.split(
            ', ')

        objeto_integrante = Integrante(nombre, alias, especie, ocupacion,
                                       int(velocidad), int(
                                           fuerza), int(resistencia),
                                       poder, int(cant_poder), totem)
        self.integrantes.append(objeto_integrante)

    def mostrar_equipo(self) -> None:
        print(f"\n{self.nombre_equipo} - {self.idiologia}")


'''La clase Enfrentamiento organiza la comparación de los atributos
de Habilidad de los objetos Integrante'''
class Enfrentamiento(Equipo):
    def __init__(self) -> None:
        pass

    def pelea(self, peleador1, peleador2) -> str:
        '''Esta función retorna el objeto Integrante con el valor de
        tipo habilidad más alto'''
        tipo_habilidad = int(random.randint(1, 4))
        print(f"\n{peleador1.alias} Vs {peleador2.alias}")
      
        if tipo_habilidad == 1:
            if peleador1.velocidad > peleador2.velocidad:
                return print(f"Por velocidad gana: {peleador1.alias}")
            elif peleador1.velocidad < peleador2.velocidad:
                return print(f"Por velocidad gana: {peleador2.alias}")
            else:
                print(f"Hay un empate, los dos son iguales de veloces")
                self.pelea(peleador1, peleador2)
        elif tipo_habilidad == 2:
            if peleador1.fuerza > peleador2.fuerza:
                return print(f"Por fuerza gana {peleador1.alias}")
            elif peleador1.fuerza < peleador2.fuerza:
                return print(f"Por fuerza gana: {peleador2.alias}")
            else:
                print(f"Hay un empate, los dos son iguales de fuertes")
                self.pelea(peleador1, peleador2)
        elif tipo_habilidad == 3:
            if peleador1.resistencia > peleador2.resistencia:
                return print(f"Por resistencia gana: {peleador1.alias}")
            elif peleador1.resistencia < peleador2.resistencia:
                return print(f"Por resistencia gana: {peleador2.alias}")
            else:
                print(f"Hay un empate, son muy resistentes, no se rinden")
                self.pelea(peleador1, peleador2)
        elif tipo_habilidad == 4:
            if peleador1.cant_poder > peleador2.cant_poder:
                return print(f"Por cantidad de poder gana: {peleador1.alias}")
            elif peleador1.cant_poder < peleador2.cant_poder:
                return print(f"Por cantidad de poder gana: {peleador2.alias}")
            else:
                print(f"Hay un empate, sus poderes van a la par")
                return self.pelea(peleador1, peleador2)

    def peleadores(self, equipo1, equipo2) -> None:
        cant_peleadores = len(equipo1.integrantes)
        num_peleador = random.randint(0, cant_peleadores - 1)
        peleador1 = equipo1.integrantes[num_peleador]

        cant_peleadores2 = len(equipo2.integrantes)
        num_peleador2 = random.randint(0, cant_peleadores2 - 1)
        peleador2 = equipo2.integrantes[num_peleador2]

        self.pelea(peleador1, peleador2)

    def mostrar_peleadores(self, equipo1, equipo2) -> None:
        '''Esta subrutina imprime la ficha técnica de los integrantes del equipo'''
        
        print(f"\n{equipo1.nombre_equipo}")

        for i in equipo1.integrantes:
            print(i.ficha_tecnica())

        print(f"\n{equipo2.nombre_equipo}")
        for i in equipo2.integrantes:
            print(i.ficha_tecnica())
