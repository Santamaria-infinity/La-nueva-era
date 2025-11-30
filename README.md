# 🌍 El Inicio de 1 Nueva Era

Un juego de texto interactivo con animaciones ASCII que cuenta la historia de la humanidad después de un evento apocalíptico.

![Versión](https://img.shields.io/badge/versión-0.0.7-blue)
![Python](https://img.shields.io/badge/python-3.x-green)
![Plataforma](https://img.shields.io/badge/plataforma-Termux-orange)

---

## 📖 Historia

En el año 2157, un asteroide masivo se dirige hacia la Tierra. Los más ricos y poderosos huyen en naves secretas hacia Marte, abandonando a miles de millones de personas a su suerte.

Cuando el asteroide impacta, algo extraño sucede: todo desaparece excepto los humanos y la tierra árida. Sin recursos, la humanidad cae en el caos... hasta que un ángel aparece y te elige como el salvador de la especie humana.

**¿Podrás reconstruir el mundo y salvar a la humanidad?**

---

## ✨ Características

- 📜 **Historia épica completa** - "El Principio" con 9 partes narrativas y **Capítulo 2: La Caída del Creador**  
- 🎨 **Animaciones ASCII detalladas** - 7 animaciones del capítulo 1 + nuevas animaciones del capítulo 2  
- 💾 **Sistema de guardado** - 3 slots de guardado independientes  
- 🔄 **Actualizaciones automáticas** - Detecta nuevas versiones desde GitHub  
- 🎮 **Menú interactivo** - Navegación intuitiva y fácil de usar  
- 📱 **Optimizado para Termux** - Funciona perfectamente en Android  

---

## 🎬 Animaciones Incluidas

1. 🚀 **Científicos Huyendo** - Las naves de la elite despegando hacia Marte  
2. ⚡ **Desintegración Total** - Todo desaparece en una luz brillante  
3. 🌍 **Tierra Desolada** - El paisaje árido y sin vida  
4. 💀 **Caos Humano** - La lucha desesperada por sobrevivir  
5. ☁️ **Lluvia Milagrosa** - El agua cae sobre la tierra seca  
6. ✨ **Ángel Aparece** - Un ser de luz se materializa  
7. ⚡ **Poder Otorgado** - La energía divina fluye hacia ti  
8. 🏰 **Capítulo 2: La Caída del Creador** - Nuevas escenas y animaciones que continúan la historia  

---

## 📥 Instalación en Termux

### Requisitos Previos

```bash
pkg update
pkg install python git
```
### Dar permiso de almacenamiento (Opcional)


Este paso es obligatorio o Termux dará error al acceder a /storage/emulated/0.

```bash
termux-setup-storage
```

Acepta los permisos.

### Descargar el Juego

```bash
cd /storage/emulated/0
git clone https://github.com/Santamaria-infinity/La-nueva-era.git
cd La-Nueva-Era
```

### Ejecutar el Juego

```bash
python main.py
```

---

## 🎮 Cómo Jugar

1. **Nueva Partida** - Comienza una nueva aventura
2. **Cargar Partida** - Continúa desde donde lo dejaste (3 slots disponibles)
3. **Salir** - Cierra el juego

### Controles

- Usa los **números** para seleccionar opciones del menú
- Presiona **ENTER** para continuar la historia
- El juego se guarda automáticamente después de completar "El Principio"

---

## 🔄 Actualizar el Juego

Cuando haya una nueva versión disponible, el juego te lo notificará automáticamente.

Para actualizar, ejecuta:

```bash
cd /storage/emulated/0/La-Nueva-Era
git pull origin main
```

---

## 📂 Estructura del Proyecto

```
game/
├── main.py                    # Archivo principal del juego
├── version.json               # Información de versión
├── animations/
│   └── text_animation.py      # Efectos de texto animado
├── ascii_art/
│   ├── menu_art.py            # Arte del menú principal
│   └── story_art.py           # Animaciones de la historia
├── story/
│   └── el_principio.py        # Historia completa
├── game_logic/
│   └── save_system.py         # Sistema de guardado
├── utils/
│   └── version_checker.py     # Verificador de actualizaciones
└── README.md                  # Este archivo
```

---

## 🛠️ Desarrollo

### Versión Actual: 0.0.0.1

**Fecha de lanzamiento:** 15 de enero de 2024

**Changelog:**
- ✅ Versión inicial del juego
- ✅ Historia completa "El Principio"
- ✅ Sistema de guardado con 3 slots
- ✅ Animaciones ASCII completas
- ✅ Sistema de actualizaciones automáticas

---

## 🐛 Reportar Problemas

Si encuentras algún bug o tienes sugerencias, por favor:

1. Ve a la sección **Issues** en GitHub
2. Click en **New Issue**
3. Describe el problema o sugerencia
4. Incluye capturas de pantalla si es posible

---

## 📜 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

## 👨‍💻 Autor

Creado con ❤️ para la comunidad de Termux

---

## 🌟 Agradecimientos

Gracias a todos los que juegan y apoyan este proyecto. ¡Disfruta la aventura!

---

## 📞 Contacto

- **GitHub Issues:** Para reportar bugs o sugerencias
- **Versión:** 0.0.0.1
- **Plataforma:** Termux (Android)

---

**¡Que comience la nueva era!** 🌍✨

