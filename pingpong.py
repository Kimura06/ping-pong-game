import pygame
import sys
pygame.init()


WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")
FPS = 60
CLOCK = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_SIZE = 20


player1 = pygame.Rect(30, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 50, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect((WIDTH - BALL_SIZE) // 2, (HEIGHT - BALL_SIZE) // 2, BALL_SIZE, BALL_SIZE)


player_speed = 5
ball_speed_x, ball_speed_y = 4, 4


score1, score2 = 0, 0
font = pygame.font.Font(None, 50)


game_mode = None
difficulty = None
winning_score = 5

def draw_text(text, font, color, x, y):

    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    SCREEN.blit(textobj, textrect)

def draw_objects():

    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, WHITE, player1)
    pygame.draw.rect(SCREEN, WHITE, player2)
    pygame.draw.ellipse(SCREEN, WHITE, ball)
    pygame.draw.aaline(SCREEN, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    display_score()
    pygame.display.flip()

def display_score():
    """Отображение счета."""
    score_text1 = font.render(f"{score1}", True, WHITE)
    score_text2 = font.render(f"{score2}", True, WHITE)
    SCREEN.blit(score_text1, (WIDTH // 4, 20))
    SCREEN.blit(score_text2, (3 * WIDTH // 4, 20))

def move_ball():

    global ball_speed_x, ball_speed_y, score1, score2

    ball.x += ball_speed_x
    ball.y += ball_speed_y


    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1


    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1


    if ball.left <= 0:
        score2 += 1
        reset_ball()
    if ball.right >= WIDTH:
        score1 += 1
        reset_ball()

def reset_ball():

    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x *= -1

def move_players(keys):

    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= player_speed
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += player_speed
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= player_speed
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += player_speed

def ai_move():

    global player2

    if difficulty == 'easy':

        if ball.centery > player2.centery:
            player2.y += 2
        elif ball.centery < player2.centery:
            player2.y -= 2
    elif difficulty == 'medium':

        if ball.centery > player2.centery:
            player2.y += 4
        elif ball.centery < player2.centery:
            player2.y -= 4
    elif difficulty == 'hard':

        if ball.centery > player2.centery:
            player2.y += 6
        elif ball.centery < player2.centery:
            player2.y -= 6

def show_menu():

    global game_mode, difficulty, winning_score

    while True:
        SCREEN.fill(BLACK)
        draw_text("PINGPONG", font, WHITE, WIDTH // 2, HEIGHT // 4)
        draw_text("PLAYGAME", font, WHITE, WIDTH // 2, HEIGHT // 2)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH // 2 - 100 < pygame.mouse.get_pos()[0] < WIDTH // 2 + 100 and HEIGHT // 2 - 25 < pygame.mouse.get_pos()[1] < HEIGHT // 2 + 25:
                    choose_mode()

def choose_mode():

    global game_mode, difficulty, winning_score

    while True:
        SCREEN.fill(BLACK)
        draw_text("Choose Game Mode", font, WHITE, WIDTH // 2, HEIGHT // 4)
        draw_text("1. Player vs Player", font, WHITE, WIDTH // 2, HEIGHT // 2 - 50)
        draw_text("2. Player vs AI", font, WHITE, WIDTH // 2, HEIGHT // 2 + 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH // 2 - 150 < pygame.mouse.get_pos()[0] < WIDTH // 2 + 150 and HEIGHT // 2 - 75 < pygame.mouse.get_pos()[1] < HEIGHT // 2 - 25:
                    game_mode = 'multiplayer'
                    choose_winning_score()
                elif WIDTH // 2 - 150 < pygame.mouse.get_pos()[0] < WIDTH // 2 + 150 and HEIGHT // 2 + 25 < pygame.mouse.get_pos()[1] < HEIGHT // 2 + 75:
                    game_mode = 'single'
                    choose_difficulty()

def choose_difficulty():

    global difficulty

    while True:
        SCREEN.fill(BLACK)
        draw_text("Choose Difficulty", font, WHITE, WIDTH // 2, HEIGHT // 4)
        draw_text("1. Easy", font, WHITE, WIDTH // 2, HEIGHT // 2 - 50)
        draw_text("2. Medium", font, WHITE, WIDTH // 2, HEIGHT // 2)
        draw_text("3. Hard", font, WHITE, WIDTH // 2, HEIGHT // 2 + 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH // 2 - 100 < pygame.mouse.get_pos()[0] < WIDTH // 2 + 100 and HEIGHT // 2 - 75 < pygame.mouse.get_pos()[1] < HEIGHT // 2 - 25:
                    difficulty = 'easy'
                    choose_winning_score()
                elif WIDTH // 2 - 100 < pygame.mouse.get_pos()[0] < WIDTH // 2 + 100 and HEIGHT // 2 - 25 < pygame.mouse.get_pos()[1] < HEIGHT // 2 + 25:
                    difficulty = 'medium'
                    choose_winning_score()
                elif WIDTH // 2 - 100 < pygame.mouse.get_pos()[0] < WIDTH // 2 + 100 and HEIGHT // 2 + 25 < pygame.mouse.get_pos()[1] < HEIGHT // 2 + 75:
                    difficulty = 'hard'
                    choose_winning_score()

def choose_winning_score():

    global winning_score

    while True:
        SCREEN.fill(BLACK)
        draw_text("Choose Winning Score", font, WHITE, WIDTH // 2, HEIGHT // 4)
        draw_text("1. 5", font, WHITE, WIDTH // 2, HEIGHT // 2 - 50)
        draw_text("2. 10", font, WHITE, WIDTH // 2, HEIGHT // 2)
        draw_text("3. 15", font, WHITE, WIDTH // 2, HEIGHT // 2 + 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH // 2 - 100 < pygame.mouse.get_pos()[0] < WIDTH // 2 + 100 and HEIGHT // 2 - 75 < pygame.mouse.get_pos()[1] < HEIGHT // 2 - 25:
                    winning_score = 5
                    game_loop()
                elif WIDTH // 2 - 100 < pygame.mouse.get_pos()[0] < WIDTH // 2 + 100 and HEIGHT // 2 - 25 < pygame.mouse.get_pos()[1] < HEIGHT // 2 + 25:
                    winning_score = 10
                    game_loop()
                elif WIDTH // 2 - 100 < pygame.mouse.get_pos()[0] < WIDTH // 2 + 100 and HEIGHT // 2 + 25 < pygame.mouse.get_pos()[1] < HEIGHT // 2 + 75:
                    winning_score = 15
                    game_loop()

def game_loop():

    global score1, score2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()


        if game_mode == 'single':
            ai_move()
        move_players(keys)
        move_ball()


        if score1 == winning_score or score2 == winning_score:
            draw_text("GAMEOVER", font, WHITE, WIDTH // 2, HEIGHT // 2)
            pygame.display.flip()
            pygame.time.wait(2000)
            score1, score2 = 0, 0
            show_menu()

        draw_objects()
        CLOCK.tick(FPS)


show_menu()



