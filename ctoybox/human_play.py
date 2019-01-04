import toybox, sys
from toybox.toybox import Toybox, Input
import numpy as np
import argparse
import pygame
import pygame.key
from pygame.locals import *
import pygame.surfarray


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='human_play for toybox')
    parser.add_argument('game', type=str, help='try one of amidar, breakout, space_invaders')

    args = parser.parse_args()
    print('Starting up: '+args.game)
    pygame.init()

    with Toybox(args.game) as tb:
        w = tb.get_width()
        h = tb.get_height()

        pygame.display.set_mode((w, h))
        clock = pygame.time.Clock()
        FPS = 24

        quit = False
        while not quit:
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit = True
                    break
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    quit = True
                    break
            key_state = pygame.key.get_pressed()
            player_input = Input()
            player_input.left = key_state[K_LEFT] or key_state[K_a]
            player_input.right = key_state[K_RIGHT] or key_state[K_d]
            player_input.up = key_state[K_UP] or key_state[K_w]
            player_input.down = key_state[K_DOWN] or key_state[K_s]
            player_input.button1 = key_state[K_z] or key_state[K_SPACE]
            player_input.button2 = key_state[K_x] or key_state[K_RSHIFT] or key_state[K_LSHIFT]

            tb.apply_action(player_input)
            image = tb.get_rgb_frame()
            screen = pygame.display.get_surface()
            pygame.surfarray.blit_array(screen, np.swapaxes(image,0,1))
            pygame.display.update()
            clock.tick(FPS)
    pygame.quit()
    sys.exit()