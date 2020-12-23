import sys, pygame
pygame.init()

# COLORES
negro = (0, 0, 0)
blanco = (255, 255, 255)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

size = (720, 450)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.display.set_caption("Pong")

pygame.mouse.set_visible(0)

ph = 30
pw = 90

#--- JUGADOR 1
kY = 100
kX = 10

kXs = 0
kYs = 0

#--- JUGADOR 2
kY2 = 100
kX2 = 670

kXs2 = 0
kYs2 = 0

#--- BOLA
ballY = 225
ballX = 360

ballXs = 3
ballYs = 3

#--- BUCLE PRINCIPAL
gameOver = False
while not gameOver:
    #--- APARTADO DEL SISTEMA
    for event in pygame.event.get():
        if event.type == pygame.QUIT: gameOver = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameOver = True

            if event.key == pygame.K_UP:
                kYs = -3
            if event.key == pygame.K_DOWN:
                kYs = 3
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                kYs = 0
            if event.key == pygame.K_DOWN:
                kYs = 0
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                kYs2 = -3
            if event.key == pygame.K_s:
                kYs2 = 3
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                kYs2 = 0
            if event.key == pygame.K_s:
                kYs2 = 0
    
    #--- LOGICA DEL JUEGO
    kX += kXs
    kY += kYs

    kX2 += kXs2
    kY2 += kYs2

    if (kY > 370):
        kY = 360
    if (kY < 0):
        kY = 1
    
    if (kY2 > 370):
        kY2 = 360
    if (kY2 < 0):
        kY2 = 1
    
    #--- BOLA
    if (ballX > 710 or ballX < 0):
        ballX = 360
        ballY = 225
        ballXs *= -1
        ballYs *= -1
        kY = 100
        kX = 10
        kY2 = 100
        kX2 = 670
        
    if (ballY > 430 or ballY < 2):
        ballYs *= -1
    ballX += ballXs
    ballY += ballYs

#    mP = pygame.mouse.get_pos()
#    mPx = mP[0]
#    mPy = mP[1]

    screen.fill(negro)
    
    pOne = pygame.draw.rect(screen, blanco, (kX, kY, ph, pw))
    pTwo = pygame.draw.rect(screen, blanco, (kX2, kY2, ph, pw))

    ball = pygame.draw.circle(screen, blanco, (ballX, ballY), 15)

    if ball.colliderect(pOne) or ball.colliderect(pTwo):
        ballXs *= -1
    pygame.display.flip()
    clock.tick(60)