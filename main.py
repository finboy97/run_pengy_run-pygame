import random

import pygame
import math

# We use the sys module to get the exit method.
from sys import exit

# I want to use the State Machine library for my own learning.
from source import gamestate
from source import icicle
from source.icicle import Icicle

game_statemachine = gamestate.Game_State()

# Start and initiate pygame - called before every program.
pygame.init()
game_statemachine.start_game()


screen = pygame.display.set_mode(
    (800, 500)

#NOTES:
# Penguin jump time- 772-782ms


)  # This creates the window the game will be shown in.
pygame.display.set_caption(
    "Fin's game"
)  # This changes the name shown at the top of the window.
clock = pygame.time.Clock()
my_font = pygame.font.Font("font/snowy-season/Snowy Season/Snowy Season.ttf", 100)



floor_sprite = pygame.image.load("graphics/tile355_2_extended.png").convert_alpha()

current_score = 0
score_surf = my_font.render(str(current_score), False, "White").convert_alpha()
score_rect = score_surf.get_rect(center=(550, 40))

current_time = 0
timer_surf = my_font.render(str(current_time), False, "White").convert_alpha()
timer_rect = timer_surf.get_rect(center=(100,40))

game_over_surf = my_font.render("GAME OVER", False, "Red").convert_alpha()
game_over_rect = game_over_surf.get_rect(center=(400, 200))

penguin_surface = pygame.image.load("graphics/pixel_penguin_2.png").convert_alpha()
penguin_rectangle = penguin_surface.get_rect(bottomleft=(20, 400))
penguin_gravity = 0

background_image = pygame.image.load("graphics/tundra.jpg").convert_alpha()

icicle_surface = pygame.image.load("graphics/custom/icicle-cropped.png")
icicle_vector = [800, 400]
icicle_rect = icicle_surface.get_rect(midbottom=(icicle_vector[0], icicle_vector[1]))

finish_peng = pygame.transform.scale(penguin_surface, (200,300))
finish_rect = finish_peng.get_rect(center=(80,150))
finish_score = 0

finish_text_surf = my_font.render(f"SCORE: {finish_score}",False,"White").convert_alpha()
finish_text_rect = finish_text_surf.get_rect(center = (300,400))

restart_text = my_font.render("Restart", False, "White").convert_alpha()
restart_rect = restart_text.get_rect(center = (500,300))

pygame.mixer.init(channels=2)

music_channel = pygame.mixer.Channel(1)

def start_music():
    music = pygame.mixer.music.load("music/penguin_game_2.wav")
    pygame.mixer.music.play(-1)

start_music()

game_over_music = pygame.mixer.Sound("music/penguin_game_over_music_1.wav")
game_over_sound = pygame.mixer.Channel(2)

icicle_list = []

counter=0
ms_since_start=0

random_gen_count = random.Random()
generation_count = 25
random_num = 0
time_since_last_icicle = 0
jump_time = 800

while True:
    #print(game_statemachine.current_state)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # QUIT is a pygame constant.
            pygame.quit()  # this ends the pygame code running.
            exit()  # this is from the sys module - it stops the while loop running (ends all code effectively).
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE) and (penguin_rectangle.bottom == 400):
                penguin_gravity = -25
            if (event.key == pygame.K_SPACE) and (game_statemachine.current_state == game_statemachine.game_over):
                current_score = 0
                current_time = 0
                start_music()
                game_statemachine.restart()

    if game_statemachine.current_state==game_statemachine.game_live:
        random_num = random_gen_count.randrange(1000)
        screen.blit(background_image, (0, 0))
        screen.blit(penguin_surface, penguin_rectangle)
        # Draw all our elements
        screen.blit(floor_sprite, (0, 400))
        pygame.draw.rect(screen, "Pink", score_rect)
        pygame.draw.rect(screen, "Pink", score_rect, 10)
        screen.blit(score_surf, score_rect)
        screen.blit(timer_surf,timer_rect)

        for icicle in icicle_list:
            icicle.draw_icicle()
            if penguin_rectangle.colliderect(icicle.get_rect()):
                pygame.mixer.music.stop()
                game_statemachine.end_current_game()
                game_over_music.play()
            if icicle.update_icicle():
                current_score+=1
                icicle_list.remove(icicle)
            score_surf = my_font.render(str(current_score), False, "White").convert_alpha()


        penguin_gravity += 1
        penguin_rectangle.bottom += penguin_gravity
        if penguin_rectangle.bottom >= 400:
            penguin_rectangle.bottom = 400

        pygame.key.get_pressed()
        if penguin_rectangle.colliderect(icicle_rect):
            game_statemachine.end_current_game()


        clock.tick(60)
        counter += 1
        time_since_last_icicle+=clock.get_time()

        if counter==60:
            current_time+=1
            timer_surf=my_font.render(str(current_time),False, "White").convert_alpha()
            counter=0

    if game_statemachine.current_state==game_statemachine.game_over:
        screen.fill("Black")
        pygame.draw.rect(screen,"Black",game_over_rect)
        icicle_list.clear()
        finish_score = current_score
        finish_text_surf = my_font.render(f"SCORE: {finish_score}", False, "White").convert_alpha()
        screen.blit(game_over_surf, game_over_rect)
        screen.blit(finish_peng,finish_rect)
        screen.blit(finish_text_surf,finish_text_rect)

    pygame.display.update()


    if (random_num < generation_count) & (time_since_last_icicle > jump_time):
        new_icicle = Icicle([800, 400], screen)
        icicle_list.append(new_icicle)
        time_since_last_icicle = 0.0


