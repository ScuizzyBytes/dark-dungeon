import sys

import pygame
from animation import load_idle_animations, load_walk_animations

pygame.init()

class Game:
    def __init__(self) -> None:
        
        # Variables
        W, H = 800, 600
        self.screen = pygame.display.set_mode((W, H))
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.GROUND_X, self.GROUND_Y = 400, 500
        self.Block_x, self.Block_y = 0, 550
        self.fliped = False
        self.running = True
        
        # Jumping Variables
        self.Jumping_High = 15
        self.velocity_y = 0
        self.jumping = False
        self.gravity = 0.5  
        self.jump_strength = -10
        self.ground_level = 490
        
        # Animations Variables
        self.player_anim_walk = 0
        self.player_anim_idle = 0
        self.is_walking = False
        
        # Images
        self.player_image = pygame.image.load("dark-dungeon/assets/player.png").convert_alpha()
        self.block_image = pygame.image.load("dark-dungeon/assets/block1.png").convert_alpha()
        self.block1_image = pygame.image.load("dark-dungeon/assets/block.png").convert_alpha()
        self.background = pygame.image.load("dark-dungeon/assets/background.png").convert_alpha()
        
        # Scaled Images
        self.scale_background = pygame.transform.scale(self.background, (W, H))
        self.scaled_block = pygame.transform.scale(self.block_image, (15, 15))
        self.scaled_block1 = pygame.transform.scale(self.block1_image, (15, 20))
        self.scaled_player = pygame.transform.scale(self.player_image, (60, 70))

        # ColorKeys
        self.scaled_player.set_colorkey((255, 255, 255))
        
        # Block Layers
        self.blocks = [(x, 550) for x in range(0, 800, 15)]
        
        self.layer1 = [(x, 565) for x in range(0, 800, 15)]
        self.layer2 = [(x, 580) for x in range(0, 800, 15)]
        
        self.walk_images = load_walk_animations()
        self.idle_images = load_idle_animations()
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print()
                
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.scale_background, (0, 0))
            
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_SPACE] and not self.jumping:
                self.velocity_y = self.jump_strength
                self.jumping = True
            
            for b_x, b_y in self.blocks:
                self.screen.blit(self.scaled_block, (b_x, b_y))
            
            for b_x, b_y in self.layer1:
                self.screen.blit(self.scaled_block1, (b_x, b_y))
                
            for b_x, b_y in self.layer2:
                self.screen.blit(self.scaled_block1, (b_x, b_y))
                
            self.velocity_y += self.gravity
            self.GROUND_Y += self.velocity_y
            
            self.is_walking = False
            
            if self.GROUND_Y >= self.ground_level:
                self.GROUND_Y = self.ground_level
                self.velocity_y = 0
                self.jumping = False
                self.player_anim_walk += 1

            if keys[pygame.K_a]:
                self.GROUND_X -= 4
                self.fliped = False
                self.is_walking = True
                self.player_anim_idle = 0
            if keys[pygame.K_d]:
                self.GROUND_X += 4
                self.fliped = True
                self.is_walking = True
                self.player_anim_idle = 0
            
            if  self.is_walking:
                self.player_anim_walk += 1
                frame_index = (self.player_anim_walk // 6) % len(self.walk_images)
                self.current_image = self.walk_images[frame_index]
            else:
                frames_index2 = (self.player_anim_idle // 6) % len(self.idle_images)
                self.current_image = self.idle_images[frames_index2]
                self.player_anim_idle += 1
            
            if self.fliped:
                self.current_image = pygame.transform.flip(self.current_image, True, False)
                
            self.screen.blit(self.current_image, (self.GROUND_X, self.GROUND_Y))

            self.clock.tick(self.FPS)
            pygame.display.flip()

        pygame.quit()
        sys.exit()
    

game = Game()
game.run()
