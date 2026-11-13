from info_recetario import  InformacionRecetario
from conector_prolog import PrologConector

def main():
    conector = PrologConector("prolog/reglas.pl")
    recetario = InformacionRecetario(conector)

    # 1. Obtener todas las recetas con detalle agrupado
    print("=== 1. obtener_detalle_receta() ===")
    res_todos = recetario.obtener_detalle_receta()
    print("Respuesta:", res_todos, "\n")

    # 2. Obtener detalle de una receta por nombre
    arg_nombre = "mole_poblano"
    print(f"=== 2. obtener_detalle_receta_por_nombre('{arg_nombre}') ===")
    res_detalle_nombre = recetario.obtener_detalle_receta_por_nombre(arg_nombre)
    print("Respuesta:", res_detalle_nombre, "\n")

    # 3. Filtrar recetas por tiempo máximo (en minutos)
    arg_tiempo = 30
    print(f"=== 3. receta_por_tiempo({arg_tiempo}) ===")
    res_tiempo = recetario.receta_por_tiempo(arg_tiempo)
    print("Respuesta:", res_tiempo, "\n")

    # 4. Filtrar recetas por región / estado
    arg_region = "sonora"
    print(f"=== 4. receta_por_region('{arg_region}') ===")
    res_region = recetario.receta_por_region(arg_region)
    print("Respuesta:", res_region, "\n")

    # 5. Buscar existencia de receta por nombre
    arg_busqueda = "tacos_al_pastor"
    print(f"=== 5. busqueda_receta_por_nombre('{arg_busqueda}') ===")
    res_busqueda = recetario.busqueda_receta_por_nombre(arg_busqueda)
    print("Respuesta:", res_busqueda, "\n")

    # 6. Traer platillos por nivel de picor
    arg_picor = "alto"
    print(f"=== 6. traer_platillos_por_nivel_de_picor('{arg_picor}') ===")
    res_picor = recetario.traer_platillos_por_nivel_de_picor(arg_picor)
    print("Respuesta:", res_picor, "\n")

if __name__ == "__main__":
    main()
    print("Programa finalizado")