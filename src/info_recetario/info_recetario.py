from conector_prolog import PrologConector

class InformacionRecetario:
    """
    Clase que representa la información del recetario y permite obtener detalles de las recetas.
    """
    def __init__(self, conector: PrologConector):
        self.conector = conector

    def obtener_detalle_receta(self): 
        recetas = self.conector.hacer_consulta("detalle_receta(Platillo, Tipo, Region, Picante, Tiempo, _)")

        print("Recetas obtenidas de Prolog:")

        for receta in recetas:
            print(f"Platillo: {receta['Platillo']}, Tipo: {receta['Tipo']}, Región: {receta['Region']}, Picante: {receta['Picante']}, Tiempo: {receta['Tiempo']} min")