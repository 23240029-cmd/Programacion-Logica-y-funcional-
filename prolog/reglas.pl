% ====================================================================
% CONSULTA DE HECHOS DESDE RECETAS.PL
:- consult('recetas.pl').
% ====================================================================
% =====================================================================
% REGLAS
% =====================================================================
% --------------------------------------------------------------------
% Regla para agregar platillos completos
% --------------------------------------------------------------------
:- dynamic platillo/3, ingrediente/2, picante/2, tiempo_preparacion/2.

agregar_platillo(Nombre, Tipo, Region, ListaIngredientes, NivelPicante, Tiempo) :-
    assertz(platillo(Nombre, Tipo, Region)),
    assertz(picante(Nombre, NivelPicante)),
    assertz(tiempo_preparacion(Nombre, Tiempo)),
    agregar_ingredientes(Nombre, ListaIngredientes).

% Regla para insertar una lista de ingredientes
agregar_ingredientes(_, []).
agregar_ingredientes(Nombre, [H|T]) :-
    assertz(ingrediente(Nombre, H)),
    agregar_ingredientes(Nombre, T).

% --------------------------------------------------------------------
% Consultas y filto de los platillos
% --------------------------------------------------------------------

% Consultar platillos por su estado/región
platillo_de_region(Platillo, Region) :-
    platillo(Platillo, _, Region).

% Consultar platillos rápidos (preparación menor o igual a X minutos)
receta_rapida(Platillo, MinutosMax) :-
    tiempo_preparacion(Platillo, Tiempo),
    Tiempo =< MinutosMax.

% --------------------------------------------------------------------
% Reglas combinadas (osea que usan 2 o mas hechos jaja)
% --------------------------------------------------------------------

% Regla 1: Platillo apto para personas que no comen picante o comen muy poco,
% Con un tiempo de preparación máximo
opcion_suave_y_rapida(Platillo, TiempoMax) :-
    picante(Platillo, bajo),
    tiempo_preparacion(Platillo, Tiempo),
    Tiempo =< TiempoMax.

% Regla 2: Platillos picantes de una región específica
platillo_picante_regional(Platillo, Region, NivelPicante) :-
    platillo(Platillo, _, Region),
    picante(Platillo, NivelPicante),
    (NivelPicante == medio ; NivelPicante == alto).

% Regla 3: Receta completa con detalles (platillo, picante, tiempo e ingrediente)
% Esta regla puede servirnos para llamarla a la interfaz de Python 
detalle_receta(Platillo, Tipo, Region, NivelPicante, Tiempo, Ingrediente) :-
    platillo(Platillo, Tipo, Region),
    picante(Platillo, NivelPicante),
    tiempo_preparacion(Platillo, Tiempo),
    ingrediente(Platillo, Ingrediente).

% Regla 4: Buscar platillos que contengan dos ingredientes obligatorios a la vez
platillo_con_dos_ingredientes(Platillo, Ingrediente1, Ingrediente2) :-
    ingrediente(Platillo, Ingrediente1),
    ingrediente(Platillo, Ingrediente2),
    Ingrediente1 \== Ingrediente2.

% Regla 5: Alergias
% Platillo seguro si NO tiene el ingrediente que proboca alergia
platillo_sin_ingrediente(Platillo, IngredienteProhibido) :-
    platillo(Platillo, _, _),
    \+ ingrediente(Platillo, IngredienteProhibido).