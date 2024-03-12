import pygame
import random
#to check modules in pygame
pygame.init()

#colors
red = (255, 0 , 0)
green = (0,255,0)
white = (255,255,255)
black = (0,0,0)

# creating window
# set_mode : takes input like tuple 1200 - width, 500 - height
screen_width = 1200
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))

#title
pygame.display.set_caption("Snake with Swap")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])

#game loop
def game_loop():

    #game specific variable
    exit_game = False
    game_over = False

    snake_x = 45
    snake_y = 55

    velocity_x = 0
    velocity_y = 0
    init_velocity = 5

    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)

    score = 0

    snake_size = 10
    fps = 30

    snk_list = []
    snk_len = 1

    while not exit_game:

        if game_over:
            gameWindow.fill(white)
            text_screen("Game over! Press Enter to Continue", red, screen_width/2, screen_height/2)
        
        else:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 1
                # print("Score : ",score * 10)
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_len += 2

            gameWindow.fill(white)
            text_screen("Score: " + str(score * 10) ,red, 5,5 )
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            # controls snake length
            if len(snk_list)>snk_len:
                del snk_list[0]

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over == True
            

            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

game_loop()