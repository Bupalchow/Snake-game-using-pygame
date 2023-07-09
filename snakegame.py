import pygame
import random
pygame.init()
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
green = (0, 0, 0)
blue = (0, 255, 0)
red = (255, 0, 0)
snake_size = 20
snake_x = window_width // 2
snake_y = window_height // 2
snake_x_change = 0
snake_y_change = 0
snake_speed = 10
snake_body = []
snake_length = 1
food_x = round(random.randrange(0, window_width - snake_size) / 20.0) * 20.0
food_y = round(random.randrange(0, window_height - snake_size) / 20.0) * 20.0
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
game_over = False
def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(window, blue, [segment[0], segment[1], snake_size, snake_size])
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_size
                snake_x_change = 0
    snake_x += snake_x_change
    snake_y += snake_y_change
    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x = round(random.randrange(0, window_width - snake_size) / 20.0) * 20.0
        food_y = round(random.randrange(0, window_height - snake_size) / 20.0) * 20.0
        snake_length += 1
    if snake_x < 0 or snake_x >= window_width or snake_y < 0 or snake_y >= window_height:
        game_over = True
    snake_head = [snake_x, snake_y]
    snake_body.append(snake_head)
    if len(snake_body) > snake_length:
        del snake_body[0]
    if snake_head in snake_body[:-1]:
        game_over = True
    window.fill(green)
    draw_snake(snake_body)
    pygame.draw.rect(window, red, [food_x, food_y, snake_size, snake_size])
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(text, (10, 10))
    pygame.display.update()
    clock.tick(snake_speed)
pygame.quit()
