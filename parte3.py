from datasets import load_dataset
import pandas as pd

dataset = load_dataset('mstz/heart_failure')

data = dataset['train']

df = pd.DataFrame(data)

df_is_dead = df[df['is_dead'] == 1]
df_alive = df[df['is_dead'] == 0]

promedio_is_dead = df_is_dead['age'].mean()
promedio_is_alive = df_alive['age'].mean()

print('Promedio Edad Vivos:',promedio_is_alive) 
print('Promedio Edad Muertos:',promedio_is_dead)

#Verificar que los tipos de datos son correctos en cada colúmna (por ejemplo que no existan colúmnas numéricas en formato de cadena).
print(df.info())

#Calcular la cantidad de hombres fumadores vs mujeres fumadoras (usando agregaciones en Pandas).
hombre_fumador = df[(df['is_male']== 1) & (df['is_smoker'] == 1)].shape[0]
mujer_fumadora = df[(df['is_male']== 0) & (df['is_smoker'] == 1)].shape[0]

print('Hombre Fumador: ', hombre_fumador)
print('Mujer Fumadora: ', mujer_fumadora)
