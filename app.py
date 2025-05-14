import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np

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
    import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np

# Configuración básica de la página sin estilización externa
st.set_page_config(
    page_title="Sistema de Gestión de Agroquímicos",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Aplicar CSS básico sin depender de recursos externos
st.markdown("""
<style>
    /* Estilos básicos que no requieren carga externa */
    .main {
        background-color: #1E1E1E;
        color: #E0E0E0;
    }
    
    h1, h2, h3 {
        color: #FF8C00;
    }
    
    /* Estilos para el contenedor de autocompletado */
    .autocomplete-container {
        position: relative;
        width: 100%;
    }
    
    .autocomplete-items {
        position: absolute;
        background-color: #333;
        border: 1px solid #555;
        z-index: 99;
        width: 100%;
        border-radius: 0 0 8px 8px;
    }
    
    .autocomplete-item {
        padding: 10px;
        cursor: pointer;
        border-bottom: 1px solid #444;
    }
    
    .autocomplete-item:hover {
        background-color: #444;
    }
</style>
""", unsafe_allow_html=True)

# El resto del código con implementación simplificada del autocompletado

# Carga de datos iniciales
@st.cache_data
def load_initial_data():
    # Semillas
    semillas = [
        {"tipo": "SEMILLA", "producto": "GIRASOL HIBRIDO", "droga": "Germoplasma híbrido", "precio": 200.0, "unidad": "US$/bolsa"},
        {"tipo": "SEMILLA", "producto": "GIRASOL HIBRIDO CL", "droga": "Germoplasma híbrido resistente a imidazolinonas", "precio": 243.0, "unidad": "US$/bolsa"},
        {"tipo": "SEMILLA", "producto": "MAIZ VT3P", "droga": "Germoplasma híbrido tecnología VT3Pro", "precio": 193.0, "unidad": "US$/bolsa"},
        {"tipo": "SEMILLA", "producto": "MAIZ Hibrido", "droga": "Germoplasma híbrido", "precio": 147.0, "unidad": "US$/bolsa"},
        {"tipo": "SEMILLA", "producto": "MAIZ VIPTERA3", "droga": "Germoplasma híbrido tecnología Viptera", "precio": 175.0, "unidad": "US$/bolsa"},
        {"tipo": "SEMILLA", "producto": "MAIZ MG/RR2", "droga": "Germoplasma híbrido con tecnología MG/RR2", "precio": 175.0, "unidad": "US$/bolsa"},
        {"tipo": "SEMILLA", "producto": "MAIZ MG CL", "droga": "Germoplasma híbrido con tecnología MG CL", "precio": 162.0, "unidad": "US$/bolsa"},
        {"tipo": "SEMILLA", "producto": "SOJA RR", "droga": "Germoplasma con tecnología RR", "precio": 0.72, "unidad": "US$/kg"},
        {"tipo": "SEMILLA", "producto": "SORGO GRAN.HIBR.", "droga": "Germoplasma híbrido granífero", "precio": 8.30, "unidad": "US$/kg"},
        {"tipo": "SEMILLA", "producto": "SORGO GRAN. IG", "droga": "Germoplasma granífero IG", "precio": 9.40, "unidad": "US$/kg"},
        {"tipo": "SEMILLA", "producto": "TRIGO FISCALIZADO", "droga": "Germoplasma fiscalizado", "precio": 0.46, "unidad": "US$/kg"},
        {"tipo": "SEMILLA", "producto": "GALANT HL", "droga": "Haloxifop-R-metil éster", "precio": 22.0, "unidad": "US$/kg"},
        {"tipo": "SEMILLA", "producto": "GALANT RLPU", "droga": "Haloxifop-R-metil éster", "precio": 10.0, "unidad": "US$/bolsa"},
        {"tipo": "SEMILLA", "producto": "GALANT MAX", "droga": "Haloxifop-R-metil éster", "precio": 43.0, "unidad": "US$/kg"},
        {"tipo": "SEMILLA", "producto": "GEMMIT TOP", "droga": "Haloxifop-R-metil éster", "precio": 30.0, "unidad": "US$/kg"},
        {"tipo": "SEMILLA", "producto": "GESAGARD 50 FW", "droga": "Prometrina", "precio": 10.4, "unidad": "US$/litro"},
    ]
    
    # Herbicidas
    herbicidas = [
        {"tipo": "HERBICIDA", "producto": "2,4-D etilhexilico 97%", "droga": "Ácido 2,4-diclorofenoxiacético", "precio": 6.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "2,4 D AMINA 50%", "droga": "Ácido 2,4-diclorofenoxiacético", "precio": 4.3, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "2,4 DB 100%", "droga": "Ácido 4-(2,4-diclorofenoxi)butírico", "precio": 13.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "2,4D PLUS", "droga": "Ácido 2,4-diclorofenoxiacético plus", "precio": 4.5, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ACETOCLOR c/antídoto", "droga": "Acetoclor con antídoto", "precio": 8.2, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ACURON UNO", "droga": "Mezcla de herbicidas", "precio": 39.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ADENGO", "droga": "Tiencarbazon-metil + Isoxaflutole", "precio": 103.8, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ATECTRA BV", "droga": "Dicamba", "precio": 12.6, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ATRAZINA 50", "droga": "Atrazina", "precio": 5.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ATRAZINA 90 WG", "droga": "Atrazina", "precio": 8.5, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "AUTHORITY", "droga": "Sulfentrazone", "precio": 23.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "AXIAL PLUS", "droga": "Pinoxaden", "precio": 45.5, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "BANVEL", "droga": "Dicamba", "precio": 11.1, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "BASAGRAN 60", "droga": "Bentazon", "precio": 28.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "BICEP-PACK GOLD", "droga": "S-metolacloro + Atrazina", "precio": 124.0, "unidad": "US$/pack"},
        {"tipo": "HERBICIDA", "producto": "BRODAL", "droga": "Diflufenican", "precio": 34.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "BROMOTRIL", "droga": "Bromoxinil", "precio": 20.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "CLEARSOL DF p/12 has", "droga": "Imazapir", "precio": 150.0, "unidad": "US$/pack"},
        {"tipo": "HERBICIDA", "producto": "CONVEY", "droga": "Flumetsulam + Diclosulam", "precio": 330.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "DASEN", "droga": "Herbicida post-emergente", "precio": 40.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "DINAMIC 70 WG", "droga": "Amicarbazone", "precio": 37.0, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "DUAL GOLD", "droga": "S-metolacloro", "precio": 7.7, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "EGEMON", "droga": "Mezcla de herbicidas", "precio": 11.5, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ELEVORE", "droga": "Halauxifen-metil", "precio": 175.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "EQUIP WG pack p/ 5 ha", "droga": "Foramsulfuron + Iodosulfuron", "precio": 228.0, "unidad": "US$/pack"},
        {"tipo": "HERBICIDA", "producto": "ENLIST", "droga": "2,4-D colina", "precio": 6.00, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "FINESSE", "droga": "Clorsulfuron + Metsulfuron", "precio": 330.0, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "FLOSIL", "droga": "Fluroxipir", "precio": 10.1, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "FLUROCLORIDONA 25%", "droga": "Flurocloridona", "precio": 18.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "GLIFOSATO 54%", "droga": "N-(fosfonometil)glicina", "precio": 4.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "GLIFOMAX GS", "droga": "N-(fosfonometil)glicina", "precio": 5.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "GLIFOPAMPA", "droga": "N-(fosfonometil)glicina", "precio": 3.8, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "GLIFO TOP", "droga": "N-(fosfonometil)glicina", "precio": 6.1, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "GUARDIAN", "droga": "Acetoclor", "precio": 7.4, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "HARNESS", "droga": "Acetoclor", "precio": 7.1, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "HEAT", "droga": "Saflufenacil", "precio": 325.0, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "HUSSAR OD PLUS", "droga": "Iodosulfuron + Mefenpir", "precio": 366.2, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "INTERFIELD p/5 has", "droga": "Imazetapir + Imazapir", "precio": 108.0, "unidad": "US$/pack"},
        {"tipo": "HERBICIDA", "producto": "KATRIN (p/10 has)", "droga": "Cletodim", "precio": 98.0, "unidad": "US$/pack"},
        {"tipo": "HERBICIDA", "producto": "LAUDIS", "droga": "Tembotrione", "precio": 122.2, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "LIGATE", "droga": "Rimsulfuron + Tifensulfuron", "precio": 195.0, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "LONTREL", "droga": "Clopiralid", "precio": 37.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "M.C.P.A. 25%", "droga": "MCPA", "precio": 4.80, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "MERIT WG pack p/ 66 ha", "droga": "Metsulfuron-metil", "precio": 1230, "unidad": "US$/pack"},
        {"tipo": "HERBICIDA", "producto": "METSULFURON METIL 60%", "droga": "Metsulfuron-metil", "precio": 39.00, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "PACTO", "droga": "Flumioxazin", "precio": 390.0, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "PARAQUAT", "droga": "Paraquat", "precio": 2.8, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "PEAK PACK L (p/20 has)", "droga": "Prosulfuron + Dicamba", "precio": 132.0, "unidad": "US$/pack"},
        {"tipo": "HERBICIDA", "producto": "PIVOT H", "droga": "Imazetapir", "precio": 6.2, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "PRESIDE", "droga": "Flumetsulam", "precio": 29.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "PRODIGIO 60", "droga": "Mezcla de herbicidas", "precio": 28.1, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "PUMA EXTRA", "droga": "Fenoxaprop-etil", "precio": 27.2, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ROUNDUP FG", "droga": "Glifosato", "precio": 7.6, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ROUNDUP FULL II", "droga": "Glifosato", "precio": 6.1, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "ROUNDUP CONTROLMAX", "droga": "Glifosato", "precio": 7.73, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "SELECT", "droga": "Cletodim", "precio": 6.40, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "SENCOREX X10", "droga": "Metribuzin", "precio": 20.4, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "SPIDER", "droga": "Diclosulam", "precio": 275.0, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "STAGGER", "droga": "Cletodim", "precio": 46.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "STARANE XTRA", "droga": "Fluroxipir", "precio": 26.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "SULFOSATO Touchdown", "droga": "Glifosato", "precio": 4.3, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "TEXARO", "droga": "Diclosulam + Halauxifen", "precio": 385.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "TITUS 25 WG", "droga": "Rimsulfuron", "precio": 230.0, "unidad": "US$/kg"},
        {"tipo": "HERBICIDA", "producto": "TOP GROUND (p/20 has)", "droga": "Picloram + Fluroxipir", "precio": 340.0, "unidad": "US$/pack"},
        {"tipo": "HERBICIDA", "producto": "TORDON 24 K", "droga": "Picloram", "precio": 10.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "TRIFLURALINA-premerge", "droga": "Trifluralina", "precio": 16.5, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "UP STAGE EC 50", "droga": "Metazaclor", "precio": 17.0, "unidad": "US$/litro"},
        {"tipo": "HERBICIDA", "producto": "YAMATO TOP", "droga": "Mezcla de herbicidas", "precio": 94.0, "unidad": "US$/litro"}
    ]
    
    # Insecticidas
    insecticidas = [
        {"tipo": "INSECTICIDA", "producto": "ABAMECTINA 3,6%", "droga": "Abamectina", "precio": 12.5, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "ACEFATO 97%", "droga": "Acefato", "precio": 19.5, "unidad": "US$/kg"},
        {"tipo": "INSECTICIDA", "producto": "ALSYSTIN 48 SC", "droga": "Triflumuron", "precio": 86.3, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "AMPLIGO", "droga": "Clorantraniliprole + Lambda-cialotrina", "precio": 101.0, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "CLAP SC", "droga": "Insecticida biológico", "precio": np.nan, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "CORAGEN", "droga": "Clorantraniliprole", "precio": 150.0, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "CURYOM FIT UV", "droga": "Lufenuron + Profenofos", "precio": 173.3, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "CIPERMETRINA 25%", "droga": "Cipermetrina", "precio": 7.5, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "DECIS 5%", "droga": "Deltametrina", "precio": 5.5, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "DECIS FLOW", "droga": "Deltametrina", "precio": 94.6, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "DECIS FORTE 10%", "droga": "Deltametrina", "precio": 34.4, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "DIPEL DF", "droga": "Bacillus thuringiensis", "precio": 43.0, "unidad": "US$/kg"},
        {"tipo": "INSECTICIDA", "producto": "ENGEO", "droga": "Tiametoxam + Lambda-cialotrina", "precio": 25.4, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "EXALT SC", "droga": "Spinetoram", "precio": 248.0, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "EXPEDITION", "droga": "Acetamiprid + Bifentrin", "precio": 39.0, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "FASTAC DUO", "droga": "Alfa-cipermetrina + Acetamiprid", "precio": 25.0, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "FIGHTER PLUS", "droga": "Imidacloprid + Beta-ciflutrina", "precio": 83.5, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "INTREPID", "droga": "Metoxifenocide", "precio": 38.0, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "KARATE ZEON 25%", "droga": "Lambda-cialotrina", "precio": 44.6, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "SOLOMON", "droga": "Imidacloprid", "precio": 29.1, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "STARKLE (5,1 kg)", "droga": "Dinotefuran", "precio": 710, "unidad": "US$/pack"},
        {"tipo": "INSECTICIDA", "producto": "TRACER", "droga": "Spinosad", "precio": 254.0, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "PHIL LAMBDA 5%", "droga": "Lambda-cialotrina", "precio": 7.8, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "QUINTAL XTRA", "droga": "Clorpirifos + Cipermetrina", "precio": 83.0, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "TRANSFORM", "droga": "Sulfoxaflor", "precio": 234.5, "unidad": "US$/litro"}
    ]
    
    # Fungicidas
    fungicidas = [
        {"tipo": "FUNGICIDA", "producto": "ALLEGRO", "droga": "Kresoxim-metil", "precio": 26.0, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "AMISTAR XTRA", "droga": "Azoxistrobina + Ciproconazol", "precio": 24.9, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "ARACONAZOLE 43%", "droga": "Tebuconazole", "precio": 11.0, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "CARBENDAZIM 50%", "droga": "Carbendazim", "precio": 6.8, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "CINCHA", "droga": "Difenoconazole", "precio": 15.0, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "COMET", "droga": "Piraclostrobina", "precio": 60.0, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "CRIPTON", "droga": "Trifloxistrobina + Protioconazole", "precio": 32.01, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "CRIPTON XPRO", "droga": "Trifloxistrobina + Protioconazole + Bixafen", "precio": 54.32, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "MANCOZEB", "droga": "Mancozeb", "precio": 6.0, "unidad": "US$/kg"},
        {"tipo": "FUNGICIDA", "producto": "NATIVO SC 300", "droga": "Trifloxistrobina + Tebuconazole", "precio": np.nan, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "OPERA", "droga": "Piraclostrobina + Epoxiconazole", "precio": 23.0, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "ORQUESTA ULTRA", "droga": "Piraclostrobina + Epoxiconazole + Fluxapyroxad", "precio": 32.0, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "REFLECT XTRA", "droga": "Isopyrazam + Azoxistrobina", "precio": np.nan, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "SPHERE MAX", "droga": "Trifloxistrobina + Ciproconazol", "precio": 55.3, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "STINGER", "droga": "Azoxistrobina + Difenoconazole", "precio": 26.0, "unidad": "US$/litro"}
    ]
    
    # Fertilizantes
    fertilizantes = [
        {"tipo": "FERTILIZANTE", "producto": "AZUFRE GRANULADO", "droga": "Azufre elemental", "precio": 230, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "CLORURO DE POTASIO", "droga": "KCl", "precio": 490, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "FOSZINC", "droga": "Fósforo + Zinc", "precio": 980, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "FOSFATO DIAMONICO", "droga": "DAP", "precio": 870, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "FOSF MONOAMONICO", "droga": "MAP", "precio": 880, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "MAP AZUFRADO", "droga": "MAP + S", "precio": 690, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "NITR de AMONIO CALC.", "droga": "CAN", "precio": 525, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "SOLMIX N 28 - S 5,2", "droga": "Solución nitrogenada con azufre", "precio": 455, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "SOLMIX Zn (27-5-04 Zn)", "droga": "Solución con zinc", "precio": 490, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "SULFATO de AMONIO", "droga": "Sulfato de amonio", "precio": 450, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "SULFATO de CALCIO", "droga": "Sulfato de calcio", "precio": 326, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "SUPERFOSF. SIMPLE", "droga": "Superfosfato simple", "precio": 390, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "SUPERFOSF. TRIPLE", "droga": "Superfosfato triple", "precio": 700, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "U.A.N. 32", "droga": "Solución UAN", "precio": 490, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "UREA GRANULADA", "droga": "CO(NH₂)₂", "precio": 560, "unidad": "US$/tn"}
    ]
    
    # Curasemillas
    curasemillas = [
        {"tipo": "CURASEMILLA", "producto": "ACRONIS 2,5 lt", "droga": "Tiram + Carbendazim", "precio": 48.0, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "CHUCARO", "droga": "Tiametoxam + Tebuconazole + Fludioxonil", "precio": 94.1, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "CKC Liquid Soja", "droga": "Inoculante biológico", "precio": 3.5, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "CKC Rizoflo Premium Soj", "droga": "Inoculante premium", "precio": 3.6, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "CKC Pack Sistémico", "droga": "Inoculante + fungicida", "precio": 4.5, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "CKC Pack Soja Premium", "droga": "Inoculante premium", "precio": 7.5, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "CONFIDOR 70 WG", "droga": "Imidacloprid", "precio": 56.0, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "CREATE PACK FAST", "droga": "Clothianidin + Ciantraniliprole", "precio": 129.50, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "CRUISER PACK", "droga": "Tiametoxam + Fludioxonil + Metalaxil-M", "precio": 442.1, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "DIVIDEND", "droga": "Difenoconazole + Metalaxil-M", "precio": 11.1, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "DIVIDEND EXTRA", "droga": "Difenoconazole + Metalaxil-M + Sedaxane", "precio": 18.6, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "NITRAGIN CELL TECH ds", "droga": "Bradyrhizobium japonicum", "precio": 2.40, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "NITRAPACK", "droga": "Inoculante + protector", "precio": 3.7, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "PREMIS", "droga": "Triticonazole", "precio": 48.0, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "PUCARA", "droga": "Tiametoxam + Lambda-cialotrina", "precio": 107.67, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "SCENIC", "droga": "Fluoxastrobin + Protioconazole + Tebuconazole", "precio": 32.98, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "SISTIVA (p/4000 kg)", "droga": "Fluxapyroxad", "precio": 330.00, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "SUMI-EIGHT MT", "droga": "Diniconazole-M + Thiram", "precio": 29.0, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "VIBRANCE INTEGRAL", "droga": "Sedaxane + Difenoconazole + Metalaxil-M + Fludioxonil", "precio": 64.30, "unidad": "US$/dosis"}
    ]
    
    # Aceites y coadyuvantes
    aceites = [
        {"tipo": "ACEITE", "producto": "ACEITE METILADO", "droga": "Éster metílico de ácidos grasos", "precio": 3.0, "unidad": "US$/litro"},
        {"tipo": "ACEITE", "producto": "AJUSTE", "droga": "Aceite mineral parafinado", "precio": 45.0, "unidad": "US$/litro"},
        {"tipo": "ACEITE", "producto": "DASH MSO MAX", "droga": "Éster metílico de aceite de soja", "precio": 16.0, "unidad": "US$/litro"},
        {"tipo": "ACEITE", "producto": "RIZOSPRAY EXTREMO", "droga": "Tensioactivo siliconado", "precio": 18.5, "unidad": "US$/litro"},
        {"tipo": "ACEITE", "producto": "SULFATO de AMONIO lq", "droga": "Sulfato de amonio líquido", "precio": 1.3, "unidad": "US$/litro"}
    ]
    
    # Combinar todos los productos
    productos = semillas + herbicidas + insecticidas + fungicidas + fertilizantes + curasemillas + aceites
    
    # Crear dataframe y agregar fecha de actualización
    df = pd.DataFrame(productos)
    df['fecha'] = "05/05/2025"
    
    # Asegurar que el ID sea único
    df['id'] = range(1, len(df) + 1)
    
    return df

# Función para filtrar productos por tipo
def filtrar_por_tipo(df, tipo):
    if tipo == "TODOS":
        return df
    return df[df['tipo'] == tipo]

# Función para normalizar texto para búsqueda
def normalizar_texto(texto):
    import unicodedata
    import re
    if isinstance(texto, str):
        texto = texto.lower()
        texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')
        texto = re.sub(r'[^a-z0-9]', '', texto)
    return texto

# Función para buscar productos
def buscar_productos(df, busqueda):
    if not busqueda:
        return None
    
    # Normalizar la búsqueda
    busqueda_norm = normalizar_texto(busqueda)
    
    # Normalizar las columnas del DataFrame para la búsqueda
    df['producto_norm'] = df['producto'].apply(normalizar_texto)
    df['droga_norm'] = df['droga'].apply(lambda x: normalizar_texto(x) if pd.notna(x) else '')
    
    # Buscar coincidencia exacta primero
    resultado = df[(df['producto_norm'] == busqueda_norm) | (df['droga_norm'] == busqueda_norm)]
    
    # Si no hay resultado exacto, buscar parcial
    if resultado.empty:
        resultado = df[df['producto_norm'].str.contains(busqueda_norm) | df['droga_norm'].str.contains(busqueda_norm)]
    
    # Limpiar columnas temporales
    df.drop(['producto_norm', 'droga_norm'], axis=1, inplace=True)
    
    return resultado if not resultado.empty else None

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
        
        # Campo de búsqueda
        col1, col2 = st.columns([3, 1])
        with col1:
            busqueda = st.text_input("Buscar producto o droga...")
        with col2:
            buscar = st.button("Buscar", type="primary")
        
        if buscar or busqueda:
            resultado = buscar_productos(df, busqueda)
            if resultado is not None and not resultado.empty:
                producto = resultado.iloc[0]
                
                # Mostrar información del producto encontrado
                st.success(f"Producto encontrado: {producto['producto']}")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Tipo:** {producto['tipo']}")
                    st.write(f"**Droga:** {producto['droga']}")
                
                with col2:
                    precio = "s/d" if pd.isna(producto['precio']) else producto['precio']
                    unidad = producto['unidad'] if pd.notna(producto['unidad']) else ""
                    st.write(f"**Precio:** {precio} {unidad}")
                    st.write(f"**Última actualización:** {producto['fecha']}")
                
                # Si hay más resultados, mostrarlos
                if len(resultado) > 1:
                    st.write("Otros productos similares:")
                    st.dataframe(resultado[1:].drop(['id', 'fecha'], axis=1), hide_index=True)
            else:
                st.error("Producto no encontrado. Intente con otro término de búsqueda.")
    
    # Pestaña 2: Lista de Productos
    with tab2:
        st.header("Lista de Productos")
        
        # Selector de tipo
        tipo_filtro = st.selectbox(
            "Filtrar por tipo:",
            ["TODOS"] + sorted(df['tipo'].unique().tolist())
        )
        
        # Filtrar productos
        productos_filtrados = filtrar_por_tipo(df, tipo_filtro)
        
        # Mostrar tabla
        st.dataframe(
            productos_filtrados.drop('id', axis=1),
            column_config={
                "tipo": "Tipo",
                "producto": "Producto",
                "droga": "Droga (Principio Activo)",
                "precio": st.column_config.NumberColumn("Precio", format="%.2f"),
                "unidad": "Unidad",
                "fecha": "Actualización"
            },
            use_container_width=True,
            hide_index=True
        )
    
    # Pestaña 3: Agregar Producto
    with tab3:
        st.header("Agregar Nuevo Producto")
        
        # Formulario para agregar nuevo producto
        with st.form("nuevo_producto_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                tipo = st.selectbox(
                    "Tipo de producto:",
                    sorted(df['tipo'].unique().tolist())
                )
                producto = st.text_input("Nombre del producto:", key="nuevo_producto")
                droga = st.text_input("Droga (Principio activo):", key="nueva_droga")
            
            with col2:
                precio = st.number_input("Precio:", min_value=0.0, step=0.1, format="%.2f")
                unidad = st.text_input("Unidad (US$/litro, US$/kg, etc.):", key="nueva_unidad")
            
            submitted = st.form_submit_button("Agregar Producto")
            
            if submitted:
                if not producto or not tipo or precio <= 0 or not unidad:
                    st.error("Por favor complete los campos requeridos: Tipo, Producto, Precio y Unidad.")
                else:
                    # Crear nuevo producto
                    nuevo_id = df['id'].max() + 1
                    nuevo_producto = {
                        'id': nuevo_id,
                        'tipo': tipo,
                        'producto': producto,
                        'droga': droga if droga else "No especificada",
                        'precio': precio,
                        'unidad': unidad,
                        'fecha': datetime.now().strftime("%d/%m/%Y")
                    }
                    
                    # Agregar a dataframe y guardar en session_state
                    df_nuevo = pd.DataFrame([nuevo_producto])
                    df_actualizado = pd.concat([df, df_nuevo], ignore_index=True)
                    st.session_state.productos = df_actualizado.to_dict('records')
                    
                    st.success(f"Producto '{producto}' agregado correctamente.")
                    st.experimental_rerun()
    
    # Pestaña 4: Por Categoría
    with tab4:
        st.header("Productos por Categoría")
        
        # Gráfico de distribución por tipo usando componentes nativos de Streamlit
        st.subheader("Distribución de productos por categoría")
        conteo_tipos = df['tipo'].value_counts().reset_index()
        conteo_tipos.columns = ['Tipo', 'Cantidad']
        
        # Crear gráfico de barras usando Streamlit
        st.bar_chart(conteo_tipos.set_index('Tipo'))
        
        # Mostrar productos por categoría en tabs
        categoria_tabs = st.tabs(sorted(df['tipo'].unique().tolist()))
        
        for i, tipo in enumerate(sorted(df['tipo'].unique())):
            with categoria_tabs[i]:
                productos_tipo = df[df['tipo'] == tipo]
                st.dataframe(
                    productos_tipo.drop(['id', 'tipo'], axis=1),
                    column_config={
                        "producto": "Producto",
                        "droga": "Droga (Principio Activo)",
                        "precio": st.column_config.NumberColumn("Precio", format="%.2f"),
                        "unidad": "Unidad",
                        "fecha": "Actualización"
                    },
                    use_container_width=True,
                    hide_index=True
                )
                
                # Análisis de precios para esta categoría
                if not productos_tipo['precio'].isna().all():
                    st.subheader(f"Análisis de precios: {tipo}")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        precio_promedio = productos_tipo['precio'].mean()
                        precio_max = productos_tipo['precio'].max()
                        precio_min = productos_tipo['precio'].min()
                        
                        st.metric("Precio promedio", f"{precio_promedio:.2f}")
                        st.metric("Precio máximo", f"{precio_max:.2f}")
                        st.metric("Precio mínimo", f"{precio_min:.2f}")
                    
                    with col2:
                        # Mostrar estadísticas en lugar de gráfico
                        st.write("**Estadísticas de precios:**")
                        st.write(f"- Mediana: {productos_tipo['precio'].median():.2f}")
                        st.write(f"- Desviación estándar: {productos_tipo['precio'].std():.2f}")
                        st.write(f"- Cantidad de productos: {len(productos_tipo)}")

    # Pie de página
    st.divider()
    st.write("### Instrucciones de uso:")
    st.markdown("""
    - En la pestaña **Consulta de Precios** puedes buscar rápidamente los precios de cualquier producto.
    - En **Lista de Productos** puedes ver todos los productos y filtrarlos por tipo.
    - Usa **Agregar Producto** para incluir nuevos productos a tu lista.
    - En **Por Categoría** puedes ver los productos organizados por su tipo y análisis de precios.
    """)
    st.caption("Sistema de Gestión de Agroquímicos - Versión 1.0 - Mayo 2025")

if __name__ == "__main__":
    main()
