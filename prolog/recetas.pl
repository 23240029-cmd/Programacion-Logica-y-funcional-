% ====================================================================
% RECETAS DE COMIDAS DE MÉXICO
% ====================================================================
% =====================================================================
% HECHOS
% =====================================================================
% --------------------------------------------------------------------
% 1. platillo(Nombre, Tipo, Region/Estado)
% --------------------------------------------------------------------
platillo(mole_poblano, plato_fuerte, puebla).
platillo(chiles_en_nogada, plato_fuerte, puebla).
platillo(cochinita_pibil, plato_fuerte, yucatan).
platillo(panuchos, plato_ligero, yucatan).
platillo(pozole_blanco, plato_fuerte, guerrero).
platillo(pozole_rojo, plato_fuerte, jalisco).
platillo(birria, plato_fuerte, jalisco).
platillo(torta_ahogada, plato_fuerte, jalisco).
platillo(enchiladas_mineras, plato_fuerte, guanajuato).
platillo(guacamayas, plato_fuerte, guanajuato).
platillo(caldo_tlalpeno, plato_fuerte, cdmx).
platillo(tacos_al_pastor, plato_fuerte, cdmx).
platillo(tlayuda, plato_fuerte, oaxaca).
platillo(mole_negro, plato_fuerte, oaxaca).
platillo(pescado_a_la_veracruzana, plato_fuerte, veracruz).
platillo(zacahuil, plato_fuerte, huasteca).
platillo(ceviche_de_camaron, entrada, sinaloa).
platillo(chilitos_rellenos_de_cazon, plato_fuerte, campeche).
platillo(cabrito_asado, plato_fuerte, nuevo_leon).
platillo(machaca_con_huevo, desayuno, nuevo_leon).
platillo(discada, plato_fuerte, coahuila).
platillo(tamales_oaxaquenos, plato_ligero, oaxaca).
platillo(cajeta_con_nieve, postre, guanajuato).
platillo(chongos_zamoranos, postre, michoacan).
platillo(carnitas, plato_fuerte, michoacan).
platillo(carne_asada_sonorense, plato_fuerte, sonora).
platillo(chimichangas, plato_fuerte, sonora).
platillo(caldo_de_queso, plato_fuerte, sonora).
platillo(gallina_pinta, plato_fuerte, sonora).
platillo(burritos_percherones, plato_fuerte, sonora).
platillo(cahuamanta, plato_fuerte, sonora).
platillo(coyotas, postre, sonora).

% --------------------------------------------------------------------
% 2. ingrediente(Platillo, Ingrediente)
% --------------------------------------------------------------------

% Mole Poblano
ingrediente(mole_poblano, pollo).
ingrediente(mole_poblano, chile_poblano).
ingrediente(mole_poblano, chocolate).
ingrediente(mole_poblano, ajonjoli).
ingrediente(mole_poblano, manteca).

% Chiles en Nogada
ingrediente(chiles_en_nogada, chile_poblano).
ingrediente(chiles_en_nogada, carne_molida).
ingrediente(chiles_en_nogada, nuez_de_castilla).
ingrediente(chiles_en_nogada, granada).
ingrediente(chiles_en_nogada, manzana).

% Cochinita Pibil
ingrediente(cochinita_pibil, cerdo).
ingrediente(cochinita_pibil, achiote).
ingrediente(cochinita_pibil, naranja_agria).
ingrediente(cochinita_pibil, hoja_de_platano).
ingrediente(cochinita_pibil, cebolla_morada).

% Panuchos
ingrediente(panuchos, tortilla).
ingrediente(panuchos, frijoles_refritos).
ingrediente(panuchos, cochinita_pibil).
ingrediente(panuchos, cebolla_morada).
ingrediente(panuchos, aguacate).

% Pozole Blanco
ingrediente(pozole_blanco, maiz_pozolero).
ingrediente(pozole_blanco, cerdo).
ingrediente(pozole_blanco, oregano).
ingrediente(pozole_blanco, cebolla).
ingrediente(pozole_blanco, lechuga).

% Pozole Rojo
ingrediente(pozole_rojo, maiz_pozolero).
ingrediente(pozole_rojo, cerdo).
ingrediente(pozole_rojo, chile_guajillo).
ingrediente(pozole_rojo, chile_ancho).
ingrediente(pozole_rojo, oregano).

% Sopa de Lima
ingrediente(sopa_de_lima, pollo).
ingrediente(sopa_de_lima, lima).
ingrediente(sopa_de_lima, tortilla).
ingrediente(sopa_de_lima, tomates).

% Birria
ingrediente(birria, chivo).
ingrediente(birria, chile_guajillo).
ingrediente(birria, chile_ancho).
ingrediente(birria, comino).
ingrediente(birria, oregano).

% Torta Ahogada
ingrediente(torta_ahogada, birote).
ingrediente(torta_ahogada, carnitas).
ingrediente(torta_ahogada, chile_de_arbol).
ingrediente(torta_ahogada, tomates).

% Enchiladas Mineras
ingrediente(enchiladas_mineras, tortilla).
ingrediente(enchiladas_mineras, queso_fresco).
ingrediente(enchiladas_mineras, chile_guajillo).
ingrediente(enchiladas_mineras, papa).
ingrediente(enchiladas_mineras, zanahoria).

% Guacamayas
ingrediente(guacamayas, bolillo).
ingrediente(guacamayas, chicharron_duro).
ingrediente(guacamayas, salsa_pico_de_gallo).
ingrediente(guacamayas, limon).

% Caldo Tlalpeño
ingrediente(caldo_tlalpeno, pollo).
ingrediente(caldo_tlalpeno, chile_chipotle).
ingrediente(caldo_tlalpeno, garbanzo).
ingrediente(caldo_tlalpeno, zanahoria).
ingrediente(caldo_tlalpeno, aguacate).

% Tacos al Pastor
ingrediente(tacos_al_pastor, tortilla).
ingrediente(tacos_al_pastor, cerdo).
ingrediente(tacos_al_pastor, achiote).
ingrediente(tacos_al_pastor, pina).
ingrediente(tacos_al_pastor, cilantro).

% Tlayuda
ingrediente(tlayuda, tortilla_grande).
ingrediente(tlayuda, asiento_de_cerdo).
ingrediente(tlayuda, frijol).
ingrediente(tlayuda, quesillo).
ingrediente(tlayuda, tasajo).

% Mole Negro
ingrediente(mole_negro, pollo).
ingrediente(mole_negro, chile_chilhuacle).
ingrediente(mole_negro, chocolate).
ingrediente(mole_negro, hoja_santa).
ingrediente(mole_negro, ajonjoli).

% Pescado a la Veracruzana
ingrediente(pescado_a_la_veracruzana, huachinango).
ingrediente(pescado_a_la_veracruzana, tomates).
ingrediente(pescado_a_la_veracruzana, aceitunas).
ingrediente(pescado_a_la_veracruzana, alcaparras).
ingrediente(pescado_a_la_veracruzana, cebolla).

% Zacahuil
ingrediente(zacahuil, masa_martajada).
ingrediente(zacahuil, cerdo).
ingrediente(zacahuil, chile_ancho).
ingrediente(zacahuil, chile_guajillo).
ingrediente(zacahuil, hoja_de_platano).

% Ceviche de Camarón
ingrediente(ceviche_de_camaron, camaron).
ingrediente(ceviche_de_camaron, limon).
ingrediente(ceviche_de_camaron, pepino).
ingrediente(ceviche_de_camaron, cebolla_morada).
ingrediente(ceviche_de_camaron, chile_serrano).

% Chilitos Rellenos de Cazón
ingrediente(chilitos_rellenos_de_cazon, chile_xcatik).
ingrediente(chilitos_rellenos_de_cazon, cazon).
ingrediente(chilitos_rellenos_de_cazon, tomate).
ingrediente(chilitos_rellenos_de_cazon, cebolla).
ingrediente(chilitos_rellenos_de_cazon, epazote).

% Cabrito Asado
ingrediente(cabrito_asado, cabrito).
ingrediente(cabrito_asado, sal).
ingrediente(cabrito_asado, carbon).

% Machaca con Huevo
ingrediente(machaca_con_huevo, machaca_de_res).
ingrediente(machaca_con_huevo, huevo).
ingrediente(machaca_con_huevo, tomate).
ingrediente(machaca_con_huevo, chile_verde).
ingrediente(machaca_con_huevo, cebolla).

% Discada
ingrediente(discada, carne_de_res).
ingrediente(discada, carne_de_cerdo).
ingrediente(discada, tocino).
ingrediente(discada, salchicha).
ingrediente(discada, salsa_pato).

% Tamales Oaxaqueños
ingrediente(tamales_oaxaquenos, masa_de_maiz).
ingrediente(tamales_oaxaquenos, mole_negro).
ingrediente(tamales_oaxaquenos, pollo).
ingrediente(tamales_oaxaquenos, hoja_de_platano).
ingrediente(tamales_oaxaquenos, manteca).

% Cajeta con Nieve
ingrediente(cajeta_con_nieve, cajeta_de_celaya).
ingrediente(cajeta_con_nieve, nieve_de_vainilla).
ingrediente(cajeta_con_nieve, nuez).

% Chongos Zamoranos
ingrediente(chongos_zamoranos, leche).
ingrediente(chongos_zamoranos, cuajo).
ingrediente(chongos_zamoranos, azucar).
ingrediente(chongos_zamoranos, canela).

% Carnitas
ingrediente(carnitas, cerdo).
ingrediente(carnitas, manteca).
ingrediente(carnitas, naranja).
ingrediente(carnitas, sal).

% Carne Asada Sonorense
ingrediente(carne_asada_sonorense, diezmillo_de_res).
ingrediente(carne_asada_sonorense, tortilla_de_harina).
ingrediente(carne_asada_sonorense, carbon_de_mezquite).
ingrediente(carne_asada_sonorense, sal).

% Chimichangas
ingrediente(chimichangas, tortilla_sobaquera).
ingrediente(chimichangas, carne_deshebrada).
ingrediente(chimichangas, frijoles_refritos).
ingrediente(chimichangas, aceite).

% Caldo de Queso
ingrediente(caldo_de_queso, queso_panela).
ingrediente(caldo_de_queso, papa).
ingrediente(caldo_de_queso, chile_california).
ingrediente(caldo_de_queso, tomate).

% Gallina Pinta
ingrediente(gallina_pinta, cola_de_res).
ingrediente(gallina_pinta, frijol).
ingrediente(gallina_pinta, maiz_pozolero).
ingrediente(gallina_pinta, chile_california).
ingrediente(gallina_pinta, ajo).

% Burritos Percherones
ingrediente(burritos_percherones, tortilla_sobaquera).
ingrediente(burritos_percherones, carne_asada).
ingrediente(burritos_percherones, queso_manchego).
ingrediente(burritos_percherones, aguacate).

% Cahuamanta
ingrediente(cahuamanta, mantarraya).
ingrediente(cahuamanta, camaron).
ingrediente(cahuamanta, apio).
ingrediente(cahuamanta, zanahoria).
ingrediente(cahuamanta, chile_pasilla).

% Coyotas
ingrediente(coyotas, harina_de_trigo).
ingrediente(coyotas, piloncillo).
ingrediente(coyotas, manteca_vegetal).
ingrediente(coyotas, levadura).
% --------------------------------------------------------------------
% 3. picante(Platillo, Nivel)  [bajo, medio, alto]
% --------------------------------------------------------------------
% Nivel Bajo 
picante(cajeta_con_nieve, bajo).
picante(chongos_zamoranos, bajo).
picante(coyotas, bajo).
picante(cabrito_asado, bajo).
picante(carne_asada_sonorense, bajo).
picante(caldo_de_queso, bajo).
picante(carnitas, bajo).
picante(chimichangas, bajo).
picante(chiles_en_nogada, bajo).
picante(cochinita_pibil, bajo).
picante(gallina_pinta, bajo).
picante(machaca_con_huevo, bajo).
picante(panuchos, bajo).
picante(pescado_a_la_veracruzana, bajo).
picante(pozole_blanco, bajo).
picante(sopa_de_lima, bajo).
picante(tacos_al_pastor, bajo).
picante(tlayuda, bajo).

% Nivel Medio
picante(birria, medio).
picante(burritos_percherones, medio).
picante(cahuamanta, medio).
picante(caldo_tlalpeno, medio).
picante(ceviche_de_camaron, medio).
picante(chilitos_rellenos_de_cazon, medio).
picante(discada, medio).
picante(enchiladas_mineras, medio).
picante(mole_negro, medio).
picante(mole_poblano, medio).
picante(pozole_rojo, medio).
picante(tamales_oaxaquenos, medio).
picante(zacahuil, medio).

% Nivel Alto
picante(guacamayas, alto).
picante(torta_ahogada, alto).

% --------------------------------------------------------------------
% 4. tiempo_preparacion(Platillo, Minutos)
% --------------------------------------------------------------------
tiempo_preparacion(cajeta_con_nieve, 5).
tiempo_preparacion(guacamayas, 15).
tiempo_preparacion(machaca_con_huevo, 20).
tiempo_preparacion(ceviche_de_camaron, 25).
tiempo_preparacion(panuchos, 30).
tiempo_preparacion(tacos_al_pastor, 35).
tiempo_preparacion(coyotas, 40).
tiempo_preparacion(sopa_de_lima, 40).
tiempo_preparacion(tlayuda, 40).
tiempo_preparacion(caldo_de_queso, 45).
tiempo_preparacion(chimichangas, 45).
tiempo_preparacion(enchiladas_mineras, 45).
tiempo_preparacion(caldo_tlalpeno, 50).
tiempo_preparacion(pescado_a_la_veracruzana, 50).
tiempo_preparacion(chilitos_rellenos_de_cazon, 50).
tiempo_preparacion(discada, 60).
tiempo_preparacion(torta_ahogada, 60).
tiempo_preparacion(carne_asada_sonorense, 60).
tiempo_preparacion(burritos_percherones, 60).
tiempo_preparacion(chongos_zamoranos, 90).
tiempo_preparacion(cahuamanta, 90).
tiempo_preparacion(chiles_en_nogada, 120).
tiempo_preparacion(tamales_oaxaquenos, 120).
tiempo_preparacion(pozole_blanco, 150).
tiempo_preparacion(pozole_rojo, 150).
tiempo_preparacion(cabrito_asado, 180).
tiempo_preparacion(gallina_pinta, 180).
tiempo_preparacion(mole_poblano, 180).
tiempo_preparacion(mole_negro, 200).
tiempo_preparacion(carnitas, 210).
tiempo_preparacion(cochinita_pibil, 240).
tiempo_preparacion(birria, 240).
tiempo_preparacion(zacahuil, 600).