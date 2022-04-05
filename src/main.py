import pygame
from constants import WIDTH, HEIGHT,SQUARE_SIZE, DARKGRAY , BLACK
from levels import Grid
import levelList

FPS = 60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Nonograms by Nooa')



def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    grid = Grid()



    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #Leftclick
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                print("Leftclick",row, col)

                if grid.grid_check(int(row),int(col)):
                    grid.new_marker(int(row),int(col), BLACK)
                    #grid.check_for_complition()
                else:
                    grid.remove_marker(int(row),int(col))
                pygame.display.update()

            #Rightclick
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                print("Rightclick",row, col)
                if grid.grid_check(int(row),int(col)):
                    grid.new_marker(int(row),int(col), DARKGRAY)
                else:
                    grid.remove_marker(int(row),int(col))
                pygame.display.update()

        grid.draw(WIN)
        pygame.display.update()

    pygame.quit()

main()