import pygame
pygame.init()
screen = pygame.display.set_mode([800, 600])
Run = True
pic = pygame.image.load("wackyball.bmp")
WHITE = (255, 255, 255)
picx = 0
picy = 0
BLACK = (0,0,0)
timer = pygame.time.Clock()      #init
speedx = 5
speedy = 5
paddleh = 25
paddley = 500
paddlew = 200
picw = 30
pich = 30
points = 0
lives = 10
pygame.mixer.init()
font = pygame.font.SysFont("None",30)
pop = pygame.mixer.Sound("get_point.wav")
boing = pygame.mixer.Sound("hit_wall.wav")
splat = pygame.mixer.Sound("splat.wav")
music = pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)


while Run:      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_a:
                points = 0
                live = 10

            
    picx += speedx    
    picy += speedy
    
     

    if picx <= 0 or picx + pic.get_width() >= 800:   
        speedx =- speedx
        boing.play() #play sound
    if picy <= 0:
        speedy =- speedy
    if picy >= 600:
        splat.play() #live - 1
        lives -=1
        speedy = -speedy

    screen.fill(BLACK)
    screen.blit(pic, (picx, picy))  


    paddlex = pygame.mouse.get_pos()[0]   
    paddlex -= paddlew
    pygame.draw.rect(screen, WHITE, (paddlex, paddley, paddlew, paddleh))   


    if picy + pich >= paddley and picy + pich <= paddley + paddleh and speedy > 0:    
        if picx + picw  >= paddlex + paddlew:
            points += 1   #got point
            pop.play()
            speedy = -speedy
            
        
    draw_string = "lives: " + str(lives) + " points: " + str(points)
    

    text = font.render(draw_string, True, WHITE) 
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 15
  


    screen.blit(text, text_rect)
    pygame.display.flip()  
    timer.tick(65)

pygame.quit()   
    


    
    
            
        
