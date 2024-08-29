from Robot import Robot, Ataque
from Competition import CompetenciaLiga
from Report import Reporte
import json

def main():
    # Ruta del archivo JSON
    file_path = 'C:\\Users\\Tomas Doren\\Desktop\\Proyectos VSC\\Paradigmas\\Tarea_1_TD\\robots01.json'


    # Leer el archivo JSON y extraer los robots
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"El archivo {file_path} no fue encontrado.")
        return
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {file_path}.")
        return

    # Extraer los robots del archivo JSON
    robots_data = data.get('robots', [])

    # Crear instancias de Robot
    robots = []
    for robot_data in robots_data:
        # Crear instancias de Ataque desde los datos JSON
        ataques = [Ataque(**attack) for attack in robot_data.get('attacks', [])]
        
        # Crear la instancia de Robot con los ataques y habilidades
        robot = Robot(
            nombre=robot_data.get('name'),
            energia=robot_data.get('energy'),
            ataques=ataques,
        )
        robots.append(robot)

    # Verificar que haya al menos un robot para la competencia
    if not robots:
        print("No hay robots disponibles para la competencia.")
        return

    # Crear y ejecutar la competencia con todos los robots
    competencia = CompetenciaLiga(robots)
    competencia.realizar_competencia()

    # Generar reportes
    competencia.generar_reporte()
    

if __name__ == "__main__":
    main()
