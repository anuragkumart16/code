import pygame
root=pygame.display.set_mode((244,255))
pygame.display.set_caption("Anurag")

Quit=False
#game_loop
while Quit==False:
     for event in pygame.event.get():
          if event.type==pygame.QUIT:
               Quit=True
          

print("loop is ended")
pygame.quit()
quit()
