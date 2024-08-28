import matplotlib.pyplot as plt

class Reporte:
    def __init__(self, competencia):
        self.competencia = competencia

    def generar_grafico_usos_ataques(self):
        for robot in self.competencia.robots:
            usos = self.competencia.resultados[robot.nombre]['usos_ataques']
            ataques = list(usos.keys())
            cantidades = list(usos.values())

            if ataques:  # Asegurarse de que hay ataques registrados
                plt.figure(figsize=(10, 6))
                plt.bar(ataques, cantidades, color='skyblue')
                plt.xlabel('Ataques')
                plt.ylabel('Cantidad de usos')
                plt.title(f'Cantidad de usos de cada ataque - {robot.nombre}')
                plt.xticks(rotation=45)
                plt.tight_layout()  # Ajusta el layout para evitar que los nombres de los ataques se solapen
                plt.show()
                plt.clf()
            else:
                print(f"No se registraron usos de ataques para {robot.nombre}.")
