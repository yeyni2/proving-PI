import pygame
import random
import math

pygame.init()

dict = {}
WIDTH, HEIGHT = 700, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pi")
win.fill("white")

FONT = pygame.font.Font(None, 30)
rect_size = (WIDTH - 200, HEIGHT - 300)
RED, BLUE = (255, 0, 0), (0, 0, 255)


def draw(pos_x, pos_y, color, text, count):
    pygame.draw.rect(win, "black", (100, 100, rect_size[0], rect_size[1]), 1)
    pygame.draw.circle(win, "black", (WIDTH/2, (HEIGHT-100)/2), rect_size[0]/2, 1)
    pygame.draw.rect(win, color, (pos_x, pos_y, 1, 1))
    if count == 1:
        pygame.draw.rect(win, "white", (0, HEIGHT - 200, WIDTH, 200))
        win.blit(text, (WIDTH / 3, HEIGHT - 100))
    pygame.display.update()


def main():
    run = True
    pi_str = "pi = "
    pi_val = 0
    sqr_val = 0
    circle_val = 0
    color = RED
    count = 1
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        x, y = random.randrange(100, rect_size[0] + 100), random.randrange(100, rect_size[0] + 100)
        true_y1 = (WIDTH + math.sqrt(
                    WIDTH ** 2 - 4 * (x ** 2 - x * WIDTH + WIDTH ** 2 / 2 - (rect_size[0]/2) ** 2))) / 2
        true_y2 = (WIDTH - math.sqrt(
                    WIDTH ** 2 - 4 * (x ** 2 - x * WIDTH + WIDTH ** 2 / 2 - (rect_size[0]/2) ** 2))) / 2
        if (x, y) in dict:
            continue
        else:
            dict[(x, y)] = 1
            if true_y1 >= y >= true_y2:
                circle_val += 1
                color = RED
            elif y != true_y1 and y != true_y2:
                color = BLUE
            else:
                continue
            sqr_val += 1
            pi_val = (circle_val/sqr_val)*4
            text = FONT.render(pi_str + str(pi_val), True, (0, 0, 0))
            draw(x, y, color, text, count)
            count += 1
            if count == 1700:
                count = 1







    pygame.quit()


if __name__ == '__main__':
    main()
