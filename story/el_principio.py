#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sys
import os

# Importar las animaciones de texto y arte ASCII
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from animations.text_animation import slow_print, clear_screen, print_centered
from ascii_art.story_art import (
    cientificos_huyendo, 
    desintegracion, 
    lluvia_milagrosa, 
    angel_aparece, 
    poder_otorgado,
    tierra_desolada,
    caos_humano
)

def print_title(text):
    """Función auxiliar para imprimir títulos"""
    clear_screen()
    print("\n" + "="*60)
    print_centered(text)
    print("="*60 + "\n")

def parte_1_descubrimiento():
    """Parte 1: El descubrimiento del asteroide"""
    print_title("PARTE 1: EL DESCUBRIMIENTO")
    time.sleep(2)
    
    slow_print("\nAño 2157. Observatorio Espacial Internacional.")
    time.sleep(1)
    slow_print("\nLos científicos detectan algo aterrador...")
    time.sleep(1.5)
    slow_print("\nUn asteroide masivo se dirige hacia la Tierra.")
    time.sleep(1.5)
    slow_print("\nTiempo estimado de impacto: 6 meses.")
    time.sleep(2)
    
    slow_print("\n\n[Dr. Chen]: 'Esto... esto no puede ser real.'")
    time.sleep(1.5)
    slow_print("\n[Dra. Martínez]: 'Los cálculos son correctos. Es inevitable.'")
    time.sleep(1.5)
    slow_print("\n[Director]: 'Debemos informar a los gobiernos inmediatamente.'")
    time.sleep(2)
    
    slow_print("\n\nLa noticia se filtra a los medios...")
    time.sleep(1.5)
    slow_print("\nEl pánico se apodera del mundo entero.")
    time.sleep(2)
    
    input("\n\n[Presiona ENTER para continuar...]")

def parte_2_evacuacion():
    """Parte 2: La evacuación de los ricos"""
    print_title("PARTE 2: LA GRAN TRAICIÓN")
    time.sleep(2)
    
    slow_print("\nMientras el mundo entra en pánico...")
    time.sleep(1.5)
    slow_print("\nLos más ricos y poderosos tienen un plan secreto.")
    time.sleep(2)
    
    slow_print("\n\n[Presidente del Consejo Mundial]: 'Las naves están listas.'")
    time.sleep(1.5)
    slow_print("\n[Multimillonario]: '¿Cuántos podemos llevar?'")
    time.sleep(1.5)
    slow_print("\n[Científico Jefe]: 'Solo 10,000 personas. La elite.'")
    time.sleep(2)
    
    slow_print("\n\nConstruyeron naves en secreto...")
    time.sleep(1.5)
    slow_print("\nMientras el resto del mundo sufría.")
    time.sleep(2)
    
    slow_print("\n\nLlega el día de la evacuación...")
    time.sleep(2)
    
    # Mostrar animación de científicos huyendo
    cientificos_huyendo()
    
    clear_screen()
    slow_print("\nLas naves despegan hacia Marte...")
    time.sleep(1.5)
    slow_print("\nDejando atrás a miles de millones de personas.")
    time.sleep(1.5)
    slow_print("\nLos pobres y la clase media... abandonados a su suerte.")
    time.sleep(2)
    
    input("\n\n[Presiona ENTER para continuar...]")

def parte_3_impacto():
    """Parte 3: El impacto del asteroide"""
    print_title("PARTE 3: EL IMPACTO")
    time.sleep(2)
    
    slow_print("\n3 días después de la evacuación...")
    time.sleep(1.5)
    slow_print("\nEl asteroide entra en la atmósfera terrestre.")
    time.sleep(2)
    
    slow_print("\n\nEl cielo se ilumina como mil soles...")
    time.sleep(1.5)
    slow_print("\nUn estruendo ensordecedor sacude el planeta.")
    time.sleep(1.5)
    slow_print("\n\n💥 ¡IMPACTO! 💥")
    time.sleep(2)
    
    slow_print("\n\nLa onda expansiva recorre el mundo...")
    time.sleep(1.5)
    slow_print("\nTerremotos. Tsunamis. Volcanes en erupción.")
    time.sleep(1.5)
    slow_print("\nEl cielo se oscurece con cenizas.")
    time.sleep(2)
    
    slow_print("\n\nPero algo extraño sucede...")
    time.sleep(2)
    slow_print("\nEl asteroide no destruye la Tierra por completo.")
    time.sleep(1.5)
    slow_print("\nEn su lugar, libera una energía desconocida.")
    time.sleep(2)
    
    slow_print("\n\nUna luz brillante cubre el planeta...")
    time.sleep(2)
    
    # Mostrar animación de desintegración
    desintegracion()
    
    clear_screen()
    slow_print("\nCuando la luz se desvanece...")
    time.sleep(1.5)
    slow_print("\nTodo ha cambiado.")
    time.sleep(2)
    
    input("\n\n[Presiona ENTER para continuar...]")

def parte_4_supervivientes():
    """Parte 4: Los supervivientes"""
    print_title("PARTE 4: LOS SUPERVIVIENTES")
    time.sleep(2)
    
    slow_print("\nTodo ha desaparecido...")
    time.sleep(1.5)
    slow_print("\nEdificios, vehículos, ropa, tecnología...")
    time.sleep(1.5)
    slow_print("\nIncluso los animales y las plantas.")
    time.sleep(2)
    
    slow_print("\n\nSolo quedan los humanos...")
    time.sleep(1.5)
    slow_print("\nDesnudos. Vulnerables. Asustados.")
    time.sleep(2)
    
    slow_print("\n\nY la tierra...")
    time.sleep(1.5)
    slow_print("\nÁrida. Seca. Sin vida.")
    time.sleep(2)
    
    # Mostrar animación de tierra desolada
    tierra_desolada()
    
    clear_screen()
    slow_print("\nMiles de millones de personas...")
    time.sleep(1.5)
    slow_print("\nSin comida. Sin agua. Sin refugio.")
    time.sleep(2)
    
    slow_print("\n\n[Mujer]: '¿Qué... qué ha pasado?'")
    time.sleep(1.5)
    slow_print("\n[Hombre]: 'Todo... todo se ha ido.'")
    time.sleep(1.5)
    slow_print("\n[Niño]: 'Tengo hambre... y sed...'")
    time.sleep(2)
    
    slow_print("\n\nLa desesperación se apodera de todos.")
    time.sleep(2)
    
    input("\n\n[Presiona ENTER para continuar...]")

def parte_5_guerra():
    """Parte 5: La guerra por los recursos"""
    print_title("PARTE 5: LA GUERRA")
    time.sleep(2)
    
    slow_print("\nSin recursos, la humanidad se vuelve salvaje...")
    time.sleep(2)
    slow_print("\nComienza la lucha por la supervivencia.")
    time.sleep(2)
    
    slow_print("\n\nPeleas por comida...")
    time.sleep(1.5)
    slow_print("\nPeleas por agua...")
    time.sleep(1.5)
    slow_print("\nPeleas por cualquier cosa que pueda ayudar a sobrevivir.")
    time.sleep(2)
    
    # Mostrar animación de caos humano
    caos_humano()
    
    clear_screen()
    slow_print("\nLa violencia se extiende por todo el planeta...")
    time.sleep(1.5)
    slow_print("\nHermanos contra hermanos.")
    time.sleep(1.5)
    slow_print("\nPadres contra hijos.")
    time.sleep(1.5)
    slow_print("\nLa civilización ha colapsado.")
    time.sleep(2)
    
    slow_print("\n\nMiles mueren cada día...")
    time.sleep(1.5)
    slow_print("\nPor hambre. Por sed. Por violencia.")
    time.sleep(2)
    
    slow_print("\n\nLa humanidad está al borde de la extinción.")
    time.sleep(2)
    
    input("\n\n[Presiona ENTER para continuar...]")

def parte_6_milagro():
    """Parte 6: El milagro"""
    print_title("PARTE 6: EL MILAGRO")
    time.sleep(2)
    
    slow_print("\nDespués de 7 días de horror...")
    time.sleep(1.5)
    slow_print("\nCuando todo parece perdido...")
    time.sleep(2)
    
    slow_print("\n\nEl cielo comienza a cambiar.")
    time.sleep(2)
    slow_print("\nNubes oscuras se forman sobre la tierra seca.")
    time.sleep(2)
    
    slow_print("\n\nY entonces...")
    time.sleep(2)
    slow_print("\n\n¡Comienza a llover!")
    time.sleep(2)
    
    # Mostrar animación de lluvia
    lluvia_milagrosa()
    
    clear_screen()
    slow_print("\nLa lluvia cae sobre la tierra árida...")
    time.sleep(1.5)
    slow_print("\nLas personas levantan sus rostros al cielo.")
    time.sleep(1.5)
    slow_print("\nBeben el agua con desesperación.")
    time.sleep(2)
    
    slow_print("\n\n[Mujer]: '¡Agua! ¡Es agua!'")
    time.sleep(1.5)
    slow_print("\n[Hombre]: '¡Estamos salvados!'")
    time.sleep(1.5)
    slow_print("\n[Anciano]: 'Es un milagro...'")
    time.sleep(2)
    
    slow_print("\n\nPero la lluvia no es suficiente...")
    time.sleep(1.5)
    slow_print("\nNo hay comida. No hay plantas. No hay animales.")
    time.sleep(1.5)
    slow_print("\nLa humanidad aún está condenada.")
    time.sleep(2)
    
    input("\n\n[Presiona ENTER para continuar...]")

def parte_7_aparicion():
    """Parte 7: La aparición del ángel"""
    print_title("PARTE 7: LA APARICIÓN")
    time.sleep(2)
    
    slow_print("\nAl décimo día después del impacto...")
    time.sleep(1.5)
    slow_print("\nMientras las personas beben de los charcos...")
    time.sleep(2)
    
    slow_print("\n\nUna luz brillante desciende del cielo.")
    time.sleep(2)
    
    # Mostrar animación del ángel apareciendo
    angel_aparece()
    
    clear_screen()
    slow_print("\nUn ser de luz pura se presenta ante la humanidad...")
    time.sleep(2)
    slow_print("\nSu voz resuena en la mente de todos.")
    time.sleep(2)
    
    slow_print("\n\n[Ángel]: 'Humanidad... he venido a ofrecerles una oportunidad.'")
    time.sleep(2)
    slow_print("\n[Ángel]: 'Uno de ustedes será elegido.'")
    time.sleep(2)
    slow_print("\n[Ángel]: 'Recibirá el poder de crear vida.'")
    time.sleep(2)
    slow_print("\n[Ángel]: 'Plantas, animales, todo lo necesario para sobrevivir.'")
    time.sleep(2)
    
    slow_print("\n\nLa multitud queda en silencio...")
    time.sleep(1.5)
    slow_print("\nTodos miran al ángel con esperanza.")
    time.sleep(2)
    
    slow_print("\n\n[Ángel]: 'Pero solo uno puede recibir este don.'")
    time.sleep(2)
    slow_print("\n[Ángel]: 'Y ese elegido... eres tú.'")
    time.sleep(2)
    
    slow_print("\n\nEl ángel te señala directamente.")
    time.sleep(2)
    
    input("\n\n[Presiona ENTER para continuar...]")

def parte_8_eleccion():
    """Parte 8: La elección"""
    print_title("PARTE 8: EL ELEGIDO")
    time.sleep(2)
    
    slow_print("\nTodos los ojos se posan sobre ti...")
    time.sleep(1.5)
    slow_print("\nMiles de personas te miran con esperanza.")
    time.sleep(2)
    
    slow_print("\n\n[Ángel]: 'Acércate.'")
    time.sleep(2)
    
    slow_print("\n\nCon piernas temblorosas, caminas hacia el ser de luz.")
    time.sleep(2)
    
    slow_print("\n\n[Ángel]: 'Te he elegido porque tu corazón es puro.'")
    time.sleep(2)
    slow_print("\n[Ángel]: 'No buscaste pelear. No buscaste robar.'")
    time.sleep(2)
    slow_print("\n[Ángel]: 'Ayudaste a otros incluso cuando tú también sufrías.'")
    time.sleep(2)
    
    slow_print("\n\nEl ángel extiende su mano hacia ti...")
    time.sleep(2)
    
    # Mostrar animación del poder siendo otorgado
    poder_otorgado()
    
    clear_screen()
    slow_print("\nUna energía increíble fluye por tu cuerpo...")
    time.sleep(1.5)
    slow_print("\nSientes el poder de la creación en tus manos.")
    time.sleep(2)
    
    slow_print("\n\n[Ángel]: 'Ahora tienes el poder de salvar a tu especie.'")
    time.sleep(2)
    slow_print("\n[Ángel]: 'Usa este don sabiamente.'")
    time.sleep(2)
    slow_print("\n[Ángel]: 'Reconstruye el mundo. Crea vida. Da esperanza.'")
    time.sleep(2)
    
    slow_print("\n\nEl ángel comienza a desvanecerse...")
    time.sleep(2)
    
    slow_print("\n\n[Ángel]: 'El futuro de la humanidad está en tus manos.'")
    time.sleep(2)
    
    slow_print("\n\nY desaparece.")
    time.sleep(2)
    
    input("\n\n[Presiona ENTER para continuar...]")

def parte_9_nuevo_comienzo():
    """Parte 9: El nuevo comienzo"""
    print_title("PARTE 9: EL NUEVO COMIENZO")
    time.sleep(2)
    
    slow_print("\nTe quedas solo frente a miles de personas...")
    time.sleep(1.5)
    slow_print("\nTodas esperan que hagas algo.")
    time.sleep(2)
    
    slow_print("\n\nCierras los ojos...")
    time.sleep(1.5)
    slow_print("\nSientes el poder fluyendo en tu interior.")
    time.sleep(2)
    
    slow_print("\n\nExtiendes tus manos hacia el suelo árido...")
    time.sleep(2)
    
    slow_print("\n\nY comienzas a crear.")
    time.sleep(2)
    
    slow_print("\n\n🌱 Brotes verdes emergen de la tierra seca.")
    time.sleep(2)
    slow_print("\n🌳 Árboles crecen a velocidad imposible.")
    time.sleep(2)
    slow_print("\n🌾 Campos de trigo se extienden hasta el horizonte.")
    time.sleep(2)
    slow_print("\n🐦 Pájaros aparecen en el cielo.")
    time.sleep(2)
    slow_print("\n🦌 Animales corren por las praderas recién nacidas.")
    time.sleep(2)
    
    slow_print("\n\nLa multitud estalla en lágrimas de alegría...")
    time.sleep(2)
    
    slow_print("\n\n[Mujer]: '¡Es real! ¡Está creando vida!'")
    time.sleep(1.5)
    slow_print("\n[Hombre]: '¡Estamos salvados!'")
    time.sleep(1.5)
    slow_print("\n[Niño]: '¡Mira! ¡Hay manzanas en ese árbol!'")
    time.sleep(2)
    
    slow_print("\n\nLas personas corren hacia los árboles frutales...")
    time.sleep(1.5)
    slow_print("\nComen por primera vez en días.")
    time.sleep(1.5)
    slow_print("\nLloran de felicidad.")
    time.sleep(2)
    
    input("\n\n[Presiona ENTER para continuar...]")

def epilogo():
    """Epílogo: El futuro"""
    print_title("EPÍLOGO: EL FUTURO")
    time.sleep(2)
    
    slow_print("\nPasan los meses...")
    time.sleep(1.5)
    slow_print("\nCon tu poder, reconstruyes el mundo.")
    time.sleep(2)
    
    slow_print("\n\nCreas bosques, océanos, montañas...")
    time.sleep(1.5)
    slow_print("\nDevuelves la vida al planeta.")
    time.sleep(2)
    
    slow_print("\n\nLa humanidad aprende de sus errores...")
    time.sleep(1.5)
    slow_print("\nYa no hay ricos ni pobres.")
    time.sleep(1.5)
    slow_print("\nTodos trabajan juntos para sobrevivir.")
    time.sleep(2)
    
    slow_print("\n\nMientras tanto, en Marte...")
    time.sleep(2)
    slow_print("\nLos que huyeron observan desde lejos.")
    time.sleep(1.5)
    slow_print("\nVen cómo la Tierra revive.")
    time.sleep(2)
    
    slow_print("\n\n[Multimillonario]: 'Imposible... la Tierra está... viva.'")
    time.sleep(1.5)
    slow_print("\n[Científico]: 'Hay vegetación. Agua. Vida.'")
    time.sleep(1.5)
    slow_print("\n[Presidente]: 'Nos equivocamos... los abandonamos...'")
    time.sleep(2)
    
    slow_print("\n\nIntentarán regresar...")
    time.sleep(1.5)
    slow_print("\nPero esa es otra historia.")
    time.sleep(2)
    
    slow_print("\n\nPor ahora, la humanidad tiene una segunda oportunidad.")
    time.sleep(2)
    slow_print("\nY tú eres su guardián.")
    time.sleep(2)
    
    slow_print("\n\n✨ FIN DE 'EL PRINCIPIO' ✨")
    time.sleep(3)
    
    input("\n\n[Presiona ENTER para Continuar...]")

def show_intro_story():
    """Función principal que ejecuta toda la historia"""
    parte_1_descubrimiento()
    parte_2_evacuacion()
    parte_3_impacto()
    parte_4_supervivientes()
    parte_5_guerra()
    parte_6_milagro()
    parte_7_aparicion()
    parte_8_eleccion()
    parte_9_nuevo_comienzo()
    epilogo()

if __name__ == "__main__":
    show_intro_story()
