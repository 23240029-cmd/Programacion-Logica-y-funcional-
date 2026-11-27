import sys
import os
from pathlib import Path
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk
from conector_prolog import PrologConector


# ====================================================================
# COMPONENTE: VENTANA EMERGENTE DE DETALLES DE LA RECETA
# ====================================================================
class VentanaDetalles(ctk.CTkToplevel):
    def __init__(self, master, receta):
        super().__init__(master)
        nombre_limpio = str(receta["Platillo"]).replace('_', ' ').title()
        self.title(f"Detalles: {nombre_limpio}")
        self.geometry("420x480")
        self.configure(fg_color="#1e212b")
        self.attributes("-topmost", True)

        ctk.CTkLabel(
            self, text=nombre_limpio, font=("Arial", 22, "bold"), text_color="white"
        ).pack(pady=(25, 5), padx=20)

        subtitulo = f"{receta['Tipo'].replace('_', ' ').title()} • {receta['Region'].replace('_', ' ').title()}"
        ctk.CTkLabel(
            self, text=subtitulo, font=("Arial", 13), text_color="#ff5c5c"
        ).pack(pady=(0, 15))

        stats = ctk.CTkFrame(self, fg_color="#282c37", corner_radius=10)
        stats.pack(fill="x", padx=25, pady=5)
        ctk.CTkLabel(
            stats, text=f"Tiempo: {receta['Tiempo']} mins", font=("Arial", 13, "bold"), text_color="white"
        ).pack(side="left", padx=20, pady=12)
        ctk.CTkLabel(
            stats, text=f"Picor: {receta['Picante'].title()}", font=("Arial", 13, "bold"), text_color="white"
        ).pack(side="right", padx=20, pady=12)

        # Lista de ingredientes
        ctk.CTkLabel(
            self, text="INGREDIENTES NECESARIOS:", font=("Arial", 11, "bold"), text_color="#a0aab2"
        ).pack(anchor="w", padx=25, pady=(20, 5))

        scroll_ing = ctk.CTkScrollableFrame(self, fg_color="#282c37", corner_radius=10)
        scroll_ing.pack(fill="both", expand=True, padx=25, pady=(0, 20))

        for ing in receta["Ingredientes"]:
            ing_limpio = str(ing).replace('_', ' ').capitalize()
            ctk.CTkLabel(
                scroll_ing, text=f"•  {ing_limpio}", font=("Arial", 14), text_color="#e5e7eb", anchor="w"
            ).pack(fill="x", padx=15, pady=4)


# ====================================================================
# COMPONENTE: TARJETA INDIVIDUAL DE RECETA
# ====================================================================
class TarjetaReceta(ctk.CTkFrame):
    def __init__(self, master, receta, comando_click=None, **kwargs):
        super().__init__(master, fg_color="#282c37", border_color="#4a4d59", border_width=1, corner_radius=15, **kwargs)

        # 1. Contenedor superior de la imagen
        self.image_frame = ctk.CTkFrame(self, fg_color="#3b3f4e", height=130, corner_radius=15)
        self.image_frame.pack(fill="x", padx=2, pady=2)
        self.image_frame.pack_propagate(False)

        # Cargar la imagen dinámicamente desde assets/recetas/
        img_ctk = self.cargar_imagen_platillo(receta["Platillo"])
        if img_ctk:
            self.lbl_imagen = ctk.CTkLabel(self.image_frame, text="", image=img_ctk)
            self.lbl_imagen.place(relx=0.5, rely=0.5, anchor="center")

        # Etiqueta flotante de la Región encima de la imagen
        self.lbl_region = ctk.CTkLabel(
            self.image_frame,
            text=str(receta["Region"]).replace('_', ' ').title(),
            fg_color="#1e212b", text_color="white",
            corner_radius=10, font=("Arial", 11, "bold"), padx=10, pady=2
        )
        self.lbl_region.place(relx=0.95, rely=0.12, anchor="ne")

        # 2. Contenido (Textos y botón)
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True, padx=15, pady=15)

        self.lbl_nombre = ctk.CTkLabel(
            self.content_frame,
            text=str(receta["Platillo"]).replace('_', ' ').title(),
            font=("Arial", 17, "bold"), text_color="white", anchor="w", wraplength=200
        )
        self.lbl_nombre.pack(fill="x")

        self.lbl_tipo = ctk.CTkLabel(
            self.content_frame,
            text=str(receta["Tipo"]).replace('_', ' ').title(),
            font=("Arial", 12), text_color="#a0aab2", anchor="w"
        )
        self.lbl_tipo.pack(fill="x", pady=(2, 10))

        # 3. Tiempo y Picante
        self.stats_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.stats_frame.pack(fill="x", pady=(0, 15))

        ctk.CTkLabel(
            self.stats_frame, text=f"{receta['Tiempo']} min", text_color="#d1d5db", font=("Arial", 12, "bold")
        ).pack(side="left")

        ctk.CTkLabel(
            self.stats_frame, text=f"{str(receta['Picante']).title()}", text_color="#d1d5db", font=("Arial", 12, "bold")
        ).pack(side="right")

        # 4. Botón Detalles
        self.btn_detalles = ctk.CTkButton(
            self.content_frame,
            text="Ver Detalles →",
            fg_color="#1e212b", hover_color="#ff5c5c",
            border_color="#4a4d59", border_width=1,
            command=comando_click
        )
        self.btn_detalles.pack(fill="x", side="bottom")

    def cargar_imagen_platillo(self, nombre_platillo):
        ruta_assets = Path(__file__).resolve().parents[2] / "assets" / "recetas"
        nombre_limpio = str(nombre_platillo).strip().lower()

        posibles = [
            ruta_assets / f"{nombre_limpio}.jpg",
            ruta_assets / f"{nombre_limpio}.jpeg",
            ruta_assets / f"{nombre_limpio}.png",
            ruta_assets / "default.jpg",
            ruta_assets / "default.jpeg",
            ruta_assets / "default.png"
        ]

        for ruta in posibles:
            if ruta.exists():
                imagen_pil = Image.open(ruta)
                return ctk.CTkImage(light_image=imagen_pil, dark_image=imagen_pil, size=(280, 130))
        return None


# ====================================================================
# APLICACION PRINCIPAL
# ====================================================================
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Recetario Inteligente Prolog")
        self.geometry("1150x680")
        self.configure(fg_color="#1e212b")

        self.conector = PrologConector("prolog/reglas.pl")

        self.todos_ingredientes = self.obtener_ingredientes_unicos()
        self.todas_regiones = self.obtener_regiones_unicas()
        self.vars_ingredientes = {}

        # ---------------------------------------------------------
        # 1. PANEL LATERAL IZQUIERDO
        # ---------------------------------------------------------
        self.panel_lateral = ctk.CTkFrame(self, width=290, fg_color="#282c37", corner_radius=0)
        self.panel_lateral.pack(side="left", fill="y")
        self.panel_lateral.pack_propagate(False)

        ctk.CTkLabel(
            self.panel_lateral, text="Recetario Experto", font=("Arial", 20, "bold"), text_color="white"
        ).pack(pady=(20, 10), padx=20, anchor="w")

        # Buscador de la despensa
        self.entry_buscar_ingrediente = ctk.CTkEntry(
            self.panel_lateral, placeholder_text="Filtrar ingrediente...", fg_color="#1e212b", border_color="#4a4d59"
        )
        self.entry_buscar_ingrediente.pack(pady=5, padx=20, fill="x")
        self.entry_buscar_ingrediente.bind("<KeyRelease>", self.filtrar_lista_despensa)

        ctk.CTkLabel(
            self.panel_lateral, text="MI DESPENSA", font=("Arial", 10, "bold"), text_color="#a0aab2"
        ).pack(padx=20, anchor="w", pady=(10, 5))

        self.scroll_despensa = ctk.CTkScrollableFrame(self.panel_lateral, fg_color="transparent")
        self.scroll_despensa.pack(fill="both", expand=True, padx=10)
        self.poblar_despensa(self.todos_ingredientes)

        # Switch de Regla Combinada (opcion_suave_y_rapida)
        self.var_opcion_suave = ctk.StringVar(value="off")
        ctk.CTkSwitch(
            self.panel_lateral, text="Opcion Suave (Sin chile)",
            variable=self.var_opcion_suave, onvalue="on", offvalue="off",
            progress_color="#ff5c5c", font=("Arial", 12, "bold")
        ).pack(pady=(15, 5), padx=20, anchor="w")

        # Botones de accion
        self.btn_consultar = ctk.CTkButton(
            self.panel_lateral, text="Consultar Prolog",
            fg_color="#ff5c5c", hover_color="#e04848", font=("Arial", 14, "bold"), height=40,
            command=self.ejecutar_consulta
        )
        self.btn_consultar.pack(pady=(10, 5), padx=20, fill="x")

        self.btn_limpiar = ctk.CTkButton(
            self.panel_lateral, text="Limpiar Filtros",
            fg_color="transparent", border_color="#4a4d59", border_width=1, hover_color="#3b3f4e",
            command=self.limpiar_filtros
        )
        self.btn_limpiar.pack(pady=(0, 15), padx=20, fill="x")

        # ---------------------------------------------------------
        # 2. AREA PRINCIPAL DERECHA
        # ---------------------------------------------------------
        self.area_principal = ctk.CTkFrame(self, fg_color="transparent")
        self.area_principal.pack(side="right", fill="both", expand=True)

        # Barra Superior
        self.barra_superior = ctk.CTkFrame(self.area_principal, height=75, fg_color="#282c37", corner_radius=0)
        self.barra_superior.pack(fill="x")
        self.barra_superior.pack_propagate(False)

        self.entry_buscar_nombre = ctk.CTkEntry(
            self.barra_superior, placeholder_text="Buscar platillo por nombre (ej. tacos, mole)...",
            width=300, fg_color="#1e212b", border_color="#4a4d59"
        )
        self.entry_buscar_nombre.pack(side="left", padx=20, pady=20)
        self.entry_buscar_nombre.bind("<Return>", lambda e: self.ejecutar_consulta())

        self.combo_tiempo = ctk.CTkOptionMenu(
            self.barra_superior,
            values=["Cualquier tiempo", "< 30 mins", "< 60 mins", "< 120 mins"],
            fg_color="#1e212b", button_color="#4a4d59", button_hover_color="#ff5c5c"
        )
        self.combo_tiempo.pack(side="right", padx=20, pady=20)

        opciones_region = ["Todas las regiones"] + [r.replace('_', ' ').title() for r in self.todas_regiones]
        self.combo_region = ctk.CTkOptionMenu(
            self.barra_superior,
            values=opciones_region,
            fg_color="#1e212b", button_color="#4a4d59", button_hover_color="#ff5c5c"
        )
        self.combo_region.pack(side="right", padx=5, pady=20)

        # Encabezado de resultados
        self.lbl_contador = ctk.CTkLabel(
            self.area_principal, text="Recetas", font=("Arial", 22, "bold"), text_color="white"
        )
        self.lbl_contador.pack(pady=(20, 10), padx=25, anchor="w")

        # Cuadricula desplazable de tarjetas
        self.grid_recetas = ctk.CTkScrollableFrame(self.area_principal, fg_color="transparent")
        self.grid_recetas.pack(fill="both", expand=True, padx=15, pady=10)
        self.grid_recetas.grid_columnconfigure((0, 1, 2), weight=1)

        # Cargar todas las recetas desde el arranque
        self.ejecutar_consulta()

    # ====================================================================
    # METODOS DE CONSULTA DIRECTA A PROLOG
    # ====================================================================
    def obtener_ingredientes_unicos(self):
        res = self.conector.hacer_consulta("ingrediente(_, Ing)")
        return sorted(list({str(r["Ing"]) for r in res}))

    def obtener_regiones_unicas(self):
        res = self.conector.hacer_consulta("platillo(_, _, Reg)")
        return sorted(list({str(r["Reg"]) for r in res}))

    def poblar_despensa(self, lista_ingredientes):
        for widget in self.scroll_despensa.winfo_children():
            widget.destroy()

        for ing in lista_ingredientes:
            if ing not in self.vars_ingredientes:
                self.vars_ingredientes[ing] = ctk.StringVar(value="off")

            texto = ing.replace('_', ' ').capitalize()
            chk = ctk.CTkCheckBox(
                self.scroll_despensa, text=texto,
                variable=self.vars_ingredientes[ing], onvalue=ing, offvalue="off",
                fg_color="#ff5c5c", hover_color="#ff5c5c", font=("Arial", 12)
            )
            chk.pack(pady=4, padx=5, anchor="w")

    def filtrar_lista_despensa(self, event=None):
        filtro = self.entry_buscar_ingrediente.get().strip().lower().replace(' ', '_')
        filtrados = [i for i in self.todos_ingredientes if filtro in i]
        self.poblar_despensa(filtrados)

    def limpiar_filtros(self):
        self.entry_buscar_nombre.delete(0, "end")
        self.entry_buscar_ingrediente.delete(0, "end")
        self.combo_region.set("Todas las regiones")
        self.combo_tiempo.set("Cualquier tiempo")
        self.var_opcion_suave.set("off")
        for var in self.vars_ingredientes.values():
            var.set("off")
        self.poblar_despensa(self.todos_ingredientes)
        self.ejecutar_consulta()

    def ejecutar_consulta(self):
        # Leer valores de la UI
        busqueda_nombre = self.entry_buscar_nombre.get().strip().lower().replace(' ', '_')
        region_sel = self.combo_region.get()
        texto_tiempo = self.combo_tiempo.get()
        solo_suave = (self.var_opcion_suave.get() == "on")
        ingredientes_elegidos = [ing for ing, var in self.vars_ingredientes.items() if var.get() != "off"]

        # Mapear tiempo maximo
        if "30" in texto_tiempo:
            tiempo_max = 30
        elif "60" in texto_tiempo:
            tiempo_max = 60
        elif "120" in texto_tiempo:
            tiempo_max = 120
        else:
            tiempo_max = 9999

        # Consultar a Prolog
        if solo_suave:
            # Usa la regla combinada: opcion_suave_y_rapida(Platillo, TiempoMax)
            raw = self.conector.hacer_consulta(f"opcion_suave_y_rapida(Platillo, {tiempo_max})")
            candidatos = {str(r["Platillo"]) for r in raw}
        else:
            raw = self.conector.hacer_consulta(f"receta_rapida(Platillo, {tiempo_max})")
            candidatos = {str(r["Platillo"]) for r in raw}

        # Filtrar por Region usando la regla platillo_de_region(Platillo, Region)
        if region_sel != "Todas las regiones":
            region_atomo = region_sel.lower().replace(' ', '_')
            raw_reg = self.conector.hacer_consulta(f"platillo_de_region(Platillo, {region_atomo})")
            de_region = {str(r["Platillo"]) for r in raw_reg}
            candidatos = candidatos.intersection(de_region)

        # Filtrar por ingredientes seleccionados en "Mi Despensa"
        for ing in ingredientes_elegidos:
            raw_ing = self.conector.hacer_consulta(f"ingrediente(Platillo, {ing})")
            con_ing = {str(r["Platillo"]) for r in raw_ing}
            candidatos = candidatos.intersection(con_ing)

        # 3. Armar los detalles completos de los platillos que pasaron todos los filtros
        resultados_finales = []
        for platillo in sorted(list(candidatos)):
            if busqueda_nombre and busqueda_nombre not in platillo:
                continue

            det = self.conector.hacer_consulta(
                f"detalle_receta({platillo}, Tipo, Region, Picante, Tiempo, Ing)"
            )
            if det:
                ingredientes_platillo = sorted(list({str(d["Ing"]) for d in det}))
                resultados_finales.append({
                    "Platillo": platillo,
                    "Tipo": str(det[0]["Tipo"]),
                    "Region": str(det[0]["Region"]),
                    "Picante": str(det[0]["Picante"]),
                    "Tiempo": det[0]["Tiempo"],
                    "Ingredientes": ingredientes_platillo
                })

        self.actualizar_tarjetas(resultados_finales)

    def actualizar_tarjetas(self, resultados):
        for widget in self.grid_recetas.winfo_children():
            widget.destroy()

        self.lbl_contador.configure(text=f"Recetas Recomendadas ({len(resultados)})")

        if not resultados:
            ctk.CTkLabel(
                self.grid_recetas,
                text="Ningun platillo cumple con todos esos filtros \nPrueba desmarcando algun ingrediente o subiendo el tiempo.",
                font=("Arial", 15), text_color="#a0aab2"
            ).grid(row=0, column=0, columnspan=3, pady=60)
            return

        fila, columna = 0, 0
        for receta in resultados:
            tarjeta = TarjetaReceta(
                master=self.grid_recetas,
                receta=receta,
                comando_click=lambda r=receta: VentanaDetalles(self, r)
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