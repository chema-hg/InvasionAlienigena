#!/usr/bin/env python3
"""Tipo juego de los marcianitos"""

import sys
from time import sleep
# Para poder poner el juego en pausa un momento cuando la nave es alcanzada.

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien



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

        # Crea una instancia para guardar las estadísticas del juego.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        # La llamada a Ship() requiere un argumento, una instancia de AlienInvasion. El argumento self
        # se refiere aquí a la instancia actual de AlienInvasión. Este es el parámetro que da a Ship acceso a los
        # recursos del juego, como, por ejemplo, el objeto screen. Asignamos una instancia de Ship a self.ship.

        self.bullets = pygame.sprite.Group()
        # Usamos este grupo para dibujar balas en la pantalla a cada paso por el bucle principal.
        # Y actualizar la posición de cada bala.

        self.aliens = pygame.sprite.Group()
        # Creamos un grupo para alojar la flota de aliens

        self._create_fleet()

        # Hace el boton play
        self.play_button = Button(self, "Jugar")


    def run_game(self):
        """Inicia el bucle principal del juego"""
        while True:
            self._check_events()
            # Método auxiliar que usamos dentro de la clase. Para ello en python
            # ponemos un guion bajo delante del nombre del método.

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Si el evento es click con el ratón.
                mouse_pos: tuple = pygame.mouse.get_pos() # cordenadas x e y del cursor al hacer clic.
                self._check_play_button(mouse_pos)

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

    def _check_play_button(self, mouse_pos):
        """Inicia un juego nuevo cuando el jugador hace clic en Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # Esta bandera contiene un valor True o False y el juego se reiniciará solo si se hace
        # click en play y el juego no esta activo actualmente. Esto es porque si no pusieramos esto
        # el boton seguiría respondiendo a los clicks incluso cuando no es visible. Por eso se
        # desactiva.
        if button_clicked and not self.stats.game_active:
            # Restablece los parámetros del juego al nivel inicial
            # Si no estuviese empezaríamos con los de la última partida.
            self.settings.initialize_dynamic_settings()
            # Para ver si el clic del ratón se colapsa con el espacio del boton.
            # Restablece las estadísticas del juego para que el jugador tenga 3 naves nuevas.
            self.stats.reset_stats()
            # Para que el juego comience en cuanto el código de esta función termine de ejecutarse.

            self.stats.game_active = True
            self.sb.prep_score()

            # Se deshace de los aliens y las balas que pudieran quedar en la pantalla.
            self.aliens.empty()
            self.bullets.empty()

            # Crea una flota nueva y centra la nave.
            self._create_fleet()
            self.ship.center_ship()

            # Oculta el cursor del ratón de la ventana cuando comienza el juego
            pygame.mouse.set_visible(False)



    def _fire_bullet(self):
        """Crea una bala nueva y la añade al grupo de balas"""
        # Comprobaremos cuantas balas hay en pantalla antes de crear una nueva.
        # Asi limitamos el número de balas en pantalla a las que se definen en settings.
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        # Cuando llamamos a update el grupo llama automáticamente a update() para cada
        # uno de sus sprites, en este caso las balas.
        # Se eliminan las balas que han desaparecido por la parte superior de la pantalla.
        # Al usar un bucle for con una lista se espera que esta tendrá la misma longitud mientras
        # se ejecute el bucle. Por eso, como no podemos quitar elementos de una lista mientras se
        # está ejecutando el bucle usamos una copia de la lista y una vez comprobado si la bala ha
        # salido de la parte superior de la pantalla la borramos de la misma.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Muestra la cantidad de balas vivas en cada ciclo del bucle.
        # Sirve para comprobar si todas las cosas funcionan, ya que se tarda más en escribir la salida
        # del terminal que en dibujar los gráficos en la pantalla del juego.
        # print(len(self.bullets))
        # El siguiente código busca balas que hayan dado a los aliens.
        # La función sprite.groupcollide() compara los rectángulos de cada elemento las bales con los
        # aliens. Devuelve un diccionario que contiene las balas y los aliens que han chocado.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_point * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        # Los dos argumentos True le dicen a Pygame que borren las balas y los aliens que choquen.
        # Podriamos hacer una superbala que arrasara a todos los aliens por su camino poniendo
        # el primer argumento booleano como False.
        if not self.aliens:
            # Destruye las balas existentes y crea una flota nueva.
            self.bullets.empty()
            self._create_fleet()
            # acelera el juego al destruir la flota enemiga
            self.settings.increase_speed()

    def _update_aliens(self):
        """
         Comprueba si la flota está en un borde,
        después actualiza las posiciones de todos los aliens de la flota.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Busca colisiones entre la nave y los aliens.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Busca aliens llegando al fondo de la pantalla
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Responde al impacto de un alien en la nave"""
        if self.stats.ships_left > 0:
            # Disminuye ships_left.
            self.stats.ships_left -= 1

            # Se deshace de los aliens y balas restantes
            self.aliens.empty()
            self.bullets.empty()

            # Crea una flota nueva y centra la nave
            self._create_fleet()
            self.ship.center_ship()

            # Pausa cuando se destruye la nave
            sleep(0.7)

        else:
            self.stats.game_active = False
            # Muestra el cursos del ratón al terminar el juego
            pygame.mouse.set_visible(True)


    def _check_aliens_bottom(self):
        """Comprueba si algún alien ha llegado al fondo de la pantalla"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Si el marcianito llega al fondo de la pantalla se trata como si hubiese
                # sido alcanzada.
                self._ship_hit()
                break

    def _create_fleet(self):
        """Crea la flota de aliens"""
        # Hace un alien. Creamos una instancia de Alien()
        alien = Alien(self)
        # Crea un alien y halla el número de aliens en una fila.
        # El espacio entre aliens es igual a la anchura de un alien.
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determina el número de filas de aliens que caben en la pantalla.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Crea la flota completa de aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        # Crea un alien y lo coloca en una fila.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Responde adecuadamente si algún alien ha llegado al borde"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Baja toda la flota y cambia su dirección"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        # Rellenamos la pantalla con el color de fondo elegido usando
        # el método fill() que actua sobre una superficie y solo tiene
        # un argumento: el color.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Después de rellenar el fondo, dibujamos la nave en la pantalla llamando a
        # ship.blitme() para que la nave aparezca encima del fondo.

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        # Cuando llamamos a draw() en un grupo, Pygame dibuja cada elemento del grupo
        # en la posición definida por su atributo rect. El argumento que le pasamos es una
        # superficie en la que dibujar los elementos del grupo.

        # Dibuja la información de la puntuación
        self.sb.show_score()

        # Dibuja el botón para jugar si el juego está inactivo.
        # Para que sea visible encima de los demás elementos de la pantalla lo dibujamos después
        # de dibujar los otros elementos, pero antes de cambiar a una pantalla nueva.
        if not self.stats.game_active:
            self.play_button.draw_button()

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
