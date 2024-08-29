import random

class Ataque:
    def __init__(self, name, type, objective, damage, precision, recharge):
        self.nombre = name
        self.tipo = type
        self.objetivo = objective
        self.daño = damage
        self.precisión = precision
        self.recarga = recharge


class Robot:
    def __init__(self, nombre, energia, ataques):
        self.nombre = nombre
        self.energia = energia
        self.energia_maxima = energia
        self.ataques = ataques

    def atacar(self, oponente, competencia):
        ataque = random.choice(self.ataques)
        # Registro del uso del ataque
        if ataque.nombre not in competencia.resultados[self.nombre]['usos_ataques']:
            competencia.resultados[self.nombre]['usos_ataques'][ataque.nombre] = 0
        competencia.resultados[self.nombre]['usos_ataques'][ataque.nombre] += 1
        
        # Realización del ataque
        if random.randint(1, 100) <= ataque.precisión:
            oponente.energia -= ataque.daño
            print(f"{self.nombre} atacó con {ataque.nombre} a {oponente.nombre} causando {ataque.daño} de daño.")
        else:
            print(f"{self.nombre} falló el ataque {ataque.nombre}.")