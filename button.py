# Pygame no cuenta con un método integrado para hacer botone, asi que se
# crea una clase Button para crear un rectangulo relleno con una etiqueta.
# Se puede usar este código para hacer cualquier botón en el juego.

import pygame.font
# Módulo que permite mostrar texto en la pantalla.

class Button:

    def __init__(self, ai_game, msg):
        """Inica todos los atributos del boton"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Configura las dimensiones y propiedades del boton
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0) # verde claro
        self.text_color = (255, 255, 255) # texto blanco
        self.font = pygame.font.SysFont(None, 48) # none = fuente predeterminada, 48 tamaño texto.

        # Crea el objeto rect del botón y lo centra.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # creamos un rectángulo para el botón
        self.rect.center = self.screen_rect.center
        # Configuramos su atributo center para que coincida con el de la pantalla.

        # Solo hay que preparar el mensaje del botón una vez.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """"Convierte el mensaje en una imagen renderizada y centra el texto en el botón"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        # Convierte el texto almacenado en msg en una imagen. Argumentos posicionales:
        # msg es el texto
        # True es el suavizado
        # colores de la fuente
        # colores del fondo. (sino se incluye pygame intenta poner un fondo trasparente.
        self.msg_image_rect = self.msg_image.get_rect() # centramos la imagen en el boton
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Dibuja un boton sin contenido y luego el mensaje
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)





