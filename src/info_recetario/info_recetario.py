"""
% Delgado Alcantar Emilio.
% Valenzuela Hurtado Ana Guadalupe.
% Sepulveda Becerra Frida Paulina.
% Cervarntes Guerrero Eduardo Agustin.
"""

from conector_prolog import PrologConector
from util.formato_prolog import agrupar_recetas_dict, formato_busqueda_receta, agrupar_receta_unica_dict    
from util.constantes import NIVEL_DE_PICOR

class InformacionRecetario:
    """
    Clase que representa la información del recetario y permite obtener detalles de las recetas.
    """
    def __init__(self, conector: PrologConector):
        self.conector = conector

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

    def traer_platillos_por_nivel_de_picor(self, picor: str):
        if picor not in NIVEL_DE_PICOR:
            return []

        recetas = self.conector.hacer_consulta(f"picante(Platillo, {picor})")
        return recetas

    def obtener_detalle_receta(self): 
        """
        Obtiene todos el detalle de las recetas disponibles en el recetario
        """
        recetas = self.conector.hacer_consulta("detalle_receta(Platillo, Tipo, Region, Picante, Tiempo, Ingrediente)")
    
        return agrupar_recetas_dict(recetas)

    def filtro_por_tiempo(self, tiempo):
        """
        Filtra las recetas por tiempo máximo (en minutos). y con su detalle completo.
        """
        recetas_tiempo = self.receta_por_tiempo(tiempo)

        for receta_tiempo in recetas_tiempo:
            nombre_receta = receta_tiempo['Platillo']
            detalle_receta = self.obtener_detalle_receta_por_nombre(nombre_receta)
            
            if detalle_receta:
                yield detalle_receta

    def filtro_por_region(self, region):
        recetas_region = self.receta_por_region(region)

        for receta_region in recetas_region:
            nombre_receta = receta_region['Platillo']
            detalle_receta = self.obtener_detalle_receta_por_nombre(nombre_receta)
            
            if detalle_receta:
                yield detalle_receta

    def filtro_por_picor(self, picor):
        recetas_picor = self.traer_platillos_por_nivel_de_picor(picor)

        for receta_picor in recetas_picor:
            nombre_receta = receta_picor['Platillo']
            detalle_receta = self.obtener_detalle_receta_por_nombre(nombre_receta)
            
            if detalle_receta:
                yield detalle_receta

    def filtro_suave_y_rapido(self, tiempo: int):
        """
        Consulta la regla opcion_suave_y_rapida de Prolog (Picante bajo + Tiempo <= max).
        """
        recetas = self.conector.hacer_consulta(f"opcion_suave_y_rapida(Platillo, {tiempo})")
        # Aquí reutilizas su patrón N+1 (poco eficiente, pero respeta su arquitectura)
        for receta in recetas:
            nombre = receta['Platillo']
            detalle = self.obtener_detalle_receta_por_nombre(nombre)
            if detalle:
                yield detalle

    def filtro_alergias(self, ingrediente_prohibido: str):
        """
        Consulta la regla platillo_sin_ingrediente de Prolog.
        """
        recetas = self.conector.hacer_consulta(f"platillo_sin_ingrediente(Platillo, {ingrediente_prohibido})")
        for receta in recetas:
            nombre = receta['Platillo']
            detalle = self.obtener_detalle_receta_por_nombre(nombre)
            if detalle:
                yield detalle
