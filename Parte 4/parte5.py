import requests
import pandas as pd


def descargar_datos (url: str, nombre_archivo:str = "datos_descargados.csv"):
    response = requests.get(url)

    if response.status_code == 200:
        with open(nombre_archivo, 'w' , encoding='utf-8') as archivo:
            archivo.write(response.text)
        print(f'Datos descargados y guardados en {nombre_archivo}')
    else:
        print('Error al descargar. Codigo de estado: {response.status_code}')

url = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'
descargar_datos (url,"heart_failure_clinical_records_dataset.csv")

datos = pd.read_csv('heart_failure_clinical_records_dataset.csv')

def limpiar_datos(df: pd.DataFrame):
    
    if df.isnull().sum().any():
        print('Valores Faltantes en el DataSet')
    
    # Dropo filas repetidas
    filas_antes = len(df)
    df.drop_duplicates(inplace=True)
    filas_despues = len(df)
    print(f'Se eliminaron {filas_antes-filas_despues} filas repetidas')
    
    #Maths
    Q1,Q3 = df['age'].quantile([0.25,0.75])
    IQR = Q3 - Q1
    lower_bound =   Q1 - 1.5 *IQR
    upper_bound =   Q3 + 1.5 *IQR

    #Filtro valores atipicos
    filtro = (df['age'] >= lower_bound) & (df['age']<= upper_bound)
    df[filtro]
    
    #Cateogira Edad
    bins = [0,13,20,39,59, float('inf')]
    labels = ['Niño', 'Adolescente', 'Jovenes Adulto','Adulto','Adulto Mayor']
    df['categoria_edad'] = pd.cut(df['age'],bins=bins, labels=labels, right = False)

    return df


datos_limpios = limpiar_datos(datos)
print(datos_limpios)