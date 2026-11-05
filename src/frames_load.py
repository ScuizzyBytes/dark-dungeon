import os
import pygame

# Получаем абсолютный путь к папке src, где лежит frames_load.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_walk_animations():
    walk_dir = os.path.join(BASE_DIR, "../assets/walk_anim/walk_nopick")
    walk_staright = [
        pygame.transform.scale(
            pygame.image.load(os.path.join(walk_dir, f"walk_0{i}.png")).convert_alpha(), 
            (60, 70)
        )
        for i in range(8)
    ]
    return walk_staright

def load_idle_animations():
    idle_dir = os.path.join(BASE_DIR, "../assets/idle_anim/idle_nopick")
    idle_anim = [
        pygame.transform.scale(
            pygame.image.load(os.path.join(idle_dir, f"idle_0{i}.png")).convert_alpha(), 
            (60, 70)
        )
        for i in range(5)
    ]
    return idle_anim

def load_attack_animations():
    attack_dir = os.path.join(BASE_DIR, "../assets/attack_frames/attack_anim")
    attack_anim = [
        pygame.transform.scale(
            pygame.image.load(os.path.join(attack_dir, f"attack_0{i}.png")).convert_alpha(), 
            (60, 70)
        )
        for i in range(5)
    ]
    return attack_anim