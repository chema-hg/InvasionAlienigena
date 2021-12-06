"""Administrará la mayor parte del comportamiento de la nave
del jugador."""
import pygame


# Pygame usa los archivos bmp por defecto
# Es importante que el color de fondo de la imagen seleccionada tenga un fondo
# trasparente o sólido que se pueda combinar con el color del fondo del juego.

class Ship:
    """Una clase para gestionar la nave"""

    def __init__(self, ai_game):
        """inicializa la nave y configura su posición inicial"""
        self.screen = ai_game.screen
        # asignamos la pantalla a un atributo de Ship para poder acceder fácilmente
        # en todos los métodos de la clase.
        self.screen_rect = ai_game.screen.get_rect()
        # Accedemos al atributo rect de la pantalla usando el método get_rect(). Esto
        # nos permite posicionar la nave en la posición correcta de la pantalla.

        # Carga la imagen de la nave y obtiene su rect
        self.image = pygame.image.load('images/ship.bmp')
        # Para cargar la imagen de la nave
        self.rect = self.image.get_rect()
        # Cuando se carga la imagen, llamamos a get_rect() para acceder al atributo rect de
        # la superficie de la nave y poder usarlo luego para colocar el cohete.

        self.settings = ai_game.settings

        # Coloca inicialmente cada nave en el centro de la parte inferior de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

        # Guarda un valor decimal para la posición horizontal de la nave
        # Esto es porque podemos usar un valor decimal para el atributo rect, pero el rect
        # solo utilizará la parte entera de ese valor porque representa pixeles. Para poder hacer
        # un seguimiento definimos este atributo self.x que pueda guardar valores decimales.
        self.x = float(self.rect.x)

        # Bandera de movimiento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Actualiza la posición de la nave en función de la bandera de movimiento"""
        # Actualiza el valor x de la nave, no el rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Actualiza el objeto rect de self.x
        # Solo la parte entera de self.x se guarda en self.rect.x pero nos sirve
        # para mostrar la nave.
        self.rect.x = self.x

    def blitme(self):
        """Dibuja una nave en su lugar actual"""
        self.screen.blit(self.image, self.rect)
        # Dibuja la imagen en la pantalla en la posición especificada por self.rect

# Pygame nos permite gestionar los elementos del juego como que fuesen rectángulos.
# por eso trataremos tanto la pantalla como la nave como rectángulos en esta clase.
# Cuando se trabaja con un objeto rect (rectángulo) podemos usar las coordenadas x e y de los
# bordes superior, inferior, derecho e izquierdo del rectángulo, además del centro, para
# colocar el objeto.
# Para centrar un elemento del juego, trabajaremos con los atributos center, centerx o centery
# del rectángulo.
# Cuando trabajemos en un borde de la pantalla, usaremos top, bottom, left o right. También hay
# atributos que combinan estas propiedades como midbottom, midtop, midleft y midright.

# En pygame el ORIGEN DE LA PANTALLA (0,0) está en la esquina superior izquierda. Las coordenadas
# aumentan al bajar y moverse hacia la derecha. Las coordenadas hacen referencia la objeto ventana
# del juego y no a la ventana física.
