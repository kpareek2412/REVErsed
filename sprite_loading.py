
import pygame 
import sprite_sheet
pygame.init()

scr_width = 500
scr_height = 500

BG = (0,0,0)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)





sprite_sheet_img = pygame.image.load("Games\\reversed\\bat.png")
spritesheet = sprite_sheet.Spritesheet(sprite_sheet_img)

frame_0 = spritesheet.get_img(0,100,100, 0.5,black)


screen = pygame.display.set_mode((scr_width,scr_height))
pygame.display.set_caption('Sprite loading')

run = True

while run:

    screen.fill(BG)

    screen.blit(frame_0, (0,0))

    

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()
quit()