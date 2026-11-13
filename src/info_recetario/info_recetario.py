from conector_prolog import PrologConector
from util.formato_prolog import agrupar_recetas_dict, formato_busqueda_receta, agrupar_receta_unica_dict    
from util.constantes import NIVEL_DE_PICOR

class InformacionRecetario:
    """
    Clase que representa la información del recetario y permite obtener detalles de las recetas.
    """
    def __init__(self, conector: PrologConector):
        self.conector = conector

    def obtener_detalle_receta(self): 
        recetas = self.conector.hacer_consulta("detalle_receta(Platillo, Tipo, Region, Picante, Tiempo, Ingrediente)")
        return agrupar_recetas_dict(recetas)

    def obtener_detalle_receta_por_nombre(self, nombre: str):
        """
        Obtiene el detalle de una receta específica por su nombre.
        """
        # Nota: Usa 'detalle_receta' si no creaste la regla 'detalle_receta_por_nombre' en Prolog
        recetas = self.conector.hacer_consulta(f"detalle_receta({formato_busqueda_receta(nombre)}, Tipo, Region, Picante, Tiempo, Ingredientes)")
        return agrupar_receta_unica_dict(recetas)

    def receta_por_tiempo(self, tiempo: int):
        """
        Usada para filtrar platillos menores o iguales a un tiempo máximo.
        """
        recetas = self.conector.hacer_consulta(f"receta_rapida(Platillo, {tiempo})")
        return recetas

    def receta_por_region(self, region: str): 
        """
        Usada para obtener las recetas especificadas dada una región determinada.
        """
        recetas = self.conector.hacer_consulta(f"platillo_de_region(Platillo, {region})")
        return recetas

    def busqueda_receta_por_nombre(self, nombre_platillo: str):
        """
        Verifica si existe una receta dado su nombre.
        """
        receta = self.conector.hacer_consulta(f"platillo({formato_busqueda_receta(nombre_platillo)}, _, _)")
        return receta

    def traer_platillos_por_nivel_de_picor(self, picor: str):
        if picor not in NIVEL_DE_PICOR:
            return []

        recetas = self.conector.hacer_consulta(f"picante(Platillo, {picor})")
        return recetas  # <-- Faltaba este return