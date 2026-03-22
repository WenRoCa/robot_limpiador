"""
Hecho por : Rocha Cantu Nidia Wendoly  Fecha: 22  de Marzo 2026
Clase: Inteligencia artificial y su ética - Tema 4.6 Robotica - Actividad 26
MIA - Intituto Tecnológico de Nuevo Laredo - Prof. Carlos Arturo Guerrero Crespo
Titulo: Diseña tu Primer Robot Virtual
Descripción:
Proyecto de Inteligencia Artificial que simula un robot
autónomo capaz de limpiar un área, evitar obstáculos
y optimizar rutas de limpieza."""

import time
import os

# =========================
# CLASE BASE
# =========================
class RobotAutonomo:
    def __init__(self, nombre):
        self.nombre = nombre

    def navegar_a_destino(self, x, y):
        # Simula navegación a un punto
        return True

# =========================
# CLASE ROBOT LIMPIADOR CON ANIMACIÓN
# =========================
class RobotLimpiador(RobotAutonomo):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.areas_limpias = set()
        self.bateria = 100
        self.capacidad_basura = 100

    def limpiar_area(self, x, y):
        if (x, y) in self.areas_limpias:
            return False

        if self.bateria <= 0:
            print("Batería agotada, recargando...")
            self.recargar()
            return False

        if self.capacidad_basura <= 0:
            print("Basura llena, vaciando...")
            self.vaciar_basura()
            return False

        self.bateria -= 1
        self.capacidad_basura -= 1
        self.areas_limpias.add((x, y))
        return True

    def recargar(self):
        time.sleep(1)
        self.bateria = 100
        print("Batería recargada.")

    def vaciar_basura(self):
        time.sleep(1)
        self.capacidad_basura = 100
        print("Basura vaciada.")

    def mostrar_mapa(self, ancho, alto, robot_pos=None):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(alto):
            fila = ""
            for x in range(ancho):
                if robot_pos == (x, y):
                    fila += "🤖 "
                elif (x, y) in self.areas_limpias:
                    fila += "[OK] "
                else:
                    fila += "[ ] "
            print(fila)
        print(f"Batería: {self.bateria}% | Basura: {self.capacidad_basura}%")
        time.sleep(0.3)

    def planificar_ruta_limpieza(self, ancho, alto):
        print(f"\nPlanificando ruta de limpieza para área {ancho}x{alto}")
        areas_limpiadas = 0

        for y in range(alto):
            fila = range(ancho) if y % 2 == 0 else reversed(range(ancho))
            for x in fila:
                if self.navegar_a_destino(x, y):
                    self.mostrar_mapa(ancho, alto, robot_pos=(x, y))
                    if self.limpiar_area(x, y):
                        areas_limpiadas += 1

                if self.bateria <= 20:
                    self.recargar()

                if self.capacidad_basura <= 10:
                    self.vaciar_basura()

        self.mostrar_mapa(ancho, alto)
        print(f"Limpieza completada. Áreas limpiadas: {areas_limpiadas}")
        return areas_limpiadas

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    robot = RobotLimpiador("RoboLimpio")
    total = robot.planificar_ruta_limpieza(ancho=6, alto=4)
    print(f"\nÁreas limpiadas: {robot.areas_limpias}")
    print(f"Batería restante: {robot.bateria}%")
    print(f"Basura restante: {robot.capacidad_basura}%")