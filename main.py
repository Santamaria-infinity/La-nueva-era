#!/usr/bin/env python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from animations.text_animation import clear_screen, type_text, slow_print
from ascii_art.menu_art import show_title, show_menu
from story.el_principio import show_intro_story
from story.capitulo_2 import capitulo_2
from game_logic.save_system import SaveSystem
from utils.version_checker import check_for_updates

def main_menu():
    """Menú principal del juego"""
    save_system = SaveSystem()
    
    # Verificar actualizaciones al iniciar
    check_for_updates()
    
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
    
    # Mostrar la historia de introducción (Capítulo 1)
    show_intro_story()
    
    # Transición al Capítulo 2
    clear_screen()
    type_text("\n\n", 0.05)
    type_text("═" * 70 + "\n", 0.02)
    type_text("          CONTINUARÁ...\n", 0.05)
    type_text("═" * 70 + "\n\n", 0.02)
    input("\nPresiona ENTER para continuar con el Capítulo 2...")
    
    # Mostrar Capítulo 2: La Caída del Creador
    capitulo_2()
    
    # Crear datos iniciales del jugador
    player_data = {
        "name": "Superviviente",
        "level": 2,
        "mana": 50,
        "max_mana": 50,
        "location": "Tierras Salvajes del Exilio",
        "inventory": ["Círculo Mágico Básico"],
        "skills": ["Creación Básica", "Magia de Tierra", "Magia de Viento", "Magia de Agua"],
        "capitulo_2_completado": True
    }
    
    # Guardar la partida
    save_system.save_game(slot, player_data)
    
    clear_screen()
    type_text("\n✅ Partida guardada en Slot " + str(slot) + "\n", 0.05)
    type_text("Regresando al menú principal...\n", 0.05)
    input("\nPresiona ENTER para continuar...")

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
        
        # Verificar si ya completó el Capítulo 2
        if player_data.get('capitulo_2_completado', False):
            clear_screen()
            type_text("\n✅ Ya completaste el Capítulo 2: La Caída del Creador\n", 0.05)
            type_text("El Capítulo 3 está en desarrollo...\n", 0.05)
            input("\nPresiona ENTER para volver al menú principal...")
        else:
            # Mostrar el Capítulo 2 si aún no lo completó
            capitulo_2()
            
            # Marcar como completado
            player_data['capitulo_2_completado'] = True
            save_system.save_game(slot, player_data)
            
            clear_screen()
            type_text("\n✅ Capítulo 2 completado\n", 0.05)
            type_text("Partida guardada automáticamente\n", 0.05)
            input("\nPresiona ENTER para volver al menú principal...")

if __name__ == "__main__":
    main_menu()
