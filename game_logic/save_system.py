#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

class SaveSystem:
    """Sistema de guardado con 3 slots"""
    
    def __init__(self):
        self.save_dir = "saves"
        self.create_save_directory()
    
    def create_save_directory(self):
        """Crear directorio de guardados si no existe"""
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
    
    def get_save_path(self, slot):
        """Obtener ruta del archivo de guardado"""
        return os.path.join(self.save_dir, f"save_slot_{slot}.json")
    
    def save_game(self, slot, player_data):
        """Guardar partida en un slot específico (1-3)"""
        if slot not in [1, 2, 3]:
            return False
        
        save_path = self.get_save_path(slot)
        
        try:
            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(player_data, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error al guardar: {e}")
            return False
    
    def load_game(self, slot):
        """Cargar partida desde un slot específico (1-3)"""
        if slot not in [1, 2, 3]:
            return None
        
        save_path = self.get_save_path(slot)
        
        if not os.path.exists(save_path):
            return None
        
        try:
            with open(save_path, 'r', encoding='utf-8') as f:
                player_data = json.load(f)
            return player_data
        except Exception as e:
            print(f"Error al cargar: {e}")
            return None
    
    def delete_save(self, slot):
        """Eliminar una partida guardada"""
        if slot not in [1, 2, 3]:
            return False
        
        save_path = self.get_save_path(slot)
        
        if os.path.exists(save_path):
            try:
                os.remove(save_path)
                return True
            except Exception as e:
                print(f"Error al eliminar: {e}")
                return False
        
        return False
    
    def list_saves(self):
        """Listar todas las partidas guardadas"""
        saves = {}
        
        for slot in [1, 2, 3]:
            save_data = self.load_game(slot)
            if save_data:
                saves[slot] = save_data
        
        return saves

