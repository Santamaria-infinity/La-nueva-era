#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
CAPÍTULO 2: LA CAÍDA DEL CREADOR
Historia épica del protagonista desde ser adorado como un dios hasta descubrir la magia elemental
"""

import sys
import os
import time

# Agregar el directorio raíz al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from animations.text_animation import clear_screen, print_slow
from animations.capitulo_2_texto import *
from ascii_art.capitulo_2_art import *

def pausa(segundos):
    """Pausa simple"""
    time.sleep(segundos)

def capitulo_2():
    """Capítulo 2: La Caída del Creador"""
    
    clear_screen()
    
    # ==================== PARTE 1: DÍAS DE GLORIA ====================
    
    texto_dias_de_gloria_1()
    pausa(2)
    
    reino_prospero()
    pausa(2)
    
    texto_dias_de_gloria_2()
    pausa(2)
    
    adoracion_pueblo()
    pausa(2)
    
    texto_dias_de_gloria_3()
    pausa(2)
    
    adoracion_pueblo()
    pausa(2)
    
    texto_dias_de_gloria_4()
    pausa(2)
    
    texto_dias_de_gloria_5()
    pausa(3)
    
    # ==================== PARTE 2: EL REGRESO DEL ÁNGEL ====================
    
    texto_regreso_angel_1()
    pausa(2)
    
    angel_blanco_aparece()
    pausa(3)
    
    texto_regreso_angel_2()
    pausa(2)
    
    texto_regreso_angel_3()
    pausa(2)
    
    perdida_poderes()
    pausa(2)
    
    texto_regreso_angel_4()
    pausa(2)
    
    texto_regreso_angel_5()
    pausa(2)
    
    texto_regreso_angel_6()
    pausa(3)
    
    # ==================== PARTE 3: LA CAÍDA ====================
    
    texto_caida_1()
    pausa(2)
    
    adoracion_pueblo()
    pausa(2)
    
    texto_caida_2()
    pausa(2)
    
    texto_caida_3()
    pausa(2)
    
    texto_caida_4()
    pausa(3)
    
    # ==================== PARTE 4: LA TRAICIÓN ====================
    
    texto_traicion_1()
    pausa(2)
    
    traicion()
    pausa(2)
    
    texto_traicion_2()
    pausa(2)
    
    texto_traicion_3()
    pausa(2)
    
    traicion()
    pausa(2)
    
    texto_traicion_4()
    pausa(2)
    
    texto_traicion_5()
    pausa(2)
    
    texto_traicion_6()
    pausa(3)
    
    # ==================== PARTE 5: EL EXILIO ====================
    
    texto_exilio_1()
    pausa(2)
    
    expulsion()
    pausa(2)
    
    texto_exilio_2()
    pausa(2)
    
    expulsion()
    pausa(2)
    
    texto_exilio_3()
    pausa(2)
    
    texto_exilio_4()
    pausa(3)
    
    # ==================== PARTE 6: LA DESESPERACIÓN ====================
    
    texto_desesperacion_1()
    pausa(2)
    
    perdida_poderes()
    pausa(2)
    
    texto_desesperacion_2()
    pausa(2)
    
    texto_desesperacion_3()
    pausa(2)
    
    texto_desesperacion_4()
    pausa(3)
    
    # ==================== PARTE 7: LA REVELACIÓN ====================
    
    texto_revelacion_1()
    pausa(2)
    
    angel_caido_aparece()
    pausa(3)
    
    texto_revelacion_2()
    pausa(2)
    
    texto_revelacion_3()
    pausa(2)
    
    texto_revelacion_4()
    pausa(2)
    
    texto_revelacion_5()
    pausa(2)
    
    angel_caido_aparece()
    pausa(2)
    
    texto_revelacion_6()
    pausa(2)
    
    texto_revelacion_7()
    pausa(2)
    
    texto_revelacion_8()
    pausa(2)
    
    texto_revelacion_9()
    pausa(2)
    
    texto_revelacion_10()
    pausa(3)
    
    # ==================== PARTE 8: EL DESCUBRIMIENTO ====================
    
    texto_descubrimiento_1()
    pausa(2)
    
    perdida_poderes()
    pausa(2)
    
    texto_descubrimiento_2()
    pausa(2)
    
    circulo_magico()
    pausa(2)
    
    texto_descubrimiento_3()
    pausa(2)
    
    circulo_magico()
    pausa(2)
    
    texto_descubrimiento_4()
    pausa(2)
    
    texto_descubrimiento_5()
    pausa(2)
    
    # --- DESCUBRIMIENTO DE TIERRA ---
    
    texto_descubrimiento_6()
    pausa(2)
    
    magia_elementos()
    pausa(2)
    
    texto_descubrimiento_7()
    pausa(2)
    
    magia_elementos()
    pausa(2)
    
    texto_descubrimiento_8()
    pausa(2)
    
    texto_descubrimiento_9()
    pausa(2)
    
    texto_descubrimiento_10()
    pausa(2)
    
    magia_elementos()
    pausa(2)
    
    texto_descubrimiento_11()
    pausa(3)
    
    # --- DESCUBRIMIENTO DE VIENTO ---
    
    texto_descubrimiento_12()
    pausa(2)
    
    magia_elementos()
    pausa(2)
    
    texto_descubrimiento_13()
    pausa(2)
    
    texto_descubrimiento_14()
    pausa(2)
    
    texto_descubrimiento_15()
    pausa(2)
    
    texto_descubrimiento_16()
    pausa(3)
    
    # --- DESCUBRIMIENTO DE AGUA ---
    
    texto_descubrimiento_17()
    pausa(2)
    
    magia_elementos()
    pausa(2)
    
    texto_descubrimiento_18()
    pausa(2)
    
    texto_descubrimiento_19()
    pausa(2)
    
    texto_descubrimiento_20()
    pausa(3)
    
    # --- FINAL DEL CAPÍTULO ---
    
    texto_descubrimiento_21()
    pausa(2)
    
    magia_elementos()
    pausa(2)
    
    texto_descubrimiento_22()
    pausa(2)
    
    texto_descubrimiento_23()
    pausa(2)
    
    texto_descubrimiento_24()
    pausa(2)
    
    texto_descubrimiento_25()
    pausa(3)
    
    magia_elementos()
    pausa(5)
    
    clear_screen()
    print_slow("\n\n")
    print_slow("═" * 70)
    print_slow("\n          FIN DEL CAPÍTULO 2: LA CAÍDA DEL CREADOR")
    print_slow("\n═" * 70)
    print_slow("\n\n")
    pausa(3)

if __name__ == "__main__":
    capitulo_2()
