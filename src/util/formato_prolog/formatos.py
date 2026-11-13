def agrupar_recetas_dict(resultados_prolog: list[dict]) -> dict:
        recetas = {}

        for fila in resultados_prolog:
            nombre = fila['Platillo']

        # Si el platillo aún no existe en el diccionario, inicializamos su estructura
        if nombre not in recetas:
            recetas[nombre] = {
                'tipo': fila['Tipo'],
                'region': fila['Region'],
                'picante': fila['Picante'],
                'tiempo': fila['Tiempo'],
                'ingredientes': []
            }

        # Agregamos el ingrediente actual (evitando duplicados por si acaso)
        ingrediente = fila['Ingrediente']
        if ingrediente not in recetas[nombre]['ingredientes']:
            recetas[nombre]['ingredientes'].append(ingrediente)

        return recetas

def formato_busqueda_receta(receta_front: str):
    """
    Formatea el nombre del platillo enviado desde el front para Prolog:
    Quita espacios a los lados, pasa a minúsculas y cambia espacios internos por guiones bajos.
    """
    return receta_front.strip().lower().replace(" ", "_")


def agrupar_receta_unica_dict(resultados_prolog: list[dict]) -> dict:
    """
    Agrupa los detalles de UNA sola receta cuando viene desglosada por ingredientes (varias filas con el mismo platillo).
    """
    if not resultados_prolog:
        return {}

    # Tomamos la estructura básica de la primera fila
    primera_fila = resultados_prolog[0]
    receta_unitaria = {
        'tipo': primera_fila.get('Tipo'),
        'region': primera_fila.get('Region'),
        'picante': primera_fila.get('Picante'),
        'tiempo': primera_fila.get('Tiempo'),
        'ingredientes': []
    }

    # Recorremos todas las filas para recolectar sus ingredientes sin duplicados
    for fila in resultados_prolog:
        ingrediente = fila.get('Ingrediente')
        if ingrediente and ingrediente not in receta_unitaria['ingredientes']:
            receta_unitaria['ingredientes'].append(ingrediente)

    return receta_unitaria