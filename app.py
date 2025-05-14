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

# Carga de datos iniciales
@st.cache_data
def load_initial_data():
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
    
    # Herbicidas
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
    
    # Insecticidas
    insecticidas = [
        {"tipo": "INSECTICIDA", "producto": "ABAMECTINA 3,6%", "principio_activo": "Abamectina", "precio": 12.5, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "ACEFATO 97%", "principio_activo": "Acefato", "precio": 19.5, "unidad": "US$/kg"},
        {"tipo": "INSECTICIDA", "producto": "ALSYSTIN 48 SC", "principio_activo": "Triflumuron", "precio": 86.3, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "AMPLIGO", "principio_activo": "Clorantraniliprole + Lambda-cialotrina", "precio": 101.0, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "CLAP SC", "principio_activo": "Insecticida biológico", "precio": np.nan, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "CORAGEN", "principio_activo": "Clorantraniliprole", "precio": 150.0, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "CURYOM FIT UV", "principio_activo": "Lufenuron + Profenofos", "precio": 173.3, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "CIPERMETRINA 25%", "principio_activo": "Cipermetrina", "precio": 7.5, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "DECIS 5%", "principio_activo": "Deltametrina", "precio": 5.5, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "DECIS FLOW", "principio_activo": "Deltametrina", "precio": 94.6, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "DECIS FORTE 10%", "principio_activo": "Deltametrina", "precio": 34.4, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "DIPEL DF", "principio_activo": "Bacillus thuringiensis", "precio": 43.0, "unidad": "US$/kg"},
        {"tipo": "INSECTICIDA", "producto": "ENGEO", "principio_activo": "Tiametoxam + Lambda-cialotrina", "precio": 25.4, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "EXALT SC", "principio_activo": "Spinetoram", "precio": 248.0, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "EXPEDITION", "principio_activo": "Acetamiprid + Bifentrin", "precio": 39.0, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "FASTAC DUO", "principio_activo": "Alfa-cipermetrina + Acetamiprid", "precio": 25.0, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "FIGHTER PLUS", "principio_activo": "Imidacloprid + Beta-ciflutrina", "precio": 83.5, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "INTREPID", "principio_activo": "Metoxifenocide", "precio": 38.0, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "KARATE ZEON 25%", "principio_activo": "Lambda-cialotrina", "precio": 44.6, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "SOLOMON", "principio_activo": "Imidacloprid", "precio": 29.1, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "STARKLE (5,1 kg)", "principio_activo": "Dinotefuran", "precio": 710, "unidad": "US$/pack"},
        {"tipo": "INSECTICIDA", "producto": "TRACER", "principio_activo": "Spinosad", "precio": 254.0, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "PHIL LAMBDA 5%", "principio_activo": "Lambda-cialotrina", "precio": 7.8, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "QUINTAL XTRA", "principio_activo": "Clorpirifos + Cipermetrina", "precio": 83.0, "unidad": "US$/litro"},
        {"tipo": "INSECTICIDA", "producto": "TRANSFORM", "principio_activo": "Sulfoxaflor", "precio": 234.5, "unidad": "US$/litro"}
    ]
    
    # Fungicidas
    fungicidas = [
        {"tipo": "FUNGICIDA", "producto": "ALLEGRO", "principio_activo": "Kresoxim-metil", "precio": 26.0, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "AMISTAR XTRA", "principio_activo": "Azoxistrobina + Ciproconazol", "precio": 24.9, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "ARACONAZOLE 43%", "principio_activo": "Tebuconazole", "precio": 11.0, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "CARBENDAZIM 50%", "principio_activo": "Carbendazim", "precio": 6.8, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "CINCHA", "principio_activo": "Difenoconazole", "precio": 15.0, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "COMET", "principio_activo": "Piraclostrobina", "precio": 60.0, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "CRIPTON", "principio_activo": "Trifloxistrobina + Protioconazole", "precio": 32.01, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "CRIPTON XPRO", "principio_activo": "Trifloxistrobina + Protioconazole + Bixafen", "precio": 54.32, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "MANCOZEB", "principio_activo": "Mancozeb", "precio": 6.0, "unidad": "US$/kg"},
        {"tipo": "FUNGICIDA", "producto": "NATIVO SC 300", "principio_activo": "Trifloxistrobina + Tebuconazole", "precio": np.nan, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "OPERA", "principio_activo": "Piraclostrobina + Epoxiconazole", "precio": 23.0, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "ORQUESTA ULTRA", "principio_activo": "Piraclostrobina + Epoxiconazole + Fluxapyroxad", "precio": 32.0, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "REFLECT XTRA", "principio_activo": "Isopyrazam + Azoxistrobina", "precio": np.nan, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "SPHERE MAX", "principio_activo": "Trifloxistrobina + Ciproconazol", "precio": 55.3, "unidad": "US$/litro"},
        {"tipo": "FUNGICIDA", "producto": "STINGER", "principio_activo": "Azoxistrobina + Difenoconazole", "precio": 26.0, "unidad": "US$/litro"}
    ]
    
    # Fertilizantes
    fertilizantes = [
        {"tipo": "FERTILIZANTE", "producto": "AZUFRE GRANULADO", "principio_activo": "Azufre elemental", "precio": 230, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "CLORURO DE POTASIO", "principio_activo": "KCl", "precio": 490, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "FOSZINC", "principio_activo": "Fósforo + Zinc", "precio": 980, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "FOSFATO DIAMONICO", "principio_activo": "DAP", "precio": 870, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "FOSF MONOAMONICO", "principio_activo": "MAP", "precio": 880, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "MAP AZUFRADO", "principio_activo": "MAP + S", "precio": 690, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "NITR de AMONIO CALC.", "principio_activo": "CAN", "precio": 525, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "SOLMIX N 28 - S 5,2", "principio_activo": "Solución nitrogenada con azufre", "precio": 455, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "SOLMIX Zn (27-5-04 Zn)", "principio_activo": "Solución con zinc", "precio": 490, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "SULFATO de AMONIO", "principio_activo": "Sulfato de amonio", "precio": 450, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "SULFATO de CALCIO", "principio_activo": "Sulfato de calcio", "precio": 326, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "SUPERFOSF. SIMPLE", "principio_activo": "Superfosfato simple", "precio": 390, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "SUPERFOSF. TRIPLE", "principio_activo": "Superfosfato triple", "precio": 700, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "U.A.N. 32", "principio_activo": "Solución UAN", "precio": 490, "unidad": "US$/tn"},
        {"tipo": "FERTILIZANTE", "producto": "UREA GRANULADA", "principio_activo": "CO(NH₂)₂", "precio": 560, "unidad": "US$/tn"}
    ]
    
    # Curasemillas
    curasemillas = [
        {"tipo": "CURASEMILLA", "producto": "ACRONIS 2,5 lt", "principio_activo": "Tiram + Carbendazim", "precio": 48.0, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "CHUCARO", "principio_activo": "Tiametoxam + Tebuconazole + Fludioxonil", "precio": 94.1, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "CKC Liquid Soja", "principio_activo": "Inoculante biológico", "precio": 3.5, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "CKC Rizoflo Premium Soj", "principio_activo": "Inoculante premium", "precio": 3.6, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "CKC Pack Sistémico", "principio_activo": "Inoculante + fungicida", "precio": 4.5, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "CKC Pack Soja Premium", "principio_activo": "Inoculante premium", "precio": 7.5, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "CONFIDOR 70 WG", "principio_activo": "Imidacloprid", "precio": 56.0, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "CREATE PACK FAST", "principio_activo": "Clothianidin + Ciantraniliprole", "precio": 129.50, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "CRUISER PACK", "principio_activo": "Tiametoxam + Fludioxonil + Metalaxil-M", "precio": 442.1, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "DIVIDEND", "principio_activo": "Difenoconazole + Metalaxil-M", "precio": 11.1, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "DIVIDEND EXTRA", "principio_activo": "Difenoconazole + Metalaxil-M + Sedaxane", "precio": 18.6, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "NITRAGIN CELL TECH ds", "principio_activo": "Bradyrhizobium japonicum", "precio": 2.40, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "NITRAPACK", "principio_activo": "Inoculante + protector", "precio": 3.7, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "PREMIS", "principio_activo": "Triticonazole", "precio": 48.0, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "PUCARA", "principio_activo": "Tiametoxam + Lambda-cialotrina", "precio": 107.67, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "SCENIC", "principio_activo": "Fluoxastrobin + Protioconazole + Tebuconazole", "precio": 32.98, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "SISTIVA (p/4000 kg)", "principio_activo": "Fluxapyroxad", "precio": 330.00, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "SUMI-EIGHT MT", "principio_activo": "Diniconazole-M + Thiram", "precio": 29.0, "unidad": "US$/dosis"},
        {"tipo": "CURASEMILLA", "producto": "VIBRANCE INTEGRAL", "principio_activo": "Sedaxane + Difenoconazole + Metalaxil-M + Fludioxonil", "precio": 64.30, "unidad": "US$/dosis"}
    ]
    
    # Aceites y coadyuvantes
    aceites = [
        {"tipo": "ACEITE", "producto": "ACEITE METILADO", "principio_activo": "Éster metílico de ácidos grasos", "precio": 3.0, "unidad": "US$/litro"},
        {"tipo": "ACEITE", "producto": "AJUSTE", "principio_activo": "Aceite mineral parafinado", "precio": 45.0, "unidad": "US$/litro"},
        {"tipo": "ACEITE", "producto": "DASH MSO MAX", "principio_activo": "Éster metílico de aceite de soja", "precio": 16.0, "unidad": "US$/litro"},
        {"tipo": "ACEITE", "producto": "RIZOSPRAY EXTREMO", "principio_activo": "Tensioactivo siliconado", "precio": 18.5, "unidad": "US$/litro"},
        {"tipo": "ACEITE", "producto": "SULFATO de AMONIO lq", "principio_activo": "Sulfato de amonio líquido", "precio": 1.3, "unidad": "US$/litro"}
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

# Función para obtener opciones de búsqueda en tiempo real
def obtener_opciones_busqueda(df, texto, max_opciones=10):
    if not texto or len(texto) < 2:
        return []
    
    # Normalizar el texto de búsqueda
    texto_norm = normalizar_texto(texto)
    
    # Normalizar las columnas del DataFrame para la búsqueda
    df['producto_norm'] = df['producto'].apply(normalizar_texto)
    df['principio_activo_norm'] = df['principio_activo'].apply(lambda x: normalizar_texto(x) if pd.notna(x) else '')
    
    # Crear función para calcular puntuación de coincidencia
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
    
    # Devolver opciones para el select_box
    if resultados.empty:
        return []
    
    # Crear las opciones con formato "PRODUCTO (TIPO) - Principio Activo"
    opciones = []
    for _, row in resultados.head(max_opciones).iterrows():
        opcion_texto = f"{row['producto']} ({row['tipo']}) - {row['principio_activo']}"
        opciones.append((row['id'], opcion_texto))
    
    return opciones

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
        
        # Creamos un contenedor para la barra de búsqueda y el dropdown
        search_container = st.container()
        
        with search_container:
            # Agregar un campo de texto para la búsqueda
            texto_busqueda = st.text_input("Buscar producto o principio activo...", key="texto_busqueda")
            
            # Obtener opciones de autocompletado basadas en el texto de búsqueda
            if texto_busqueda:
                opciones = obtener_opciones_busqueda(df, texto_busqueda)
                
                if opciones:
                    # Preparar las opciones para el selectbox
                    ids = [id for id, _ in opciones]
                    textos = [texto for _, texto in opciones]
                    
                    # Agregar opción "Seleccionar..." al principio
                    ids.insert(0, -1)
                    textos.insert(0, "Seleccionar un producto...")
                    
                    # Crear un selectbox con las opciones
                    seleccion_index = st.selectbox(
                        "Productos encontrados:",
                        range(len(textos)),
                        format_func=lambda i: textos[i]
                    )
                    
                    # Si se seleccionó un producto (no la opción "Seleccionar...")
                    if seleccion_index > 0:
                        # Guardar el ID del producto seleccionado
                        producto_id = ids[seleccion_index]
                        
                        # Obtener el producto del DataFrame
                        producto = df[df['id'] == producto_id].iloc[0]
                        
                        # Mostrar información del producto
                        st.success(f"Producto seleccionado: {producto['producto']}")
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"**Tipo:** {producto['tipo']}")
                            st.write(f"**Principio activo:** {producto['principio_activo']}")
                        
                        with col2:
                            precio = "s/d" if pd.isna(producto['precio']) else producto['precio']
                            unidad = producto['unidad'] if pd.notna(producto['unidad']) else ""
                            st.write(f"**Precio:** {precio} {unidad}")
                            st.write(f"**Última actualización:** {producto['fecha']}")
                else:
                    st.warning("No se encontraron productos que coincidan con tu búsqueda.")
        
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
                "principio_activo": "Principio Activo",
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
                principio_activo = st.text_input("Principio activo:", key="nuevo_principio_activo")
            
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
                        'principio_activo': principio_activo if principio_activo else "No especificado",
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
                        "principio_activo": "Principio Activo",
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
      Empieza a escribir para ver sugerencias en el menú desplegable.
    - En **Lista de Productos** puedes ver todos los productos y filtrarlos por tipo.
    - Usa **Agregar Producto** para incluir nuevos productos a tu lista.
    - En **Por Categoría** puedes ver los productos organizados por su tipo y análisis de precios.
    """)
    st.caption("Sistema de Gestión de Agroquímicos - Versión 1.0 - Mayo 2025")

# CSS personalizado para mejorar el estilo del dropdown
st.markdown("""
<style>
    div[data-baseweb="select"] {
        margin-top: 0px;
    }
    
    .stSelectbox label {
        font-weight: bold;
    }
    
    .stSelectbox select {
        padding: 10px;
        border-radius: 5px;
    }
    
    /* Estilos para el contenedor de búsqueda */
    .search-container {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
