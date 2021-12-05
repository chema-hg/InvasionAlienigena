#!/usr/bin/env python3
"""Tipo juego de los marcianitos"""

import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Clase general para gestionar los recursos y el comportamiento del juego"""

    def __init__(self):
        """Inicializa el juego y crea recursos"""
        pygame.init()
        # inicia la configuración del fondo para que pygame funcione correctamente.
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # crea una ventana en la que dibujaremos los datos del juego.
        # Esta ventana la asignamos al atributo self.screen para que este disponible
        # para todos los metodos de la clase.

        # sustituir lo anterior por esto si queremos pantalla completa.
        # asegurarse de poder salir pulsando q que sino no deja.
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Invasión Alienígena")

        self.ship = Ship(self)
        # la llamada a Ship() requiere un argumento, una instancia de AlienInvasion. El argumento self
        # se refiere aqui a la instancia actual de AlienInvasión. Este es el parametro que da a Ship acceso a los
        # recursos del juego, como, por ejemplo, el objeto screen. Asignamos una instancia de Ship a self.ship.

    def run_game(self):
        """Inicia el bucle principal del juego"""
        while True:
            self._check_events()
            # metodo auxiliar que usamos dentro de la clase. Para ello en python
            # ponemos un guion bajo delante del nombre del método.
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Responde a pulsaciones del teclado y eventos de ratón"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Si el evento es una pulsación de tecla (KEYDOWN)
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                # Si el evento es levantar una tecla (KEYUP)
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responde a pulsaciones de teclas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == K_q:
            # Salir del juego usando la tecla q
            sys.exit()

    def _check_keyup_events(self, event):
        """Responde a liberaciones de teclas"""
        if event.key == pygame.K_RIGHT:
            # mueve la nave a la derecha al pulsar flecha derecha.
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # Rellenamos la pantalla con el color de fondo elegido usando
        # el metodo fill() que actua sobre una superficie y solo tiene
        # un argumento: el color.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Despues de rellenar el fondo, dibujamos la nave en la pantalla llamando a
        # ship.blitme() para que la nave aparezca encima del fondo.

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
