import math
import os
from random import randint
from collections import deque

import pygame
from pygame.locals import *
from game_file import Bird, PipePair
import numpy as np

FPS = 120
ANIMATION_SPEED = 1.5
WIN_WIDTH = 284 * 2     
WIN_HEIGHT = 512
    
class game_main():
    def __init__(self, genome, display_surface, score_font, clock):
        self.fitness = 0
        self.score = 0
        self.genome = genome
        self.middle_agg_data = -1

        self.display_surface = display_surface
        self.score_font = score_font
        self.clock = clock
        
    def load_images(self):
        def load_image(img_file_name):
            file_name = os.path.join('.', 'images', img_file_name)
            img = pygame.image.load(file_name)
            img.convert()
            return img

        return {'background': load_image('background.png'),
                'pipe-end': load_image('pipe_end.png'),
                'pipe-body': load_image('pipe_body.png'),
                
                'bird-wingup': load_image('bird_wing_up.png'),
                'bird-wingdown': load_image('bird_wing_down.png')}

    def msec_to_frames(self, milliseconds, fps=FPS):
        return fps * milliseconds / 1000.0

    @property
    def main(self):
        images = self.load_images()

        bird = Bird(50, int(WIN_HEIGHT/2 - Bird.HEIGHT/2), 2,
                    (images['bird-wingup'], images['bird-wingdown']))

        pipes = deque()

        frame_clock = 0  # this counter is only incremented if the game isn't paused
        score = 0
        done = False
        while not done:
            self.clock.tick(FPS)
            if not (frame_clock % self.msec_to_frames(PipePair.ADD_INTERVAL)):
                pp = PipePair(images['pipe-end'], images['pipe-body'])
                pipes.append(pp)
            if len(pipes) > 0:
                data = [(pipes[0].bottom_data+pipes[0].top_data)/2, bird.y, (pipes[0].x-bird.x)]
            else:
                data = [-1, -1, bird.y/10, -1]
            if self.genome.forward(data)[0] == 1:
                bird.msec_to_climb = Bird.CLIMB_DURATION

            # check for collisions
            pipe_collision = any(p.collides_with(bird) for p in pipes)
            if pipe_collision:
                done = True
                
            if 0 >= bird.y or bird.y >= WIN_HEIGHT - Bird.HEIGHT:
                done - True
                self.fitness -= 5
                
            if len(pipes) > 0:
                middle_data = (pipes[0].bottom_data+pipes[0].top_data)/2
                if self.middle_agg_data == -1:
                    self.middle_agg_data = middle_data
                elif (self.middle_agg_data == middle_data) and abs(bird.y-self.middle_agg_data) > abs(bird.y-middle_data):
                    self.fitness += 10
                    self.middle_agg_data = middle_data
                elif (self.middle_agg_data == middle_data) and abs(bird.y-self.middle_agg_data) < abs(bird.y-middle_data):
                    self.fitness -= 1
                    self.middle_agg_data = middle_data
                elif (self.middle_agg_data == middle_data) and abs(bird.y-self.middle_agg_data) == abs(bird.y-middle_data):
                    self.fitness -= 1.1
                    self.middle_agg_data = middle_data

            for x in (0, WIN_WIDTH / 2):
                self.display_surface.blit(images['background'], (x, 0))

            while pipes and not pipes[0].visible:
                pipes.popleft()

            for p in pipes:
                p.update()
                self.display_surface.blit(p.image, p.rect)

            bird.update()
            self.display_surface.blit(bird.image, bird.rect)

            # update and display score
            for p in pipes:
                if p.x + PipePair.WIDTH < bird.x and not p.score_counted:
                    self.score += 1
                    self.fitness += 20
                    p.score_counted = True

            score_surface = self.score_font.render(str(self. score), True, (255, 255, 255))
            score_x = WIN_WIDTH/2 - score_surface.get_width()/2
            self.display_surface.blit(score_surface, (score_x, PipePair.PIECE_HEIGHT))

            pygame.display.flip()
            frame_clock += 1
        #pygame.quit()

