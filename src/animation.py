import pygame


def load_walk_animations():
    walk_staright = [
        pygame.transform.scale(pygame.image.load("dark-dungeon/assets/walk_anim/walk_nopick/walk_00.png").convert_alpha(), (60, 70)),
        pygame.transform.scale(pygame.image.load("dark-dungeon/assets/walk_anim/walk_nopick/walk_01.png").convert_alpha(), (60, 70)),
        pygame.transform.scale(pygame.image.load("dark-dungeon/assets/walk_anim/walk_nopick/walk_02.png").convert_alpha(), (60, 70)),
        pygame.transform.scale(pygame.image.load("dark-dungeon/assets/walk_anim/walk_nopick/walk_03.png").convert_alpha(), (60, 70)),
        pygame.transform.scale(pygame.image.load("dark-dungeon/assets/walk_anim/walk_nopick/walk_04.png").convert_alpha(), (60, 70)),
        pygame.transform.scale(pygame.image.load("dark-dungeon/assets/walk_anim/walk_nopick/walk_05.png").convert_alpha(), (60, 70)),
        pygame.transform.scale(pygame.image.load("dark-dungeon/assets/walk_anim/walk_nopick/walk_06.png").convert_alpha(), (60, 70)),
        pygame.transform.scale(pygame.image.load("dark-dungeon/assets/walk_anim/walk_nopick/walk_07.png").convert_alpha(), (60, 70))
    ]
    
    return walk_staright

def load_idle_animations():
    idle_anim = [
        pygame.transform.scale(pygame.image.load("dark-dungeon/assets/idle_anim/idle_nopick/idle_00.png").convert_alpha(), (60, 70)),
        pygame.transform.scale(pygame.image.load("dark-dungeon/assets/idle_anim/idle_nopick/idle_01.png").convert_alpha(), (60, 70)),
        pygame.transform.scale(pygame.image.load("dark-dungeon/assets/idle_anim/idle_nopick/idle_02.png").convert_alpha(), (60, 70)),
        pygame.transform.scale(pygame.image.load("dark-dungeon/assets/idle_anim/idle_nopick/idle_03.png").convert_alpha(), (60, 70)),
        pygame.transform.scale(pygame.image.load("dark-dungeon/assets/idle_anim/idle_nopick/idle_04.png").convert_alpha(), (60, 70))
    ]
    
    return idle_anim

