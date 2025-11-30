import requests
import json
import os
import sys

# Añadir el directorio padre al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from animations.text_animation import slow_print, clear_screen, print_centered

def get_local_version():
    """Obtiene la versión actual del juego desde version.json."""
    try:
        with open(os.path.join(os.path.dirname(__file__), '../version.json'), 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"version": "0.0.0.0", "changelog": ["No se encontró el archivo de versión local."]}

def get_remote_version():
    """Obtiene la última versión del juego desde GitHub."""
    # ¡IMPORTANTE! Reemplaza 'TU_USUARIO' y 'TU_REPO' con tu usuario y nombre de repositorio de GitHub
    github_url = "https://raw.githubusercontent.com/TU_USUARIO/TU_REPO/main/game/version.json"
    try:
        response = requests.get(github_url)
        response.raise_for_status()  # Lanza un error para códigos de estado HTTP incorrectos
        return response.json()
    except requests.exceptions.RequestException as e:
        # print(f"Error al conectar con GitHub: {e}")
        return None

def check_for_updates():
    """Compara la versión local con la remota y notifica al usuario."""
    local_data = get_local_version()
    remote_data = get_remote_version()

    if not remote_data:
        # print_centered("No se pudo verificar actualizaciones (problema de conexión).")
        return False

    local_version = local_data.get("version", "0.0.0.0")
    remote_version = remote_data.get("version", "0.0.0.0")

    if remote_version > local_version:
        clear_screen()
        print_centered("╔══════════════════════════════════════════════════════════════╗")
        print_centered("║                      ¡NUEVA ACTUALIZACIÓN DISPONIBLE!          ║")
        print_centered("╚══════════════════════════════════════════════════════════════╝")
        slow_print(f"\nTu versión: {local_version}")
        slow_print(f"Versión disponible: {remote_version}\n")
        slow_print("Novedades:\n")
        for item in remote_data.get("changelog", []):
            slow_print(f"- {item}")
        slow_print("\nPara actualizar, por favor, sigue estos pasos en Termux:")
        slow_print("1. Abre Termux y navega a la carpeta de tu juego:")
        slow_print("   cd /storage/emulated/0/La\\ nueva\\ era")
        slow_print("2. Ejecuta los comandos de Git para descargar la actualización:")
        slow_print("   git pull origin main")
        slow_print("\n¡Disfruta de la nueva versión!")
        input("\n[Presiona ENTER para continuar...]")
        return True
    else:
        # print_centered("Tu juego está actualizado.")
        return False

if __name__ == "__main__":
    check_for_updates()
