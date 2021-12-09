import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """Una clase para dar información de la puntuación"""

    def __init__(self, ai_game):
        """Inicializa los atributos de la puntuación"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Configuración de la fuente para mostrar la información
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara la imagen de la puntuación inicial
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Convierte la información en una imagen renderizada"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"POINTS {rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Muestra la puntuación en la parte superior derecha de la pantalla
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Convierte la puntuación más alta en una imagen renderizada"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"MAX. {high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Centra la puntuación más alta en la parte superior de la pantalla.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Dibuja la puntación, nivel y naves en la pantalla"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """Comprueba si hay una puntuación más alta"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Convierte el nivel en una clase renderizada."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Coloca el nivel debajo de la puntuación.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

        # El método prep_leve() crea una imagen a partir del valor guardado en stats.level y configura el atributo right
        # de la imagen para que coincida con el atributo right de la puntuación. Luego establece el atributo top 10 px
        # pr debajo del borde inferior de la imagen de la puntuación  para dejar espacio entre el marcador y el nivel.

    def prep_ships(self):
        """Muestran cuantas naves quedan por pantalla"""
        self.ships = Group() # Crea un grupo vacio par recoger las instancias de la nave
        for ship_number in range(self.stats.ships_left): # para rellenar el grupo se ejecuta este bucle.
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)