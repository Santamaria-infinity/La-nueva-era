import requests
import json
import os
import sys

# Añadir el directorio padre al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from animations.text_animation import slow_print, clear_screen, print_centered

def get_local_version():
    try:
        with open(os.path.join(os.path.dirname(__file__), '../version.json'), 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"version": "0.0.0.0", "changelog": ["No se encontró el archivo de versión local."]}

def get_remote_version():
    github_url = "https://raw.githubusercontent.com/Santamaria-infinity/La-nueva-era/main/version.json"
    try:
        response = requests.get(github_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None

def check_for_updates():
    local_data = get_local_version()
    remote_data = get_remote_version()

    if not remote_data:
        return False

    local_version = local_data.get("version", "0.0.0.0")
    remote_version = remote_data.get("version", "0.0.0.0")

    # Convertir a tuplas para comparar correctamente
    local_v = tuple(map(int, local_version.split(".")))
    remote_v = tuple(map(int, remote_version.split(".")))

    if remote_v > local_v:
        clear_screen()
        print_centered("╔════════════════════════════════════════╗")
        print_centered("║    ¡NUEVA ACTUALIZACIÓN DISPONIBLE!   ║")
        print_centered("╚════════════════════════════════════════╝")
        slow_print(f"\nTu versión: {local_version}")
        slow_print(f"Versión disponible: {remote_version}\n")
        slow_print("Novedades:\n")
        for item in remote_data.get("changelog", []):
            slow_print(f"- {item}")
        slow_print("\nPara actualizar, sigue estos pasos en Termux:")
        slow_print("1. Abre Termux y entra a la carpeta del juego:")
        slow_print("   cd /storage/emulated/0/La\\ nueva\\ era")
        slow_print("2. Descarga la actualización con:")
        slow_print("   git pull origin main")
        slow_print("\n¡Disfruta de la nueva versión!")
        input("\n[Presiona ENTER para continuar...]")
        return True
    else:
        clear_screen()
        print_centered("Tu juego ya está actualizado.")
        return False

if __name__ == "__main__":
    check_for_updates()
