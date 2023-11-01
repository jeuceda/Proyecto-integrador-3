import pandas as pd
import requests
import argparse

def descargar_datos(url):
    response = requests.get(url)
    data = response.json() 
    return data

def procesar_datos(data):
    df = pd.DataFrame(data)
    df['categoria'] = pd.cut(df['columna_para_categorizar'], bins=3, labels=['Grupo A', 'Grupo B', 'Grupo C'])
    
    return df

# Función para exportar a un archivo CSV
def exportar_csv(df, nombre_archivo):
    df.to_csv(nombre_archivo, index=False)

if __name__ == "__main__":
    # Argumentos del terminal
    parser = argparse.ArgumentParser(description='Procesamiento de datos desde URL')
    parser.add_argument('url', type=str, help='URL de los datos')
    parser.add_argument('nombre_archivo', type=str, help='Nombre del archivo CSV de salida')
    args = parser.parse_args()

    # Descargar datos desde la URL proporcionada
    datos = descargar_datos(args.url)

    # Procesar los datos y categorizar en grupos
    dataframe_procesado = procesar_datos(datos)

    # Exportar el DataFrame a un archivo CSV
    exportar_csv(dataframe_procesado, args.nombre_archivo)
