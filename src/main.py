from info_recetario import info_recetario

def main():
    conector  = info_recetario.PrologConector("prolog/reglas.pl")
    recetario = info_recetario.InformacionRecetario(conector)
    recetario.obtener_detalle_receta()