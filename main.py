#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from animations.text_animation import clear_screen, type_text, slow_print
from ascii_art.menu_art import show_title, show_menu
from story.el_principio import show_intro_story
from game_logic.save_system import SaveSystem

def main_menu():
    """Menú principal del juego"""
    save_system = SaveSystem()
    
    while True:
        clear_screen()
        show_title()
        show_menu()
        
        choice = input("\n> Elige una opción (1-3): ").strip()
        
        if choice == "1":
            # Nueva Partida
            clear_screen()
            type_text("Iniciando nueva partida...\n", 0.05)
            slot = select_save_slot(save_system, mode="save")
            if slot:
                start_new_game(save_system, slot)
        
        elif choice == "2":
            # Cargar Partida
            clear_screen()
            slot = select_save_slot(save_system, mode="load")
            if slot:
                load_game(save_system, slot)
        
        elif choice == "3":
            # Salir
            clear_screen()
            type_text("Gracias por jugar 'El inicio de 1 nueva era'\n", 0.05)
            type_text("Hasta pronto, superviviente...\n", 0.05)
            sys.exit(0)
        
        else:
            slow_print("\n❌ Opción inválida. Intenta de nuevo.", 0.03)
            input("\nPresiona ENTER para continuar...")

def select_save_slot(save_system, mode="save"):
    """Seleccionar slot de guardado (1-3)"""
    clear_screen()
    
    if mode == "save":
        type_text("=== SELECCIONAR SLOT DE GUARDADO ===\n\n", 0.03)
    else:
        type_text("=== CARGAR PARTIDA ===\n\n", 0.03)
    
    # Mostrar los 3 slots
    for i in range(1, 4):
        save_data = save_system.load_game(i)
        if save_data:
            print(f"[{i}] Slot {i} - Nivel {save_data.get('level', 1)} | {save_data.get('location', 'Desconocido')}")
        else:
            print(f"[{i}] Slot {i} - Vacío")
    
    print("\n[0] Volver al menú")
    
    choice = input("\n> Elige un slot (0-3): ").strip()
    
    if choice == "0":
        return None
    elif choice in ["1", "2", "3"]:
        slot = int(choice)
        
        if mode == "load":
            save_data = save_system.load_game(slot)
            if not save_data:
                slow_print("\n❌ Este slot está vacío.", 0.03)
                input("\nPresiona ENTER para continuar...")
                return None
        
        return slot
    else:
        slow_print("\n❌ Opción inválida.", 0.03)
        input("\nPresiona ENTER para continuar...")
        return None

def start_new_game(save_system, slot):
    """Iniciar una nueva partida"""
    clear_screen()
    
    # Mostrar la historia de introducción
    show_intro_story()
    
    # Crear datos iniciales del jugador
    player_data = {
        "name": "Superviviente",
        "level": 1,
        "mana": 10,
        "max_mana": 10,
        "location": "Ruinas del Mundo Antiguo",
        "inventory": [],
        "skills": ["Creación Básica"]
    }
    
    # Guardar la partida
    save_system.save_game(slot, player_data)
    
    type_text("\n✅ Partida guardada en Slot " + str(slot) + "\n", 0.05)
    input("\nPresiona ENTER para continuar...")
    
    # Aquí continuaría el juego...
    game_loop(save_system, slot, player_data)

def load_game(save_system, slot):
    """Cargar una partida existente"""
    clear_screen()
    
    player_data = save_system.load_game(slot)
    
    if player_data:
        type_text(f"Cargando partida del Slot {slot}...\n", 0.05)
        type_text(f"\nBienvenido de nuevo, {player_data['name']}\n", 0.05)
        type_text(f"Nivel: {player_data['level']}\n", 0.03)
        type_text(f"Ubicación: {player_data['location']}\n", 0.03)
        
        input("\nPresiona ENTER para continuar...")
        
        # Aquí continuaría el juego...
        game_loop(save_system, slot, player_data)

def game_loop(save_system, slot, player_data):
    """Loop principal del juego"""
    clear_screen()
    type_text("\n🎮 El juego continuará aquí...\n", 0.05)
    type_text("(Esta es la versión inicial del menú)\n", 0.03)
    input("\nPresiona ENTER para volver al menú principal...")

if __name__ == "__main__":
    main_menu()

