import customtkinter as ctk
from info_recetario import InformacionRecetario
from conector_prolog import PrologConector

# ====================================================================
# COMPONENTE DE TARJETA (Para que Agustín lo mande a llamar)
# ====================================================================
class TarjetaReceta(ctk.CTkFrame):
    def __init__(self, master, nombre, tipo, region, tiempo, picante, comando_click=None, **kwargs):
        """
        Componente reutilizable para mostrar una receta.
        Agustín solo necesita instanciar esta clase pasándole los datos de Prolog.
        """
        # Colores basados en el diseño oscuro del prototipo
        super().__init__(master, fg_color="#282c37", border_color="#4a4d59", border_width=1, corner_radius=15, **kwargs)

        # 1. Contenedor de la Imagen (Placeholder superior)
        self.image_frame = ctk.CTkFrame(self, fg_color="#4a4d59", height=120, corner_radius=15)
        self.image_frame.pack(fill="x", padx=2, pady=2)
        self.image_frame.pack_propagate(False) # Evita que se encoja

        # Etiqueta de la región (Ej. CDMX, Jalisco) arriba a la derecha
        self.lbl_region = ctk.CTkLabel(
            self.image_frame, 
            text=str(region).replace('_', ' ').title(), 
            fg_color="#1e212b", text_color="white", 
            corner_radius=10, font=("Arial", 11, "bold"), padx=10, pady=2
        )
        self.lbl_region.pack(anchor="ne", padx=10, pady=10)

        # 2. Contenedor del contenido (Textos y botón)
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True, padx=15, pady=15)

        # Título de la receta
        self.lbl_nombre = ctk.CTkLabel(
            self.content_frame, 
            text=str(nombre).replace('_', ' ').title(), 
            font=("Arial", 18, "bold"), text_color="white", anchor="w"
        )
        self.lbl_nombre.pack(fill="x")

        # Categoría (Ej. Plato Fuerte)
        self.lbl_tipo = ctk.CTkLabel(
            self.content_frame, 
            text=str(tipo).replace('_', ' ').title(), 
            font=("Arial", 12), text_color="#a0aab2", anchor="w"
        )
        self.lbl_tipo.pack(fill="x", pady=(0, 10))

        # 3. Contenedor de estadísticas (Tiempo y Picante) en la misma fila
        self.stats_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.stats_frame.pack(fill="x", pady=(0, 15))

        self.lbl_tiempo = ctk.CTkLabel(
            self.stats_frame, 
            text=f"⏱️ {tiempo} min", 
            text_color="#d1d5db", font=("Arial", 12, "bold")
        )
        self.lbl_tiempo.pack(side="left")

        self.lbl_picante = ctk.CTkLabel(
            self.stats_frame, 
            text=f"🌶️ {str(picante).title()}", 
            text_color="#d1d5db", font=("Arial", 12, "bold")
        )
        self.lbl_picante.pack(side="right")

        # 4. Botón de acción
        self.btn_detalles = ctk.CTkButton(
            self.content_frame, 
            text="Ver Detalles →", 
            fg_color="#1e212b", hover_color="#ff5c5c", # Rojo tipo Tailwind al pasar el mouse
            border_color="#4a4d59", border_width=1,
            command=comando_click
        )
        self.btn_detalles.pack(fill="x", side="bottom")


# ====================================================================
# EJEMPLO DE CÓMO AGUSTÍN DEBE ALIMENTAR EL COMPONENTE
# ====================================================================
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Recetario Inteligente Prolog")
        self.geometry("1100x650")
        self.configure(fg_color="#1e212b")

        # =========================================================
        # 1. PANEL LATERAL IZQUIERDO (EL QUE AGUSTÍN BORRÓ)
        # =========================================================
        self.panel_lateral = ctk.CTkFrame(self, width=280, fg_color="#282c37", corner_radius=0)
        self.panel_lateral.pack(side="left", fill="y")
        self.panel_lateral.pack_propagate(False)

        # Título del panel
        ctk.CTkLabel(self.panel_lateral, text="🍳 Recetario Experto", font=("Arial", 20, "bold"), text_color="white").pack(pady=(20, 10), padx=20, anchor="w")

        # Buscador de ingredientes
        self.entry_buscar_ingrediente = ctk.CTkEntry(self.panel_lateral, placeholder_text="Buscar ingrediente...", fg_color="#1e212b", border_color="#ff5c5c")
        self.entry_buscar_ingrediente.pack(pady=10, padx=20, fill="x")

        # Contenedor de la Despensa (Scroll)
        ctk.CTkLabel(self.panel_lateral, text="MI DESPENSA", font=("Arial", 10, "bold"), text_color="#a0aab2").pack(padx=20, anchor="w", pady=(10,5))
        self.scroll_despensa = ctk.CTkScrollableFrame(self.panel_lateral, fg_color="transparent")
        self.scroll_despensa.pack(fill="both", expand=True, padx=10)

        # Variables de estado para los ingredientes (Ejemplos fijos por ahora)
        self.var_cerdo = ctk.StringVar(value="off")
        self.var_tomate = ctk.StringVar(value="off")
        self.var_poblano = ctk.StringVar(value="on")

        ctk.CTkCheckBox(self.scroll_despensa, text="🥩 Cerdo", variable=self.var_cerdo, onvalue="cerdo", offvalue="off", fg_color="#ff5c5c", hover_color="#ff5c5c").pack(pady=5, anchor="w")
        ctk.CTkCheckBox(self.scroll_despensa, text="🍅 Tomates", variable=self.var_tomate, onvalue="tomates", offvalue="off", fg_color="#ff5c5c", hover_color="#ff5c5c").pack(pady=5, anchor="w")
        ctk.CTkCheckBox(self.scroll_despensa, text="🌶️ Chile Poblano", variable=self.var_poblano, onvalue="chile_poblano", offvalue="off", fg_color="#ff5c5c", hover_color="#ff5c5c").pack(pady=5, anchor="w")

        # Filtro de Regla Avanzada de Prolog
        self.var_opcion_suave = ctk.StringVar(value="off")
        ctk.CTkSwitch(self.panel_lateral, text="Opción Suave (Sin chile)", variable=self.var_opcion_suave, onvalue="on", offvalue="off", progress_color="#ff5c5c").pack(pady=15, padx=20, anchor="w")

        # Botón de ejecución
        self.btn_consultar = ctk.CTkButton(
            self.panel_lateral, 
            text="Consultar Prolog", 
            fg_color="#ff5c5c", hover_color="#e04848", font=("Arial", 14, "bold"), height=40,
            command=self.ejecutar_consulta  # <--- ESTO ES LO CLAVE
        )
        self.btn_consultar.pack(pady=20, padx=20, fill="x", side="bottom")


        # =========================================================
        # 2. ÁREA PRINCIPAL DERECHA (BÚSQUEDA Y RESULTADOS)
        # =========================================================
        self.area_principal = ctk.CTkFrame(self, fg_color="transparent")
        self.area_principal.pack(side="right", fill="both", expand=True)

        # BARRA SUPERIOR (La que Agustín sí dejó)
        self.barra_superior = ctk.CTkFrame(self.area_principal, height=70, fg_color="#282c37", corner_radius=0)
        self.barra_superior.pack(fill="x")
        self.barra_superior.pack_propagate(False)

        self.entry_buscar_nombre = ctk.CTkEntry(self.barra_superior, placeholder_text="Buscar platillo por nombre...", width=300, fg_color="#1e212b", border_color="#ff5c5c")
        self.entry_buscar_nombre.pack(side="left", padx=20, pady=20)

        self.combo_tiempo = ctk.CTkOptionMenu(self.barra_superior, values=["Cualquier tiempo", "< 30 mins", "< 60 mins"], fg_color="#1e212b", button_color="#4a4d59", button_hover_color="#ff5c5c")
        self.combo_tiempo.pack(side="right", padx=20, pady=20)

        self.combo_region = ctk.CTkOptionMenu(self.barra_superior, values=["Todas las regiones", "Puebla", "Yucatán", "Sonora"], fg_color="#1e212b", button_color="#4a4d59", button_hover_color="#ff5c5c")
        self.combo_region.pack(side="right", padx=5, pady=20)

        # RESULTADOS (Grid)
        ctk.CTkLabel(self.area_principal, text="Recetas Recomendadas", font=("Arial", 24, "bold"), text_color="white").pack(pady=(20, 10), padx=30, anchor="w")
        
        self.grid_recetas = ctk.CTkScrollableFrame(self.area_principal, fg_color="transparent")
        self.grid_recetas.pack(fill="both", expand=True, padx=20, pady=10)
        self.grid_recetas.grid_columnconfigure((0, 1, 2), weight=1)

        # Aquí insertarías un dummy label temporal para ver que funciona el grid
        ctk.CTkLabel(self.grid_recetas, text="Aquí irán las Tarjetas de Receta...").grid(row=0, column=0, pady=20)

    def ejecutar_consulta(self):
        conector = PrologConector("prolog/reglas.pl")
        recetario = InformacionRecetario(conector)
        
        # 2. Leer valores de la UI
        tiempo_max = self.combo_tiempo.get()
        
        # 3. Lógica condicional: ¿Usamos la regla avanzada?
        if self.var_opcion_suave.get() == "on":
            # Llamar al nuevo método que agregaste para usar la regla de Anna/Frida
            resultados = list(recetario.filtro_suave_y_rapido(int(tiempo_max)))
        else:
            # Llamar al método estándar de Agustín
            resultados = list(recetario.filtro_por_tiempo(int(tiempo_max)))
            
        # 4. Actualizar el grid visual
        self.actualizar_tarjetas(resultados)

    def actualizar_tarjetas(self, resultados):
        # 1. Limpiar las tarjetas de la consulta anterior
        for widget in self.grid_recetas.winfo_children():
            widget.destroy()

        if not resultados:
            ctk.CTkLabel(self.grid_recetas, text="No se encontraron recetas con estos filtros", font=("Arial", 16), text_color="#a0aab2").grid(row=0, column=0, pady=50)
            return

        # 2. Dibujar las nuevas tarjetas acomodadas en Grid (3 columnas)
        fila = 0
        columna = 0
        
        for receta in resultados:
            # Los nombres de las llaves ("Platillo", "Tipo") dependen de cómo las agrupó Agustín en su dict
            tarjeta = TarjetaReceta(
                master=self.grid_recetas,
                nombre=receta.get("Platillo", "Desconocido"),
                tipo=receta.get("Tipo", "N/A"),
                region=receta.get("Region", "N/A"),
                tiempo=receta.get("Tiempo", 0),
                picante=receta.get("Picante", "N/A"),
                comando_click=lambda r=receta.get("Platillo"): print(f"Abriendo receta: {r}")
            )
            
            tarjeta.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")
            
            columna += 1
            if columna > 2:
                columna = 0
                fila += 1

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = App()
    app.mainloop()