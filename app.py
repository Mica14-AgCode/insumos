import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(
    page_title="Sistema de Gestión de Agroquímicos",
    page_icon="🌱",
    layout="wide"
)

# Función para convertir "s/d" a NaN
def convert_sd_to_nan(value):
    if isinstance(value, str) and value.lower() == 's/d':
        return np.nan
    return value

# Carga de datos iniciales
@st.cache_data
def load_initial_data():
    # [mantener todos los datos de insumos como está]
    # usando las categorías correctas como me proporcionaste
    
    # Semillas
    semillas = [
        {"tipo": "SEMILLA", "producto": "GIRASOL HIBRIDO", "principio_activo": "Germoplasma híbrido", "precio": 200.0, "unidad": "US$/bolsa"},
        {"tipo": "SEMILLA", "producto": "GIRASOL HIBRIDO CL", "principio_activo": "Germoplasma híbrido resistente a imidazolinonas", "precio": 243.0, "unidad": "US$/bolsa"},
        {"tipo": "SEMILLA", "producto": "MAIZ VT3P", "principio_activo": "Germoplasma híbrido tecnología VT3Pro", "precio": 193.0, "unidad": "US$/bolsa"},
        {"tipo": "SEMILLA", "producto": "MAIZ Hibrido", "principio_activo": "Germoplasma híbrido", "precio": 147.0, "unidad": "US$/bolsa"},
        {"tipo": "SEMILLA", "producto": "MAIZ VIPTERA3", "principio_activo": "Germoplasma híbrido tecnología Viptera", "precio": 175.0, "unidad": "US$/bolsa"},
        {"tipo": "SEMILLA", "producto": "MAIZ MG/RR2", "principio_activo": "Germoplasma híbrido con tecnología MG/RR2", "precio": 175.0, "unidad": "US$/bolsa"},
        {"tipo": "SEMILLA", "producto": "MAIZ MG CL", "principio_activo": "Germoplasma híbrido con tecnología MG CL", "precio": 162.0, "unidad": "US$/bolsa"},
        {"tipo": "SEMILLA", "producto": "SOJA RR", "principio_activo": "Germoplasma con tecnología RR", "precio": 0.72, "unidad": "US$/kg"},
        {"tipo": "SEMILLA", "producto": "SORGO GRAN.HIBR.", "principio_activo": "Germoplasma híbrido granífero", "precio": 8.30, "unidad": "US$/kg"},
        {"tipo": "SEMILLA", "producto": "SORGO GRAN. IG", "principio_activo": "Germoplasma granífero IG", "precio": 9.40, "unidad": "US$/kg"},
        {"tipo": "SEMILLA", "producto": "TRIGO FISCALIZADO", "principio_activo": "Germoplasma fiscalizado", "precio": 0.46, "unidad": "US$/kg"},
    ]
    
    # Herbicidas (incluyendo los productos que estaban mal categorizados)
    herbicidas = [
        {"tipo": "HERBICIDA", "producto": "2,4-D etilhexilico 97%", "principio_activo": "Ácido 2,4-diclorofenoxiacético", "precio": 6.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "2,4 D AMINA 50%", "principio_activo": "Ácido 2,4-diclorofenoxiacético", "precio": 4.3, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "2,4 DB 100%", "principio_activo": "Ácido 4-(2,4-diclorofenoxi)butírico", "precio": 13.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "2,4D PLUS", "principio_activo": "Ácido 2,4-diclorofenoxiacético plus", "precio": 4.5, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ACETOCLOR c/antídoto", "principio_activo": "Acetoclor con antídoto", "precio": 8.2, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ACURON UNO", "principio_activo": "Mezcla de herbicidas", "precio": 39.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ADENGO", "principio_activo": "Tiencarbazon-metil + Isoxaflutole", "precio": 103.8, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ATECTRA BV", "principio_activo": "Dicamba", "precio": 12.6, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ATRAZINA 50", "principio_activo": "Atrazina", "precio": 5.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ATRAZINA 90 WG", "principio_activo": "Atrazina", "precio": 8.5, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "AUTHORITY", "principio_activo": "Sulfentrazone", "precio": 23.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "AXIAL PLUS", "principio_activo": "Pinoxaden", "precio": 45.5, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "BANVEL", "principio_activo": "Dicamba", "precio": 11.1, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "BASAGRAN 60", "principio_activo": "Bentazon", "precio": 28.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "BICEP-PACK GOLD", "principio_activo": "S-metolacloro + Atrazina", "precio": 124.0, "unidad": "US$/pack"},
        {"tipo": "HERBICIDA", "producto": "BRODAL", "principio_activo": "Diflufenican", "precio": 34.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "BROMOTRIL", "principio_activo": "Bromoxinil", "precio": 20.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "CLEARSOL DF p/12 has", "principio_activo": "Imazapir", "precio": 150.0, "unidad": "US$/pack"},
        {"tipo": "HERBICIDA", "producto": "CONVEY", "principio_activo": "Flumetsulam + Diclosulam", "precio": 330.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "DASEN", "principio_activo": "Herbicida post-emergente", "precio": 40.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "DINAMIC 70 WG", "principio_activo": "Amicarbazone", "precio": 37.0, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "DUAL GOLD", "principio_activo": "S-metolacloro", "precio": 7.7, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "EGEMON", "principio_activo": "Mezcla de herbicidas", "precio": 11.5, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ELEVORE", "principio_activo": "Halauxifen-metil", "precio": 175.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "EQUIP WG pack p/ 5 ha", "principio_activo": "Foramsulfuron + Iodosulfuron", "precio": 228.0, "unidad": "US$/pack"},
        {"tipo": "HERBICIDA", "producto": "ENLIST", "principio_activo": "2,4-D colina", "precio": 6.00, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "FINESSE", "principio_activo": "Clorsulfuron + Metsulfuron", "precio": 330.0, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "FLOSIL", "principio_activo": "Fluroxipir", "precio": 10.1, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "FLUROCLORIDONA 25%", "principio_activo": "Flurocloridona", "precio": 18.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "GALANT HL", "principio_activo": "Haloxifop-R-metil éster", "precio": 22.0, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "GALANT RLPU", "principio_activo": "Haloxifop-R-metil éster", "precio": 10.0, "unidad": "US$/bolsa"},
        {"tipo": "HERBICIDA", "producto": "GALANT MAX", "principio_activo": "Haloxifop-R-metil éster", "precio": 43.0, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "GEMMIT TOP", "principio_activo": "Haloxifop-R-metil éster", "precio": 30.0, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "GESAGARD 50 FW", "principio_activo": "Prometrina", "precio": 10.4, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "GLIFOSATO 54%", "principio_activo": "N-(fosfonometil)glicina", "precio": 4.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "GLIFOMAX GS", "principio_activo": "N-(fosfonometil)glicina", "precio": 5.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "GLIFOPAMPA", "principio_activo": "N-(fosfonometil)glicina", "precio": 3.8, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "GLIFO TOP", "principio_activo": "N-(fosfonometil)glicina", "precio": 6.1, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "GUARDIAN", "principio_activo": "Acetoclor", "precio": 7.4, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "HARNESS", "principio_activo": "Acetoclor", "precio": 7.1, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "HEAT", "principio_activo": "Saflufenacil", "precio": 325.0, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "HUSSAR OD PLUS", "principio_activo": "Iodosulfuron + Mefenpir", "precio": 366.2, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "INTERFIELD p/5 has", "principio_activo": "Imazetapir + Imazapir", "precio": 108.0, "unidad": "US$/pack"},
        {"tipo": "HERBICIDA", "producto": "KATRIN (p/10 has)", "principio_activo": "Cletodim", "precio": 98.0, "unidad": "US$/pack"},
        {"tipo": "HERBICIDA", "producto": "LAUDIS", "principio_activo": "Tembotrione", "precio": 122.2, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "LIGATE", "principio_activo": "Rimsulfuron + Tifensulfuron", "precio": 195.0, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "LONTREL", "principio_activo": "Clopiralid", "precio": 37.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "M.C.P.A. 25%", "principio_activo": "MCPA", "precio": 4.80, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "MERIT WG pack p/ 66 ha", "principio_activo": "Metsulfuron-metil", "precio": 1230, "unidad": "US$/pack"},
        {"tipo": "HERBICIDA", "producto": "METSULFURON METIL 60%", "principio_activo": "Metsulfuron-metil", "precio": 39.00, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "PACTO", "principio_activo": "Flumioxazin", "precio": 390.0, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "PARAQUAT", "principio_activo": "Paraquat", "precio": 2.8, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "PEAK PACK L (p/20 has)", "principio_activo": "Prosulfuron + Dicamba", "precio": 132.0, "unidad": "US$/pack"},
        {"tipo": "HERBICIDA", "producto": "PIVOT H", "principio_activo": "Imazetapir", "precio": 6.2, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "PRESIDE", "principio_activo": "Flumetsulam", "precio": 29.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "PRODIGIO 60", "principio_activo": "Mezcla de herbicidas", "precio": 28.1, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "PUMA EXTRA", "principio_activo": "Fenoxaprop-etil", "precio": 27.2, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ROUNDUP FG", "principio_activo": "Glifosato", "precio": 7.6, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ROUNDUP FULL II", "principio_activo": "Glifosato", "precio": 6.1, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ROUNDUP CONTROLMAX", "principio_activo": "Glifosato", "precio": 7.73, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "SELECT", "principio_activo": "Cletodim", "precio": 6.40, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "SENCOREX X10", "principio_activo": "Metribuzin", "precio": 20.4, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "SPIDER", "principio_activo": "Diclosulam", "precio": 275.0, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "STAGGER", "principio_activo": "Cletodim", "precio": 46.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "STARANE XTRA", "principio_activo": "Fluroxipir", "precio": 26.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "SULFOSATO Touchdown", "principio_activo": "Glifosato", "precio": 4.3, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "TEXARO", "principio_activo": "Diclosulam + Halauxifen", "precio": 385.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "TITUS 25 WG", "principio_activo": "Rimsulfuron", "precio": 230.0, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "TOP GROUND (p/20 has)", "principio_activo": "Picloram + Fluroxipir", "precio": 340.0, "unidad": "US$/pack"},
        {"tipo": "HERBICIDA", "producto": "TORDON 24 K", "principio_activo": "Picloram", "precio": 10.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "TRIFLURALINA-premerge", "principio_activo": "Trifluralina", "precio": 16.5, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "UP STAGE EC 50", "principio_activo": "Metazaclor", "precio": 17.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "YAMATO TOP", "principio_activo": "Mezcla de herbicidas", "precio": 94.0, "unidad": "US$/litro"}
    ]
    
    # Resto de categorías igual que en tu código original
    # ...
    
    # Continuar con el resto igual que en tu código original

# Función para normalizar texto para búsqueda (mejorada)
def normalizar_texto(texto):
    import unicodedata
    import re
    if isinstance(texto, str):
        # Convertir a minúsculas
        texto = texto.lower()
        # Eliminar acentos
        texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')
        # Eliminar caracteres especiales pero mantener espacios para búsquedas más flexibles
        texto = re.sub(r'[^a-z0-9\s]', '', texto)
        # Reemplazar múltiples espacios por uno solo
        texto = re.sub(r'\s+', ' ', texto).strip()
        # Manejar casos especiales como 2,4-D, 24D, etc.
        texto = texto.replace("24d", "24 d").replace("24 d", "2 4 d")
    return texto

# Función para obtener sugerencias para el dropdown estilo Google
def obtener_sugerencias(df, texto, max_sugerencias=10):
    if not texto or len(texto) < 2:
        return []
    
    # Normalizar el texto de búsqueda
    texto_norm = normalizar_texto(texto)
    
    # Normalizar las columnas del DataFrame para la búsqueda
    df['producto_norm'] = df['producto'].apply(normalizar_texto)
    df['principio_activo_norm'] = df['principio_activo'].apply(lambda x: normalizar_texto(x) if pd.notna(x) else '')
    
    # Calcular puntuación para cada producto
    def calcular_puntuacion(row):
        puntuacion = 0
        
        # Coincidencia exacta
        if row['producto_norm'] == texto_norm:
            puntuacion += 100
        if row['principio_activo_norm'] == texto_norm:
            puntuacion += 90
            
        # Coincidencia al inicio del nombre
        if row['producto_norm'].startswith(texto_norm):
            puntuacion += 80
        if row['principio_activo_norm'].startswith(texto_norm):
            puntuacion += 70
        
        # Coincidencia parcial
        if texto_norm in row['producto_norm']:
            puntuacion += 60
        if texto_norm in row['principio_activo_norm']:
            puntuacion += 50
        
        # Coincidencia por tokens (palabras)
        tokens_busqueda = texto_norm.split()
        tokens_producto = row['producto_norm'].split()
        tokens_principio = row['principio_activo_norm'].split()
        
        for token in tokens_busqueda:
            if token in tokens_producto:
                puntuacion += 20
            if token in tokens_principio:
                puntuacion += 15
        
        return puntuacion
    
    # Aplicar puntuación
    df['puntuacion'] = df.apply(calcular_puntuacion, axis=1)
    
    # Filtrar resultados con puntuación > 0 y ordenar
    resultados = df[df['puntuacion'] > 0].sort_values('puntuacion', ascending=False)
    
    # Limpiar columnas temporales
    df.drop(['producto_norm', 'principio_activo_norm', 'puntuacion'], axis=1, inplace=True)
    
    if resultados.empty:
        return []
    
    # Formato: sólo el nombre del producto (como en Google)
    sugerencias = []
    for _, row in resultados.head(max_sugerencias).iterrows():
        sugerencias.append({
            "id": int(row['id']),
            "texto": row['producto'],
            "tipo": row['tipo']
        })
    
    return sugerencias

# Agregar estilos CSS para el dropdown de autocompletado estilo Google
def set_autocomplete_styles():
    return """
    <style>
    /* Estilos generales para tema oscuro */
    body {
        background-color: #1E1E1E;
        color: #E0E0E0;
    }
    
    /* Contenedor de búsqueda */
    .search-container {
        position: relative;
        width: 100%;
        margin-bottom: 20px;
    }
    
    /* Input de búsqueda */
    .search-input {
        width: 100%;
        padding: 12px 15px;
        font-size: 16px;
        border: 1px solid #444;
        border-radius: 8px;
        background-color: #333;
        color: white;
        outline: none;
    }
    
    .search-input:focus {
        border-color: #FF8C00;
        box-shadow: 0 0 0 2px rgba(255, 140, 0, 0.3);
    }
    
    /* Dropdown de autocompletado */
    .autocomplete-items {
        position: absolute;
        border-radius: 0 0 8px 8px;
        z-index: 99;
        top: 100%;
        left: 0;
        right: 0;
        background-color: #333;
        border: 1px solid #444;
        border-top: none;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        max-height: 300px;
        overflow-y: auto;
    }
    
    .autocomplete-item {
        padding: 12px 15px;
        cursor: pointer;
        display: flex;
        align-items: center;
        transition: background-color 0.2s;
        border-bottom: 1px solid #444;
    }
    
    .autocomplete-item:last-child {
        border-bottom: none;
        border-radius: 0 0 8px 8px;
    }
    
    .autocomplete-item:hover {
        background-color: #444;
    }
    
    .autocomplete-item-icon {
        margin-right: 10px;
        color: #999;
        width: 20px;
    }
    
    .autocomplete-item-text {
        flex-grow: 1;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        color: #E0E0E0;
    }
    
    .autocomplete-item-type {
        color: #999;
        font-size: 12px;
        margin-left: 10px;
        white-space: nowrap;
    }
    
    /* Info del producto seleccionado */
    .product-info {
        background-color: #333;
        border-radius: 8px;
        padding: 20px;
        margin-top: 20px;
        border-left: 4px solid #FF8C00;
    }
    
    .product-title {
        font-size: 20px;
        font-weight: bold;
        color: #FF8C00;
        margin-bottom: 15px;
    }
    
    .product-detail {
        display: flex;
        justify-content: space-between;
        border-bottom: 1px solid #444;
        padding: 8px 0;
    }
    
    .product-detail-label {
        font-weight: 500;
        color: #999;
    }
    
    .product-detail-value {
        color: white;
    }
    </style>
    """

# Crear el componente de autocompletado estilo Google
def crear_componente_autocompletado(df, key="buscador"):
    # Inicializar el estado de sesión para el autocompletado
    if f"texto_busqueda_{key}" not in st.session_state:
        st.session_state[f"texto_busqueda_{key}"] = ""
    if f"producto_seleccionado_{key}" not in st.session_state:
        st.session_state[f"producto_seleccionado_{key}"] = None
    
    # Aplicar estilos CSS
    st.markdown(set_autocomplete_styles(), unsafe_allow_html=True)
    
    # Crear contenedor para el componente de búsqueda
    st.markdown(f"<div class='search-container' id='search-container-{key}'>", unsafe_allow_html=True)
    
    # Campo de búsqueda personalizado con HTML
    st.markdown(
        f"""
        <input type="text" id="search-input-{key}" class="search-input" 
               placeholder="Buscar producto o principio activo..." 
               value="{st.session_state[f'texto_busqueda_{key}']}">
        """, 
        unsafe_allow_html=True
    )
    
    # Inicializar el contenedor para las sugerencias de autocompletado
    if st.session_state[f"texto_busqueda_{key}"]:
        sugerencias = obtener_sugerencias(df, st.session_state[f"texto_busqueda_{key}"])
        
        if sugerencias:
            # Crear HTML para el dropdown de sugerencias
            suggestions_html = f"""
            <div class="autocomplete-items" id="autocomplete-{key}">
            """
            
            for sugerencia in sugerencias:
                suggestions_html += f"""
                <div class="autocomplete-item" data-id="{sugerencia['id']}" data-text="{sugerencia['texto']}">
                    <div class="autocomplete-item-icon">
                        <i class="fas fa-search"></i>
                    </div>
                    <div class="autocomplete-item-text">{sugerencia['texto']}</div>
                    <div class="autocomplete-item-type">{sugerencia['tipo']}</div>
                </div>
                """
            
            suggestions_html += "</div>"
            
            # Renderizar el dropdown
            st.markdown(suggestions_html, unsafe_allow_html=True)
    
    # Cerrar el contenedor de búsqueda
    st.markdown("</div>", unsafe_allow_html=True)
    
    # JavaScript para el manejo del autocompletado
    js_code = f"""
    <script>
    // Función para manejar la entrada en el campo de búsqueda
    const searchInput = document.getElementById('search-input-{key}');
    
    if (searchInput) {{
        searchInput.addEventListener('input', function(e) {{
            const searchText = e.target.value;
            
            // Enviar el texto de búsqueda a Streamlit
            window.parent.postMessage({{
                type: "streamlit:setComponentValue",
                value: {{
                    type: "text_update",
                    key: "{key}",
                    text: searchText
                }}
            }}, "*");
        }});
    }}
    
    // Capturar clics en los elementos de autocompletado
    document.addEventListener('click', function(e) {{
        const item = e.target.closest('.autocomplete-item');
        if (item) {{
            const productId = item.getAttribute('data-id');
            const productText = item.getAttribute('data-text');
            
            // Actualizar el valor en el campo de búsqueda
            if (searchInput) {{
                searchInput.value = productText;
            }}
            
            // Enviar mensaje a Streamlit para procesar la selección
            window.parent.postMessage({{
                type: "streamlit:setComponentValue",
                value: {{
                    type: "product_selected",
                    key: "{key}",
                    id: Number(productId),
                    text: productText
                }}
            }}, "*");
        }}
    }});
    
    // Cerrar el dropdown si se hace clic fuera
    document.addEventListener('click', function(e) {{
        if (!e.target.closest('.search-container') && !e.target.closest('.autocomplete-items')) {{
            const dropdown = document.getElementById('autocomplete-{key}');
            if (dropdown) {{
                dropdown.style.display = 'none';
            }}
        }}
    }});
    </script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    """
    
    # Renderizar JavaScript
    st.markdown(js_code, unsafe_allow_html=True)
    
    # Componente HTML para recibir eventos
    component_value = components.html(
        f"""
        <div id="receiver-{key}" style="display:none;"></div>
        """, 
        height=0
    )
    
    # Procesar eventos del componente
    if component_value:
        if isinstance(component_value, dict):
            if component_value.get('type') == 'text_update' and component_value.get('key') == key:
                st.session_state[f"texto_busqueda_{key}"] = component_value.get('text', '')
                st.experimental_rerun()
            
            elif component_value.get('type') == 'product_selected' and component_value.get('key') == key:
                st.session_state[f"producto_seleccionado_{key}"] = component_value.get('id')
                st.session_state[f"texto_busqueda_{key}"] = component_value.get('text', '')
                st.experimental_rerun()
    
    # Devolver el estado actual
    return {
        "texto": st.session_state[f"texto_busqueda_{key}"],
        "producto_id": st.session_state[f"producto_seleccionado_{key}"]
    }

# Función para mostrar la información del producto
def mostrar_informacion_producto(df, producto_id):
    producto = df[df['id'] == producto_id].iloc[0]
    
    # Mostrar información del producto con estilo mejorado
    st.markdown('<div class="product-info">', unsafe_allow_html=True)
    st.markdown(f'<div class="product-title">{producto["producto"]}</div>', unsafe_allow_html=True)
    
    # Tipo
    st.markdown(
        f'<div class="product-detail"><span class="product-detail-label">Tipo:</span><span class="product-detail-value">{producto["tipo"]}</span></div>',
        unsafe_allow_html=True
    )
    
    # Principio activo
    st.markdown(
        f'<div class="product-detail"><span class="product-detail-label">Principio activo:</span><span class="product-detail-value">{producto["principio_activo"]}</span></div>',
        unsafe_allow_html=True
    )
    
    # Precio
    precio = "s/d" if pd.isna(producto['precio']) else f"{producto['precio']:.2f}"
    st.markdown(
        f'<div class="product-detail"><span class="product-detail-label">Precio:</span><span class="product-detail-value">{precio} {producto["unidad"]}</span></div>',
        unsafe_allow_html=True
    )
    
    # Fecha
    st.markdown(
        f'<div class="product-detail"><span class="product-detail-label">Última actualización:</span><span class="product-detail-value">{producto["fecha"]}</span></div>',
        unsafe_allow_html=True
    )
    
    st.markdown('</div>', unsafe_allow_html=True)

# Función principal
def main():
    # Cargar datos
    df = load_initial_data()
    
    # Título de la aplicación
    st.title("Sistema de Gestión de Agroquímicos")
    st.write("Fecha de actualización: 05/05/2025")
    
    # Crear pestañas
    tab1, tab2, tab3, tab4 = st.tabs(["Consulta de Precios", "Lista de Productos", "Agregar Producto", "Por Categoría"])
    
    # Pestaña 1: Consulta de Precios
    with tab1:
        st.header("Consulta de Precios")
        
        # Componente de búsqueda estilo Google
        busqueda_resultado = crear_componente_autocompletado(df)
        
        # Mostrar el producto seleccionado
        if busqueda_resultado["producto_id"]:
            # Mostrar la información del producto
            mostrar_informacion_producto(df, busqueda_resultado["producto_id"])
        
        # Si hay búsqueda pero no hay producto seleccionado, mostrar resultados completos
        elif busqueda_resultado["texto"]:
            # Buscar todos los productos que coincidan con la búsqueda
            producto_norm = normalizar_texto(busqueda_resultado["texto"])
            resultados = df[
                df['producto'].apply(lambda x: normalizar_texto(x)).str.contains(producto_norm) |
                df['principio_activo'].apply(lambda x: normalizar_texto(str(x)) if pd.notna(x) else "").str.contains(producto_norm)
            ]
            
            if not resultados.empty:
                st.markdown("<h3 style='margin-top: 30px;'>Resultados de la búsqueda</h3>", unsafe_allow_html=True)
                
                # Mostrar tabla con resultados
                st.dataframe(
                    resultados[['tipo', 'producto', 'principio_activo', 'precio', 'unidad']],
                    column_config={
                        "tipo": "Tipo",
                        "producto": "Producto",
                        "principio_activo": "Principio Activo",
                        "precio": st.column_config.NumberColumn("Precio", format="%.2f"),
                        "unidad": "Unidad"
                    },
                    use_container_width=True,
                    hide_index=True
                )
        
        # Agregar instrucciones claras
        with st.expander("Consejos para la búsqueda"):
            st.markdown("""
            - Puedes buscar por nombre de producto o principio activo
            - La búsqueda funciona aunque escribas solo una parte del nombre
            - Es flexible con los acentos y mayúsculas
            - Ejemplos:
                - "2,4D" encontrará todos los productos con 2,4-D
                - "glifo" encontrará todos los productos con glifosato
                - "ciperme" encontrará Cipermetrina
            """)
    
    # Contenido de las otras pestañas sigue igual que en tu código original
    # ...

    # Aplicar estilo CSS personalizado
    st.markdown("""
    <style>
    .main {
        background-color: #1E1E1E;
        color: #E0E0E0;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #FF8C00;
    }
    
    /* Estilos para pestañas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        background-color: #2D2D2D;
        border-radius: 8px;
        padding: 5px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 4px;
        padding: 10px 16px;
        color: #E0E0E0;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #FF8C00;
        color: white;
    }
    
    /* Botones */
    .stButton button {
        border-radius: 5px;
        background-color: #FF8C00;
        color: white;
        border: none;
        padding: 10px 15px;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
