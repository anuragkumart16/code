import pygame
root=pygame.display.set_mode((244,244))
pygame.display.set_caption("Anurag")

Quit=False
while Quit==False:
     for event in pygame.event.get():
          if event.type==pygame.QUIT:#it makes the red cross button work
               Quit=True
          print(event)
          if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_RIGHT:
                    print("You pressed right arrow key")
               elif event.key==pygame.K_UP:
                    print("you pressed up arrow key")
               elif event.key==pygame.K_LEFT:
                    print("you pressed right arrow key")
               elif event.key==pygame.K_DOWN:
                    print("you pressed down arrow key")


pygame.quit()
quit()
