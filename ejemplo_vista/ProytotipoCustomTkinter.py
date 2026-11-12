import customtkinter as ctk

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
        self.geometry("900x600")
        self.configure(fg_color="#1e212b") # Fondo principal oscuro

        # Título principal de la ventana
        self.lbl_titulo = ctk.CTkLabel(self, text="Recetas Recomendadas", font=("Arial", 24, "bold"), text_color="white")
        self.lbl_titulo.pack(pady=20, padx=20, anchor="w")

        # ScrollableFrame donde irán todas las tarjetas
        self.grid_recetas = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.grid_recetas.pack(fill="both", expand=True, padx=10, pady=10)

        # Configurar el grid para que tenga 3 columnas adaptables
        self.grid_recetas.grid_columnconfigure(0, weight=1)
        self.grid_recetas.grid_columnconfigure(1, weight=1)
        self.grid_recetas.grid_columnconfigure(2, weight=1)

        # ------------------------------------------------------------
        # AQUÍ ES DONDE ENTRA EL BACKEND DE AGUSTÍN
        # Supongamos que esta lista viene de su consulta a pyswip:
        # list(prolog.query("detalle_receta(Platillo, Tipo, Region, Picante, Tiempo, _)"))
        # ------------------------------------------------------------
        datos_de_prolog = [
            {"nombre": "chiles_en_nogada", "tipo": "plato_fuerte", "region": "puebla", "tiempo": 120, "picante": "bajo"},
            {"nombre": "tacos_al_pastor", "tipo": "plato_fuerte", "region": "cdmx", "tiempo": 35, "picante": "medio"},
            {"nombre": "cochinita_pibil", "tipo": "plato_fuerte", "region": "yucatan", "tiempo": 240, "picante": "bajo"},
            {"nombre": "guacamayas", "tipo": "plato_fuerte", "region": "guanajuato", "tiempo": 15, "picante": "alto"},
            {"nombre": "cajeta_con_nieve", "tipo": "postre", "region": "guanajuato", "tiempo": 5, "picante": "bajo"}
        ]

        # Agustín solo hace un for loop y manda a llamar a tu componente "TarjetaReceta"
        fila = 0
        columna = 0
        
        for receta in datos_de_prolog:
            # Instanciar la tarjeta creada arriba
            tarjeta = TarjetaReceta(
                master=self.grid_recetas,
                nombre=receta["nombre"],
                tipo=receta["tipo"],
                region=receta["region"],
                tiempo=receta["tiempo"],
                picante=receta["picante"],
                comando_click=lambda r=receta["nombre"]: print(f"Consultar detalles de: {r}")
            )
            
            # Posicionar en el grid (3 columnas)
            tarjeta.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")
            
            columna += 1
            if columna > 2:
                columna = 0
                fila += 1

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = App()
    app.mainloop()