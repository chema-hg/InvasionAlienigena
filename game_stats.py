class GameStats:
    """Estadísticas del juego"""
    def __init__(self, ai_game):
        """Inicializa las estadísticas"""
        self.settings = ai_game.settings
        self.reset_stats()
        # inicia el juego en un estado inactivo
        self.game_active = False
        # La puntuación más alta no se debe restablecer
        self.high_score = 0


    def reset_stats(self):
        """Inicializa las estadísticas que pueden cambiar durante el juego"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
