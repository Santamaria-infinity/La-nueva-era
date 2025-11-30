# 🚀 Guía Completa: Publicar y Actualizar tu Juego en GitHub desde Termux 🚀

Esta guía te ayudará a subir tu juego a GitHub y a gestionar las actualizaciones para que tus jugadores puedan recibirlas directamente en Termux.

---

## 🎯 **Objetivo:**

1.  Crear un repositorio en GitHub para tu juego.
2.  Subir todos los archivos de tu juego a GitHub.
3.  Configurar el sistema de versiones para que detecte y notifique nuevas actualizaciones.
4.  Aprender a publicar nuevas versiones de tu juego.

---

## 🛠️ **Requisitos Previos:**

*   **Termux instalado** en tu dispositivo Android.
*   **Conexión a internet**.
*   **Tu juego** en la carpeta `/storage/emulated/0/La nueva era/game/`.

---

## **Paso 1: Instalar Git en Termux**

Git es la herramienta que usaremos para interactuar con GitHub.

1.  Abre Termux.
2.  Actualiza los paquetes e instala Git:
    ```bash
    pkg update && pkg install git -y
    ```
    *   `pkg update`: Actualiza la lista de paquetes.
    *   `pkg install git -y`: Instala Git (el `-y` acepta automáticamente las preguntas).

---

## **Paso 2: Crear una Cuenta en GitHub**

Si ya tienes una, puedes saltar este paso.

1.  Abre tu navegador web (Chrome, Firefox, etc.) en tu celular.
2.  Ve a la página de GitHub: [https://github.com](https://github.com)
3.  Haz clic en **"Sign up"** (Registrarse).
4.  Sigue las instrucciones para crear tu cuenta. Necesitarás un correo electrónico y una contraseña.

---

## **Paso 3: Crear un Nuevo Repositorio en GitHub**

Un repositorio es donde se guardará tu proyecto en GitHub.

1.  Una vez que hayas iniciado sesión en GitHub, haz clic en el **icono de "+"** (más) en la esquina superior derecha de la pantalla.
2.  Selecciona **"New repository"** (Nuevo repositorio).
3.  **Configura tu repositorio:**
    *   **Repository name (Nombre del repositorio):** `la-nueva-era` (o el nombre que prefieras para tu juego, pero usa minúsculas y guiones).
    *   **Description (Descripción):** (Opcional) Una breve descripción de tu juego.
    *   **Public/Private (Público/Privado):** Selecciona **"Public"** (Público) para que el sistema de versiones pueda acceder a él.
    *   **NO marques "Add a README file"**, "Add .gitignore" ni "Choose a license". Ya los tenemos en tu proyecto.
4.  Haz clic en el botón verde **"Create repository"** (Crear repositorio).

---

## **Paso 4: Configurar Git en Termux y Subir tu Juego**

Ahora vamos a conectar tu carpeta local con el repositorio de GitHub.

1.  **Navega a la carpeta de tu juego en Termux:**
    ```bash
    cd /storage/emulated/0/La\ nueva\ era/game
    ```
    *   Asegúrate de estar en la carpeta `game` que contiene `main.py`, `animations`, `ascii_art`, etc.

2.  **Configura tu nombre de usuario y correo electrónico de Git:**
    *   Reemplaza `"Tu Nombre"` con tu nombre de usuario de GitHub.
    *   Reemplaza `"tu_email@ejemplo.com"` con el correo electrónico que usaste para GitHub.
    ```bash
    git config --global user.name "Tu Nombre"
    git config --global user.email "tu_email@ejemplo.com"
    ```

3.  **Inicializa un repositorio Git local:**
    ```bash
    git init
    ```
    *   Esto crea una carpeta oculta `.git` en tu proyecto.

4.  **Agrega todos los archivos de tu juego al área de preparación de Git:**
    ```bash
    git add .
    ```
    *   El `.` significa "todos los archivos y carpetas en el directorio actual".

5.  **Confirma los cambios (crea un "commit"):**
    ```bash
    git commit -m "Versión inicial 0.0.0.1 del juego 'La Nueva Era'"
    ```
    *   `-m` es para el mensaje del commit. Usa un mensaje descriptivo.

6.  **Conecta tu repositorio local con el de GitHub:**
    *   **¡IMPORTANTE!** Reemplaza `TU_USUARIO` con tu nombre de usuario de GitHub y `TU_REPO` con el nombre de tu repositorio (por ejemplo, `la-nueva-era`).
    *   Puedes encontrar esta URL en la página de tu repositorio en GitHub, haz clic en el botón verde "Code" y copia la URL HTTPS.
    ```bash
    git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
    ```

7.  **Establece la rama principal (main):**
    ```bash
    git branch -M main
    ```

8.  **Sube tus archivos a GitHub:**
    ```bash
    git push -u origin main
    ```
    *   La primera vez que hagas esto, GitHub te pedirá tu **nombre de usuario** y **contraseña/token de acceso personal**.
        *   **Contraseña:** Si tienes la autenticación de dos factores activada, necesitarás crear un "Personal Access Token" (Token de Acceso Personal) en GitHub en lugar de usar tu contraseña normal. Si no, tu contraseña debería funcionar.
        *   **Cómo crear un Personal Access Token (si lo necesitas):**
            1.  En GitHub, ve a **Settings** (Configuración) -> **Developer settings** (Configuración de desarrollador) -> **Personal access tokens** (Tokens de acceso personal) -> **Tokens (classic)**.
            2.  Haz clic en **"Generate new token"** (Generar nuevo token).
            3.  Dale un nombre (ej. `termux-game`).
            4.  Marca los permisos `repo`.
            5.  Haz clic en "Generate token".
            6.  **Copia el token inmediatamente**, ya que no podrás verlo de nuevo. Usa este token como tu "contraseña" cuando `git push` te lo pida.

---

## **Paso 5: Actualizar la URL del Repositorio en `version_checker.py`**

Para que tu juego sepa dónde buscar las actualizaciones.

1.  Abre el archivo `version_checker.py` en Termux:
    ```bash
    nano /storage/emulated/0/La\ nueva\ era/game/utils/version_checker.py
    ```
2.  Busca la línea que dice:
    ```python
    github_url = "https://raw.githubusercontent.com/TU_USUARIO/TU_REPO/main/game/version.json"
    ```
3.  **Reemplaza `TU_USUARIO` con tu nombre de usuario de GitHub** y **`TU_REPO` con el nombre de tu repositorio** (el que creaste en el Paso 3).
    *   Por ejemplo, si tu usuario es `MiUsuario` y tu repo es `la-nueva-era`, la línea quedaría:
        ```python
        github_url = "https://raw.githubusercontent.com/MiUsuario/la-nueva-era/main/game/version.json"
        ```
4.  Guarda el archivo: `Ctrl + S`, luego `Ctrl + X`.

---

## **Paso 6: ¡Prueba tu Juego!**

1.  Ejecuta tu juego desde `main.py`:
    ```bash
    python /storage/emulated/0/La\ nueva\ era/game/main.py
    ```
2.  Deberías ver la versión `v0.0.0.1` en la esquina del menú.
3.  Como es la primera versión, no debería haber ninguna notificación de actualización.

---

## **Paso 7: Publicar una Nueva Versión (¡Cuando tengas cambios!)**

Cuando quieras que tus jugadores reciban una actualización:

1.  **Edita el archivo `version.json`** en tu Termux:
    ```bash
    nano /storage/emulated/0/La\ nueva\ era/game/version.json
    ```
    *   Cambia `"version": "0.0.0.1"` a `"version": "0.0.0.2"` (o la siguiente versión).
    *   **Actualiza el `changelog`** con las novedades de esta versión.
    *   Guarda el archivo.

2.  **Realiza cualquier otro cambio en el código de tu juego.**

3.  **Sube los cambios a GitHub desde Termux:**
    ```bash
    cd /storage/emulated/0/La\ nueva\ era/game
    git add .
    git commit -m "Versión 0.0.0.2 - [Breve descripción de los cambios]"
    git push origin main
    ```
    *   Reemplaza `[Breve descripción de los cambios]` con un mensaje claro de lo que actualizaste.

4.  **¡Listo!** La próxima vez que un jugador inicie el juego, recibirá la notificación de la nueva versión y las instrucciones para actualizar con `git pull`.

---

## **Paso 8: Cómo los Jugadores Actualizan el Juego**

Cuando les digas a tus jugadores que hay una nueva versión, ellos solo necesitarán hacer esto en Termux:

1.  Abrir Termux.
2.  Navegar a la carpeta del juego:
    ```bash
    cd /storage/emulated/0/La\ nueva\ era/game
    ```
3.  Ejecutar el comando para descargar los cambios:
    ```bash
    git pull origin main
    ```
    *   Esto descargará la nueva versión de tu juego desde GitHub.

---

¡Felicidades! Ahora tienes un sistema de versiones completo para tu juego. Si tienes alguna duda en el proceso, ¡no dudes en preguntar!
