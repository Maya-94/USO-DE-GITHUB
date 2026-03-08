import pygame
import sys

# Inicializar
pygame.init()
ANCHO, ALTO = 600, 800
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tarjeta Día de la Mujer")

# --- CONFIGURACIÓN ---
# IMPORTANTE: Asegúrate de que la imagen esté en la carpeta del proyecto
# y se llame exactamente 'rosa.jpg'
try:
    fondo = pygame.image.load("rosa.jpg")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
except:
    fondo = pygame.Surface((ANCHO, ALTO))
    fondo.fill((50, 0, 50))  # Fondo morado si no hay foto

fuente = pygame.font.SysFont("serif", 30, bold=True)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

texto = [
    "Ésta linda rosa para",
    "para ti mujer hermosa",
    "que con tan linda sonrisa",
    "pintas de colores el universo",
    "",
    "¡FELIZ DÍA!",
    "Un abrazo..."
]


def ejecutar():
    y_texto = ALTO
    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pantalla.blit(fondo, (0, 0))

        # Dibujar texto animado
        for i, linea in enumerate(texto):
            render = fuente.render(linea, True, BLANCO)
            sombra = fuente.render(linea, True, NEGRO)
            x = ANCHO // 2 - render.get_width() // 2
            y = y_texto + (i * 50)
            pantalla.blit(sombra, (x + 2, y + 2))  # Sombra
            pantalla.blit(render, (x, y))

        if y_texto > 250:  # Sube hasta esta posición
            y_texto -= 2

        pygame.display.flip()
        reloj.tick(60)


ejecutar()