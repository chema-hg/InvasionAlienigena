#!/usr/bin/env python3
"""Tipo juego de los marcianitos"""

import sys

import pygame


class AlienInvasion:
    """Clase general para gestionar los recursos y el comportamiento del juego"""

    def __init__(self):
        """Inicializa el juego y crea recursos"""
        pygame.init()
        # inicia la configuración del fondo para que pygame funcione correctamente.

        self.screen = pygame.display.set_mode((1200, 800))
        # crea una ventana en la que dibujaremos los datos del juego.
        # Esta ventana la asignamos al atributo self.screen para que este disponible
        # para todos los metodos de la clase.
        pygame.display.set_caption("Invasión Alienígena")

        # Configura el color del fondo
        # En Pygame se usa RGB.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Incia el bucle principal del juego"""
        while True:
            # Busca eventos del teclado y el ratón
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Rellenamos la pantalla con el color de fondo elegido usando
            # el metodo fill() que actua sobre una superficie y solo tiene
            # un argumento: el color.
            self.screen.fill(self.bg_color)

            # Hace visible la última pantalla dibujada
            # dibuja una pantalla vacia en cada paso por el bucle while, borrando
            # la pantalla antigua para que solo se vea la nueva. Esto sirve para actualizar
            # constantemente la pantalla para mostrar las nuevas posiciones de los elementos y
            # ocultar las viejas creando la ilusión de un movimiento suave.
            pygame.display.flip()


if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()
