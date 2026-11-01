import json
import sys

import pygame
from src.frames_load import (
    load_attack_animations,
    load_idle_animations,
    load_walk_animations,
)

pygame.init()

with open("dark-dungeon/data/player.json", "r", encoding="utf-8") as f:
    player_data = json.load(f)
    
with open("dark-dungeon/data/main_menu.json", "r", encoding="utf-8") as f:
    main_menu_data = json.load(f)

class Game:
    def __init__(self) -> None:
        # Game Variables
        W, H = 800, 600
        self.screen = pygame.display.set_mode((W, H))
        pygame.display.set_caption("The Last Vein")
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.GROUND_X, self.GROUND_Y = 400, 500
        self.Block_x, self.Block_y = 0, 550
        self.running = True
        self.Main_Menu = True
        self.settings = False
        self.counter = 0
        self.Brightness = 80
        
        # Jumping Variables
        self.Jumping_High = 15
        self.velocity_y = 0
        self.jumping = False
        self.gravity = 0.5  
        self.jump_strength = -10
        self.ground_level = 490
        
        # Animations Variables
        self.is_walking = player_data["state"]["is_walking"]
        self.attacking = player_data["state"]["attacking"]
        self.fliped = player_data["state"]["fliped"]
        self.player_anim_walk = player_data["state"]["player_anim_walk"]
        self.player_anim_idle = player_data["state"]["player_anim_idle"]
        self.player_anim_attack = player_data["state"]["player_anim_attack"]
        
        # Buttons Variables
        self.Play_Button_Y = main_menu_data["Play_Button"]["Play_Button_Y"]
        self.Play_Button_X = main_menu_data["Play_Button"]["Play_Button_X"]
        self.Button_Width = main_menu_data["Play_Button"]["Width"]
        self.Button_Height = main_menu_data["Play_Button"]["Height"]
        
        # Buttons2 Variables
        self.Play_Button_Y2 = main_menu_data["Main_Menu_Button2"]["Main_Menu_Button_Y2"]
        self.Play_Button_X2 = main_menu_data["Main_Menu_Button2"]["Main_Menu_Button_X2"]
        self.Button_Width2 = main_menu_data["Main_Menu_Button2"]["Width2"]
        self.Button_Height2 = main_menu_data["Main_Menu_Button2"]["Height2"]
        
        # Settings Button Variables
        self.Settings_Button_Y3 = main_menu_data["Settings_Button"]["Settings_Button_Y3"]
        self.Settings_Button_X3 = main_menu_data["Settings_Button"]["Settings_Button_X3"]
        self.Button_Width3 = main_menu_data["Settings_Button"]["Width3"]
        self.Button_Height3 = main_menu_data["Settings_Button"]["Height3"]
        
        self.Settings_Button_Y4 = main_menu_data["Settings_Button2"]["Settings_Button_Y4"]
        self.Settings_Button_X4 = main_menu_data["Settings_Button2"]["Settings_Button_X4"]
        self.Button_Width4 = main_menu_data["Settings_Button2"]["Width4"]
        self.Button_Height4 = main_menu_data["Settings_Button2"]["Height4"]
        
        self.Brightness_Button_Y5 = main_menu_data["Brightness_Button"]["Settings_Button_Y5"]
        self.Brightness_Button_X5 = main_menu_data["Brightness_Button"]["Settings_Button_X5"]
        self.Button_Width5 = main_menu_data["Brightness_Button"]["Width5"]
        self.Button_Height5 = main_menu_data["Brightness_Button"]["Height5"]
        
        self.Brightness_Button_X6 = main_menu_data["Brightness_Button2"]["Brightness_Button_X6"]
        self.Brightness_Button_Y6 = main_menu_data["Brightness_Button2"]["Brightness_Button_Y6"]
        self.Button_Width6 = main_menu_data["Brightness_Button2"]["Width6"]
        self.Button_Height6 = main_menu_data["Brightness_Button2"]["Height6"]
        
        self.Settings_Button_X8 = main_menu_data["Settings_Button3"]["Settings_Button_X8"]
        self.Settings_Button_Y8 = main_menu_data["Settings_Button3"]["Settings_Button_Y8"]
        self.Button_Width8 = main_menu_data["Settings_Button3"]["Width8"]
        self.Button_Height8 = main_menu_data["Settings_Button3"]["Height8"]
        
        # Images
        self.player_image = pygame.image.load("dark-dungeon/assets/player.png").convert_alpha()
        self.block_image = pygame.image.load("dark-dungeon/assets/block1.png").convert_alpha()
        self.block1_image = pygame.image.load("dark-dungeon/assets/block.png").convert_alpha()
        self.background = pygame.image.load("dark-dungeon/assets/background.png").convert_alpha()
        self.settings_image = pygame.image.load("dark-dungeon/assets/settings.png").convert_alpha()
        
        # Scaled Images
        self.scale_background = pygame.transform.scale(self.background, (W, H))
        self.scaled_block = pygame.transform.scale(self.block_image, (15, 15))
        self.scaled_block1 = pygame.transform.scale(self.block1_image, (15, 20))
        self.scaled_player = pygame.transform.scale(self.player_image, (60, 70))
        self.scaled_settings = pygame.transform.scale(self.settings_image, (40, 40))
        self.scaled_settings2 = pygame.transform.scale(self.settings_image, (70, 70))
        
        small_bg = pygame.transform.smoothscale(self.scale_background, (W // 10, H // 10))
        self.blured_bg = pygame.transform.smoothscale(small_bg, (W, H))
        
        # ColorKeys
        self.scaled_player.set_colorkey((255, 255, 255))
        self.scaled_settings.set_colorkey((255, 255, 255))
        self.scaled_settings2.set_colorkey((255, 255, 255))
        self.settings_rect = self.scaled_settings.get_rect(topleft=(self.Play_Button_X2, self.Play_Button_Y2))
        self.settings_rect2 = self.scaled_settings2.get_rect(topleft=(720, 20))
        
        # Button
        self.button_rect = pygame.Rect(self.Play_Button_X, self.Play_Button_Y, self.Button_Width, self.Button_Height)
        self.button_rect2 = pygame.Rect(self.Play_Button_X2, self.Play_Button_Y2, self.Button_Width2, self.Button_Height2)
        self.button_rect3 = pygame.Rect(self.Settings_Button_X3, self.Settings_Button_Y3, self.Button_Width3, self.Button_Height3)
        self.button_rect4 = pygame.Rect(self.Settings_Button_X4, self.Settings_Button_Y4, self.Button_Width4, self.Button_Height4)
        self.button_rect5 = pygame.Rect(self.Brightness_Button_X5, self.Brightness_Button_Y5, self.Button_Width5, self.Button_Height5)
        self.button_rect6 = pygame.Rect(self.Brightness_Button_X6, self.Brightness_Button_Y6, self.Button_Width6, self.Button_Height6)
        self.button_rect7 = pygame.Rect(self.Brightness_Button_X6 + 185, self.Brightness_Button_Y6, self.Button_Width6, self.Button_Height6)
        
        # Overlay Settings
        self.overlay = pygame.Surface((W, H))
        self.overlay.fill((0, 0, 0))
        self.overlay.set_alpha(128)
        
        self.overlay2 = pygame.Surface((W, H))
        self.overlay2.fill((0, 0, 0))
        self.overlay2.set_alpha(200)
        
        # Font Settings
        self.font = pygame.font.SysFont(None, 60)   
        self.font2 = pygame.font.SysFont(None, 120)
        self.font3 = pygame.font.SysFont(None, 120)
        self.font4 = pygame.font.SysFont(None, 100)
        self.font5 = pygame.font.SysFont(None, 50)
        self.font6 = pygame.font.SysFont(None, 80)
        self.font7 = pygame.font.SysFont(None, 50)
        
        # Block Layers
        self.blocks = [(x, 550) for x in range(0, 800, 15)]
        self.layer1 = [(x, 565) for x in range(0, 800, 15)]
        self.layer2 = [(x, 580) for x in range(0, 800, 15)]
        
        self.walk_images = load_walk_animations()
        self.idle_images = load_idle_animations()
        self.attack_images = load_attack_animations()
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.Main_Menu:
                        if self.button_rect.collidepoint(event.pos):
                                self.Main_Menu = False
                        elif self.settings_rect.collidepoint(event.pos):
                                self.settings = True
                                self.Main_Menu = False
                    elif self.settings:
                        if self.button_rect6.collidepoint(event.pos):
                            self.Brightness = min(self.Brightness + 10, 100)
                        elif self.button_rect7.collidepoint(event.pos):
                            self.Brightness = max(self.Brightness - 10, 0)
                    if not self.Main_Menu and self.settings_rect2.collidepoint(event.pos):
                            self.settings = True
                    if self.Main_Menu and self.settings_rect2.collidepoint(event.pos):
                            self.settings = True
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not self.Main_Menu:
                        self.settings = True
                        self.Main_Menu = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not self.Main_Menu:
                    self.settings = True
                    self.Main_Menu = False
                    self.counter += 1
                    if self.counter % 2 == 0:
                        self.settings = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and not self.settings and not self.Main_Menu:
                    self.attacking = True
                    

            if self.Main_Menu:          
                self.screen.blit(self.blured_bg, (0, 0))
                self.screen.blit(self.overlay, (0, 0))
                
                pygame.draw.rect(self.screen, (43, 176, 23), self.button_rect, border_radius=8)
                pygame.draw.rect(self.screen, (0, 0, 0), self.button_rect, width=4, border_radius=8)
                
                pygame.draw.rect(self.screen, (89, 89, 89), self.button_rect2, border_radius=8)
                pygame.draw.rect(self.screen, (0, 0, 0), self.button_rect2, width=4, border_radius=8)
                
                self.text_surface = self.font.render("Play", True, (0, 0, 0))
                self.text_surface2 = self.font2.render("The Last Vein", True, (0, 0, 0))
                self.text_surface3 = self.font3.render("The Last Vein", True, (36, 89, 43))
                
                self.screen.blit(self.text_surface, (350, 255))
                self.screen.blit(self.text_surface2, (140, 120))
                self.screen.blit(self.text_surface3, (142.5, 122.5))
                self.screen.blit(self.text_surface2, (145, 125))
                self.screen.blit(self.scaled_settings, (265, 310))
                
                pygame.display.flip()
                continue
            
            elif self.settings:
                self.screen.blit(self.blured_bg, (0, 0))
                self.screen.blit(self.overlay2, (0, 0))
                
                pygame.draw.rect(self.screen, (50, 50, 50), self.button_rect3, border_radius=8)
                
                pygame.draw.rect(self.screen, (102, 101, 100), self.settings_rect, border_radius=8)
                pygame.draw.rect(self.screen, (0, 0, 0), self.settings_rect, width=4, border_radius=8)
                
                pygame.draw.rect(self.screen, (102, 101, 100), self.button_rect3, border_radius=8)
                pygame.draw.rect(self.screen, (0, 0, 0), self.button_rect3, width=4, border_radius=8)
                
                pygame.draw.rect(self.screen, (102, 101, 100), self.button_rect4, border_radius=8)
                pygame.draw.rect(self.screen, (0, 0, 0), self.button_rect4, width=4, border_radius=8)
                
                pygame.draw.rect(self.screen, (50, 50, 50), self.button_rect5, border_radius=8)
                pygame.draw.rect(self.screen, (0, 0, 0), self.button_rect5, width=4, border_radius=8)
                
                pygame.draw.rect(self.screen, (50, 50, 50), self.button_rect6, border_radius=8)
                pygame.draw.rect(self.screen, (0, 0, 0), self.button_rect6, width=4, border_radius=8)
                
                pygame.draw.rect(self.screen, (50, 50, 50), self.button_rect7, border_radius=8)
                pygame.draw.rect(self.screen, (0, 0, 0), self.button_rect7, width=4, border_radius=8)
                
                self.Rect_Brightness = pygame.Rect(370, 235, 60, 60)
                self.Rect_Brightness = pygame.Rect(580, 235, 60, 60)
                
                text_surface4 = self.font4.render("Settings", True, (0, 0, 0))
                text_surface5 = self.font5.render("Brightness", True, (255, 255, 255))
                text_surface6 = self.font6.render("+", True, (79, 191, 10))
                text_surface7 = self.font6.render("-", True, (184, 18, 9))
                text_surface8 = self.font7.render(str(self.Brightness) + "%", True, (255, 255, 255))
                text_surface9 = self.font5.render("To go back press ESC...", True, (255, 255, 255))
                
                self.screen.blit(text_surface4, (250, 120))
                self.screen.blit(text_surface5, (170, 250))
                self.screen.blit(text_surface6, (385, 235))
                self.screen.blit(text_surface7, (577, 235))
                self.screen.blit(text_surface8, (460, 250))
                self.screen.blit(text_surface9, (200, 530))
                pygame.display.flip()
                continue
                
            self.screen.blit(self.scale_background, (0, 0))
            self.screen.blit(self.scaled_settings2, (720, 20))
            
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
            
            if  self.attacking:
                self.player_anim_attack += 1
                
                total_duration_ticks = 24 / len(self.attack_images)
                idx = int(self.player_anim_attack // total_duration_ticks)
                
                if idx >= len(self.attack_images):
                    self.attacking = False
                    self.player_anim_attack = 0
                    idx = len(self.attack_images) - 1
                self.current_image = self.attack_images[idx]
            elif self.is_walking:
                self.player_anim_walk += 1
                self.current_image = self.walk_images[(self.player_anim_walk // 6) % len(self.walk_images)]
            else:
                self.player_anim_idle += 1
                self.current_image = self.idle_images[(self.player_anim_idle // 6) % len(self.idle_images)]
            
            if self.fliped:
                self.current_image = pygame.transform.flip(self.current_image, True, False)
                
            self.screen.blit(self.current_image, (self.GROUND_X, self.GROUND_Y))

            self.clock.tick(self.FPS)
            pygame.display.flip()

        pygame.quit()
        sys.exit()
    

game = Game()
game.run()