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
