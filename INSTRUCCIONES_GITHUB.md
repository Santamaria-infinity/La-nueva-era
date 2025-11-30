# 📦 Instrucciones para Publicar el Juego en GitHub

## 🎯 Objetivo
Publicar tu juego en GitHub para que los usuarios puedan descargarlo y recibir actualizaciones automáticas.

---

## 📱 Paso 1: Instalar Git en Termux

Abre Termux y ejecuta:

```bash
pkg update
pkg install git
```

---

## 🌐 Paso 2: Crear Cuenta en GitHub (desde el celular)

1. Abre tu navegador (Chrome, Firefox, etc.)
2. Ve a: **https://github.com**
3. Click en **"Sign up"** (Registrarse)
4. Completa el formulario:
   - **Username** (nombre de usuario): Elige un nombre único (ejemplo: `tu_nombre_dev`)
   - **Email**: Tu correo electrónico
   - **Password**: Una contraseña segura
5. Verifica tu email
6. ¡Listo! Ya tienes cuenta en GitHub

---

## 📂 Paso 3: Crear un Repositorio en GitHub

1. En GitHub, click en el botón **"+"** (arriba a la derecha)
2. Selecciona **"New repository"**
3. Completa los datos:
   - **Repository name**: `la-nueva-era` (o el nombre que prefieras)
   - **Description**: "Juego de texto ASCII - La Nueva Era"
   - **Public** (para que todos puedan descargarlo)
   - ✅ Marca **"Add a README file"**
4. Click en **"Create repository"**
5. **¡IMPORTANTE!** Copia la URL de tu repositorio (ejemplo: `https://github.com/TU_USUARIO/la-nueva-era`)

---

## 🔧 Paso 4: Configurar Git en Termux

Ejecuta estos comandos en Termux (reemplaza con tus datos):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_email@ejemplo.com"
```

---

## 📤 Paso 5: Subir el Juego a GitHub

### 5.1 Navega a la carpeta del juego:

```bash
cd /storage/emulated/0/La\ nueva\ era
```

### 5.2 Inicializa Git:

```bash
git init
```

### 5.3 Agrega todos los archivos:

```bash
git add .
```

### 5.4 Crea el primer commit:

```bash
git commit -m "Versión inicial 0.0.0.1"
```

### 5.5 Conecta con tu repositorio de GitHub:

Reemplaza `TU_USUARIO` y `TU_REPO` con tus datos:

```bash
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
```

Ejemplo:
```bash
git remote add origin https://github.com/juan_dev/la-nueva-era.git
```

### 5.6 Sube los archivos a GitHub:

```bash
git branch -M main
git push -u origin main
```

**Nota:** Te pedirá tu usuario y contraseña de GitHub. Si tienes autenticación de dos factores, necesitarás crear un **Personal Access Token** (te explico abajo).

---

## 🔑 Crear Personal Access Token (si es necesario)

Si GitHub te pide un token en lugar de contraseña:

1. Ve a GitHub en tu navegador
2. Click en tu foto de perfil → **Settings**
3. Scroll hasta abajo → **Developer settings**
4. **Personal access tokens** → **Tokens (classic)**
5. **Generate new token** → **Generate new token (classic)**
6. Dale un nombre: "Termux Access"
7. Marca el checkbox: **repo** (acceso completo a repositorios)
8. Click en **Generate token**
9. **¡COPIA EL TOKEN!** (solo se muestra una vez)
10. Usa este token como contraseña cuando Git te lo pida

---

## 🔄 Paso 6: Actualizar el archivo version_checker.py

Edita el archivo `/utils/version_checker.py` y reemplaza esta línea:

```python
github_url = "https://raw.githubusercontent.com/TU_USUARIO/TU_REPO/main/version.json"
```

Por tu URL real, ejemplo:

```python
github_url = "https://raw.githubusercontent.com/juan_dev/la-nueva-era/main/version.json"
```

Para editar en Termux:

```bash
nano /storage/emulated/0/La\ nueva\ era/utils/version_checker.py
```

Presiona `Ctrl + X`, luego `Y`, luego `Enter` para guardar.

---

## 🚀 Paso 7: Publicar una Nueva Versión

Cuando hagas cambios y quieras publicar una nueva versión:

### 7.1 Actualiza el archivo `version.json`:

```bash
nano /storage/emulated/0/La\ nueva\ era/version.json
```

Cambia la versión y el changelog:

```json
{
  "version": "0.0.0.2",
  "release_date": "2024-01-16",
  "changelog": [
    "Nuevas animaciones mejoradas",
    "Corrección de bugs",
    "Sistema de actualizaciones implementado"
  ]
}
```

### 7.2 Sube los cambios a GitHub:

```bash
cd /storage/emulated/0/La\ nueva\ era
git add .
git commit -m "Versión 0.0.0.2 - Mejoras y correcciones"
git push origin main
```

---

## 📥 Cómo los Usuarios Descargan el Juego

Los usuarios pueden descargar tu juego con:

```bash
cd /storage/emulated/0
git clone https://github.com/TU_USUARIO/TU_REPO.git
cd TU_REPO
python main.py
```

---

## 🔄 Cómo los Usuarios Actualizan el Juego

Cuando publiques una nueva versión, los usuarios solo necesitan:

```bash
cd /storage/emulated/0/La\ nueva\ era
git pull origin main
```

**¡Y el juego detectará automáticamente la nueva versión!** 🎉

---

## 📋 Resumen de Comandos Importantes

| Acción | Comando |
|--------|---------|
| Ver estado de Git | `git status` |
| Agregar cambios | `git add .` |
| Crear commit | `git commit -m "mensaje"` |
| Subir a GitHub | `git push origin main` |
| Descargar cambios | `git pull origin main` |
| Ver versión actual | `cat version.json` |

---

## ✅ Checklist Final

- [ ] Git instalado en Termux
- [ ] Cuenta de GitHub creada
- [ ] Repositorio creado en GitHub
- [ ] Git configurado con tu nombre y email
- [ ] Juego subido a GitHub
- [ ] URL actualizada en `version_checker.py`
- [ ] Probado el sistema de actualizaciones

---

## 🆘 Problemas Comunes

### Error: "Permission denied"
```bash
chmod +x /storage/emulated/0/La\ nueva\ era/main.py
```

### Error: "fatal: not a git repository"
```bash
cd /storage/emulated/0/La\ nueva\ era
git init
```

### Error al hacer push
- Verifica que la URL del repositorio sea correcta
- Usa un Personal Access Token en lugar de contraseña

---

## 🎮 ¡Listo!

Ahora tu juego está en GitHub y los usuarios recibirán notificaciones automáticas cuando publiques nuevas versiones.

**URL de tu juego:** `https://github.com/TU_USUARIO/TU_REPO`

¡Comparte este link con tus amigos para que jueguen! 🚀

