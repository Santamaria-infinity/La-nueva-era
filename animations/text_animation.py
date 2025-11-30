#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import os

def clear_screen():
    """Limpiar la pantalla de la terminal"""
    os.system('clear' if os.name != 'nt' else 'cls')

def type_text(text, delay=0.05):
    """Efecto de escritura letra por letra"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def slow_print(text, delay=0.03):
    """Imprimir texto con efecto de escritura"""
    type_text(text + "\n", delay)

def print_with_delay(text, delay=1):
    """Imprimir texto y esperar"""
    print(text)
    time.sleep(delay)

def animated_dots(message, duration=2):
    """Mostrar mensaje con puntos animados"""
    sys.stdout.write(message)
    sys.stdout.flush()
    
    for _ in range(duration * 3):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.3)
    
    print()

def fade_in_text(text, delay=0.02):
    """Efecto de aparición gradual del texto"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def dramatic_pause(text, pause_time=2):
    """Mostrar texto con pausa dramática"""
    print(text)
    time.sleep(pause_time)

def flash_text(text, times=3, delay=0.3):
    """Hacer parpadear el texto"""
    for _ in range(times):
        print(text, end='\r')
        sys.stdout.flush()
        time.sleep(delay)
        print(" " * len(text), end='\r')
        sys.stdout.flush()
        time.sleep(delay)
    print(text)

def print_centered(text, width=80):
    """Imprimir texto centrado"""
    print(text.center(width))

def print_line_animation(text, delay=0.05):
    """Animar línea por línea"""
    lines = text.split('\n')
    for line in lines:
        slow_print(line, delay)
        time.sleep(0.3)

def glitch_effect(text, iterations=2):
    """Efecto de glitch en el texto"""
    import random
    chars = list(text)
    
    for _ in range(iterations):
        glitched = chars.copy()
        for i in range(len(glitched)):
            if random.random() > 0.7:
                glitched[i] = random.choice('!@#$%^&*')
        print(''.join(glitched), end='\r')
        sys.stdout.flush()
        time.sleep(0.1)
    
    print(text)

def wave_text(text, delay=0.05):
    """Efecto de onda en el texto"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
