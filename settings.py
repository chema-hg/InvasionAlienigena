class Settings:
    """Una clase para guardar todas las configuraciones del juego"""

    def __init__(self):
        """Inicializa la configuración del juego"""
        # Configuracion de las dimensiones de la pantalla
        self.screen_width = 1000
        self.screen_height = 600
        # Configura el color del fondo
        # En Pygame se usa RGB.
        self.bg_color = (230, 230, 230)
        # Velocidad de la nave
        self.ship_speed = 1.5
