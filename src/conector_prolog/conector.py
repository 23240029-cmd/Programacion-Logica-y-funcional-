"""
% Delgado Alcantar Emilio.
% Valenzuela Hurtado Ana Guadalupe.
% Sepulveda Becerra Frida Paulina.
% Cervarntes Guerrero Eduardo Agustin.
Modulo encargado de crear el objeto que representa el encapusulamiento
de python con prologo y la exposicon de metodos de prolog

clase: ConctorPrologo
"""

from pathlib import Path
from pyswip import Prolog


class PrologConector:
    def __init__(self, ruta_relativa_prolog: str):
        ruta_absoluta = Path(__file__).resolve().parents[2]
        #Se crear objeto controlador de prolog
        self.prolog = Prolog()
        
        #Variable bandera en caso de que falle el consult
        self.conexion = False
        
        #Se crea ruta dinamica para buscar el archivo
        self.ruta_archivo = (ruta_absoluta / ruta_relativa_prolog).as_posix()

        #Inicial el conector para hacer consultas
        self.iniciador_conector()


    def iniciador_conector(self):
        try:
            self.prolog.consult(self.ruta_archivo)
            self.conexion = True
            return True
        except Exception as e:
            self.conexion = False
            print(f"Error al iniciar el conector con '{self.ruta_archivo}': {e}")
            return False

    def hacer_consulta(self, query: str):
        """
            Reliaza una consulta en prolog con uso de query
            -----------------------------------------------

            Retorna un lista de diccionarios para trabajar, por ejemplo:

            [
                {'Abuelo': 'carlos', 'Nieto': 'maria'},
                {'Abuelo': 'carlos', 'Nieto': 'pedro'}
            ]
        """
        if not self.conexion:
            raise Exception(f"Error con la conexion del archivo {self.ruta_archivo}")

        try:
            return list(self.prolog.query(query))
        except Exception as e:
            print(f"Error al iniciar el conector con '{self.ruta_archivo}': {e}")
            return []
