class Settings:
    """Una clase para guardar todas las configuraciones éstaticas (que no varian) del juego"""

    def __init__(self):
        """Inicializa la configuración del juego"""
        # Configuración de las dimensiones de la pantalla
        self.screen_width = 1000
        self.screen_height = 600
        # Configura el color del fondo
        # En Pygame se usa RGB.
        self.bg_color = (230, 230, 230)

        # Número de vidas
        self.ship_limit = 2  # Son 3 vidas 0,1,2

        # Configuración de las balas
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # Muchos juegos de naves limitan el número de balas que puede tener el
        # jugador en la pantalla.
        self.bullet_allowed = 4

        # Configuración del alien
        self.fleet_drop_speed = 10
        # Velocidad de bajada de los aliens al llegar al borde de la pantalla.

        # Rapidez con la que se acelera el juego cuando destruimos cada flota.
        self.speedup_scale = 1.1 # 1.1

        # Lo rapido que aumenta el valor en puntos de los aliens al avanzar el juego
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializa las configuracines que cambian durante el juego."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction = 1 es movimiento hacia la derecha y fleet_direction = -1
        # movimiento hacia la izquierda
        self.fleet_direction = 1

        # Puntuación por destrución de aliens
        self.alien_point = 50

    def increase_speed(self):
        """Incrementa las configuracines de velocidad y los valores en puntos de los aliens."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_point = int(self.alien_point * self.score_scale)



