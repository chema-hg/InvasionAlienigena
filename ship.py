"""Administrará la mayor parte del comportamiento de la nave
del jugador."""
import pygame


# Pygame usa los archivos bmp por defecto
# Es importante que el color de fondo de la imagen selecionada tenga un fondo
# trasparente o sólido que se pueda combinar con el color del fondo del juego.

class Ship:
    """Una clase para gestionar la nave"""

    def __init__(self, ai_game):
        """inicializa la nave y configura su posion inicial"""
        self.screen = ai_game.screen
        # asignamos la pantalla a un atributo de Ship para poder acceder facilmente
        # en todos los metodos de la clase.
        self.screen_rect = ai_game.screen.get_rect()
        # accedemos al atributo rect de la pantalla usando el método get_rect(). Esto
        # nos permite posicionar la nave en la posición correcta de la pantalla.

        # Carga la imagen de la nave y obtiene su rect
        self.image = pygame.image.load('images/ship.bmp')
        # Para cargar la imagen de la nave
        self.rect = self.image.get_rect()
        # Cuando se carga la imagen, llamamos a get_rect() para acceder al atributo rect de
        # la superficie de la nave y poder usarlo luego para colocar el cohete.

        # Coloca inicialmente cada nave en el centro de la parte inferor de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

        # Bandera de movimiento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Actualiza la posición de la nave en función de la bandera de movimiento"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1


    def blitme(self):
        """Dibuja una nave en su lugar actual"""
        self.screen.blit(self.image, self.rect)
        # Dibuja la imagen en la pantalla en la posición especificada por self.rect


# Pygame nos permite gestionar los elementos del juego como que fuesen rectangulos.
# por eso trataremos tanto la pantalla como la nave como rectangulos en esta clase.
# Cuando se trabaja con un objeto rect (rectangulo) podemos usar las coordenadas x e y de los
# bordes superior, inferior, derecho e izquierdo del rectangulo, además del centro, para
# colocar el objeto.
# Para centrar un elemento del juego, trabajaremos con los atributos center, centerx o centery
# del rectangulo.
# Cuando trabajemos en un borde de la pantalla, usaremos top, bottom, left o right. Tambien hay
# atributos que combinan estas propiedades como midbottom, midtop, midleft y midright.

# En pygame el ORIGEN DE LA PANTALLA (0,0) esta en la esquina superior izquierda. Las coordenadas
# aumentan al bajar y moverse hacia la derecha. Las coordenadas hacen referencia la objeto ventana
# del juego y no a la ventana física.
