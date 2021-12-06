#!/usr/bin/env python3
"""Tipo juego de los marcianitos"""

import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Clase general para gestionar los recursos y el comportamiento del juego"""

    def __init__(self):
        """Inicializa el juego y crea recursos"""
        pygame.init()
        # inicia la configuración del fondo para que pygame funcione correctamente.
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # Crea una ventana en la que dibujaremos los datos del juego.
        # Esta ventana la asignamos al atributo self.screen para que esté disponible
        # para todos los métodos de la clase.

        # sustituir lo anterior por esto si queremos pantalla completa.
        # asegurarse de poder salir pulsando q que sino no deja.
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Invasión Alienígena")

        self.ship = Ship(self)
        # la llamada a Ship() requiere un argumento, una instancia de AlienInvasion. El argumento self
        # se refiere aquí a la instancia actual de AlienInvasión. Este es el parámetro que da a Ship acceso a los
        # recursos del juego, como, por ejemplo, el objeto screen. Asignamos una instancia de Ship a self.ship.

        self.bullets = pygame.sprite.Group()
        # Usamos este grupo para dibujar balas en la pantalla a cada paso por el bucle principal.
        # Y actualizar la posición de cada bala.

    def run_game(self):
        """Inicia el bucle principal del juego"""
        while True:
            self._check_events()
            # metodo auxiliar que usamos dentro de la clase. Para ello en python
            # ponemos un guion bajo delante del nombre del método.
            self.ship.update()
            self._update_bullets()
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
        elif event.key == pygame.K_q:
            # Salir del juego usando la tecla q
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responde a liberaciones de teclas"""
        if event.key == pygame.K_RIGHT:
            # mueve la nave a la derecha al pulsar flecha derecha.
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Crea una bala nueva y la añade al grupo de balas"""
        # Comprobaremos cuantas balas hay en pantalla antes de crear una nueva.
        # Asi limitamos el numero de balas en pantalla a las que se definen en settings.
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        # Cuando llamamos a update el grupo llama automáticamente a update() para cada
        # uno de sus sprites, en este caso las balas.
        # se eliminan las balas que han desaparecido por la parte superior de la pantalla.
        # Al usar un bucle for con una lista se espera que esta tendrá la misma longitud mientras
        # se ejecute el bucle. Por eso, como no podemos quitar elementos de una lista mientras se
        # esta ejecutando el bucle usamos una copia de la lista y una vez comprobado si la bala ha
        # salido de la parte superior de la pantalla la borramos de la misma.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # Muestra la cantidad de balas vivas en cada ciclo del bucle.
        # Sirve para comprobar si todas las cosas funcionan, ya que se tarda más en escribir la salida
        # del terminal que en dibujar los gráficos en la pantalla del juego.
        # print(len(self.bullets))

    def _update_screen(self):
        # Rellenamos la pantalla con el color de fondo elegido usando
        # el metodo fill() que actua sobre una superficie y solo tiene
        # un argumento: el color.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Después de rellenar el fondo, dibujamos la nave en la pantalla llamando a
        # ship.blitme() para que la nave aparezca encima del fondo.

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Hace visible la última pantalla dibujada
        # dibuja una pantalla vacía en cada paso por el bucle while, borrando
        # la pantalla antigua para que solo se vea la nueva. Esto sirve para actualizar
        # constantemente la pantalla para mostrar las nuevas posiciones de los elementos y
        # ocultar las viejas creando la ilusión de un movimiento suave.
        pygame.display.flip()


if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()
