"""
% Delgado Alcantar Emilio.
% Valenzuela Hurtado Ana Guadalupe.
% Sepulveda Becerra Frida Paulina.
% Cervarntes Guerrero Eduardo Agustin.
"""

class FiltrosProlog:
    def __init__(self, informacion_recetario):
        self.informacion_recetario = informacion_recetario
        self.filtros = []

    def filtro_por_tiempo(self, filtro_tiempo):
        pass

    def aplicar_filtros(self, datos):
        for filtro in self.filtros:
            datos = filtro(datos)
        return datos