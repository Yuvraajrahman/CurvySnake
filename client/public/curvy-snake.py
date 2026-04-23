import time
import pygame
import math
import random

pygame.init()

'''Input display'''
width = 1200
height = 400
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont("Arial", 30)
message = font.render(" Select difficulty level of the 'CURVY SNAKE':   1 = EASY, 2 = MEDIUM, 3 = HARD", True,
                      (255, 255, 255))
screen.blit(message, (50, 50))

pygame.display.update()

# input
level = None
while level not in ['1', '2', '3']:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode in ['1', '2', '3']:
                level = event.unicode

snake_speed = 0
head_radius = 0
snake_radius = 0
target_radius = 0
# difficulty level
if level == "1":
    snake_speed = 3
    head_radius = 16
    snake_radius = 10
    target_radius = 15
elif level == "2":
    snake_speed = 5
    head_radius = 8
    snake_radius = 5
    target_radius = 10
elif level == "3":
    snake_speed = 10
    head_radius = 5
    snake_radius = 3
    target_radius = 5

# display
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Curvy Snake")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREEN2 = (0, 102, 0)

clock = pygame.time.Clock()

# set up the snake
# head_radius = 7
# snake_radius = 5
snake_x = width // 2
snake_y = height // 2
# snake_speed = 5
snake_angle = 0
snake_segments = [(snake_x, snake_y)]

# set up the targets
targets = []
last_target_spawn_time = 0
target_spawn_interval = 5000
num_targets_to_spawn = 5
last_snake_length = len(snake_segments)


# set up the mid-point circle algorithm
def draw_circle(center_x, center_y, radius):
    x = radius
    y = 0
    err = 0

    while x >= y:
        pygame.draw.circle(screen, WHITE, (center_x + x, center_y + y), snake_radius)
        pygame.draw.circle(screen, WHITE, (center_x + y, center_y + x), snake_radius)
        pygame.draw.circle(screen, WHITE, (center_x - y, center_y + x), snake_radius)
        pygame.draw.circle(screen, WHITE, (center_x - x, center_y + y), snake_radius)
        pygame.draw.circle(screen, WHITE, (center_x - x, center_y - y), snake_radius)
        pygame.draw.circle(screen, WHITE, (center_x - y, center_y - x), snake_radius)
        pygame.draw.circle(screen, WHITE, (center_x + y, center_y - x), snake_radius)
        pygame.draw.circle(screen, WHITE, (center_x + x, center_y - y), snake_radius)

        y += 1
        err += 1 + 2 * y
        if 2 * (err - x) + 1 > 0:
            x -= 1
            err += 1 - 2 * x


# set up the mid-point line algorithm
def draw_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    err = dx - dy

    while True:
        pygame.draw.circle(screen, RED, (x1, y1), snake_radius)
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy


# set up the eating animation
def draw_eating_animation(x, y, radius):
    for i in range(20):
        pygame.draw.circle(screen, GREEN, (x, y), radius + i, 3)
        pygame.display.flip()
        time.sleep(0.05)


score = 0
font = pygame.font.SysFont("Arial", 25)

# game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # clear the screen
    screen.fill(GREEN2)
    # Backgroundimage

    # draw the border
    border_width = 10
    border_rect = pygame.Rect(border_width, border_width, width - 2 * border_width, height - 2 * border_width)
    pygame.draw.rect(screen, WHITE, border_rect, border_width)

    # update the snake position
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_angle += 5
    if keys[pygame.K_RIGHT]:
        snake_angle -= 5
    if keys[pygame.K_SPACE]:
        snake_speed = 1
    if keys[pygame.K_UP]:
        snake_speed *= 2

    # convert the angle to radians
    snake_angle_rad = math.radians(snake_angle)

    # calculate the new position of the snake
    snake_x += snake_speed * math.cos(snake_angle_rad)
    snake_y -= snake_speed * math.sin(snake_angle_rad)

    # check if the snake has collided with the border
    if snake_x - head_radius < border_width or snake_x + head_radius > width - border_width or \
            snake_y - head_radius < border_width or snake_y + head_radius > height - border_width:
        running = False
        print("Game Closed")

    # append the new segment to the snake_segments list
    snake_segments.append((snake_x, snake_y))
    for target in targets:
        target_x, target_y = target
        distance = math.sqrt((snake_x - target_x) ** 2 + (snake_y - target_y) ** 2)
        if distance < target_radius + snake_radius:
            targets.remove(target)
            # append the new segments to the snake_segments list
            for i in range(10):
                snake_segments.append((snake_x, snake_y))
            # increase the score
            score += 10

            # generate a new target
            target_x = random.randint(border_width + target_radius, width - border_width - target_radius)
            target_y = random.randint(border_width + target_radius, height - border_width - target_radius)
            targets.append((target_x, target_y))
            last_target_spawn_time = pygame.time.get_ticks()

    # spawn a new target
    current_time = pygame.time.get_ticks()
    if len(targets) < num_targets_to_spawn and len(snake_segments) > last_snake_length:
        target_x = random.randint(target_radius, width - target_radius)
        target_y = random.randint(target_radius, height - target_radius)
        targets.append((target_x, target_y))
        last_target_spawn_time = current_time
        # update the last snake length
        last_snake_length = len(snake_segments)

    # draw the snake
    for i, segment in enumerate(snake_segments):
        segment_x, segment_y = segment
        if i == len(snake_segments) - 1:
            # draw the head
            draw_circle(int(segment_x), int(segment_y), head_radius)
        else:
            # draw the body segments
            draw_circle(int(segment_x), int(segment_y), snake_radius)

    # draw the targets
    for target in targets:
        target_x, target_y = target
        draw_circle(int(target_x), int(target_y), target_radius)

    # line from the snake's head to its tail
    for i in range(len(snake_segments) - 1):
        x1, y1 = snake_segments[i]
        x2, y2 = snake_segments[i + 1]
        draw_line(int(x1), int(y1), int(x2), int(y2))

    # limit the length of the snake_segments list
    max_segments = 50
    if len(snake_segments) > max_segments:
        snake_segments.pop(0)

    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, WHITE)
    score_rect = score_text.get_rect(center=(width / 2, 50))
    screen.blit(score_text, score_rect)

    # spawn new targets 
    if len(targets) < num_targets_to_spawn and time.time() - last_target_spawn_time > target_spawn_interval:
        target_x = random.randint(border_width + target_radius, width - border_width - target_radius)
        target_y = random.randint(border_width + target_radius, height - border_width - target_radius)
        targets.append((target_x, target_y))
        last_target_spawn_time = time.time()

    if snake_x - snake_radius < border_width or snake_x + snake_radius > width - border_width or \
            snake_y - snake_radius < border_width or snake_y + snake_radius > height - border_width:
        running = False
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("GAME OVER", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(width / 2, height / 2))
        screen.blit(game_over_text, game_over_rect)
        pygame.display.update()

        # wait for 3 seconds
        time_start = time.time()
        while time.time() - time_start < 3:
            pass

    laser_length = 10 + int(snake_speed * 10)
    laser_width = 2
    laser_offset = 50
    laser_start_pos = (int(snake_x + (head_radius + laser_offset) * math.cos(snake_angle_rad)),
                       int(snake_y - (head_radius + laser_offset) * math.sin(snake_angle_rad)))
    laser_end_pos = (int(laser_start_pos[0] + laser_length * math.cos(snake_angle_rad)),
                     int(laser_start_pos[1] - laser_length * math.sin(snake_angle_rad)))
    pygame.draw.line(screen, GREEN, laser_start_pos, laser_end_pos, laser_width)

    current_speed = 1.0 + 0.2 * (score // 10)
    if snake_speed != current_speed:
        snake_speed = current_speed
    pygame.display.update()
    clock.tick(60)

"END GAME MESSAGE"
font_size = 120
game_over_font = pygame.font.Font(None, font_size)
game_over_text = game_over_font.render("Game Over", True, WHITE)
score_font = pygame.font.Font(None, font_size // 2)
score_text = score_font.render("Score: " + str(score), True, BLACK)
game_over_rect = game_over_text.get_rect()
score_rect = score_text.get_rect()
score_rect.top = game_over_rect.bottom + 20
score_rect.centerx = game_over_rect.centerx
screen.blit(game_over_text, (width / 2 - 150, height / 2 - 30))
screen.blit(score_text, score_rect)
pygame.display.update()
time.sleep(3)
pygame.quit()
