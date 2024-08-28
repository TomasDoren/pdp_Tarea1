class CompetenciaLiga:
    def __init__(self, robots):
        self.robots = robots
        self.resultados = {robot.nombre: {'victorias': 0, 'derrotas': 0, 'usos_ataques': {}} for robot in robots}

    def realizar_batalla(self, robot1, robot2):
        print(f"\nIniciando batalla entre {robot1.nombre} y {robot2.nombre}")
        robot1.energia = robot1.energia_maxima
        robot2.energia = robot2.energia_maxima

        turno = 0
        while robot1.energia > 0 and robot2.energia > 0:
            turno += 1
            if turno % 2 == 1:
                robot1.atacar(robot2, self)
            else:
                robot2.atacar(robot1, self)

        if robot1.energia > 0:
            ganador = robot1
            perdedor = robot2
        else:
            ganador = robot2
            perdedor = robot1

        self.resultados[ganador.nombre]['victorias'] += 1
        self.resultados[perdedor.nombre]['derrotas'] += 1
        print(f"{ganador.nombre} gana la batalla.")

    def realizar_competencia(self):
        for i in range(len(self.robots)):
            for j in range(i + 1, len(self.robots)):
                self.realizar_batalla(self.robots[i], self.robots[j])

    def generar_reporte(self):
        print("\nTabla de Victorias y Derrotas:")
        for nombre, resultado in self.resultados.items():
            print(f"{nombre}: {resultado['victorias']} victorias, {resultado['derrotas']} derrotas")
