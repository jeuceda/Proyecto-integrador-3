import requests


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