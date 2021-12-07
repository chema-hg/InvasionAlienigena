class GameStats:
    """Estadísticas del juego"""
    def __init__(self, ai_game):
        """Inicializa las estadísticas"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Inicializa las estadísticas qeu pueden cambiar durante el juego"""
        self.ships_left = self.settings.ship_limit

    # Inicia Alien Invasion en estado activo.


