from Robot import Robot, Ataque
from Competition import CompetenciaLiga
from Report import Reporte

def main():
    # Definición de ataques
    ataque1 = Ataque("Arco", "long", "robot", 20, 80, 1)
    ataque2 = Ataque("Espada", "sword", "robot", 25, 90, 2)
    ataque3 = Ataque("Puñetazo", "hand", "robot", 15, 95, 0)

    # Definición de robots
    robot1 = Robot("Robot1", 100, [ataque1, ataque2])
    robot2 = Robot("Robot2", 120, [ataque2, ataque3])
    robot3 = Robot("Robot3", 110, [ataque1, ataque3])

    # Crear y ejecutar la competencia
    competencia = CompetenciaLiga([robot1, robot2, robot3])
    competencia.realizar_competencia()
    competencia.generar_reporte()

    # Generar reportes
    reporte = Reporte(competencia)
    reporte.generar_grafico_usos_ataques()

if __name__ == "__main__":
    main()
