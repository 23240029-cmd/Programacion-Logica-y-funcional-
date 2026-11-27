"""
% Delgado Alcantar Emilio.
% Valenzuela Hurtado Ana Guadalupe.
% Sepulveda Becerra Frida Paulina.
% Cervarntes Guerrero Eduardo Agustin.
Clase main
"""

import pprint
from info_recetario import InformacionRecetario
from conector_prolog import PrologConector


def main():
    conector = PrologConector("prolog/reglas.pl")
    recetario = InformacionRecetario(conector)

    # 1. Obtener todas las recetas con detalle agrupado
    print("=== 1. obtener_detalle_receta() ===")
    res_todos = recetario.obtener_detalle_receta()
    pprint.pprint(res_todos)
    print()

    # 2. Filtrar recetas por tiempo máximo (en minutos) con detalle completo
    arg_tiempo = 30
    print(f"=== 2. filtro_por_tiempo({arg_tiempo}) ===")
    res_tiempo = list(recetario.filtro_por_tiempo(arg_tiempo))
    pprint.pprint(res_tiempo)
    print()

    # 3. Filtrar recetas por región / estado con detalle completo
    arg_region = "oaxaca"
    print(f"=== 3. filtro_por_region('{arg_region}') ===")
    res_region = list(recetario.filtro_por_region(arg_region))
    pprint.pprint(res_region)
    print()

    # 4. Filtrar recetas por nivel de picor con detalle completo
    arg_picor = "medio"
    print(f"=== 4. filtro_por_picor('{arg_picor}') ===")
    res_picor = list(recetario.filtro_por_picor(arg_picor))
    pprint.pprint(res_picor)
    print()


if __name__ == "__main__":
    main()
    print("Programa finalizado")