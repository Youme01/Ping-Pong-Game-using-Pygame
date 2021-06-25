import pygame
import random

pygame.init()

clock = pygame.time.Clock()

display_width = 500
display_height = 300

#variables
x=100
y=100
radius =10
dx= 3
dy=3
speed = 30

paddle_x = 10
paddle_y = 10 
paddle_width = 3
paddle_height = 40

play_score = 0

#height and width
display = pygame.display.set_mode((display_width,display_height))

#Title
pygame.display.set_caption("Let's Pong")

#Functions:
def randomize_start():
    global x,y,dy
    x = random.randint(int(display_width/4),display_width - 20)
    y = random.randint(10, display_height - 10)
    
    if random.randint(0,2) % 2 == 0:
        dy *= -1

def hit_back():
    if x + radius > display_width:
        return True
    return False

def hit_sides():
    #Top
    if y - radius < 0:
        return True
    #Bottom
    if y + radius > display_height:
        return True
    return False

def hit_paddle():
    global play_score
    if x - radius <= paddle_x + paddle_width and y > paddle_y and y < paddle_y + paddle_height:
        play_score += 100
        return True
    return False 

def game_over():
    end_game = True
    global play_score

    display.fill((173,216,230))
    font_title = pygame.font.Font(None, 36)
    font_ins =  pygame.font.Font(None, 24)  
    txt = font_title.render("Game Over", True, (0,0,0))
    txt_rect = txt.get_rect(center = (int(display_width/2), int(display_height/3)))
    display.blit(txt,txt_rect)

    ins = font_ins.render("Press q to Quit", True, (0,0,0))
    ins_rect = ins.get_rect(center = (int(display_width/2), int(display_height/1.5)))
    display.blit(ins, ins_rect)

    R_ins = font_ins.render("Press r to Resume", True, (0,0,0))
    Rins_rect = ins.get_rect(center = (int(display_width/2), int(display_height/1.3)))
    display.blit(R_ins, Rins_rect)

    final_score = "Final Score: " + str(play_score)
    score_txt = font_ins.render(final_score,True, (0,0,128))
    Sins_rect = score_txt.get_rect(center = (int(display_width/2), int(display_height/2)))
    display.blit(score_txt, Sins_rect)

    pygame.display.flip()
    while(end_game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
                if event.key == pygame.K_r:
                    end_game = False

display.fill((173,216,230))
welcome_screen = pygame.font.Font(None, 30)
welcome = welcome_screen.render ("Let's Play Ping Pong!!", True, (0,0,128))
welcome_rect = welcome.get_rect(center = (int(display_width/2), int(display_height/3)))

startMsg = welcome_screen.render ("Hit 's' to Start, or Autostart in 5 seconds", True, (0,0,128))
startMsg_rect = startMsg.get_rect(center = (int(display_width/2), int(display_height/4)))

display.blit(welcome,welcome_rect)
display.blit(startMsg,startMsg_rect)
pygame.display.flip()

pygame.time.set_timer(pygame.USEREVENT,5000)

timer_active = True

while(timer_active):
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            timer_active = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                timer_active = False
randomize_start()
#Game Loop
while True:
    clock.tick(speed)

    pressed_key = pygame.key.get_pressed()

    # paddle movement with key pressed
    if pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]:
        if paddle_y + paddle_height + 10 <= display_height:
            paddle_y += 10
    if pressed_key[pygame.K_UP] or pressed_key[pygame.K_w]:
        if paddle_y - 10 >= 0:
            paddle_y -= 10

    #Quit game with clicking cross button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    display.fill((173,216,230))
    x += dx
    y += dy

    pygame.draw.rect(display,(0,0,128),(paddle_x,paddle_y,paddle_width,paddle_height))
    #Drawing circle
    pygame.draw.circle(display,(255,255,255),(x,y),radius)

    if x < radius :
        game_over()
        randomize_start()
        dx = abs(dx)
        play_score = 0
    if hit_back() or hit_paddle():
        dx *= -1
    if hit_sides():
        dy *= -1
    pygame.display.update()

