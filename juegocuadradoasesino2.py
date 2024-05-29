import pygame
import sys
import random

# Iniciar Pygame
pygame.init()

# Configuración de la ventana
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cuadrado asesino")

# Color del fondo
background_color = (0, 0, 0)

# tamaño y posición inicial del cuadrado
square_size = 50
x = width // 2 - square_size // 2
y = height // 2 - square_size // 2

# velocidad del cuadrado
speed = 5

# Creaación del láser para el juego
class Laser:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 20
        self.speed = 10

    def move(self):
        self.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))

# Crear un espacio para los otros cubos
class Target:
    def __init__(self):
        self.x = random.randint(0, width - 20)
        self.y = random.randint(0, height // 2 - 20)
        self.width = 20
        self.height = 20
        self.speed = 2

    def move(self):
        self.y += self.speed
        if self.y > height - self.height or self.y < 0:
            self.speed *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))

# Inicializar el puntaje y el marcador
score = 0

# Inicializar el laser
laser = None

# Inicializar los otros cubitos
targets = [Target() for _ in range(5)]

# bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Detectar las teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= speed # Mueve el cuadrado hacia arriba
    if keys[pygame.K_DOWN]:
        y += speed # Mueve el cuadrado hacia abajo
    if keys[pygame.K_RIGHT]:
        x += speed # Mueve el cuadrado hacia la derecha
    if keys[pygame.K_LEFT]:
        x -= speed # Mueve el cuadrado hacia la izquierda
    
    # Comprobar si la tecla para disparar el láser está siendo presionada
    if keys[pygame.K_SPACE]:
        if laser is None:
            laser = Laser(x + square_size // 2, y + square_size)

    # Mover el laser
    if laser is not None:
        laser.move()

    # Mover los otros cuadrados
    for target in targets:
        target.move()

    # Comprobar si el disparo del láser fue acertado y así sumar un punto al tablero
    if laser is not None:
        for target in targets:
            if (laser.x >= target.x and laser.x <= target.x + target.width and
                laser.y >= target.y and laser.y <= target.y + target.height):
                score += 1
                targets.remove(target)
                targets.append(Target())
                laser = None
                break

    # Comprobar si el láser sale de la pantalla
    if laser is not None and laser.y < 0:
        laser = None

    # mantener el cuadrado en los límites de la pantalla
    if x < 0:
        x = 0
    elif x + square_size > width:
        x = width - square_size
    if y < 0:
        y = 0
    elif y + square_size > height:
        y = height - square_size

    # llenar el fondo, y dubujar el cuadrado, el laser, y los cuadraditos a los cuales se les va a disparar para sumar puntos al marcador
    screen.fill(background_color)
    pygame.draw.rect(screen, (255, 0, 0), (x, y, square_size, square_size))
    if laser is not None:
        laser.draw(screen)
    for target in targets:
        target.draw(screen)

    # mostrar el puntaje en el marcador
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(60)

# salir de Pygame
pygame.quit()
sys.exit()