import os
import json

def obtener_ruta_datos(archivo_json):
    """Contruye ruta correcta a cualquier JSON de la carpeta datos"""
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    carpeta_raiz = os.path.dirname(carpeta_actual)
    return os.path.join(carpeta_raiz, "datos", archivo_json)


def cargar_json(archivo_json):
    """Carga un json y devuelve los datos"""
    ruta = obtener_ruta_datos(archivo_json)
    try:
        with open(ruta,"r",encoding="utf-8") as f:
            return json.load(f)
    
    except FileNotFoundError:
        print(f"Error: No se encuentra {ruta}")
        return None