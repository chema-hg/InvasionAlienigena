class Settings:
    """Una clase para guardar todas las configuraciones del juego"""

    def __init__(self):
        """Inicializa la configuración del juego"""
        # Configuración de las dimensiones de la pantalla
        self.screen_width = 1000
        self.screen_height = 600
        # Configura el color del fondo
        # En Pygame se usa RGB.
        self.bg_color = (230, 230, 230)
        # Velocidad de la nave
        self.ship_speed = 1.5
        # Configuración de las balas
        self.ship_limit = 3
        # número de naves del jugador
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # Muchos juegos de naves limitan el número de balas que puede tener el
        # jugador en la pantalla.
        self.bullet_allowed = 4
        # Configuración del alien
        self.alien_speed = 0.8
        # Velocidad de movimiento del alien hacia la derecha
        self.fleet_drop_speed = 10
        # Velocidad de bajada de los aliens al llegar al borde de la pantalla.
        # fleet_direction = 1 es movimiento hacia la derecha y fleet_direction = -1
        # movimiento hacia la izquierda
        self.fleet_direction: int = 1

