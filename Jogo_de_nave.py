import pygame

Width, Heigth = 900, 500
WIN =  pygame.display.set_mode((Width, Heigth))

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    pygame.quit()

if __name__ == "__main__":   
    main()    