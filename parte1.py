import numpy as np 
from datasets import load_dataset
import pandas as pd

dataset = load_dataset('mstz/heart_failure')

data = dataset['train']

edades = np.array(data['age'])

edades_promedio = edades.mean()

print(edades_promedio)