# https://www.makeuseof.com/pygame-collision-detection-physics/

import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.y_velocity = 1
        self.x_velocity = 1

    def update(self):
        self.rect.y += self.y_velocity
        self.rect.x += self.x_velocity


        
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))

# posições iniciais do player
x = 10
y = 320

player = Player(x, y)
player_group = pygame.sprite.Group()
player_group.add(player)

platform_group = pygame.sprite.Group()

# apenas adicionei mais obstáculos
# a colisão de grupo (linha 71) já vai verificar tudo :-)

lista="300,1,20,170|400,1,20,100|400,400,20,200"
quadrados=lista.split("|")
for q in quadrados:
    numeros=q.split(",")
    platform = Platform(int(numeros[0]), int(numeros[1]), int(numeros[2]), int(numeros[3]))
    platform_group.add(platform)

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # salva posições antes de modificá-las
    antes_x = player.rect.x
    antes_y = player.rect.y

    # captura de eventos do teclado
    pk = pygame.key.get_pressed()

    # verifica se tem que fazer algo
    if pk[pygame.K_LEFT]:
        player.rect.x -= 1
    if pk[pygame.K_RIGHT]:
        player.rect.x += 1
    if pk[pygame.K_UP]:
        player.rect.y -= 2
    if pk[pygame.K_DOWN]:
        player.rect.y += 2    

    # executa um método que está em um grupo de elementos
    # por enquanto, só tem 1 elemento no grupo
    player_group.update()

    # colidiu?
    collided = pygame.sprite.spritecollide(player, platform_group, False)

    # se colidiu...
    if collided:
        # restaura posições
        player.rect.x = antes_x
        player.rect.y = antes_y

    screen.fill("yellow")
    player_group.draw(screen)
    platform_group.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()